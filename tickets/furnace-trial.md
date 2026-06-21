---
slug: furnace-trial
status: active
title: Furnace-plan trial — Cowork-graded experiment
---

# Furnace-plan trial

The `furnace-plan` skill ([`skills/furnace-plan/`](../skills/furnace-plan/SKILL.md), explicit-invoke) self-applies a verification preflight before `ExitPlanMode` and appends a `## Verification ledger` to the plan. It is a **pre-filter, never a replacement** for Cowork review — Rex catches none of these errors himself, so Cowork stays the authoritative reviewer and the only valid oracle. The trial measures whether the mechanical layer earns its keep.

## Current state

- Positive path fires end-to-end: the CF-03 run produced the first two non-backfilled Cowork rows (2026-06-17). Ledger at [`skills/furnace-plan/trial-ledger.md`](../skills/furnace-plan/trial-ledger.md) — 20 rows.
- Check 1 sub-case **1a** (string-equality + re-read-at-write-time) landed 2026-06-18.
- Blind in-session `Explore` reviewer wired every pass ([D-043](../docs/DECISIONS.md)); Cowork remains sole ledger writer.
- **First live `cc-subagent` rows on a self-authored furnace plan: 2026-06-20** (the [D-049](../docs/DECISIONS.md) lifecycle-port plan). Blind subagent → `## Subagent review log` → Cowork transcribed 4 `cc-subagent` rows + 5 `cowork` rows. **Taint signal:** Cowork (seeing the subagent log on the twice-baked plan) still caught a Must-fix the subagent missed — division of labor holds, low anchoring; argues against "subagent writes the ledger" (D-043 stands).
- **First calibration pass: 2026-06-21** (CF-29 PRD-FORMAT pilot, [D-052](../docs/DECISIONS.md)). Blind cc-subagent (round 0, on the raw plan) → **0 must-fixes**; Cowork → **5 must-fixes** across 4 rounds. Strong divergence — the pre-filter caught none of Cowork's must-fixes on this plan: argues the cc-subagent is a pre-filter, not a Cowork substitute (D-043 stands), and *for* keeping Cowork the oracle. **Mechanics wrinkle found:** withholding the subagent log from Cowork (to keep its raw review untainted) also blocks Cowork — the sole writer — from transcribing `cc-subagent` rows, so this plan's ledger has 10 `cowork` rows and **0 `cc-subagent` rows** (see Next). Ledger continuity held across a round-4 *fresh* Cowork session — passes 1–4 all present and correctly numbered; the new session was forced to reload from disk, so [D-051](../docs/DECISIONS.md) reload-before-write held live (a fresh session is in fact *safer* for clobber than a continued one).

## Next

Calibration is now *exercised* (CF-29, above) — and the "must run on a fresh plan BEFORE building it" rule held. Three follow-ups remain:

1. **Record the CF-29 `cc-subagent` rows (pending — needs Cowork).** The round-0 subagent findings — 0 must-fixes; should-considers were exact-name section matching, ledger-row granularity, and naming who runs each verification step — live only in the session transcript. Feed them to Cowork to transcribe as `cc-subagent` rows (Cowork is the sole writer per [D-043](../docs/DECISIONS.md); the cc-subagent never writes the ledger itself). Without this the per-reviewer miss-rate tally for this plan is Cowork-only.
2. **Resolve the calibration protocol (the mechanics wrinkle).** Fix: keep Cowork's *review* blind (it grades the raw plan), but hand it the subagent's findings **separately, after its review, as transcription-only input** — this preserves the untainted comparison AND the sole-writer rule AND captures both reviewers' rows on the same plan. Clarify it in the calibration toggle of [`furnace-plan/SKILL.md`](../skills/furnace-plan/SKILL.md) and the transcribe rule of [`plan-review/SKILL.md`](../skills/plan-review/SKILL.md) — both **product** edits (scope-gated; `plan-review` redeploys by ZIP-upload). Until done, a calibration pass measures Cowork-on-raw and the cc half is recovered manually per item 1.
3. **Furnace-preflight candidate — repo-wide grep for negative claims.** During the CF-29 plan the author twice asserted "rule X lives *only* in file Y" from a single-file grep; Cowork's repo-wide grep refuted both (n=2, but same plan under iterative review). Candidate Check-1 sub-case: *an "only in X" / "appears nowhere else" / "not loaded anywhere" claim must be backed by a repo-wide grep, not a single-file one.* **Not auto-adopted** (same-plan n=2 risks ceremony-accretion) — promote to a furnace Check-1 sub-case only if it recurs in a *separate* furnace plan.

## Grade / promote / kill (one line each — full rubric in the ledger legend, do not restate here)

- **How to grade:** classify each Cowork catch into bucket 1 / 2 / 3; don't just count. Definitions + audit rubric are self-contained in the [`trial-ledger.md`](../skills/furnace-plan/trial-ledger.md) legend.
- **Promote** (invoke-skill → `ExitPlanMode` hook): only if catches collapse to mostly **bucket 3** — and earn the hook after content proves out, via live-fire.
- **Kill / branch:** mostly **bucket 1** → tighten the preflight prompt (don't kill); mostly **bucket 2** → distinct-verifier subagent fed the ledger (not a kill); mostly **bucket 3 with no count drop** → the one true execution-stage kill case.

## Why (pointers — not restated here)

- Trial mechanics, bucket rubric, audit rubric: [`skills/furnace-plan/trial-ledger.md`](../skills/furnace-plan/trial-ledger.md) (legend is self-contained).
- Decisions: [D-018](../docs/DECISIONS.md) (outside-agent write carve-out), [D-020](../docs/DECISIONS.md) (repo-hosted), [D-042](../docs/DECISIONS.md) (plan-review hosted), [D-043](../docs/DECISIONS.md) (blind reviewer + sole writer).
- Evidence + council: [`research/feedback-extracts/PATTERNS.md`](../research/feedback-extracts/PATTERNS.md), [`docs/council/council-report-2026-06-12-furnace.html`](../docs/council/council-report-2026-06-12-furnace.html).
- Retros: [`docs/retros/2026-06-16-furnace-trial-ledger.md`](../docs/retros/2026-06-16-furnace-trial-ledger.md), [`docs/retros/2026-06-17-cf-03-adoption.md`](../docs/retros/2026-06-17-cf-03-adoption.md).
