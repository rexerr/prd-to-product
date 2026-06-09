# Session retros

Short end-of-session summaries written by the agent before closing out. Name files `YYYY-MM-DD-topic.md`. At the start of a new session, read the most recent retro to resume context before touching any code.

## Discipline

- **Timestamp the H1 and number the session of the day** (`date "+%Y-%m-%d %H:%M %Z"`). Filenames are date-only, but several sessions can run in one day; without intra-day ordering, an earlier same-day retro's "not done this session" gets misread as "not done at all" after a later session already did it.
- **Write the retro before the code commit and bundle both into one push** — not a trailing retro-only commit (that double-push is the waste the retro exists to prevent).
- **Only for non-trivial sessions** — skip one-line tweaks to avoid retro-spam.

## Template

```markdown
# Retro — YYYY-MM-DD HH:MM TZ — [topic]   (Nth session of the day)

## What was completed

- [List tasks finished this session]

## Failure this session

- [bad substitution / scope creep / lost context / goal drift / none]

## Files changed

- [path/to/file.js] — [brief description of what changed]

## Key decisions made

- [Any significant technical or product choices made this session]

## Open items

- [Anything left unfinished or deferred — mirror to PARKING_LOT.md or ROADMAP.md as appropriate]

## Next session

- [What to pick up first]
```
