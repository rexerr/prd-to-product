# Retro — 2026-06-18 ~18:50 CDT — Wave-2 Sprint 3, DG-01 even-coverage synthesis rule (9th session of the day)

## What was completed

Adopted **DG-01** (designer-lane crib) as a new **conditional modular `.claude/rules` scaffold** the generator emits: `synthesis-even-coverage.md`, guarding multi-source synthesis against primacy/recency bias. Authored through `/furnace-plan`; Cowork-reviewed across **three rounds** plus a self-caught implementation-read correction. See [D-040](../DECISIONS.md) for the full decision; not restated here (CF-06).

- New template `templates/claude-rules-modular/synthesis-even-coverage.md.template` (conditional `product-rules`-style header, body cites its failure mode). **Modular-only (option a)**, gated `rule_shape == "modular" and include_synthesis_rule`; **always-on when emitted** (no `paths:` frontmatter).
- Wired: State-map row + Per-template inclusion row + `## Even-coverage synthesis rule (conditional)` gating note in `decisions.md`; **Q35a** (Cluster 6, after rule-shape determination) + marker-map entry in `intake.md`.
- Four modular fixtures updated for suppression (medium/large transcripts' Cluster-6 capture + transcript-large "Not written" + both abbreviated trees, each at **both** `product-rules` enumeration sites). Flat `output-small` / `transcript-small` deliberately untouched — verified byte-unchanged.
- Bookkeeping: DG-01 → `Adopted (→D-040)`; roadmap marker + BACKLOG S3 line updated; `DECISIONS_ACTIVE.md` reconciliation marker bumped D-035 → D-040 (was stale by five decisions).

## Failure this session

- **Tag:** none (product) — shipped clean, every defect caught **before** the product commit by the furnace/Cowork loop. But the loop caught real authoring misses worth naming.
- **Name the artifact.** rev-3 plan asserted "`rule_shape` is resolved before Cluster 5, so gate Q27c there" — built on enumerating **three** of the four modular triggers (`decisions.md:179-186`) and **missing `len(workflows) > 1`**, which depends on Q30 (Cluster 6). The Cluster-5 placement was mechanically unevaluable. Neither the furnace preflight nor Cowork's first two rounds reached it; it surfaced only when I read the actual cluster ordering to write the wiring.
- Lesson→change jump:
  - **Tool or agent?** Agent — furnace Check 1 ("cite every codebase claim to a read") was satisfied in *letter* (I read the trigger list) but not in *spirit* (I didn't enumerate **all four** members before claiming the set's timing). This is the **same under-enumeration class as Cowork Round 1** (the missed fixture/State-map sites) — a recurring "asserted a set is complete without checking every member" miss.
  - **Does it generalize?** Yes, and it now has multiple instances: Round-1 fixture under-count, the rev-3 trigger under-count, and the two Round-3 must-fixes (each `product-rules` appears **twice** per file; I named one). The throughline: **completeness claims ("all sites", "resolved before", "no X exists") need an exhaustive grep behind them, not a representative one.**
  - **→ The change it demands:** Candidate — extend furnace Check 1 to name *completeness/enumeration* claims explicitly ("when you assert a set is complete — all call sites, all triggers, every occurrence — grep for every member and paste the count"). Pairs with the already-logged string/equality-precision candidate. Hold at **propose** for the trial review; this is the third adjacent data point but the fix touches the gated furnace SKILL.md.
- **Furnace-trial signal (rich this session).** Three Cowork rounds hit **three different classes** — Round 1 bucket-1 (under-enumeration + a path-string miss), Round 2 bucket-2 (the flat+yes logic dead-end), Round 3 two bucket-1 completeness must-fixes + three bucket-3 refinements — **plus** a fourth class neither layer caught: an **ordering bug** found only by the implementation read. Strongest data point yet that some classes need a *third look* (the implementation read itself), beyond preflight + Cowork. Logged for the trial review.

## Files changed

Three product files (one new template + decisions.md + intake.md) + four modular fixtures + five bookkeeping files (DECISIONS, designer crib tracker, roadmap, BACKLOG, DECISIONS_ACTIVE) + this retro. Exact paths in `git status` (the approved plan lived in plan-mode scratch outside the repo); not enumerated here (CF-06).

## Key decisions made

- [D-040](../DECISIONS.md) — DG-01 adopted as a conditional modular scaffold, option (a) modular-only, Q35a Cluster-6/modular-gated. Not mirrored to `DECISIONS_ACTIVE.md` (template/generator content; D-039 precedent).

## Open items

- **Furnace Check-1 sharpening** — two candidates now logged at *propose* (string/equality precision from CF-03; completeness/enumeration from this session). For the next trial review to weigh against the scorecard; not adopted (gated SKILL.md edit, mid-trial instrument).
- **Pre-existing broken link** — `docs/cribs-from-designer-skills.md:37` (DG-02 row) links `[D-030](../DECISIONS.md)`, which resolves above the repo root; the file sits at `docs/` root so it should be `DECISIONS.md`. Left unfixed (out of scope); flagged for a separate sweep.
- **Wave 2 continues.** S3 remaining: CF-13 + G-14\* + AB-03; then S4 DSB (G-19), solo CF-07.
- **Commit hygiene** — Cowork's 5-row append to `skills/furnace-plan/trial-ledger.md` gets its **own dedicated** "Sweep Cowork ledger append" commit *before* the product commit (D-018 carve-out).
- **No push this session** — commits staged locally; push when asked.

## Next session

- Continue S3 — next is **CF-13** or **G-14\*** (the latter is the ~40-file provenance-banner sweep with the JSON-can't-comment fork, needs its own scoping). Open with `/furnace-plan` for either.
