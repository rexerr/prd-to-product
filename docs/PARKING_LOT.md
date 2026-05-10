# Parking lot

Items deferred mid-session that need a decision or revisit. Add an entry whenever something is deferred mid-session.

Drained at the end of each roadmap phase. Items resolve into one of three buckets: (a) a phase task, (b) a [`docs/FUTURE.md`](FUTURE.md) entry, or (c) closed as not a real concern. Resolved items stay logged here for the trail; do not silently delete.

## Format

- **[Short description]** — why it was parked, what to consider when revisiting.

## Open items

(none — drained 2026-05-10 as part of Phase 3.)

## Deferred feature ideas

(none yet)

## Resolved items

- **`env_pattern` doubled-period in emitted hook script.** *Origin: Phase 1.* Default `env_pattern` strings in [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) end with periods and the hook template appends another. Cosmetic.
  - **Disposition (2026-05-10, Phase 3 drain): bucket (b) — moved to [`docs/FUTURE.md`](FUTURE.md) "Continuous-mode watch items".** Template-text fix, not example regen; outside Phase 4's scope. Wait for second instance per ROADMAP continuous-mode discipline.
- **`examples/output-small/` is stale relative to current templates.** *Origin: Phase 1.* The `"//"` comment fields in `settings.json` and the comment headers + echo bodies in the three hook scripts diverge from current parameterized template output. Functional behavior unchanged.
  - **Disposition (2026-05-10, Phase 3 drain): bucket (a) — Phase 4.** Phase 4 scope expanded in this drain to explicitly cover `output-small` regeneration alongside medium and large.
- **`stack=other` defaults are all asked of the user.** *Origin: Phase 1.* For no-runtime projects the answer is "(none)" for almost everything. Reasonable behavior; for other `other` shapes (e.g., a Rust CLI) the user fills in.
  - **Disposition (2026-05-10, Phase 3 drain): bucket (c) — closed.** No recurring user friction. If a pattern emerges across multiple `other` runs, re-open.
- **`stack_summary_one_line` for `stack=other` + `deploy_target=none` is not in the table.** *Origin: Phase 2 dog-food.* Decisions table covers Next/React/Node/Python permutations but not `other + none`. The dog-food run derived "Skill-development workspace (markdown only, no runtime)" by hand.
  - **Disposition (2026-05-10, Phase 3 drain): bucket (b) — moved to [`docs/FUTURE.md`](FUTURE.md) "Continuous-mode watch items".** Decisions-table fix, not example regen; outside Phase 4's scope. Wait for second `stack=other`-class project before extending the table.

## Cross-references

- Roadmap and current phase: [`ROADMAP.md`](../ROADMAP.md).
- Decisions log: [`docs/DECISIONS.md`](DECISIONS.md).
- Session retros: [`docs/retros/`](retros/).
- V2-and-beyond items (deferred from MVP, not from a session): [`docs/FUTURE.md`](FUTURE.md).
