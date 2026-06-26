# Retro — 2026-06-26 11:48 CDT — Kanban schema upgrade + render redesign (Pass 1 of kanban-into-scaffold)   (1st session of the day)

Picking up [D-069] / board row 40 ([`tickets/kanban-into-scaffold.md`](../../tickets/kanban-into-scaffold.md)): build the one-board kanban into the `context-engineering` scaffold. This session designed the upgraded board schema and shipped **Pass 1** — this repo's own board + render tool (the dogfood before the scaffold port).

## What was completed

- **Brainstorm → convergence** on the board schema ([`~/brainstorms/2026-06-25-scaffold-board-tags-formats.md`](../../../brainstorms/2026-06-25-scaffold-board-tags-formats.md)): a **two-axis tag system** (`gate:`/`area:`, max 2, render-validated against a `<!-- TAGS -->` block), a one-word **Type** column, and a plain-English **Gloss** — the readability lever for a non-engineer reading his own board. Axes generalize; values are per-project, so the scaffold can ship the mechanism without this repo's `council`/`furnace` vocabulary ([D-013]/[D-019] guardrail).
- **`/furnace-plan` → 3 Cowork rounds** on the port plan (`~/.claude/plans/validated-tumbling-pine.md`). The blind `Explore` reviewer passed clean; **Cowork caught four real executable defects it missed** — render-tool path off the generator allowlist (must emit `.claude/scripts/`, not `scripts/`), `check-live-links.py` falsely cited as a scaffolded precedent, a `## Conventions` block that would contradict the new Gloss, and a `parent.parent` root-path break at the deeper emit depth. All folded in.
- **Pass 1 shipped + verified:** `BACKLOG.md` migrated to the 7-column schema (`f2ba832`); `render-backlog-kanban.py` rebuilt for 7-col parse + tag validation + gloss/chips/title-link; restyled Vercel/Tailwind-clean (`5706f1b`). Verified: 0-warning clean render, **6/6 RED validation tests**, grep-confirmed element counts, 0 tan/left-border/ticket-button remnants.
- **Schema simplified mid-build:** dropped the **Next** column (8→7) once Rex saw the rendered board — Seq already answers "which item is next," the gloss carries the rest, and the long Next cells were the source of row-fatness. Render redesigned to taste (white/zinc, no left stripe, headline-is-the-link).

## Failure this session

- **Tag:** goal drift (process-order variant; **n=2** on this shape — see [2026-06-24-batch-b](2026-06-24-batch-b-council-and-kanban.md)).
- **Name the artifact.** The full furnace + 3 Cowork rounds ran on an **8-column schema with a Next column and an "open ticket" button** — both of which Rex changed *the moment he first saw the rendered board* ("the next line… seems redundant"; "no button… the headline can be a hyperlink"). The review was **show-then-nothing → review → show**, when it should have been **show → settle → review**. A throwaway board render during the brainstorm would have surfaced Next-redundancy and the design direction *before* the heavy plan gauntlet.
- **Tool or agent?** Agent. I reached for maximal process (brainstorm → furnace → 3 Cowork rounds) before putting the cheap concrete artifact in front of Rex.
- **Impact: low.** What Cowork reviewed was the port *mechanics* (sync-safety across shapes/fixture/generator), which are orthogonal to column count — so the review's substance survived the schema change intact. Nothing was re-done; the cost was ordering, not waste.
- **Does it generalize?** Yes — same shape as batch-b (maximal process ahead of validating the concrete thing with Rex). Now n=2. **The cheap lever:** when the deliverable is a *thing Rex will look at*, render a rough version and show it **before** the review gauntlet. Not adopting a rule yet (Rule-of-Two: n=2, watch for n=3 before accreting a guardrail) — recorded so the tag log carries the evidence.

## Process/environment notes (not agent failures)

- **Plan-mode confusion.** Three `ExitPlanMode` calls came back as rejections (Rex pasting Cowork feedback through the reject channel), then Rex couldn't tell we were in plan mode or find the interface — the client UI state and the harness state had diverged. I could have recognized the out-of-band Cowork loop sooner and explained the plan-mode mechanics instead of re-firing the tool.
- **iPad viewing.** `open BACKLOG.html` rendered on the Mac; `computer-use request_access` timed out because the macOS approval dialog was on the Mac Rex wasn't at. Resolved with an inline `show_widget` preview (caveat: stacks lanes vertically, can't use the widget's Claude design system faithfully). **Lesson:** when Rex is on iPad, Mac-side rendering *and* macOS permission dialogs are both unreachable — reach for inline rendering first.

## What went well

- The **furnace → Cowork layering worked as designed**: the blind pre-filter missed the bucket-2 inference errors (path allowlist, false precedent), Cowork caught them — exactly the division of labor [D-043]/[D-065] intend.
- Dropping Next came from Rex *seeing* it — good collaboration, and the board is genuinely better (thinner, more scannable).

## Files changed

- This step: `BACKLOG.md` (row 40 → `next`, gloss updated), `tickets/kanban-into-scaffold.md` (Pass-1 progress note + 7-col schema pointer), this retro. `BACKLOG.html` regenerated (gitignored, not committed).
- Earlier this session (already committed): `e84b8d6` (Cowork ledger sweep), `f2ba832` (7-col schema), `5706f1b` (render redesign).

## Key decisions made

- No new `D-NNN` this session. **D-070** (the build + supersede D-068 + name the D-001 trail) is logged at the *end* of Pass 3 when the scaffold port lands, per the plan. The 7-col schema + design are visible-by-reading (`BACKLOG.md` + the render script), not a separate decision.

## Open items / next session

- **Pass 2** — port the 7-col board model into both scaffold shapes (`templates/docs/BACKLOG.md.template`, flat + modular rule templates) + re-render the `output-small` fixture. Reconcile the template's `## Conventions`/header that contradict the Gloss. Verify by dry-run substitution diffed against the fixture.
- **Pass 3** — emit the render tool to `.claude/scripts/` (root-resolution via walk-up-to-`BACKLOG.md`), generator wiring (always-emit; per-stack tag packs — confirm `stack ==` marker support first), scaffolded `/end-session` regen, log **D-070**, retire the ticket.
- Plan: `~/.claude/plans/validated-tumbling-pine.md` (synced to the 7-col reality).
