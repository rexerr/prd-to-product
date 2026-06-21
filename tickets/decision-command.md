---
slug: decision-command
status: watching
title: /decision command — parked, low confidence it's needed
---

# /decision command

A slash command that mechanizes the clerical half of decision-logging into [`docs/DECISIONS.md`](../docs/DECISIONS.md): compute the next `D-NNN`, drop the canonical `Date / Context / Decision / Reason / Revisit if` skeleton, insert it immediately **before** the `- Currently-binding subset` footer line (not appended at EOF), and prompt the `DECISIONS_ACTIVE.md` mirror question. The human still writes the judgment content.

## Why parked

Evidence it fixes a *recurring* failure is thin — D-021 was logged cleanly by hand — and the repo deliberately resists accretion ([D-013](../docs/DECISIONS.md#d-013), [D-019](../docs/DECISIONS.md#d-019)).

## Build cost when promoted

In this repo: one file (`.claude/commands/decision.md`, bare markdown, matching `session-start`/`end-session`). Propagating to every scaffolded project is a 4-touch `context-engineering` change — new `templates/claude-commands/decision.md.template`, a row in the [generator/decisions.md](../skills/context-engineering/generator/decisions.md) inclusion table (~208–237, manifest-driven), the `NOTES.md` quick-ref tree, and a hand-authored `examples/output-small/.claude/commands/decision.md` fixture (per [D-021](../docs/DECISIONS.md#d-021): scaffolded per-project command, not a global symlink).

## Promotion trigger (Rule of Two)

By-hand decision-logging *observed* to misfire **twice** — a number collision/skip, format drift, an entry appended at EOF instead of before the footer, or a forgotten `DECISIONS_ACTIVE.md` mirror — OR logging cadence rises enough that the clerical overhead becomes a real, repeated tax.
