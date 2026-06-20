# Retro — 2026-06-20 08:58 CDT — Context-lifecycle dogfood: audited + planned, not built   (3rd session of the day)

Worked in a throwaway worktree (`claude/xenodochial-heisenberg-aef7ba`) to explore the next big rock. Ended deliberately at the plan, before building — context was mostly consumed by branch-collision firefighting, so Rex chose to preserve + resume fresh on `main`.

## What was completed

- **Read-only per-item BACKLOG audit** — [`docs/audits/2026-06-20-backlog-lifecycle-audit.md`](../audits/2026-06-20-backlog-lifecycle-audit.md). Confirms the Context-lifecycle premise and answers Rex's "are these items too verbose?" question: yes, but the bloat is a **missing-retirement-step symptom**, not bad writing — every item has a 1–3 sentence actionable core wrapped in inline session-changelog that already lives in DECISIONS/retros; ~9 items are DONE/DECLINED yet carried at full weight.
- **Steps-1–3 dogfood plan** drafted at `~/.claude/plans/eager-wandering-fairy.md` (persists outside the worktree). Twice-reviewed: blind `Explore` (D-043) + Cowork `/plan-review` round 1.
- **Three design refinements settled** (now recorded on the BACKLOG item): decisions-tier needs no ADR status-field (repo already demotes via C-10/D-026 + D-027); **slug-based ticket IDs** not a sequential counter; go-forward + one-time sweep + extract-2-mega-items-as-proof.
- Preserved: audit committed, BACKLOG resume-pointer added, this retro. Plan persists on disk.

## Failure this session

- **Tag: lost context (process friction, externally triggered).** Not a discipline failure of the planning itself — the plan is sound and bounded. But a large share of the window went to the **cross-branch `D-NNN` collision**: parallel work in another worktree minted D-047 while this branch's plan also targeted D-047, surfacing only when Cowork (reading both `main` and the worktree) caught it. We re-planned (D-046→D-047→D-048) and fast-forwarded onto main twice. Net: the build never started.
- **Two real lessons banked:**
  1. **Global sequential `D-NNN` from a shared file collides under parallel branches.** Cheap fix = standing discipline "allocate `D-NNN` as `max(local, main)+1`, renumber the loser" (worth a ~3-line CLAUDE.md add to the decisions-log section). The date+slug collision-free overhaul is a separate council-grade rock. This *directly* shaped the plan: new ticket IDs are slug-based, dodging the same trap at zero migration cost.
  2. **The blind in-session reviewer structurally cannot catch cross-branch staleness** — it reads only the local tree. Cowork caught the D-046 collision by reading `main` too. A clean datapoint that the furnace pre-filter does not subsume Cowork (for Cowork to log in the trial ledger, not me).

## Files changed (this commit)

- `docs/audits/2026-06-20-backlog-lifecycle-audit.md` (new), `BACKLOG.md` (resume pointer on the Context-lifecycle item), this retro.

## Next session (fresh, on `main`)

- Reopen `~/.claude/plans/eager-wandering-fairy.md`. **First action: re-check next-free `D-NNN` against `main`** (expected D-048, but main moves). One open sign-off awaits Rex: decisions-tier narrowing (narrow [rec] vs add ADR field for skill-port parity).
- Consider the cheap CLAUDE.md add of the `max(local,main)+1` decision-allocation rule before the next parallel session.
