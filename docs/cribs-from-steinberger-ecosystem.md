<!-- Last mined: 2026-06-17 (Round 3 + completeness pass; C-01–C-41) · Update this header on every re-mine -->

# Cribs from the Steinberger / mvanhorn ecosystem

Process and governance patterns mined from two repos that mirror this workspace's machine
(generator + verify + retro loop), plus the upstream rulebook they descend from. The goal is
**import scar tissue, not reinvent it** — these authors have run the same loop at far higher
volume and wrote down what broke.

> **Adoption sequencing** for this sheet is unified with the other crib trackers in
> [`cribs-adoption-roadmap.md`](cribs-adoption-roadmap.md) — that's where waves, the adoption
> lifecycle, and verification classes live. This sheet stays the inventory + status of record.

This is a **living adoption-tracker**, not a one-shot summary. Each crib has a stable `C-NN`
ID, the failure it prevents, where it lands in this repo, an effort estimate, and a status.
Promote a crib to a `D-NNN` decision (and an actual edit) when adopted; mark it `Declined`
with a one-line reason when it doesn't fit.

> **Why this exists.** Our own `CLAUDE.md` already does "every rule cites its failure mode" —
> and one of these repos independently re-derived that same doctrine. The architecture instinct
> is sound; the gap is *reps*. This doc closes the rep gap by borrowing other people's bugs.

## Sources mined

| Repo | What was read | Nature |
|---|---|---|
| `mvanhorn/cli-printing-press` | README, `CONCEPTS.md`, `docs/PATTERNS.md`, main `SKILL.md`, **all ~60 `docs/solutions/` cards**, ~25 `docs/retros/` | A skill-generator repo — direct mirror of this workspace |
| `mvanhorn/agentcookie` | `docs/plans/`, runbooks, `docs/audits/`, `threat-model.md`, `handoff-guides/`, `skill/SKILL.md` | A *shipped app* — shows the same author scaffolding product code, not skills |
| `steipete/agent-rules` | README + rule files | **ARCHIVED / superseded** by `agent-scripts` — the philosophy fossil |
| `steipete/agent-scripts` | READMEs, skills, rules, enforcement scripts | His **live** rulebook (~50 skills + executable guardrails). The headwater's current practice |
| `mvanhorn/last30days-skill` | Full SKILL.md (~1,835 lines), reference splits, contract tests | His most-adopted skill (43k★) — mined for SKILL.md *craft* |
| `*/` enforcement layer (Round 3) | `.claude/` hooks + settings, `committer`, validate-skills, docs-list/skill-list validators, drift checks | Across agent-scripts + cli-printing-press + agentcookie — mined for deterministic gates |
| `mvanhorn/printing-press-library` | Taxonomy, per-entry manifests, generated catalog, publish flow | Collection org — how a skill *family* stays navigable |
| `nexu-io/open-design` | `skills/` + `design-systems/` + `craft/` triad, `token-schema.ts` | Multi-skill-family org + 4-layer design tokens |

**Lineage note.** The patterns here are an *ecosystem consensus*, not one person's doctrine:
**Steinberger (philosophy) → Van Horn + Trevin (productized as the Printing Press) → OpenClaw**.
Matt Van Horn is a repeat founder (June → Weber; an earlier co → Lyft); credible, but his own
`agentcookie`-vs-generator split proves the real meta-rule is *fit the scaffold to the product*,
not "one true way." Adopt by product-fit; don't cargo-cult.

## The meta-theme

Every corpus independently converged on one spine:

> **Stable IDs + a persistent ledger + a mechanical gate beats prose every time.**
> Instructions are ~70–90% reliable under load; a gate is 100%. Demote "be thorough" into
> something a binary — or a `grep` — can check.

---

## Decisions & leanings (Rex, 2026-06-17)

Direction set while mining is still in progress. Each **graduates to a formal `D-NNN`** in
`docs/DECISIONS.md` at execution time — recorded here so the intent isn't lost between sessions.

1. **`AGENTS.md` becomes canonical; `CLAUDE.md` becomes the Claude-specific extension/pointer.**
   Reverts Rex's original intent (the CLAUDE.md-canonical arrangement was a later change he didn't
   argue against). Rationale: the workspace is cross-tool (Codex, Cowork) and a tool-neutral source
   of truth is correct for that. Resolves the divergence-audit open question. *Execution is a real
   migration* — every "see CLAUDE.md" reference, the pointer direction, and the mirror rules flip.
   → council-grade was the bar to *decide*; the decision is made, so execution is now a planning task.
   **Generator half executed 2026-06-20 (→ [D-047](DECISIONS.md)):** the `context-engineering` skill
   now scaffolds AGENTS-canonical for *both* rule shapes (flat joined modular). **This-repo half still
   deferred** — Rex scoped D-047 to generator output only; migrating this workspace's own root files
   remains the ~75–90-cross-reference planning task.

