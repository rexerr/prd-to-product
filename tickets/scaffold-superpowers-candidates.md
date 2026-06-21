---
slug: scaffold-superpowers-candidates
status: watching
title: Scaffold-level superpowers candidates for context-engineering
---

# Scaffold-level superpowers candidates

Three generated-artifact upgrades from the [superpowers handoff brief](../docs/superpowers-context-engineering-handoff.md) (reconciled 2026-06-11 — a second independent extraction that converged with the liftables, which is itself promotion evidence). Parked pending `context-engineering`'s next substantive template session.

## Candidates

1. **Pre-hardened discipline rules** — scaffolded rules ship with an Excuse→Reality table + red-flags list seeded from known rationalizations (distinct from the this-repo surface in [superpowers-liftables](superpowers-liftables.md) — this is the *emitted* rules).
2. **Project-agnostic verification-gate rule** in the default `.claude/rules/` scaffold carrying the claim→evidence mapping (tests pass → output with 0 failures, not "should pass"; subagent done → diff inspected, not its report), plus gating the generator's own "scaffold complete" claim. 2026-06-12: per-task acceptance criteria phrased so a fresh read-only subagent can check them one-by-one against a structured verdict.
3. **Ready-made adversarial review-subagent prompt template** in scaffolded `docs/`: inputs, severity calibration, strengths-first, hard verdict contract. 2026-06-12: pre-seed with documented evaluator failure modes (self-justification of found issues, superficial coverage) + an expect-calibration-rounds-before-trusting-verdicts note.

## Constraints (binding)

Harvest don't install; drop the superpowers tone; adapt to existing template structure **after reading the whole skill**; pressure-test ≥1 generated artifact before calling it done (re-fires the [pressure-test-behavior-prose](pressure-test-behavior-prose.md) preconditions). Also audit emitted commands/rules (`/session-start`, `/end-session`, scaffolded `.claude/rules/`) against arXiv 2603.25723's six-component checklist.

## Why (pointers)

[superpowers handoff brief](../docs/superpowers-context-engineering-handoff.md); [2026-06-12-harness-batch-review](../docs/retros/2026-06-12-harness-batch-review.md). Promotion trigger: the next session that substantively edits context-engineering's templates, or a scaffolded project exhibiting a failure one of these prevents.
