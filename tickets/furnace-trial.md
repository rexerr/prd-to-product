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

## Next

1. **Exercise a calibration pass** (skip the blind review once → Cowork reviews raw furnace output) for a clean cc-subagent-vs-Cowork-on-raw divergence number — documented but unexercised.

## Grade / promote / kill (one line each — full rubric in the ledger legend, do not restate here)

- **How to grade:** classify each Cowork catch into bucket 1 / 2 / 3; don't just count. Definitions + audit rubric are self-contained in the [`trial-ledger.md`](../skills/furnace-plan/trial-ledger.md) legend.
- **Promote** (invoke-skill → `ExitPlanMode` hook): only if catches collapse to mostly **bucket 3** — and earn the hook after content proves out, via live-fire.
- **Kill / branch:** mostly **bucket 1** → tighten the preflight prompt (don't kill); mostly **bucket 2** → distinct-verifier subagent fed the ledger (not a kill); mostly **bucket 3 with no count drop** → the one true execution-stage kill case.

## Why (pointers — not restated here)

- Trial mechanics, bucket rubric, audit rubric: [`skills/furnace-plan/trial-ledger.md`](../skills/furnace-plan/trial-ledger.md) (legend is self-contained).
- Decisions: [D-018](../docs/DECISIONS.md) (outside-agent write carve-out), [D-020](../docs/DECISIONS.md) (repo-hosted), [D-042](../docs/DECISIONS.md) (plan-review hosted), [D-043](../docs/DECISIONS.md) (blind reviewer + sole writer).
- Evidence + council: [`research/feedback-extracts/PATTERNS.md`](../research/feedback-extracts/PATTERNS.md), [`docs/council/council-report-2026-06-12-furnace.html`](../docs/council/council-report-2026-06-12-furnace.html).
- Retros: [`docs/retros/2026-06-16-furnace-trial-ledger.md`](../docs/retros/2026-06-16-furnace-trial-ledger.md), [`docs/retros/2026-06-17-cf-03-adoption.md`](../docs/retros/2026-06-17-cf-03-adoption.md).
