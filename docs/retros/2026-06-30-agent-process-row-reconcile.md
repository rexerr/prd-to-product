# Retro — 2026-06-30 08:51 CDT — Agent-process row reconcile (stale board gloss) — (1st session of the day)

Session-start oriented to board Seq 1, "Agent-process & context-harness upgrades." Rex asked whether to `/furnace-plan` it. Investigating before answering revealed the row was effectively complete and its gloss stale — so the work became a board reconciliation, not a plan.

## What was completed

- **Traced the Seq-1 item to ground truth.** The brief ([`agent-process-brief.md`](../agent-process-brief.md)) is source material, not a task list; its Part A was built across the 2026-06-08 group sessions (autonomy charter, `/end-session`, memory-vs-repo guardrail, seeded allowlist, timestamped-retro convention, group-5 session-start conditioning). The board gloss's "one in-repo dogfood self-edit loose end remains" pointed at applying this repo's own read-only `permissions.allow` — which was **already authorized and committed** in `94d5646` ("Group 2 dog-food"). The gloss was stale.
- **Found the one genuine remnant** (not a self-edit): a generator-logic gap. `generator/decisions.md:367` says emit a permissions-only `settings.json` when `enforce_rules_as_hooks == false`, but the manifest row at `:247` still gates emission on `== true` — a self-contradiction that would make a no-hooks scaffolded project silently lose the seeded allowlist. Verified still open this session.
- **Board reconciled:** retired the completed agent-process row; promoted "Invariant/semantic output checks" to Seq 1; logged the generator gap as a new `fix` / `area:generator` row in `backlog`.
- **Verified:** `render-backlog-kanban.py` → "0 tag warning(s)"; `check-live-links.py` → 0 broken across 115 live docs.

## Failure this session

- **Tag: lost context** — but the artifact's, not the session's. The board carried a gloss that froze at write time and drifted from git reality (claimed a loose end that commit `94d5646` had already closed). Caught by verifying against `git log`/`git show` rather than trusting the prose — exactly the discipline `/session-start` already enforces for push/sync state ("git is the source of truth, never the retro"). No new rule: the existing verify-against-git instinct worked; this is one more datum that board/retro prose needs the same treatment glosses already get. Logged n=1.
- **No furnace-plan run** — correctly. The work was a stale-row cleanup + one-file generator follow-up, neither costly-to-get-wrong nor hard-to-reverse. furnace-plan would have planned a phantom.

## Files changed

- `BACKLOG.md` — removed agent-process row, renumbered Invariant to Seq 1, added generator-allowlist `fix` row.
- This retro.

## Next session

- Board Seq 1 is now **"Invariant/semantic output checks"** (`area:generator`) — the "is this claim grounded?" generator check; write-guard + no-jargon-leak already done. Refs: [council](../council/council-report-2026-06-08.html), [D-064](../DECISIONS.md#d-064).
- The new backlog row (generator emits permissions-only `settings.json` when hooks are off) is a ≤1-file fix to `generator/decisions.md` when picked up.
- Not pushed this session (no push ask). `BACKLOG.html` is a gitignored local render, not committed.
