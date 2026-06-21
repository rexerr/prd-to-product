---
slug: optional-marker-gating
status: backlog
title: OPTIONAL-marker gating in the scaffolded verification rule
---

# OPTIONAL-marker gating

Parse-conditional latent candidate (low priority). Surfaced 2026-06-18 during CF-13 adoption ([D-041](../docs/DECISIONS.md#d-041)).

## Current state

The `verification_ui_bullet` OPTIONAL marker in both rule templates may gate a whole contiguous block rather than a single line. Single-line vs block gating is unresolved; [generator/decisions.md](../skills/context-engineering/generator/decisions.md) 269–278 doesn't cover the adjacent-marker case.

## If block-gating (candidates to investigate, not confirmed bugs — check the parse first)

- A no-visual project (`uses_visual_confirmation_gate == false`) loses the universal "Never claim success based on 'the code looks correct.'" sentence in [claude-rules-modular/session-discipline.md.template](../skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template) (it sits *inside* the marker block at line 91).
- And the logic-output bullet "Logic or data changes: run `check_cmd`, report results." in [claude-rules-flat-CLAUDE.md.template](../skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template) (line 127 — arguably worse, since a backend/CLI project most wants it).

## Fix when touched

Settle the gating semantics first (an OPTIONAL spec clarification in `decisions.md`), then if confirmed, move the universal sentence (modular) and the logic bullet (flat) outside the `verification_ui_bullet` gate. Cover both templates in one pass. CF-13's own new bullet is unaffected (placed before all markers).
