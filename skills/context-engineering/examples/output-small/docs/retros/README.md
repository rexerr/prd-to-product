# Session retros

Short end-of-session summaries written by the agent before closing out. Name files `YYYY-MM-DD-topic.md`. If a file with that name already exists, append a distinct suffix (e.g. `-2`) — never overwrite an existing retro. At the start of a new session, read the most recent retro to resume context before touching any code.

## Discipline

- **Timestamp the H1 and number the session of the day** (`date "+%Y-%m-%d %H:%M %Z"`). Filenames are date-only, but several sessions can run in one day; without intra-day ordering, an earlier same-day retro's "not done this session" gets misread as "not done at all" after a later session already did it.
- **Write the retro before the code commit and bundle both into one push** — not a trailing retro-only commit (that double-push is the waste the retro exists to prevent).
- **Only for non-trivial sessions** — skip one-line tweaks to avoid retro-spam.
- **Reference, don't restate.** When a fact already lives in a durable artifact (`DECISIONS.md`, `BACKLOG.md`, a PRD, a plan, a commit/diff), link it by path — never paste its content into the retro. Two copies drift, and the retro then silently contradicts its source. Redact any secret/PII before writing.

## Template

```markdown
# Retro — YYYY-MM-DD HH:MM TZ — [topic]   (Nth session of the day)

## What was completed

- [List tasks finished this session]

## Failure this session

- **Tag:** [scope creep / lost context / goal drift / hallucinated success / none]
- **Name the artifact.** If a failure landed, quote the specific evidence — the exact bad output, the file:line, the wrong claim — not a generic restatement of the tag. A failure with no quotable artifact is too vague to prune the rule it spawns later.
- If a failure or near-miss landed, force the lesson→change jump — don't stop at narrating it:
  - **Tool or agent?** the harness/tooling, or the agent's judgment?
  - **Does it generalize?** a one-off, or a class that will recur?
  - **→ The change it demands:** the concrete edit (rule / template / doc), or "none" with why.

## Files changed

- [path/to/file.js] — [brief description of what changed]

## Key decisions made

- [Any significant technical or product choices made this session]

## Open items

- [Anything left unfinished or deferred — mirror to BACKLOG.md (In progress / Backlog) as appropriate]

## Next session

- [What to pick up first — and name the skill to open with, if any]
```
