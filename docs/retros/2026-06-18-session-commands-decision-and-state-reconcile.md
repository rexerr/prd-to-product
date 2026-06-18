# Retro — 2026-06-18 07:37 CDT — Session-commands per-project (D-021) + `/decision` parking; post-compaction state reconciliation   (2nd session of the day)

## Context

Two threads. (1) Rex asked whether session start/end skills should be global-symlinked (like the just-migrated `furnace-plan`) or created per-project — resolved into **D-021**. (2) A follow-on "what other commands would be useful?" surfaced a `/decision` command idea, run through `/furnace-plan`; Rex chose to **park** it. Closing the session via `/end-session` then exposed a state mismatch caused by context compaction — the most useful lesson here.

## Done

- **D-021 logged** — *Session-lifecycle commands stay per-project (scaffolded); only project-invariant disciplines get the global-symlink treatment.* The reusable cut: global-symlink only when content is **project-invariant** (furnace-plan); **scaffold-from-template** when content must be tailored per repo (session-start/end-session, whose value is the per-project body — commit URL, `examples/output-small` verification, read-order). Committed `49f98b2`, pushed 2026-06-17.
- **`/decision` command parked** — explored building a command to mechanize `D-NNN` logging (next number, four-part skeleton, insert-before-footer, mirror prompt). Authored a `/furnace-plan` plan + verification ledger; Rex's call: not confident it's needed (D-021 logged clean by hand; anti-accretion ethos). Added a `## Backlog` bullet with a Rule-of-Two promotion trigger and the recorded build cost (1 file live / 4-touch to scaffold). Rode into commit `1778fc2` (2026-06-17 20:23), pushed.

## Verified

- D-021: numbered correctly, placed immediately before the `- Currently-binding subset` footer (not EOF), not mirrored to `DECISIONS_ACTIVE.md` (visible-by-reading skip precedent).
- `/decision` bullet: sits under `## Backlog`, names *what* + a promotion trigger per the section's own Format rule, cross-references (D-013/D-019/D-021) resolve.
- At `/end-session`: `git status --porcelain` empty, HEAD == origin/main, `git log -S` confirms the `/decision` bullet already lives in `1778fc2`. **No new commit fabricated** — there was nothing to commit.

## Failure this session

- **Tag: lost context.**

On `/end-session` I assumed, from in-conversation memory, that the `/decision` BACKLOG edit was uncommitted and that HEAD was my D-021 commit (`49f98b2`). The actual post-compaction state: HEAD had advanced ~10 commits (D-022→D-024, crib-miner renames, ledger sweeps), the `/decision` bullet was already committed in `1778fc2`, the tree was clean, and the clock had rolled to 2026-06-18. Had I trusted memory and run `git commit`/`push`, the best case was a confusing no-op and the worst case was narrating a fabricated commit + URL.

**Catch:** the date/number discrepancies (clock said 2026-06-18 vs my D-021 `Date: 2026-06-17`; commits referencing "D-024" vs a file I'd read as topping out at D-020) tripped the "do not continue from a state you cannot describe" reflex. Ran `git status` / `git log` / `git reflog` / `git log -S` to reconcile against reality *before* committing — found nothing to commit, and stopped.

- **Secondary miss:** D-021's `Date: 2026-06-17` was set by copying D-020's date, not by running `date`. Coincidentally correct, but the method was guessing — and it's precisely one of the clerical fields the parked `/decision` command would have gotten right deterministically. Small live data point in that command's favor, logged in its BACKLOG trigger.

## Lesson — no new guardrail

The existing discipline already prescribes the exact check that saved this: *"Verification before claiming done"* and *"Do not continue from a state you cannot describe."* This is **evidence the rules work**, not a gap needing a new rule — per the retro tag-log's own purpose (don't accrete guardrails against failures the instrument shows are already handled). Standing reminder, not a new rule: after a long/compacted session, reconcile `git status` + `git log` against in-conversation memory before any commit, and derive dates/numbers from `date`/`grep`, never from a sibling entry.
