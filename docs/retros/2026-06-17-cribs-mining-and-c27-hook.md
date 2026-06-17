# Retro — 2026-06-17 — Steinberger/Van Horn cribs mining + C-27 validation hook   (1st session of the day)

## What was completed

- **Mined the Matt Van Horn / Peter Steinberger ecosystem across 3 rounds** (cli-printing-press, agentcookie, agent-rules→agent-scripts, last30days-skill, printing-press-library, nexu-io/open-design) via subagent fan-out (conclusions, not artifacts). Produced [`docs/cribs-from-steinberger-ecosystem.md`](../cribs-from-steinberger-ecosystem.md) — a living adoption-tracker of **39 cribs (C-01–C-39)** + a divergence audit (shared spirit vs justified-by-product-shape) + blind-spots list.
- **Recorded 3 direction-setting leanings** (in the crib doc): AGENTS.md becomes canonical (reverts original intent); keep D-001 + invest in hooks-as-gates; build a `solutions/` scar-tissue library.
- **Shipped C-27 → D-017**: `.claude/hooks/validate-skills.sh`, a PreToolUse Bash hook that blocks `git commit` on malformed SKILL.md frontmatter / duplicate `name`. Authored via `/furnace-plan`, hardened across two Cowork rounds, verified (10/10 unit tests + live-fire + coexistence), committed `0071fa3`.

## Failure this session

- **none** (dominant tag). No bad substitution, no landed scope creep, no lost context, no goal drift — each phase was user-steered and gated.
- Two honest observations worth logging: (1) my `/furnace-plan` preflight **missed three real bugs** Cowork caught round 1 (fail-open commit-lockout, forgeable whole-file field grep, unterminated-frontmatter pass-through) — the expected author-blind-spot the furnace+Cowork division of labor exists to catch, working as designed. (2) I initially proposed a **too-big Phase A** (mixed enforcement + doctrine + multi-file restructuring, >300 lines); caught and re-cut during scoping, before any code.

## Furnace trial data point

- Cowork round 1: **3 bucket-2 catches** (real mechanical bugs the author missed). Round 2: **1 refinement** (the missing-closing-fence case — bucket-3-ish, a judgment-tier improvement). The converge-toward-bucket-3 pattern the furnace trial watches for held.

## Files changed

- `docs/cribs-from-steinberger-ecosystem.md` — new (commit `cf93d53`), then extended with Round 3 + decisions + C-27 status flip.
- `.claude/hooks/validate-skills.sh` — new validator hook.
- `.claude/hooks/validate-skills.test.sh` — new test harness (10 cases).
- `.claude/settings.json` — registered validate-skills in the existing `Bash` PreToolUse matcher.
- `.claude/hooks/README.md` — documented the hook.
- `docs/DECISIONS.md` + `docs/DECISIONS_ACTIVE.md` — D-017.

## Key decisions made

- **D-017** — skill-frontmatter validation hook (first hooks-as-gates adoption); v1 narrowings (grep + cheap-syntactic not full YAML; fail-open; working-tree; agent-commits-only) recorded as accepted, not silent.
- **AGENTS.md-canonical flip** decided (not executed — it's Phase B).

## Open items

- **Confirm next session that `validate-skills` actually fires** — `.claude/settings.json` may not have hot-reloaded this session; the script-level coexistence is proven but the harness invoking both hooks wants a fresh-session check (the plan's verification step 3 hard gate).
- **Phase A2 (doctrine polish):** C-09 retro→work-unit columns, C-14 dated failure tags, C-15 hoist contracts (pulled out — own pass).
- **Phase B:** AGENTS.md-canonical migration — `/furnace-plan` it; decided, not executed.
- **Phase C:** build the `solutions/` library.
- **Deferred enforcement:** C-31 PostToolUse nudge, C-29 routing-table sync, C-26 `--no-verify` deny.
- The crib doc's remaining `Proposed` cribs are the standing backlog.
- Nothing pushed this session (Rex hasn't asked).

## Next session

- First: confirm `validate-skills` fires in a fresh session (commit a deliberately-broken throwaway fixture, see the block, remove it). Then pick Phase A2, B, or C.
