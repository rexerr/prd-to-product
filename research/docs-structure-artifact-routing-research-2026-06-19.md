# Research — docs structure & artifact-output routing (2026-06-19)

**Method:** `deep-research` workflow — 5 search angles, ~15 sources fetched, claims extracted and put through 3-vote adversarial verification (2-of-3 refutes to kill). 21 claims survived; 4 were refuted. This report was hand-synthesized from the verified claim set after the workflow's final formatting agent hit a schema bug and looped (the research stages all completed cleanly; only the auto-formatter failed — see the parked-item note in [`../docs/briefs/docs-structure-and-artifact-routing-brief.md`](../docs/briefs/docs-structure-and-artifact-routing-brief.md)).

**Question:** How do mature teams and AI coding-agent tools organize project docs and route tool/skill-generated artifacts into a project's folder structure? Should `context-engineering` scaffold a doc-routing rule + pre-seeded landing zones at conception, and should the "write output to the right place" burden sit on the global skill or the project's context files?

---

## Executive summary

Across every real system studied, the dominant pattern is **convention-over-configuration: a tool defaults to a well-known landing zone established at project setup, and the project declares only its deviations** (high confidence — log4brains, adr-tools, OpenCode, .NET SDK, plus the CoC paradigm itself). The decisive finding for our specific case: **Claude Code skills have no declarative output-destination mechanism at all** — the entire skill frontmatter field set contains no `output-dir` parameter, so any "write output here" instruction *must* be authored as natural-language prose in `SKILL.md` (high confidence, primary Anthropic docs). That settles the burden question: you cannot put clean declarative routing on the global skill because the mechanism doesn't exist; the architecturally-correct split is **skill prose that defers to a project-declared convention, with the convention living in the project's context files** — which is exactly how OpenCode resolves `AGENTS.md`/`CLAUDE.md` and config (project file walked up from CWD, merged over global). Finally, **folder/IA structure does *not* materially improve AI-agent retrieval** (refuted 0-3) — it's a human-browsing and author-friction concern, so the case for scaffolding structure rests on human ergonomics and first-run tidiness, not agent capability.

---

## Findings

### F1. There is no declarative output-routing for skills — it must be prose (HIGH)

The complete skill frontmatter field set (`name`, `description`, `when_to_use`, `allowed-tools`, `context`, `agent`, `hooks`, `paths`, etc.) contains **no output-destination field**. Skills that write output specify the path in the markdown body as prose ("creates `codebase-map.html` in the current directory"; `logs/${CLAUDE_SESSION_ID}.log`). `$ARGUMENTS` is for *input* parameterization, not output routing. [claim 9, primary: Anthropic/Claude Code docs + open Agent Skills spec]

**Implication:** the global skill *cannot* carry a clean declarative "write here" parameter. The only lever is prose. So the realistic design is: skill prose says "write to the project's convention if one exists, else a default," and the **project** supplies the convention.

### F2. The dominant real-world pattern is a configurable default declared at init / project level (HIGH)

- **log4brains** (ADR tooling): output is **not** hardcoded — it's project-declared in `.log4brains.yml` via an `adrFolder` key, created by `log4brains init`, defaulting to `docs/adr`. The tool reads the project's declaration. [claims 2, 3]
- **adr-tools** (the canonical `adr.github.io` implementation): default `doc/adr`, overridable at `adr init`, and the chosen path is **persisted per-project** in a `.adr-dir` file that later commands read — convention established once at conception, artifacts routed there automatically thereafter. [claims 4, 5]
- **OpenCode**: project config (`opencode.json` in project root) is **discovered by walking up from CWD to the git root**, then **merged over** the user-global config (`~/.config/opencode/`), overriding only conflicting keys. The same traverse-up-from-CWD discovery governs its `AGENTS.md`/`CLAUDE.md` rule files. The git-bounded project is the unit that declares its own conventions. [claims 15, 16]
- **.NET SDK**: centralizes build outputs into one predictable `artifacts/` dir with a fixed **type-first taxonomy** (`bin`/`obj`/`publish`/`package` → project → pivot) the tool creates automatically, *expressly so tooling can anticipate output locations rather than scanning per-project paths*. Opt-in. (Caveat: this is build-artifact layout, analogical to doc-routing, not a direct model.) [claims 17, 18]

**Implication:** "scaffold the landing zone at project conception, tool reads/defaults to it" is the mainstream pattern, not an invention. Strong external validation for the `context-engineering`-scaffolds-it approach.

### F3. Convention-over-configuration is the governing principle, and it maps directly onto "pre-seeded zones + optional override" (HIGH)

CoC's explicit goal is to *decrease the number of decisions a developer must make without losing flexibility*; behavior works with zero config when the convention matches the desired outcome, and **explicit configuration is required only to deviate** (the Rails `Sales`-class→`sales`-table example). This is precisely the "pre-seeded landing zone + the project declares only deviations" model. [claims 19, 20; secondary: Wikipedia — adequate for a definitional claim]

### F4. In the wild, path/filename convention *is* the de-facto routing mechanism (HIGH/MEDIUM)

