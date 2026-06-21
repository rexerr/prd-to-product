---
slug: readme-install-symlink-cea
status: backlog
title: README install loop symlinks context-engineering-audit (contradicts D-019)
---

# README install loop symlinks context-engineering-audit

Low priority.

## Current state

The generic `for skill in skills/*/` loop in [README.md](../README.md) (Install) symlinks *every* `skills/*/` into `~/.claude/skills/` for a fresh cloner — including `context-engineering-audit`, which [D-019](../docs/DECISIONS.md#d-019) says should **not** be global (it's a design record, missing the field-0 gate). This predates the furnace migration and doesn't affect Rex's machine (where c-e-a is already un-symlinked). Surfaced 2026-06-17 during the furnace-plan migration ([D-020](../docs/DECISIONS.md#d-020)); the README note there was scoped to mention only `furnace-plan` to avoid worsening it.

## Fix when touched

Either exclude `context-engineering-audit` from the loop (an explicit skip, or move it out of `skills/`) or add a D-019 caveat in the Install section.

## Promotion trigger

Someone clones the repo fresh and the stray symlink causes confusion.
