# Retro — 2026-06-22 10:37 CDT — Slash-command `description` frontmatter   (2nd session of the day)

## What was completed

- Added `description:` YAML frontmatter to both slash-command templates (`session-start`, `end-session`) in `skills/context-engineering/templates/claude-commands/`, so scaffolded projects show a description in the Claude Code `/` menu instead of falling back to the body's first line.
- Synced the two `examples/output-small/.claude/commands/*.md` regression fixtures to the new emitted shape.
- Generalized the placement-table label in `generator/decisions.md` (frontmatter row was annotated "(path-scoped rules)" only; commands now use frontmatter too).

## What triggered it

Rex's new trial project (`~/Sites/cat-tracker`) appeared to be missing `/session-start` and `/end-session`. Investigation: the commands **were** scaffolded correctly and present on disk — Claude Code only reads `.claude/commands/` at session startup, so commands written mid-session don't appear until a reload. Not a scaffold bug. The one real gap surfaced was cosmetic: the command files carried no `description`, so the `/` menu had nothing clean to show.

## Verification

Structural dry-run per the strip rule (`generator/decisions.md` (c′)): template lines 1–3 frontmatter, line 4 blank (consumed by strip), lines 5–10 authoring block (stripped), line 11 banner. Confirmed both fixtures emit `---`/description/`---`/banner/blank/body with no stray blank — matches the documented frontmatter-emit shape. Diffed template head against fixture head for both commands; identical in the changed region.

## Failure tag

none — clean single-pass enhancement.

## Not done this session (handoff)

- `~/Sites/cat-tracker`'s already-scaffolded command files still lack the `description` (separate repo; backport offered to Rex, not yet done). Future scaffolds get it automatically.
