# Brief — docs structure & artifact-output routing (PINNED, needs research)

**Status:** research done 2026-06-19 ([`../../research/docs-structure-artifact-routing-research-2026-06-19.md`](../../research/docs-structure-artifact-routing-research-2026-06-19.md)) — findings **confirm the provisional design** below. Still parked pending a Rex decision + scope-gate before any change to `context-engineering`.

**Sibling to:** [`context-lifecycle-brief.md`](context-lifecycle-brief.md) — that one is about *context-loading cost* (what gets read every session). This one is about *physical placement* (where docs/artifacts land) and *how global skills route their output into a project*. They overlap but are distinct problems.

---

## The trigger

Rex: "`/docs` is full of random stuff — some organization but not real. Is this a bad setup, does it even matter to Claude Code, should we be systematic and bake it into rules?"

## What the audit found

- **A routing rule already exists** — CLAUDE.md "Where new docs go" (anchors at root; everything else → a typed subfolder by name; lazy-create; never grow the root pile). It's sound. The subfolders are real and used: `retros/` (63), `council/` (33), `audits/`, `brainstorms/`, `product-briefs/`, `cribs/`, `briefs/`, `handoffs/`, `reference/`.
- **But it was added reactively**, after sprawl. 18 of 22 root-level `docs/*.md` files predate it and are deliberately grandfathered (moving them breaks ~75–90 cross-references — not worth it incidentally). So the root *looks* messy but it's frozen legacy + a clean rule in front of it, not chaos.
- **The skill that should install this rule doesn't.** `context-engineering` scaffolds the anchor docs + `retros/`, but ships **no doc-routing rule**. So every project it creates starts clean, then sprawls exactly like this one did — and only gets a routing rule if the developer notices and writes one. This repo is the proof.
- **`.claude/rules/` does not exist here** — the skill *scaffolds* it for new projects, but this repo governs itself with CLAUDE.md prose. Decided 2026-06-19: keep CLAUDE.md, don't adopt a `.claude/rules/` dir here (over-engineering for a single-dev markdown repo).

## Does folder structure even matter to Claude Code?

Mostly **no** for retrieval — the agent finds files by grep/glob/semantic search, not by browsing folders. A flat pile and a deep tree are equally findable. What *does* matter to the agent: which files CLAUDE.md names as session-start reads, and whether cross-references resolve. **The cost of the mess is paid by the human who browses `docs/`, not by the agent.** The one place structure helps the agent is when a folder *is* a signal it already exploits ("newest file in `retros/` is the one to read"). Conclusion: this is a human-ergonomics + first-run-tidiness concern, not an agent-capability one.

## The artifact-routing discovery (the interesting part)

The `llm-council` skill does **not** create `docs/council/`. It writes to a generic `<outputs>` location with default filenames (`council-report-<ts>.html`, `council-transcript-<ts>.md`, `mapping.json`, `council-data.json`). This repo's tidy `docs/council/` with topic-suffixed names exists **because this repo's CLAUDE.md routing rule steered it there** — the proof is the early bare-default files (`council-report-2026-06-08.html`, no topic) sitting next to later steered ones.

