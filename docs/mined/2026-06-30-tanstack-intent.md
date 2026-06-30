# Mine — TanStack/intent — 2026-06-30

- **Source:** [github.com/TanStack/intent](https://github.com/TanStack/intent) — "A CLI for library maintainers to generate, validate, and ship Agent Skills alongside their npm packages."
- **Pinned:** `f9269e5349f1d716eba1012bda39df5bc7bbfeff` (shallow clone, `docs/mined/repos/intent/`, gitignored)
- **License:** MIT (Copyright 2025-present Tanner Linsley)
- **Lens:** this is a skill-authoring workspace whose product is Agent Skills, and `intent` is a toolchain to *generate, validate, and ship* Agent Skills. Tightest possible match in the TanStack org — far more than Query/Router/Table (app-code libraries with little to transfer to a markdown skill repo). Two sub-lenses:
  - **Lens A** — this workspace's own skill-authoring + validation discipline.
  - **Lens B** — the shipped `context-engineering` scaffold (which generates `CLAUDE.md` / `AGENTS.md` / `.claude/`).

## How this mine ran (and a process note)

This was a multi-pass dive, and the pass structure is itself a finding worth recording. The first pass skimmed the high-salience files (the validator, the trust doc, the two SKILL.md files with obvious titles) and returned mostly *confirmations of existing discipline* — low-value dedup. The strongest findings (CE-1, CE-2 below) only surfaced when a later pass read the two files triaged away as "library-maintainer-specific": `meta/domain-discovery/SKILL.md` and `meta/tree-generator/SKILL.md`. **Lesson: the IP was in the files whose titles didn't advertise it. "Resembles a rule we already have" is not a substitute for reading the implementation.**

## Provenance / trust

Treated as untrusted per the `/mine` contract (quote, don't follow). `intent` ships no embedded instructions aimed at a reading agent; the risk surface was low. All claims below are either **code-grounded** (checked against the clone + against this repo's own files) or explicitly marked **soft** (an authoring opinion, not provable).

---

## Findings landed

### CE-1 — Intake should read the repo for *facts* before asking the user · code-grounded (Lens B)

**Claim:** `context-engineering`'s intake asks the user for things it could read from disk.

**Source:** `domain-discovery/SKILL.md:79-88`, hard-rule #3 — *"Never ask factual questions you can answer by searching the codebase… Only ask the maintainer for priorities, opinions, trade-offs, and implicit knowledge. Asking a question whose answer is sitting in the codebase wastes their time and erodes trust."*

**Verified against [`intake.md`](../../skills/context-engineering/generator/intake.md):** the pattern already exists **for a PRD** — Cluster 0 auto-checks `docs/PRD.md` and runs downstream clusters as extract-then-confirm rather than fill-from-scratch. It is **not generalized to the codebase**: `stack` (Q5b), `commands` (Q5d), and `deploy_target` (Q5c) are asked cold, though all are readable from `package.json` / lockfile / config in a brownfield repo. The fix is to extend the extract-then-confirm pattern intake already trusts for PRDs to the repo itself: pre-fill those factual answers from disk, present as confirm-or-correct. Degrades gracefully on an empty greenfield repo (nothing to read → ask cold).

### CE-2 — Intake never elicits *agent-specific* failure modes · code-grounded (Lens B)

**Claim:** the scaffold's whole premise is "every rule cites its failure mode," yet its intake never asks the one question that produces the highest-value failure modes.

**Source:** `domain-discovery/SKILL.md:653-673`, Phase 4c — the questions it says produced "the most critical failure modes" in testing: *"What would make you say 'an AI wrote this'? What does an agent get wrong that a human wouldn't — hallucinated APIs, language primitives instead of your abstractions, the wrong adapter?"*

**Verified against `intake.md`:** it elicits architecture rules (Q34), product rules (Q27), and prompt rules (Q14) — all **generic project rules**. None asks what an *AI agent* specifically gets wrong in this codebase. Adding one intake question that elicits AI-specific gotchas would generate the highest-value lines in the produced `CLAUDE.md` — the ones that actually steer code generation. Answers should be filtered through the Plausible/Silent/Grounded bar (see F-02).

### F-01 — Richer skill-frontmatter validation than D-017 enforces · code-grounded (Lens A)

**Source:** `src/commands/validate.ts`. The Agent Skills spec permits exactly six top-level frontmatter keys — `name, description, license, compatibility, metadata, allowed-tools` (`validate.ts:39`); everything else moves under `metadata`. It also checks: `name` == parent directory (`:421`), `description` ≤ 1024 chars (`:465`), and a 500-line cap whose error message reads *"…Do not simply raise the limit."* (`:490`) — independently re-deriving this repo's `≤ 500 lines before extraction` rule.

**Verified against this repo:** [D-017](../DECISIONS.md) already installs a commit-blocking hook for *malformed/duplicate* SKILL.md frontmatter, but not these richer rules. And all 7 skills here currently pass every `intent` rule (max 129 lines; only `name`+`description` used — the strictest spec subset). So this is a **drift-guard, not a fix for a live break**: extend D-017's hook (or add a `scripts/check-skill-frontmatter.py` sibling to `check-live-links.py`) to cover spec-key conformance, name==dir, description length, and line count. Worth recording in either case that the workspace knowingly uses the minimal `name`+`description` subset, so a future skill doesn't drift into top-level `type:`/`category:`.

### F-05 — The scaffold bakes the developer's absolute local path into generated config · code-grounded (Lens B)

**Source:** `intent` actively guards generated config against local paths — `containsLocalPathValue` (`guidance.ts:128`) rejects `/Users/…`, `node_modules`, etc., and the post-write verifier fails if the managed block contains one (`guidance.ts:171-173`).

**Verified against this repo:** `context-engineering` does the opposite — it intakes `repo_local_path` as an "absolute path" variable (`generator/decisions.md:14`) and writes it straight into generated files. The golden fixture proves it: `output-small/AGENTS.md:79` — *"Always work directly on main in `/Users/jordan/Sites/simple-form`."* This mirrors this very repo's own `CLAUDE.md` (`/Users/rexc/Sites/prd-to-product`), so it is **intentional for a single-dev local project, not a bug** — but there is no guard and no note about the cost when the repo is shared or cloned to a different machine, where an absolute path is dead. **This is a decision to make, not an auto-fix:** should generated files use a portable reference (repo-relative / "this repo") instead of an absolute path? Reversible prose-in-a-template, so a backlog decision, not a council fork.

### F-02 — "Plausible / Silent / Grounded" as the bar for a cited failure mode · soft refinement (Lens A) — parked

The triad appears **three times** across `intent` (`generate-skill:308`, `domain-discovery:451-456`, `tree-generator:412`) as *the* quality bar for a failure mode: **Plausible** (an agent would generate it), **Silent** (no immediate crash), **Grounded** (traceable to a doc/source/issue). Sharpens this repo's "every rule cites its failure mode" from a presence-check into a quality bar. Folds into CE-2 as the filter on elicited answers; optionally sharpens `principles.md`. Parked — fold in on the next templates/principles edit.

### F-03 — Cross-model skill-authoring checklist · soft, adapt-not-adopt (Lens B) — parked

Canonical version at `tree-generator:818-830`: skills consumed by Claude/Cursor/Copilot/Codex should use no XML tags in the body, **positive over negative** instructions, critical info at section *edges* (not buried), keyword-packed routing descriptions, concrete values over placeholders, self-contained except declared `requires`. On-lens (this repo ships to Claude **and** Codex). **Caveat, not papered over:** "positive over negative" partly conflicts with this repo's deliberate `EXPLICIT-INVOKE — do NOT auto-select` markers, so this is adapt-not-adopt. Parked — fold in on the next template edit.

---

## Considered and folded (not minted as rows)

- **Skill-*triggering* measurement (eval graders).** `failure-classifier.ts` defines a clean 6-way taxonomy of skill-discovery outcomes — `strict-success` · `wrong-skill-selected` · `command-attempted-but-failed` · `reference-only` · `no-discovery-attempt` · `harness-error`. Two sharp operational definitions: **strict invocation** = the agent *actually ran* the load, binary, no partial credit (`strict-invocation.ts:13`); **`reference-only`** = the agent *talked about* the right skill but never invoked it → a **named failure** (`reference-only.ts:14-19`). This is a ready-made rubric for measuring whether *this repo's own* skills fire when they should → **fold into the paused `furnace-trial` resume context** ([D-052](../DECISIONS.md)), the same way the loops-article accept-rate metric was folded. The `reference-only` concept also resonates with this repo's "claiming done vs. actually doing" discipline (an agent that cites a rule without applying it has failed in a specific way) — worth remembering even outside measurement.
- **Audience-aware trust routing** (`source-policy.ts:112-114`): when the consumer is the agent, `intent` refuses to dump unvetted skill candidates into agent context and instead routes the human to review out-of-band. Loosely echoes `/mine`'s propose-and-wait + treat-sources-as-untrusted. Note, not a row.
- **Deterministic-core / agent-edge split** (`staleness/check.ts:533`): the staleness check computes every cheap local signal (semver drift, source-list drift, artifact coverage) and explicitly *defers* the expensive remote-SHA check to the agent with `needsReview: true`. Plus an orphan detector (`buildWorkspaceCoverageSignals` — "a package exists but nothing covers it"). `check-live-links.py` already embodies "deterministic, on-demand"; the orphan direction (exists-but-uncovered) is a minor possible complement. Note, not a row.
- **Staleness via `sources:` frontmatter + impact-classification table** (no-impact / version-bump / content / breaking; "silent when nothing changes"; one-cascade-level) — dedups with `check-live-links.py` + the living-document-lifecycle. Note, not a row.

## Checked and confirmed NOT a gap (convergent design — recorded so it isn't re-mined)

- **STOP gates / anti-auto-answer in interactive intake.** `intent` uses explicit `── STOP ──` gates and "hard rules override all reasoning" because models barrel past interactive checkpoints. `intake.md` already nails this: cluster-at-a-time, and Cluster 0 explicitly forbids silently absorbing a visible PRD (*"Silent absorption is the failure mode"*). No change needed.
- **Codex blocking-hook scoping.** `intent` scopes blocking hooks to Claude/Codex per their hook locations and notes "Codex hook interception is not a complete security boundary." `context-engineering` already scopes emitted hooks to Claude (`.claude/`) and gives Codex guidance-only — convergent. *Capability note for later:* Codex blocking hooks are now feasible (`.codex/hooks.json`; Codex's edit tool is `apply_patch`, not `Edit` — `hooks/policy.ts:14`), so a future Codex-gate enhancement is possible.
- **Flat-vs-nested / minimal-library structure sizing.** `tree-generator`'s "fewer than 5 skills → flat, no router" maps to `context-engineering` already sizing output (small/medium/large; flat/modular). Convergent.

## Consolidation (per `/mine` "merge skeptically — record the merge")

Seven findings → **three board rows** pointing here, matching this repo's bundling precedent (cf. "Superpowers liftables"):

1. **Intake upgrades** (CE-1 + CE-2) — both are `intake.md`/generator improvements, same file, same work.
2. **Scaffold path-portability decision** (F-05) — kept separate; it's a decision, not a build.
3. **Skill-authoring upgrades** (F-01 + F-02 + F-03) — all skill-authoring discipline, all parked.

## Coverage statement (honest)

Read ~18 of ~160 files — but **all the IP-bearing ones**: both meta-skills (`domain-discovery`, `tree-generator` — the methodology), `validate.ts`, `trust-model.md`, `overview.md`, `guidance.ts` + `policy.ts` (guidance/hook injection), `intent-hooks.md`, `source-policy.ts`, `staleness/check.ts`, and the eval graders. **Not deep-read** (judged lower-yield, with evidence): `install/command.ts`, the per-agent hook adapters, `scanner.ts` internals (confirmed pure discovery mechanism — `scanner.ts:1-70`), `fs-cache.ts`, the `configuration`/`registry`/`cli/*` docs, and the test suite. The methodology veins are exhausted; the yield curve flattened on the mechanism pass (one upgrade + two notes vs. two headline findings from the meta-skills). Stopped deliberately rather than perform exhaustive coverage.
