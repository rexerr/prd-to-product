**The goal — set your lens by this first.** This repo's skills (`context-engineering`, `prd-creator`, `design-system-bootstrap`, siblings) exist to **improve Rex's future projects**. Judge any task by whether it changes what a skill *produces for a real downstream project*. On-goal includes this-repo work that **ports** to the scaffold or **dogfoods** a skill — not just direct skill edits. Off-goal is only work whose *sole* result is this repo's internal tidiness (polishing these process docs, or a skill's prose, with nothing produced, ported, or validated). These process docs are exhaust from the work — necessary, minimal, never the deliverable.

Read the following files in this order before responding:

1. BACKLOG.md
2. The most recent retro in docs/retros/ — pick it by **git history, not filename sort** (multiple retros can share a date, and alphabetical order then surfaces the wrong one). Run `git log --diff-filter=A --format= --name-only -- 'docs/retros/*.md' | grep -m1 retros` and read that file; if `git status` shows an uncommitted retro newer than that, read it instead. If several retros share that same latest date, skim all of them so you don't miss the newest work.
3. docs/DECISIONS_ACTIVE.md
4. Run `git status -sb` and compare local `main` to `origin/main` (ahead/behind/in-sync). **Git is the source of truth for push/commit/sync state — never the retro.**

When done, give me:

- One sentence on where we left off based on the retro. **State push/sync status only from the step-4 `git` check — never relay a retro's "pushed" / "not pushed" / "awaiting-go" line. Those freeze at write time and the retro README forbids them; if a retro carries one, ignore it and report what `git` says.**
- The next item from BACKLOG.md "In progress" (or top of "Backlog" if In progress is empty)
- Any active decisions that bear on what's next

Do not write any code. Do not propose solutions yet. Just orient us.