2. **Keep D-001 (markdown-only); invest in hooks-as-gates for determinism.** No tension between the
   two: markdown stays the output substrate, hooks (shell, wired in `settings.json`) are the
   markdown-native enforcement layer, extending the existing D-006 write-guard. Adopt the
   "executable enforcement over prose" spirit (C-23) **without** shipping binaries. D-001 is *not*
   unmade.

3. **~~Build the `solutions/` scar-tissue library.~~ CLOSED don't-build ([D-063](DECISIONS.md#d-063),
   2026-06-23).** Was billed the biggest unbuilt thing and a deliberate forward investment. Closed
   after the 2026-06-09 [self-healing-loop council](council/council-transcript-2026-06-09-self-healing-loop.md)
   (5/5 build-nothing on the structurally identical capture/tag/count system) + an empirical scan of all
   56 retro failure-sections: the log is mostly healthy and a *one-time* scan found everything a standing
   library would, so the lever is **periodic aggregation, not a card library**. CF-05 parks with it.
   Revisit only as a scaffold-emit for high-error project types (rides AB-01's [D-009](DECISIONS.md#d-009)
   gate), or if a 2nd scan finds a hidden pattern (→ mint a recurring scan ritual).

---

## Adoption table

Grouped by the surface it lands on. Status legend: **Proposed** · **Adopted** (→ links the `D-NNN`) · **Declined** (with reason).

