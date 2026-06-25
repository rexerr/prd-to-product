---
slug: kanban-into-scaffold
status: next
title: Build the kanban system (model + view) into the context-engineering scaffold
---

# Kanban system → scaffold

**Decision:** [D-069](../docs/DECISIONS.md) (reverses [D-068](../docs/DECISIONS.md)). This project is the template; the scaffold must ship the one-board kanban we engineered here. Optimize for Rex's clarity, not a hypothetical external user.

## What to build

Port the **one-board kanban model + the rendered view** into the scaffold, both shapes + fixture:

1. **`skills/context-engineering/templates/docs/BACKLOG.md.template`** — replace the multi-section shape (`Build plan / In progress / Backlog / Open decisions / Later / Done`) with the one-board kanban: `Item · Lane · Seq · Next · Refs` table, lanes `active/next/watching/backlog/blocked/icebox`, board-is-the-roadmap, the Format/lanes legend, the Done→archive note. Model on this repo's own [`BACKLOG.md`](../BACKLOG.md).
2. **Rule templates** — `claude-rules-modular/session-discipline.md.template` + `claude-rules-flat-AGENTS.md.template`: describe the board model (lanes, Seq, one-row-per-unit, thin-on-touch, board-is-roadmap), folded into the existing "When BACKLOG outgrows the session-start read" graduation rule so it stays coherent (with kanban from day one, graduation is about the `tickets/` split, not reshaping). Keep flat + modular in sync.
3. **`skills/context-engineering/examples/output-small/BACKLOG.md`** — re-render the fixture to the kanban shape (hand-authored compressed render, as today).
4. **Generic render tool** — a shape-agnostic `render-backlog-kanban.py` (maps the board table → columns) emitted as an opt-in dev-tool, like the scaffolded `check-live-links`. Wire its regen into the scaffolded `/end-session` template. Base it on this repo's [`scripts/render-backlog-kanban.py`](../scripts/render-backlog-kanban.py).
5. **`generator/decisions.md`** (+ `intake.md`/`output-summary.md` if needed) — update to reflect the new default backlog shape + the emitted render tool.
6. **Supersede [D-068]** formally when built; this ticket + D-069 already record the reversal.

## How to do it

- ~8–10 files across both shapes + fixture + generator → **feature scope**, may exceed 300 lines/session → likely **two focused passes** (template+fixture, then render-tool+generator). Scope-check before each.
- **Run it through `/furnace-plan`** — the value here is purely sync-safety (flat/modular/fixture drift is the exact failure that bit Batch A and that this whole build exists to fix). Not a gate on *whether*; a tool for *correctly*.
- Verify per CLAUDE.md: dry-run substitution diffed against the updated `output-small/` fixture; render the fixture board and confirm it parses.

## Why (don't relitigate)

The scaffold is "woefully out of sync" with what we engineer here — that drift **is** the failure ([D-069]). Do not re-council whether; the owner decided. Build it.
