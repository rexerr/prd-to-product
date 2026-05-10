# Parking lot

Items deferred mid-session that need a decision or revisit. Add an entry whenever something is deferred mid-session.

Drained at the end of each roadmap phase. Items resolve into one of three buckets: (a) a phase task, (b) a [`docs/FUTURE.md`](FUTURE.md) entry, or (c) closed as not a real concern. Resolved items stay logged here for the trail; do not silently delete.

## Format

- **[Short description]** — why it was parked, what to consider when revisiting.

## Open items

(none — env_pattern convention item resolved in-phase; see Resolved items.)

## Deferred feature ideas

(none yet)

## Resolved items

- **`env_pattern` default value is markdown-formatted, but `block-env-commit.sh.template` substitutes it into a double-quoted `echo` where backticks would trigger shell command substitution.** *Origin: Phase 4 task 1 regen.* Phase 1's retro substituted env_pattern without backticks (treating them as markdown wrappers, not value); the regenerated `output-small/block-env-commit.sh` followed the same convention.
  - **Disposition (2026-05-10, Phase 4 in-phase): resolved.** Option (a) applied: env_pattern values are now plain strings in [`generator/decisions.md`](../skills/context-engineering/generator/decisions.md). Convention statement added directly under the defaults table. The four markdown template consumers ([`AGENTS.md.template:43`](../skills/context-engineering/templates/AGENTS.md.template), [`claude-rules-flat-CLAUDE.md.template:54`](../skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template) and `:136`, [`claude-rules-modular/git-and-deploy.md.template:23`](../skills/context-engineering/templates/claude-rules-modular/git-and-deploy.md.template)) now wrap the substituted value in backticks at the substitution site. The shell consumer ([`block-env-commit.sh.template:7`](../skills/context-engineering/templates/claude-hooks/block-env-commit.sh.template)) substitutes the plain value into the double-quoted echo — no command-substitution risk. Example [`output-small/CLAUDE.md`](../skills/context-engineering/examples/output-small/CLAUDE.md) regenerated to match.
- **`env_pattern` doubled-period in emitted hook script.** *Origin: Phase 1.* Default `env_pattern` strings in [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) end with periods and the hook template appends another. Cosmetic.
  - **Disposition (2026-05-10, Phase 3 drain): bucket (b) — moved to [`docs/FUTURE.md`](FUTURE.md) "Continuous-mode watch items".** Template-text fix, not example regen; outside Phase 4's scope. Wait for second instance per ROADMAP continuous-mode discipline.
  - **Second instance + resolution (2026-05-10, Phase 4 in-phase): resolved.** Phase 4 task 1 regen surfaced the same doubled period (`Never commit .env.local..`) in `output-small/block-env-commit.sh`. Per continuous-mode discipline, second instance triggers fix. Applied option B: dropped the trailing period after the `<env_pattern>` marker in [`block-env-commit.sh.template:7`](../skills/context-engineering/templates/claude-hooks/block-env-commit.sh.template) (the period at the end of the env_pattern value already terminates the sentence). Regenerated [`output-small/.claude/hooks/block-env-commit.sh`](../skills/context-engineering/examples/output-small/.claude/hooks/block-env-commit.sh); echo now exits 2 with a single period.
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