### furnace-plan + the Cowork review loop (hot path)

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-01 | **`R<n>` / `KTD<n>` citation graph** — every requirement and key-decision gets a stable ID; every plan unit, acceptance criterion, and verification-ledger line *cites* it | A requirement silently dropped between plan and execution. Makes the plan mechanically attackable — Cowork can grep for an `R` with no unit, or a verdict with no evidence | Medium | **Deferred → watching** (→ [D-062](DECISIONS.md#d-062)) — real additive mechanism but the dropped-requirement failure is unobserved and it adds per-plan ceremony at n=1; build on a logged failure or a 2nd author |
| C-02 | **Anti-bulk-accept primitives** — per-item pre-decision fields filled *before* the verdict; reject N+ identical rationales; tie a numeric end-state gate to the score | You (or Cowork) waving through findings with one copy-pasted "systemic, won't fix" punt | Medium | **Deferred → watching** (→ [D-062](DECISIONS.md#d-062)) — real surface (the Subagent-review-log disposition step) but no bulk-decline observed; build on a logged failure or a 2nd author |
| C-03 | **Riskiest-assumption-first** — the single load-bearing assumption gets a *code-free experiment* as the first unit, before anything downstream commits | A plausible-but-wrong premise surviving into implementation and forcing a rewrite. A lighter, in-plan cousin of D-009's council rule | Small | Proposed |
| C-04 | **Absent evidence = HOLD, not pass; = N/A, not a midpoint** — parse a narrow explicit verdict line, never loose prose; missing evidence leaves the denominator | An epistemic unknown silently becoming either a free pass or a quiet `5/10` penalty | Small | Proposed |
| C-05 | **One interpretable failure mode per check** — dry-run mutating probes by default; split "rejects bad input" into its own check | 50 of 56 checks failing for one non-product reason, drowning the real signal in the ledger | Small | Proposed |

### context-engineering (the generator)

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-06 | **Scaffold fits the project *kind*** — the same author runs the full CLAUDE.md/CONCEPTS/DECISIONS stack for his skill-generator and *zero* of it for his shipped app (governs via plans + runbooks + threat-model instead) | The generator cargo-culting one canonical tree onto every project. An app should get plans+runbooks; a skill-repo gets CLAUDE.md+DECISIONS+retros | Large | Proposed |
| C-07 | **Destructive-regen safety** — fail *before* mutating; keep the snapshot recoverable until merge succeeds; same-lineage hash guard; every verdict defaults to a loud error; validation never mutates the dir it validates | **Silent data loss** when regenerating into a hand-edited repo — the worst failure for a generator; trust dies the first time. Partially covered by D-005/D-006 write-guard; verify the fail-before-mutate + lineage-guard legs exist | Medium | **Closed don't-build** (→ [D-060](DECISIONS.md#d-060)) — verified against the live hook: fail-before-mutate / loud-default / read-only-validation covered literally; lineage-guard purpose served by the session-id safety key; recoverable-snapshot served by prevention + git (both literal mechanisms N/A for a one-shot scaffolder). |
| C-08 | **Golden "should-NOT-change" fixture** — every rewrite/dedupe pass ships a fixture asserted *untouched* | An over-eager transform mangling correct input while passing collision-only tests | Small | Proposed |

### CLAUDE.md + docs discipline

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-09 | **Retro "→ durable work unit" columns** — add to the retro template: *was it the tool or the agent? · does this generalize? · → the concrete change it demands* | Retros that narrate the session but never feed back into the generator, so the class recurs. Today's template stops at "Next session" (continuity) — it never forces the lesson→change jump our thesis runs on | Small | Adopted (→ [D-024](DECISIONS.md)); scaffold-emit backport → [D-039](DECISIONS.md) |
| C-10 | **Freshness / sync marker on deliberate duplications** — a `<!-- synced: D-NN @ date -->` (or "highest mirrored ID") line on curated mirrors like `DECISIONS_ACTIVE.md` | `DECISIONS_ACTIVE.md` mirrors `DECISIONS.md` by a manual rule with *zero drift detection* today; a forgotten mirror goes silently stale. (Adopt the freshness half only — the pure "each fact in one file" invariant conflicts with our intentional active-view design) | Small | Adopted (→ [D-026](DECISIONS.md)) |
| C-11 | **Numeric "3+ occurrences" gate before minting a rule** — codify a pattern only after it appears in 3+ places (his `continuous-improvement` rule; our existing "Rule of Two" in D-008 is the same instinct) | Premature abstraction — minting a guardrail from a single instance. The *create-side* complement to our retro-tag pruning, which only handles the *remove* side | Small | Proposed |
| C-12 | **On-demand commands vs always-on constraints** — externalize occasional procedures into invokable skills/commands instead of paying context rent for them every turn in an always-on file | A bloated CLAUDE.md burning tokens every turn for procedures needed only occasionally | Medium | Proposed |
| C-13 | **Cross-repo handoff as a standalone build-spec** — a per-consumer guide with a field-mapping table + idempotency/override contract (`# manual-override` marker → skip + warn) | A downstream agent (Codex, or Cowork in another repo) acting on context it doesn't have; non-deterministic regeneration clobbering hand edits | Medium | Proposed |

### Round 2 — skill craft + live rulebook (mined 2026-06-16)

From `last30days-skill` (SKILL.md craft) and `steipete/agent-scripts` (the live, executable rulebook).

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-14 | **Dated, named, quoted-artifact failure tags** — tag each rule with the *specific run* that proves it (date + topic + the exact bad output), not a generic failure mode | Rules decaying into unverifiable platitudes; you can never answer "do we still need this rule?". Direct upgrade to our existing "cite the failure mode" doctrine — and it's also the delete-signal | Small | Adopted (→ [D-025](DECISIONS.md)); scaffold-emit backport → [D-039](DECISIONS.md) |
| C-15 | **Hoist binding contracts to the top of the file** — load-bearing rules / output contracts go *above* the body; justify by attention budget, not file size | The binding rule never entering context before the agent acts (long SKILL.md; model never reaches the rule). Real incident: rules at line 1094 never reached before synthesis | Small | Adopted (→ [D-028](DECISIONS.md)) |
| C-16 | **Decision-ready handoff brief — never escalate a bare question** — do all autonomous work first, then present plain-language stakes + completed proof + an *opinionated recommendation* + the exact options | Offloading analysis onto Rex/Cowork at the decision point; "what do you think?" with no homework. The strongest single steal for the furnace-plan handoff | Medium | Adopted (→ [D-031](DECISIONS.md)) |
| C-17 | **Description = capability + concrete-noun claim; triggers → `argument-hint`; negative scope repeated in the body** | Trigger-stuffed descriptions diluting auto-invocation signal; a boundary stated at selection-time but not where the agent actually acts | Small | Proposed |
| C-18 | **Post-generation self-check with literal grep targets** — e.g. "scan the last 15 lines for `Sources:`; if found, delete before emitting" | A rule stated but never enforced at emit time (his note: three tiers of reinforcement weren't enough; the grep self-check was the fourth) | Small | Proposed |
| C-19 | **Pointer files, never copies, for shared rules** — downstream configs are one-line pointers to one canonical source; repo-local rules sit *below* the pointer | Shared rules drifting across tools/repos; one fix needing N edits. Sharpens C-10 and raises the AGENTS.md-first question (see Divergence audit) | Small | Proposed |
| C-20 | **Doc front-matter as a machine-checked contract** — every doc carries `summary:` + `read_when:`; a validator fails the build if either is missing | Docs nobody knows when to read; freshness headers that don't *route*. Upgrade to C-10 | Small | Proposed |
| C-21 | **Skill-budget hygiene audit** — skills cost ~2% of context each; periodically flag unused / near-duplicate / over-long-description skills and trim | Skill sprawl silently eating context budget and degrading auto-routing | Small | Proposed |
| C-22 | **Provenance + confidence vocabulary in reviews** — tag each claim `clear / likely / unknown` and `introduced-by / made-visible-by / carried-forward-by`; write "not proven" rather than guess | Confident-sounding root-cause claims with no evidence trail — exactly what the Cowork reviewer hunts for | Small | Proposed |
| C-23 | **Executable enforcement over prose reminders** — a `committer` wrapper that refuses `git add .` / empty messages and runs validation in the commit path; assert skill contracts in tests (version sync, single SKILL.md) | Wrong files staged; frontmatter/version drift shipping silently; rules trusted but never checked. The markdown-native version of the printing-press's gate > prose | Medium | Proposed |
| C-24 | **Oracle-style external consult** — a structured one-shot to a stronger model with a stands-alone prompt (assume zero project knowledge), a token budget, and an explicit consent gate | Throwaway consults that waste the call because project context was assumed. Complements the D-009 council (internal, multi-perspective) with an external single-brain option | Medium | Proposed |
| C-25 | **"You ARE the X" anti-improvisation preface** — name the wrong mental model the agent might silently adopt, and forbid it ("you are the planner, not the reviewer"; "don't treat this as a search keyword") | The agent silently downgrading to a generic version of the task | Small | Proposed |

---

### Round 3 — enforcement, family organization, design tokens (mined 2026-06-17)

These directly serve the three decisions above: enforcement = the *how* of hooks-as-gates (#2);
family-org = the structure the solutions library (#3) and a growing family need.

**Enforcement / hooks** (decision #2):

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-26 | **`permissions.deny` for `git commit/push --no-verify`** — two lines in `.claude/settings.json` | An agent disabling your hooks/validators to "just get it committed." Makes every other gate non-bypassable | Trivial | Proposed |
| C-27 | **pre-commit → frontmatter validator** — globs `skills/*/SKILL.md`, strict-YAML parses, fails on missing/empty `name`/`description`, malformed frontmatter, or **duplicate `name` across skills**; same script in CI | A skill that silently won't load, or two skills colliding on `name`. The single highest-value skill-repo gate | Small | **Adopted ([D-017](DECISIONS.md)) 2026-06-17** — shipped as a PreToolUse `Bash` hook (`.claude/hooks/validate-skills.sh`), not a git pre-commit/CI; v1 is structural + cheap-syntactic, not full YAML (narrowing recorded in D-017) |
| C-28 | **`committer` commit-path guard** — wrapper rejecting `git add .`, empty messages, and a file-path-as-first-arg; restores staged first so only named paths commit | `git add -A` sweeping unrelated work into a commit. Enforces the ≤3-file scope rule *mechanically* | Small | Proposed |
| C-29 | **Generated-list-in-sync assertion** — a marker-fenced region must `deepEqual` the filesystem; CI fails on drift | The CLAUDE.md "Where to look" table or `DECISIONS_ACTIVE.md` mirror drifting from reality. **Mechanical successor to C-10's manual marker** | Small | Proposed |
| C-30 | **Generator-purity gate** — grep comment-stripped generator templates for a blacklist of source-domain tokens (`app/`, token names, sample vocabulary); fail on any hit | Violations of architecture rule #3 ("scaffolds shape, not content") leaking into emitted templates | Small | Proposed |
| C-31 | **PostToolUse frontmatter nudge** — on `Write\|Edit` of a `*.md`, instantly check frontmatter shape (advisory) | Drift accumulating silently until commit/CI hours later | Small | Proposed |

**Skill-family organization** (the growing family + the C-3 solutions library):

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-32 | **Index is a generated artifact from per-entry manifests; hand-edits CI-blocked** — counts, category table, search all fall out of one invariant | The index lying about what's on disk; merge conflicts on regen. Best collection-org steal | Medium | Proposed |
| C-33 | **Per-skill metadata manifest** — `skill.meta.json` beside each SKILL.md: version, category, owner, status, provenance | Attribution/provenance becoming folklore; no machine source for the index | Small | Proposed |
| C-34 | **Three orthogonal axes — shape/process vs shared craft** — cross-cutting rules live once in a shared layer skills opt into by reference, not copy-pasted into each SKILL.md | The same rule drifting across N skill bodies as the family grows past 4 | Medium | Proposed |
| C-35 | **Explicit one-page merge bar** — a fixed pre-add checklist every new skill clears (working example, concrete triggers, single-folder shape) | Quality dilution + overlap as the family grows | Small | Proposed |
| C-36 | **`proofs/` dir per skill** — pair each skill with its dry-run diff + retro, keyed to a run/date | "Is this tested / where did it come from" being un-auditable | Small | Proposed |

**Design-system craft** (`design-system-bootstrap`):

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-37 | **4-layer token contract with a promotion path** — classify every token: identity / required-structure / defaulted / slot-alias / brand-extension; explicit C→B→A promotion when a default emerges | "Is this token required?" ambiguity → over-specified or dangling-`var()` token files. Biggest design-system steal | Medium | Proposed |
| C-38 | **Emit a complete, self-resolving `:root`** — every token resolves with no external defaults sheet, because agents paste one brand's block into a single artifact `<style>` | Token files that break the moment they're pasted into a self-contained artifact — exactly our markdown-only delivery | Small | Proposed |
| C-39 | **Pair compiled `tokens.css` with a fixed-section `DESIGN.md` prose companion** — CSS is the machine contract; prose tells the agent *when* to use each token | A token dump with no rationale, or prose with no enforceable values | Small | Proposed |

---

### Round 1 completeness pass (recovered 2026-06-17)

Back-filled after a sweep found these were surfaced in conversation (from direct reads of the
printing-press `SKILL.md`) but never written into the doc during the original curation.

| ID | Crib | Failure it prevents | Effort | Status |
|---|---|---|---|---|
| C-40 | **Never quote human-time estimates** ("an afternoon", "~15–30 min", "quick fix") — describe scope instead: files touched, lines, relative size, or token/session cost | Estimates that are both wrong and trust-eroding. The *agent* does the work, so a wall-clock figure is fabricated — and "an afternoon to build" trains the user to distrust the output. The carve-out is genuinely time-bound external things (a CI run, an install) | Small | Proposed |
| C-41 | **Optimize for time-to-ship, not time-to-document; don't split one idea across multiple mandatory artifacts** — the printing-press v2 rewrite *deleted* mandatory research docs because they surfaced failures late | Over-scaffolding: ceremony artifacts that delay shipping and fragment one idea across files nobody reconciles | Small | Proposed |

**Reviewed and deliberately left as context, not cribs** (framing/principle, not actionable to-dos — pull in if wanted): the *agent-native dual-surface* principle (you cut dual-surface scope), the *emboss/polish/reprint + retro-vs-polish* vocabulary, and the *"secret identity / creativity ladder / absorb-and-transcend"* philosophy (it already informs the Divergence audit's spirit).

---

## Divergence audit — shared spirit, different practice

The question that matters isn't "what do we do differently from Van Horn/Steinberger" — it's
**"where does our product shape genuinely differ, and is each divergence justified by that, or
just inertia?"** Their own practice varies by product (Van Horn runs a full governance stack on
his generator and *none* on his shipped app), so fit-to-product is the rule, not imitation.

| Shared goal | Their practice | Our practice | Verdict |
|---|---|---|---|
| Plan before building | Dated, numbered, `R/KTD`-ID'd plans, persisted + cited | furnace-plan authors → Cowork attacks → not persisted/ID'd | **No justification. Adopt (C-01).** |
| Enforce quality, don't request it | Ship Go binaries / scripts that mechanically gate | Markdown-only (D-001) + one hook | **Half-justified.** Our product *is* markdown (symlink-installed, no build); a binary gate can't ship to a skill consumer. But the spirit transfers via **hooks**, which we under-use (C-07, C-23). Keep substrate, steal gates. |
| De-risk the expensive fork | Code-free experiment as plan unit U1 (`KTD1`) | Recommend a multi-LLM council (D-009) | **Both, different domains.** Council = irreversible product/architecture forks. KTD1/Oracle (C-03, C-24) = risky technical assumptions. We're missing the cheap technical one. |
| Control scope | Three-bucket (in/deferred/out) + route late finds to a friction log | Hard numeric caps (≤3 files / ≤50 lines) | **Both valid, complementary.** Theirs routes creep; ours caps size. |
| Collaboration hygiene | Full PR discipline — templates, review bots, mergify | Direct-on-main (D-002) | **Strongly justified. Keep.** They have contributors + CI; we're one person. Correct divergence. |
| Regression safety | Golden tests + verify harness + CI | Hand-written example output trees, no runner | **Partially justified.** No CI is fine solo; but we under-use golden "should-NOT-change" fixtures (C-08) and contract tests (C-23). |
| Close the learning loop | Retros → generator changes; a `solutions/` scar-tissue library | Retros → durable work units (C-09 adopted, D-024/D-039); periodic aggregate scan over the retro failure-log | **C-09 adopted.** The `solutions/` library was **closed don't-build** ([D-063](DECISIONS.md#d-063)) — at this repo's volume a one-time scan beats a standing library; the loop closes via periodic aggregation, not a card collection. |
| Source-of-truth file | **`AGENTS.md` canonical**, Claude/Codex/Cursor symlink to it (tool-neutral) | **CLAUDE.md canonical**, AGENTS.md a thin pointer | **DECIDED 2026-06-17 — flip to AGENTS.md-canonical** (Rex; reverts his original intent). **Generator half DONE 2026-06-20 (→ [D-047](DECISIONS.md));** this-repo half deferred. See Decisions & leanings. |

**The one not to unmake:** D-001 (markdown-only) is the decision most tempting to drop under their
influence and the most justified by product shape. The upgrade is *not* "ship binaries like them" —
it's "use hooks as the markdown-native gate." Touching D-001 is a council-grade fork, not a casual unmake.

---

## Recommended sequencing

Two batches, split by effort — not by importance.

**Cheap batch (do first — each a sub-50-line edit, each closes a live latent failure):**
- C-09 retro "→ work unit" columns
- C-10 `DECISIONS_ACTIVE.md` freshness marker
- C-14 dated/named/quoted-artifact failure tags (upgrades our core doctrine)
- C-15 hoist binding contracts to the top of each SKILL.md

**High-value medium (do soon — biggest single upgrade to the hot path):**
- C-16 decision-ready handoff brief for furnace-plan → Cowork/Rex

**Expensive batch (do deliberately — real build work on the hot path):**
- C-01 R/KTD citation graph
- C-02 anti-bulk-accept primitives
- C-07 destructive-regen guard (after confirming what D-005/D-006 already cover)

**Open question to resolve before it ossifies:** the AGENTS.md-first vs CLAUDE.md-first
source-of-truth inversion (see Divergence audit) — council-grade, given Codex + Cowork use.

Everything else is opportunistic.

---

## Known blind spots — what we deliberately did NOT mine

A crib sheet that doesn't name its own gaps is lying. Ranked by likely value:

1. ~~`steipete/agent-scripts`~~ — **MINED 2026-06-16** (R2). C-14–C-25 + the source-of-truth inversion. Lesson: prose → *executable enforcement* → routable ~50-skill system.
2. ~~`mvanhorn/last30days-skill`~~ — **MINED 2026-06-16** (R2). SKILL.md craft (C-14, C-15, C-17, C-18, C-25).
3. ~~`mvanhorn/printing-press-library`~~ — **MINED 2026-06-17** (R3). Collection org (C-32, C-33, C-36).
4. ~~`nexu-io/open-design`~~ — **MINED 2026-06-17** (R3). Skill-family org (C-34, C-35) + design tokens (C-37–C-39).
5. ~~Hooks / `settings.json` enforcement~~ — **MINED 2026-06-17** (R3). The gate set (C-26–C-31).
6. **The CLI-craft fleet** (`sonoscli`, `summarize`, `bslog`, etc.) — **deliberately excluded**, not a gap. Agent-native-CLI exemplars; revisit only if a real project needs a token-efficient agent tool over an API.

**Mining is effectively complete** — the high-value veins (process, craft, enforcement, org, tokens)
are drained across three rounds. Further reads would be confirmation, not discovery.

## Provenance

Generated from a 2026-06-16 session mining the repos above via subagent fan-out (three parallel
readers, each returning deduped conclusions). Not a substitute for reading the source cards when
adopting a specific crib — follow the trail before committing a `D-NNN`.