A research dataset of ~921 real repos with ADRs was built purely by globbing for Markdown files whose path contains `arch`/`adr`/`design`/`decision` and whose content includes "decision." That a path-substring search reliably locates decision records across hundreds of diverse repos is itself the evidence: real repos place these by **convention**, not via a manifest or caller-passed output-dir. [claim 12, primary: arXiv 2602.07609] Reinforced by the marker-file/discovery-probe pattern in **Argo CD** plugins — the host repo signals applicability by carrying a detectable file (glob match) or passing a `find` command run in the repo root; the tool owns the probe, the project owns the signal. [claims 13, 14]

### F5. The alternative — invoker passes the destination at call time — exists but pushes the burden onto the caller every time (HIGH)

**OpenAPI Generator** routes purely via an explicit `--output`/`-o` flag, defaulting to CWD when omitted; there is no project manifest it reads. [claims 0, 1] This is the "burden on the global tool's invoker" model — viable, but it means the decision is re-made on every invocation rather than declared once. For an interactive skill the user runs ad hoc, that's friction every run; for our case the declare-once-per-project pattern (F2) is the better fit.

### F6. Folder structure does NOT materially help AI-agent retrieval — it's a human concern (MEDIUM, from a refuted claim)

The claim *"a clean documentation structure directly improves AI retrieval quality… meaning folder/IA structure affects AI-agent retrieval and not just human browsing"* was **refuted 0-3**. The benefit of good structure that *does* hold is human-side: a known structure **removes the "where does this go?" question** that blocks authors (the blank-page problem). [claim 8, primary: Read the Docs] Separately, *context-position* matters to models (lost-in-the-middle: U-shaped attention, position determines use — claims 10, 11) — but that's about ordering *within a context window*, not folder layout on disk. **Net: the case for scaffolding doc structure rests on human ergonomics and first-run tidiness, not on making the agent retrieve better.** Confirms the original audit call.

### Docs IA frameworks (context)

Diátaxis prescribes four documentation types (tutorials, how-to, reference, explanation) and treats **architecture/organization as a first-class design concern**, not an afterthought. [claims 6, 7] Note a useful negative: the claim that a Diátaxis template files ADRs under the "Reference" quadrant was **refuted 0-3** — decision records don't have a settled home inside the four-type model, which is consistent with ADRs getting their *own* typed folder by convention (F4) rather than being slotted into a docs-type taxonomy.

---

## What this means for the decision

1. **Scaffold the routing rule + landing zones at conception — yes.** This is the mainstream pattern (F2, F3), and it solves the real (human) problem structure addresses (F6).
2. **The burden split is settled by mechanism, not preference (F1).** Skills can't declare output dirs, so: global skills stay portable and carry *prose* that defers to a project convention; the **project's context files declare the convention**. This is the OpenCode model and resolves Rex's "global skills aren't always attached to a project" objection — no project, no convention, the skill falls back to its prose default.
3. **Convention over hardcoding (F2, F4, F5).** Pre-seed a sensible default landing zone; let the project override only deviations. Don't hardcode paths into the global skill (F5's per-call burden is the inferior model for our case).
4. **Don't oversell it as an agent-capability win (F6).** Frame the scaffolded structure honestly as human-ergonomics + first-run tidiness.

---

## Caveats / confidence notes

- **F6 rests on a refuted claim** (absence of a retrieval benefit), which is weaker evidence than a confirmed one — it means *no source credibly established* a retrieval benefit, not that one provably can't exist. Treat as "no evidence for," not "proof against."
- **.NET artifacts** (F2) is a build-compiler-output convention; its relevance to *doc/agent-artifact* routing is analogical, not direct. The .NET "declared via `Directory.Build.props` the tool reads" framing was actually **refuted 1-2** (the feature is opt-in/property-driven, not a clean project-declaration-read), so lean on log4brains/adr-tools/OpenCode for the declare-once pattern, not .NET.
- **CoC findings** (F3) are sourced to Wikipedia (secondary) — fine for a definitional claim, not a contested empirical one.
- Source recency is good (most primary docs dated 2025–2026); lost-in-the-middle severity is becoming model-dependent (flatter curves on frontier models) but the position-dependence finding holds.

## Open questions (not answered by this research)

1. **Filename pattern vs. folder only** — real systems persist a *path* (`.adr-dir`, `adrFolder`); none studied prescribe a *filename* template. Does our council/brainstorm landing-zone line need the filename pattern, or just the folder? (Probably folder + let the skill name the file.)
2. **Where `deep-research` output lands** — still open; this very report is the test case (saved to `research/`, a top-level sibling, not `docs/research/`).
3. **A machine-readable convention vs. prose** — every system here uses *either* a config file the tool parses (log4brains/OpenCode) *or* prose (skills). Skills can't parse a config today (F1). Is a lightweight project manifest the skill's prose points to ("see `docs/.outputs`") worth it, or is prose-in-CLAUDE.md enough? Likely enough for now; revisit only if prose deference proves unreliable.
4. **Crib/mine-workflow alignment** — does the `/mine` staging convention (`mines/<date>-<source>/`, per BACKLOG) want to be the same mechanism as artifact landing zones, or a separate one?
