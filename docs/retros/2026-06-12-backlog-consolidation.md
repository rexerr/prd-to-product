# Retro — 2026-06-12 23:17 CDT — Scaffolded work-tracking consolidated into one lean BACKLOG.md   (4th session of the day)

## What was completed

- **`context-engineering` now scaffolds a single `BACKLOG.md`** instead of the `ROADMAP.md` + `docs/PARKING_LOT.md` + `docs/FUTURE.md` trio — mirroring this repo's own `afb2964` consolidation, but *adapted for build mode* (the design discussion's key finding): the file keeps a phased **Build plan** section a greenfield project actually needs, plus In progress / Backlog / Open decisions / Done, and "grows into" a flat backlog as phases are checked off. `BACKLOG.md` from birth (Rex-confirmed) for cross-project filename uniformity.
- **New template** `templates/docs/BACKLOG.md.template`; **deleted** `ROADMAP/PARKING_LOT/FUTURE.md.template`. **Generator wiring:** intake Q22 dropped (deferrals always have a home in BACKLOG; no gate), Q24 reworded to `backlog_include_v2` (default off, gates an optional `Later / V2` section); state map, inclusion table, Phase-1 derivation, PRD-V2-extraction, output-summary, and the marker audit-trail all repointed.
- **Reference patches** across `AGENTS.md`, flat-CLAUDE, session-discipline, session-start/end-session commands, the four `docs/*.md` cross-refs, `principles.md`, and `NOTES.md` — every `ROADMAP`/`PARKING_LOT`/`FUTURE` filename reference migrated.
- **Example tree regenerated:** `examples/output-small/` gets `BACKLOG.md` (rendered), loses `ROADMAP.md` + `docs/PARKING_LOT.md`; the three interview transcripts and both abbreviated output sketches updated to the new intake (dropped Q22, `backlog_include_v2`) and file shape.
- **Phase 0 (separate commit `db4160a`):** defused the two stale hook-premise artifacts Rex flagged — the old hook plan file's "silently ignored" claim corrected in `~/.claude/plans/` (local), and the hook retro's the-council "open item" annotated closed.

## Failure this session

- **none — but two near-misses, both caught by verification, not by the plan.**
  1. **Leanness check initially FAILED.** First template draft rendered to 489 words vs. the old session-start load of 330 — *heavier*, the opposite of the goal — because its Format section and per-section intros were verbose meta-prose about staying lean, loaded every session. Caught by the `wc -w` step (not by "it looks right"); fixed by trimming to terse Conventions + bare section headers → 313 words, now below baseline. The verification contract earned its keep exactly here.
  2. **Inventory under-counted by ~12 files.** The Phase-1 Explore agent's inventory missed the three transcripts, both abbreviated output sketches, `NOTES.md`, and three generator state-map/marker listings. The full `grep` sweep (case-insensitive, whole tree) caught them. Lesson: trust the grep, not a single inventory pass — and run it case-insensitively (`include_future`/`include_parking_lot` only surfaced on the second, case-insensitive sweep).

## Files changed

- 31 files, +161/−235 (net −74). New: `templates/docs/BACKLOG.md.template`, `examples/output-small/BACKLOG.md`, this retro. Deleted: the three old templates + two old example files. Modified: generator (`intake.md`, `decisions.md`, `output-summary.md`), `principles.md`, `NOTES.md`, 6 templates, 8 example files.

## Verification

- **Dry-run substitution diff CLEAN:** rendered `BACKLOG.md.template` with simple-form params + OPTIONAL gates (`phase_2_section` true, `later_v2_section`/`decisions_active_xref` false) → byte-identical to `examples/output-small/BACKLOG.md`.
- **Stale-reference sweep CLEAN:** whole-tree case-insensitive grep returns only two intentional refs (the template's provenance line; `## Roadmap V2` as a PRD heading-name to scan for). No orphaned `Q22`.
- **Leanness:** session-start load 313 words vs. old 330 — leaner, and the one-line-entry Conventions contract keeps it lean as it grows (the real win over ROADMAP's unbounded entries).
- **Example tree:** `BACKLOG.md` present, `ROADMAP.md`/`docs/PARKING_LOT.md` gone, all cross-refs resolve, session-start reads `BACKLOG.md` and it exists.

## Key decisions made

- **Build-mode adaptation over literal mirror:** the dog-food BACKLOG is a *continuous-mode* phaseless kanban; new projects are *build-mode*, so the scaffold keeps phases. Rejected HTML kanban (reopens D-001/D-012, heavier for the agent) and external tools (Linear/Notion break repo-portability + bake a dependency into a zero-dep scaffolding skill) — the backlog serves the agent, stays lean markdown in-repo. Full reasoning in the session discussion; no `D-NNN` (reversible template prose, no new binding invariant).
- **The "no-TBD/stub-task" convention line was cut** (flagged optional in the plan) once the leanness check forced the budget — it's a superpowers liftable that can ride a future incidental edit.

## Open items

- **Item 34 trigger fired and is deliberately deferred:** this session substantively edited context-engineering's templates, the promotion trigger for BACKLOG item 34 (scaffold-level artifact upgrades) and the superpowers liftables. Not folded in — they carry their own pressure-test preconditions. Logged here so the deferral is intentional.
- Both this session's commits (`db4160a` Phase 0, plus this consolidation) are **local, not pushed** — push only on request.
- Existing scaffolded projects (the-council, seance, qventus) still use the old ROADMAP/PARKING_LOT shape; the skill change does not retro-migrate them. Migrate per-project only if a real need arises (no auto-migration).

## Next session

- If pushing, bundle both local commits. Otherwise: the In-progress backlog items remain validation-gated; the deploy-shell pilot still needs a live-URL project. The BACKLOG consolidation is itself now testable on the next real scaffold-from-nothing run.
