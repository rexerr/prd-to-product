# Parking lot

Items deferred mid-session that need a decision or revisit. Add an entry whenever something is deferred mid-session.

## Format

- **[Short description]** — why it was parked, what to consider when revisiting.

## Items

- **`env_pattern` doubled-period in emitted hook script.** Default `env_pattern` strings in [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) end with periods (e.g., ``...Never commit `.env.local`.``) and the hook template appends another period after the marker. Substitution yields a doubled period. Cosmetic, not blocking. Surfaced in [`docs/retros/2026-05-10-phase-1-validation.md`](retros/2026-05-10-phase-1-validation.md). Fix in Phase 4 alongside example regeneration: drop the trailing period in the env_pattern defaults, or rephrase the hook template so the marker isn't followed by another period.
- **`examples/output-small/` is stale relative to current templates.** The `"//"` comment fields in `settings.json` and the comment headers + echo bodies in the three hook scripts diverge from the current parameterized template output. Functional behavior is unchanged. Surfaced in [`docs/retros/2026-05-10-phase-1-validation.md`](retros/2026-05-10-phase-1-validation.md). Fix in Phase 4: regenerate the small example as part of the medium/large regeneration pass.
- **`stack=other` defaults are all asked of the user.** [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) "Stack and deploy-target defaults" table lists `(ask user)` for every command when `stack=other`. For a no-runtime project (like this one) the answer is "(none)" for almost everything, which is reasonable. For other `other` shapes (e.g., a Rust CLI, a Go service) the user fills in. No action needed unless a pattern emerges across multiple `other` runs.
- **`stack_summary_one_line` for `stack=other` + `deploy_target=none` is not in the table.** Decisions table covers Next/React/Node/Python permutations but not `other + none`. The dog-food run derived "Skill-development workspace (markdown only, no runtime)" by hand. If `other + none` recurs, add a row to the table or a fallback rule.

## Deferred feature ideas

(none yet)

## Cross-references

- Roadmap and current phase: [`ROADMAP.md`](../ROADMAP.md).
- Decisions log: [`docs/DECISIONS.md`](DECISIONS.md).
- Session retros: [`docs/retros/`](retros/).
- V2-and-beyond items (deferred from MVP, not from a session): [`docs/FUTURE.md`](FUTURE.md).
