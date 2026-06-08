Read the following files in this order before responding:

1. AGENTS.md
2. ROADMAP.md
3. The most recent retro in docs/retros/ — pick it by **git history, not filename sort** (multiple retros can share a date, and alphabetical order then surfaces the wrong one). Run `git log --diff-filter=A --format= --name-only -- 'docs/retros/*.md' | grep -m1 retros` and read that file; if `git status` shows an uncommitted retro newer than that, read it instead. If several retros share that same latest date, skim all of them so you don't miss the newest work.
4. docs/PARKING_LOT.md

When done, give me:

- One sentence on where we left off based on the retro
- The next uncompleted item on the ROADMAP
- Any parking lot items that are now blocking progress

Do not write any code. Do not propose solutions yet. Just orient us.
