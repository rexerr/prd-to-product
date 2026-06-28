---
slug: kanban-into-scaffold
status: next
title: Build the kanban system (model + view) into the context-engineering scaffold
---

# Kanban system → scaffold

**Decision:** [D-069](../docs/DECISIONS.md) (reverses [D-068](../docs/DECISIONS.md)). This project is the template; the scaffold must ship the one-board kanban we engineered here. Optimize for Rex's clarity, not a hypothetical external user.

## Progress

- **Pass 1 (this repo's dogfood) — DONE 2026-06-26.** Schema upgraded **beyond the bare D-054 columns** (a brainstorm convergence, [`~/brainstorms/2026-06-25-scaffold-board-tags-formats.md`](../../brainstorms/2026-06-25-scaffold-board-tags-formats.md)): columns are now **`Item · Type · Lane · Seq · Tags · Gloss · Refs`** (7 — **no Next**). `Tags` = two axes `gate:`/`area:`, max 2, validated by the render against a `<!-- TAGS -->` block. `Gloss` = the plain-English line. Render restyled Vercel-clean (white/zinc, no card left-stripe, headline-is-the-ticket-link). Commits `f2ba832` (schema) + `5706f1b` (design). **Items 1–6 below now target this 7-col schema, not the bare D-054 one.** Model on this repo's [`BACKLOG.md`](../BACKLOG.md) as it stands post-Pass-1.
- **Pass 2 (scaffold templates + fixture) — DONE 2026-06-28.** Ported the 7-col board into [`BACKLOG.md.template`](../skills/context-engineering/templates/docs/BACKLOG.md.template) (two new PARAMETERIZE markers — `backlog_tags_block`, `board_seed_rows` — replacing the removed `phase_*`; dropped the multi-section body + `## Open decisions`; reconciled the stale "never inline"/phase references at template lines 3/5/11 + Conventions). Re-rendered the `output-small` fixture ([BACKLOG](../skills/context-engineering/examples/output-small/BACKLOG.md) as a complete board + the [AGENTS](../skills/context-engineering/examples/output-small/AGENTS.md) graduation bullet). Reframed the graduation rule in **both** rule shapes, verbatim-in-sync. Verified: dry-run substitution == fixture **byte-for-byte** (RED-capable), flat/modular bodies identical. Plan: `~/.claude/plans/crystalline-juggling-flute.md` (furnace + 2 Cowork rounds; both sign-offs confirmed). **Pass 3 remains** — generator wiring, render-tool emission, orphaned-intake-var reconciliation + stale abbreviated-example/transcript fixups (see plan Handoff), **D-070**.
- **Full plan (Pass 2 + 3):** `~/.claude/plans/validated-tumbling-pine.md` — twice-baked (furnace preflight + 3 Cowork rounds). Pass 3 emits the render tool to **`.claude/scripts/`** (not `scripts/` — allowlist), resolves project root by walking up to the ancestor with `BACKLOG.md`, and logs **D-070** (supersede D-068; name the D-001 trail).

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
- **Show a rough render before the gauntlet.** Before `/furnace-plan` or any Cowork review, render a throwaway version of the fixture board and put it in front of Rex to settle column/shape/design questions first — those changed the moment he saw Pass 1's board (dropped the Next column + the "open ticket" button after a full furnace + 3 Cowork rounds had reviewed the 8-col version; [retro 2026-06-26](../docs/retros/2026-06-26-kanban-schema-and-render-redesign.md), goal-drift n=2). Settle the thing he'll *look at* first; review the mechanics after.
- **Run it through `/furnace-plan`** — the value here is purely sync-safety (flat/modular/fixture drift is the exact failure that bit Batch A and that this whole build exists to fix). Not a gate on *whether*; a tool for *correctly*.
- Verify per CLAUDE.md: dry-run substitution diffed against the updated `output-small/` fixture; render the fixture board and confirm it parses.

## Why (don't relitigate)

The scaffold is "woefully out of sync" with what we engineer here — that drift **is** the failure ([D-069]). Do not re-council whether; the owner decided. Build it.
