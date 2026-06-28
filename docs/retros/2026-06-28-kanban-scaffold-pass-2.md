# Retro — 2026-06-28 09:56 CDT — Kanban → scaffold Pass 2 (templates + fixture)   (1st session of the day)

Picking up [`tickets/kanban-into-scaffold.md`](../../tickets/kanban-into-scaffold.md) (board Seq 1) after Pass 1 dogfooded the 7-col board here. This session shipped **Pass 2**: ported the one-board kanban *shape* into the `context-engineering` scaffold — both rule shapes + the one full fixture — via `/furnace-plan`. Also opened with a meta thread: documenting a **rough-render-before-the-gauntlet** working-policy story.

## What was completed

- **Rough-render policy captured.** Added the one-time Pass-2 application note to the ticket's "How to do it" ("show a rough render before the furnace/Cowork gauntlet"), and a [`BACKLOG.md`](../../BACKLOG.md) backlog row to flesh out the general policy in a new session (goal-drift n=2 evidence, not yet a minted rule). Rex's framing: the lever generalizes to "when I ask for a mockup."
- **Pass 2 shipped + verified.** Five files: [`BACKLOG.md.template`](../../skills/context-engineering/templates/docs/BACKLOG.md.template) (multi-section body → board with two new PARAMETERIZE markers `backlog_tags_block` + `board_seed_rows`, dropped `## Open decisions`, reconciled the stale "never inline"/phase references); the [`output-small/BACKLOG.md`](../../skills/context-engineering/examples/output-small/BACKLOG.md) fixture re-rendered as a complete board; the graduation rule reframed board-born in [flat](../../skills/context-engineering/templates/claude-rules-flat-AGENTS.md.template) + [modular](../../skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template) (verbatim-in-sync); and the [`output-small/AGENTS.md`](../../skills/context-engineering/examples/output-small/AGENTS.md) graduation bullet. **Verified:** dry-run substitution == fixture **byte-for-byte** (gate proven RED-capable by injecting a literal drift), flat/modular bodies identical, zero unsubstituted markers in fixtures.
- **Furnace ran as designed.** Blind Opus `Explore` reviewer caught 1 Must-fix (the `output-small/AGENTS.md` fixture would go stale — an in-scope fixture the parent plan + 3 prior Cowork rounds all missed). Cowork then caught 3 more Must-fixes the blind pass missed (dry-run gate undefined for the table body; wrong OPTIONAL-marker form nested in the `<!-- TAGS -->` comment; under-enumerated reconciliation) + refinements, across 2 rounds. All folded in; plan twice-baked before approval.

## Failure this session

- **Tag:** none (material). The plan carried defects, but every one was caught at authoring time by the furnace→Cowork pipeline *before* any code was written — that is the system working, not a session failure.
- **Worth noting (not a failure):** the blind cc-subagent passed round 1 clean while Cowork found 3 Must-fixes — the known bucket-2 limitation ([D-043]/[D-065]): a self-review can't reliably reach a marker-spec mismatch or an unreachable-pass-condition it didn't think to test. The division of labor held exactly as intended. The most valuable Cowork catch (dry-run gate undefined → `board_seed_rows`) is the **unreachable-pass-condition** class again (cf. CF-13) — a "match exactly" gate that could never pass even when the work was correct.
- **Tool or agent?** N/A — no failure landed. The rough-render lever was applied (the concrete fixture board went into the plan before the gauntlet).
- **→ Change it demands:** none.

## Files changed

- **Pass 2 product (5):** `skills/context-engineering/templates/docs/BACKLOG.md.template`, `.../examples/output-small/BACKLOG.md`, `.../templates/claude-rules-flat-AGENTS.md.template`, `.../templates/claude-rules-modular/session-discipline.md.template`, `.../examples/output-small/AGENTS.md`.
- **Tracking:** `tickets/kanban-into-scaffold.md` (rough-render note + Pass-2-DONE progress), `BACKLOG.md` (rough-render policy row), this retro.
- **Swept separately:** `skills/furnace-plan/trial-ledger.md` (Cowork's Pass-2 measurement append, [D-018] carve-out).

## Key decisions made

- No new `D-NNN`. **D-070** stays deferred to the end of Pass 3 (the build + supersede D-068 + name the D-001 trail), per the parent plan.
- Two sign-offs confirmed by Rex (ship as proposed): `gate:` fixed-generic + `area:` per-project; Build-plan phases → Seq-ordered board rows.

## Open items / next session

- **Pass 3** — generator wiring (`generator/decisions.md` + `intake.md`): wire `backlog_tags_block` (incl. generic-vs-`visual-confirm` logic) + `board_seed_rows`; retire orphaned vars (`phase_*`, `phase_2_task_placeholder`, `open_decisions_list_or_none`, `backlog_include_v2` + its `Later / V2` marker); reconcile stale abbreviated-example annotations (`output-medium/large-abbreviated.md`) + transcripts (`transcript-small/medium/large.md`); emit the render tool to `.claude/scripts/` (walk-up root resolution); wire scaffolded `/end-session` regen; log **D-070**; retire the ticket. Full handoff in the plan.
- Plan: `~/.claude/plans/crystalline-juggling-flute.md` (Pass 2); `~/.claude/plans/validated-tumbling-pine.md` (full 3-pass arc).
