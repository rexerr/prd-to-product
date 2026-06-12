# Retro — 2026-06-12 10:13 CDT — Hook stdin fixes, `if`-field adjudication, env-hook mechanism upgrade   (3rd session of the day)

## What was completed

- **Closed the hook-architecture-defect BACKLOG item in full** (entry removed from BACKLOG per its resolved-items rule; this retro is the record). `block-deploy-cli.sh` and `block-worktree.sh` rewritten from unconditional `exit 2` to payload-inspecting scripts; `block-env-commit.sh` upgraded to the same mechanism after its raw-grep limitation false-positived live mid-session. All three scripts (template + `examples/output-small/`; env also this repo's live copy) now share one mechanism: **jq-extract `.tool_input.command` → match anchored at command-word position (line start or after `| & ;`) → raw-payload coarse fallback when jq is absent** (a blocking guard must never silently disarm). Remediation text preserved in every BLOCKED message.
- **`if`-field adjudicated — dropped everywhere, with corrected understanding.** The plan's premise ("silently ignored") was WRONG; empirical tests gave the true picture: `if` is documented and honored for simple and simple-compound commands (negative-case live-fire, desktop + headless), but was twice observed letting the hook run on non-matching complex commands (2026-06-08 `git rev-list … && ls …`; 2026-06-12 a multi-heredoc fixture command — unreproduced by a plain compound, mechanism unknown). Since the script must therefore scope itself anyway, `if` adds only a drift hazard — a stale `if` after a script-pattern change silently disarms the guard (fail-open). Dropped from `claude-settings.json.template`, the example, and this repo's settings (Rex-gated, approved). Both decisions recorded in `generator/decisions.md` "Scoping is script-side"; both READMEs (template + this repo's live copy) rewritten — "Fires on" column replaced, jq-with-fallback prescribed, blast radius named (bare matcher → script runs on every Bash call; exit-0 is the common path).
- **Downstream blast-radius sweep:** `the-council` has both broken unconditional hooks emitted (scaffolded 2026-05-10) → intermittent spurious total-blocks on complex commands; fix chip spawned (see Open items). `ha-controller` is fine (hand-written payload-inspecting variant). `seance`, `squirreled`, `qventus-prototyper` and others: no emitted copies of the broken pair.
- **EnterWorktree verified real** in CLI and headless (docs citation + live-fire block in a headless session); matcher and `tool_name` branch kept. Whether `Agent isolation:worktree` surfaces a PreToolUse event remains undocumented — coverage NOT claimed, caveat written into script comments and settings comments.
- **Verification (two-tier + negatives, per plan):** script-level 25/25 (both observed FP classes as named negative cases: prose mention `git commit -m "migrate off vercel"`, embedded `Bash(git add .env*)` data) + 13/13 fallback-path with jq genuinely shadowed; harness live-fire 5/5 in a fresh headless session (vercel/worktree/EnterWorktree block with remediation text; benign compound and prose-mention pass); dry-run substitution diffs clean ×3; JSON valid ×3; exec bits preserved.
- **Bookkeeping riders:** item 25's two "still pending `.claude/` self-edit" notes corrected — both were stale (settings allowlist already seeded; session-start already 3-step). CLAUDE.md "Where to look" trimmed: AGENTS.md dropped from the session-start read list (pure 3-line pointer; explicit Rex sign-off obtained, not bundle-implied).

## Failure this session

- **none** — two near-misses worth logging, both caught by the process working as designed: (1) the plan shipped with a wrong premise (`if` ignored) — the Phase-1 hard gate + the stop-rule Rex added in plan review forced the empirical test that corrected it before any edit; (2) the first fallback design (`cmd=$payload` then anchored match) could never block in the no-jq case — caught while *writing* the test matrix, before running it; restructured to branch on jq availability. Negative-case testing — absent from the 2026-05-10 validation — is what made both catchable.

## Files changed

- `skills/context-engineering/templates/claude-hooks/block-{env-commit,deploy-cli,worktree}.sh.template` — mechanism rewrite.
- `skills/context-engineering/examples/output-small/.claude/hooks/block-{env-commit,deploy-cli,worktree}.sh` — same, substituted.
- `.claude/hooks/block-env-commit.sh` — same, this repo's live copy.
- `skills/context-engineering/templates/claude-settings.json.template`, `examples/output-small/.claude/settings.json`, `.claude/settings.json` — `if` fields removed, comments rewritten to script-side scoping, EnterWorktree isolation caveat.
- `skills/context-engineering/templates/claude-hooks/README.md.template`, `.claude/hooks/README.md` — scoping section added, table and add-a-hook steps reconciled.
- `skills/context-engineering/generator/decisions.md` — "Scoping is script-side; the `if` filter is not used" decision record; hooks table updated.
- `BACKLOG.md` — hook-defect entry removed (resolved); item 25 stale notes corrected.
- `CLAUDE.md` — AGENTS.md dropped from session-start read list (Rex-gated, approved).
- `docs/retros/2026-06-12-hook-stdin-fixes.md` — this retro.

## Key decisions made

- Recorded in [`generator/decisions.md`](../../skills/context-engineering/generator/decisions.md) ("Scoping is script-side", 2026-06-12): (a) `if` dropped — not because unsupported, but because it cannot be the sole gate (observed misfires) and shouldn't be a second one (stale-`if` fail-open drift); (b) jq-extraction + command-position anchoring with coarse raw-payload fallback — chosen over raw grep (FP class, observed live) and over hard jq dependency (a guard must not disarm on a missing dependency).
- Method note: when a guard's premise and the docs disagree, run the negative case before designing — positive-only validation (2026-05-10) is how the original defect survived.

## Open items

- **the-council fix chip spawned** (background task): replace its two unconditional hooks + drop its `if` fields, using this repo's templates as source.
- `Agent isolation:worktree` PreToolUse coverage remains an open unknown (undocumented upstream); revisit if a scaffolded project relies on the worktree gate against subagent isolation.
- Standing gated items unchanged: plan-review mining run (Workflow opt-in); BACKLOG-scaffolding consolidation decision (ship on dog-food evidence vs. wait).

## Next session

- In-progress items remain validation-blocked; the BACKLOG-scaffolding consolidation is the only one workable without an external project and needs a Rex decision on its evidence bar. The-council chip is one click away if Rex wants the downstream fix done.