**Generalization:** artifact-emitting skills (council, brainstorm, deep-research, and Rex's future repo-mining / crib work) all write to a generic `<outputs>` and rely on the host project's convention to land well. They don't self-organize. So in a fresh project with no routing rule, their output dumps at root on run #1.

## The design we converged on (provisional — do not build yet)

Two mechanisms, replacing an "11-folder menu":

1. **Universal routing rule** (always installed by `context-engineering`, no intake question). Anchors at root; everything else → typed subfolder by name; lazy-create; never grow the root pile; cite the sprawl failure mode (per "every rule cites its failure mode"). This silently handles *every* doc type, including unforeseen ones (cribs, mined-repo notes, whatever).

2. **One narrow intake question** — not "pick your folders," but **"Which artifact-emitting skills will this project run regularly?"** For each one checked, the generator pre-creates the folder **and** writes the filename-pattern line that steers the skill's generic `<outputs>` on run #1.

**Kill/keep/combine result** (sorted by: does a *skill* write it, or a *human*?):
- **Pre-seed only skill-emitted folders** — `retros/` always; `council/`, `brainstorms/` opt-in. These are the only ones that write-to-generic-`<outputs>`-and-sprawl.
- **Everything else rides the rule** — `briefs`, `handoffs`, `reference`, `cribs`, `research`, `audits`, etc. The human authors them; the routing rule catches them. No empty folders shipped.

## The split that resolves "should the burden be on the skills?"

Rex's objection: global skills (council/brainstorm/deep-research) run across many projects and **often with no project at all** — so you can't hardcode project paths into them.

Resolution: **don't.** The burden splits:
- **Global skill's job:** write to a generic `<outputs>`; *defer to the host's convention if one exists*. No project → use its own default. Stays portable. (Council already behaves this way.)
- **Project's job:** *declare* the landing zones (routing rule + filename-pattern lines in CLAUDE.md). That's the one place project-specific knowledge can live without breaking skill portability.

So the burden sits on the **project's context files**, never on the global skills.

## What's genuinely still open (why this is parked, not built)

1. Is "skill writes generic / project declares convention" actually the best pattern, or is there a cleaner ecosystem standard (a `docs/` manifest, an env var, an `.outputs` config, a per-skill output-dir param)? **Unvalidated — this is the research question.**
2. Where should `deep-research` output land? It's a skill Rex runs and it writes a file — opt-in seed like council, or ride the rule? (Currently `research/` is an ungoverned top-level sibling, not under `docs/`.)
3. Rex's real taxonomy is **"mine" + cribbed-content-from-evaluating-other-codebases + research** — does the crib/mine workflow (see the `/repo-miner` BACKLOG item) want its own staging convention that this brief should align with?
4. Does the routing rule need the filename *pattern* per skill, or just the folder?

## Research findings (2026-06-19) — they confirm the design

Full report: [`../../research/docs-structure-artifact-routing-research-2026-06-19.md`](../../research/docs-structure-artifact-routing-research-2026-06-19.md) (21 claims survived 3-vote adversarial verification). Headlines:

1. **The burden question is settled by mechanism, not preference.** Claude Code skills have **no `output-dir` frontmatter field** — routing *must* be prose (HIGH, primary Anthropic docs). So you literally can't put clean declarative routing on the global skill. The architecturally-correct split — skill prose defers to a project-declared convention; the convention lives in the project's context files — is exactly what F1 forces, and matches how OpenCode discovers `CLAUDE.md`/`AGENTS.md` and config (project file walked up from CWD, merged over global). This resolves Rex's global-skills-aren't-always-attached objection: no project → no convention → skill uses its prose default.
2. **"Scaffold the landing zone at conception" is the mainstream pattern**, not an invention — log4brains (`.log4brains.yml adrFolder`, created at `init`), adr-tools (`.adr-dir` persisted per-project), OpenCode (project config merged over global), all declare-once-then-route-automatically.
3. **Convention-over-configuration** is the governing principle: pre-seed a default, project overrides only deviations.
4. **Folder structure does NOT materially help agent retrieval** — the "clean structure improves AI retrieval" claim was **refuted 0-3**. The honest case for scaffolding structure is human ergonomics + first-run tidiness (removes the author's "where does this go?" friction), not agent capability. Confirms the original audit.

Open questions the research left (folder-vs-filename pattern; where `deep-research` output lands; manifest-vs-prose; crib/mine alignment) are listed at the end of the report.

## Proposed next step

Research is in; it **confirms** the provisional design. This is now a Rex decision, not a research gap. When promoted, it's a `context-engineering` template change → scope-gate first; likely a `D-NNN` since it touches scaffolded conventions. The concrete build would be: (1) add the universal routing rule to the flat + modular CLAUDE templates with its sprawl failure-mode cited; (2) add the narrow "which artifact-emitting skills?" intake question that pre-seeds `council/`/`brainstorms/` + writes the prose deference line; (3) pick `docs/research/` as the research home.
