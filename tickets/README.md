# tickets/ — the convention

`BACKLOG.md` is a **thin always-loaded kanban board** (one row per active unit of work). The full context to *act* on a unit lives here, in `tickets/`, read on demand. This split exists because `BACKLOG.md` is read whole at every session start: anything fat in it is a token tax paid every session forever. See [`docs/briefs/living-document-lifecycle-brief.md`](../docs/briefs/living-document-lifecycle-brief.md) for why (the registry-graduation pattern) and [`docs/DECISIONS.md`](../docs/DECISIONS.md) D-048 / D-054 for the binding rules (the board model).

## Rules

- **One active unit of work per file.** A ticket is the working surface for one item — its current state, its next action, its open questions.
- **Named by slug, not a counter** (`furnace-trial.md`, `plan-review-rehost.md`). A global sequential id is the exact shape that produced the D-046/D-047 collision when two parallel worktrees both grabbed "the next number"; slugs collide only when two agents file a ticket for the *same* work — a real duplicate worth catching. Matches the repo's existing slug/date naming for retros and councils.
- **A ticket carries context-to-act and points to the "why" — it does not restate it.** Link its `D-NNN`/retro/brief for rationale; keep the ticket itself to the actionable state. Re-hosting a decision's full reasoning here just relocates bloat.
- **Greppable frontmatter:** `status` carries the board **Lane** — `active | next | watching | backlog | blocked | icebox` (same vocabulary as the `BACKLOG.md` board), plus an optional `seq` (integer order within the actionable lanes, mirroring the board's `Seq`). A card's `status`/`seq` mirror its row's `Lane`/`Seq`; keep them in sync when the row moves.
- **Archive, don't delete.** A resolved ticket is `git mv`'d to `tickets/archive/`, never removed — a future turn can't be predicted to never need it (the retirement ritual in [`.claude/commands/end-session.md`](../.claude/commands/end-session.md) does this).
- **Link-depth rule (prevents 404s on archive-move):** link repo docs with the relative path **plus** anchor — `../docs/DECISIONS.md#d-020`, never a bare `#d-020` (file-relative, silently breaks on move). A ticket sits one level under root, so it uses one `../`; moving to `tickets/archive/` adds a second level, so the ritual re-points every link to `../../…` and re-verifies it resolves.

## Frontmatter template

```
---
slug: <kebab-case-slug>
status: active        # board Lane: active | next | watching | backlog | blocked | icebox
seq: 1                # optional — order within the actionable lanes (active/next); omit otherwise
title: <short title>
---
```

Body: current state · **Next:** the single next action · open questions · pointers to the `D-NNN`/retro/brief that hold the reasoning.
