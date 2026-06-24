# Retro — 2026-06-24 10:02 CDT — loops-article mine, link-rot cleanup, on-demand link checker   (3rd session of the day)

## What was completed

- **`/mine` on a pasted "loops" article** (half affiliate spam for "Mira", discarded as untrusted). Lensed through the project's *ultimate goal* (what `context-engineering` teaches scaffolded projects), not this workspace's own process — a deliberate second-pass correction after an initial lens-A miss. One finding adopted: the scaffold names *agentic laziness* + *self-preferential bias* ([principles.md:142](../../skills/context-engineering/principles.md)) but is silent on graduating a project to an unattended loop. Captured as `watching` row 42 + reproducible mined-doc ([docs/mined/2026-06-24-loops-article.md](../mined/2026-06-24-loops-article.md), commit `a711563`).
- **Link-rot cleanup, scoped correctly.** A by-hand scan (the loops article's own "prove one manual run first" step) found 73 broken internal links — 69 in dated retros/council (point-in-time history, **left alone**), 4 in live docs (fixed, commit `d3c006d`). Verified the fix took the live-doc count 4 → 0.
- **`/devils-advocate` on a scheduled link-rot watcher** → verdict Reconsider, kill the cron. Link rot is event-driven (renames), not time-driven, so a clock fires too late and trains notification-blindness.
- **Built the on-demand alternative instead:** [scripts/check-live-links.py](../../scripts/check-live-links.py) + a one-line CLAUDE.md Commands note (commit `77a57c6`). Exit-coded so it drops into a pre-commit hook unchanged if rot recurs.

## Verification this session

- **Link checker:** ran both modes — live `0 broken, exit 0`; `--all` `69 broken, exit 1`. Exit codes confirmed by hand.
- **Each of the 4 link fixes traced to ground truth:** `ROADMAP→BACKLOG.md.template` rename confirmed by listing `templates/docs/`; the `.claude/plans/` target confirmed absent (no dir); the `../DECISIONS.md` wrong-depth confirmed against the file's other valid `DECISIONS.md` refs.
- **Mine finding** verified by grepping `context-engineering` for loop/agentic content; deduped against `BACKLOG.md`, `docs/cribs/`, `tickets/` before proposing.
- **Not verified:** self-verified throughout — no independent subagent was used (`Self-verified — independent sub-task not spun up`). The other session's `D-065` content (see below) I did **not** review; it is not my work.

## Failure this session

- **Tag:** scope creep (cross-session git variant — a commit's content exceeded its stated scope)
- **Artifact:** commit `d3c006d` ("Fix 4 broken internal links") also contains the **entire `D-065` decision block** authored by a concurrent second session. Cause: `git add docs/DECISIONS.md` staged the *whole* working-tree copy of a file the other session had edited unstaged, sweeping its hunk into my commit. Content is not lost; `DECISIONS.md` is correct — only the commit boundary is mis-attributed.
- **Tool or agent?** Both. Agent: I staged a file without checking it was dirty from another session. Tooling: two live sessions sharing one working tree.
- **Does it generalize?** Yes, and it **corrects** the premise of `BACKLOG.md` row 21 (added by the other session): its proposed guard "stage named paths" is *insufficient* — I **did** use named paths and it still happened, because the file itself was co-edited. The real guard is per-hunk staging (`git add -p`) or separate git worktrees per session.
- **→ The change it demands:** none yet — Rule-of-Two, n=1, already parked in row 21. No `CLAUDE.md` rule accreted. When n=2 lands, the adopted rule must be the *sharper* one above, not "named paths." This retro carries that correction so the eventual rule is right.

## Files changed

- Committed earlier this session: `docs/mined/2026-06-24-loops-article.md`, `BACKLOG.md` (row 42) — `a711563`; `BACKLOG.md` / `docs/cribs-from-designer-skills.md` / `docs/DECISIONS.md` link fixes (+ the swept-in `D-065`) — `d3c006d`; `scripts/check-live-links.py` / `CLAUDE.md` — `77a57c6`.
- This step: `docs/retros/2026-06-24-loops-mine-and-link-checker.md` (this file).

## Key decisions made

- **On-demand script over scheduled cron** for live-doc link checking — driven by the devil's-advocate pass. Deliberately **not** minted as a `D-NNN`: it's a reversible dev-tool addition, not a binding cross-tool constraint, and the rationale lives in the script docstring + CLAUDE.md note + this retro. Promote to a pre-commit hook only if rot recurs.

## Open items

- **`d3c006d` mis-attribution** (D-065 under a "fix links" message): left as-is. No history surgery while the second session is live on the shared tree — content is safe and that session logged it (row 21). Gated on Rex if he ever wants it untangled.
- **F-01** loop-graduation guidance for the scaffold — `watching` row 42, gated on a scaffolded project adopting a loop.
- **Cross-session commit-sweep guard** — row 21, n=1; premise correction recorded above.

## Next session

- Pick up the **combined push** (this session's 3 commits + the second session's end-session commits) once that session finishes — then push once. No skill needed to open.
