---
slug: plan-review-rehost
status: next
seq: 1
title: plan-review rehost — first paired cc-subagent data
---

# plan-review rehost

The Cowork `plan-review` skill is versioned in-repo at [`skills/plan-review/SKILL.md`](../skills/plan-review/SKILL.md), host-agnostic ([D-042](../docs/DECISIONS.md#d-042)). Deploys by ZIP-upload, not symlinked onto the Claude Code surface.

## Current state

- Plan 1 (rehost) + Plan 2 (blind-reviewer wiring) both shipped. Craft/voice rewrite 2026-06-19: first-person→imperative, hoisted rules, failure-tags, honesty reframed from exhortation to forcing functions (citation-or-demote + bounded verdict).
- Deployed 2026-06-19 — `skills/plan-review.zip` regenerated from the craft-pass source and uploaded by Rex (carries the `Reviewer` column + transcribe-subagent-log rule, verified inside the archive).
- `furnace-plan` now spawns one blind read-only `Explore` reviewer every pass before `ExitPlanMode` ([D-043](../docs/DECISIONS.md#d-043)); Cowork stays the **sole** ledger writer.
- The stale-D-NNN guardrail sub-item already landed as furnace Check 1 sub-case **1a** (not a CLAUDE.md standing step — both observed collisions were furnace-authored plans).

## Next

First live `cc-subagent` run on a real furnace plan that emits `cc-subagent` rows **and** confirms Cowork transcribes them — the real end-to-end proof. Partially exercised (2026-06-20 self-authored plan; 2026-06-21 calibration pass), but the paired-data protocol wrinkle (blind review vs. sole-writer transcription) is live — tracked in [furnace-trial](furnace-trial.md).

## Open

- **No evals run on the skill.** If review quality matters, skill-creator's eval loop is the real validation.
- Calibration-pass use is documented but only lightly exercised.

## Why (pointers)

- [D-042](../docs/DECISIONS.md#d-042) (hosted), [D-043](../docs/DECISIONS.md#d-043) (blind reviewer + sole writer).
- Retros: [2026-06-18-plan-review-rehost](../docs/retros/2026-06-18-plan-review-rehost.md), [2026-06-19-plan-review-craft-pass](../docs/retros/2026-06-19-plan-review-craft-pass.md).
