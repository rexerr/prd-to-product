# Retro — 2026-06-08 14:03 CDT — session-start AGENTS.md read made rule-shape-conditional (group 5)   (7th session of the day)

## What this session did

Two things:

1. **Reviewed the skill-injection-by-project-type doc** (`/Users/rexc/Sites/seance/docs/references/skill-injection-by-project-type.md`) and logged it as a tracked BACKLOG item rather than building it. The doc is the *domain-layer* companion to the already-shipped *process-layer* agent-process work. Rex chose "log to BACKLOG only."
2. **Shipped group 5** — the last open piece of the "Agent-process & context-harness upgrades" BACKLOG item: harness-condition the `session-start` AGENTS.md read on `rule_shape`.

## Group 5 — what changed

- `templates/claude-commands/session-start.md.template` — `AGENTS.md` step now gated by `<!-- OPTIONAL: agents_read_step -->` on `rule_shape == "modular"`. Flat shape drops it: CLAUDE.md auto-loads and carries the rules, AGENTS.md is only a thin pointer, so reading it is wasted tokens.
- `examples/output-small/.claude/commands/session-start.md` (flat shape) — regenerated: AGENTS.md step removed, list renumbered 1–3.
- `generator/decisions.md` — added "session-start AGENTS.md read is rule-shape-conditional" under OPTIONAL block handling, naming the failure mode (a flat-shape session paying to re-open a pointer file whose target is already in context).
- `.claude/commands/session-start.md` (this repo's own, flat shape) — dropped the AGENTS.md step, renumbered 1–3. This was the gated dog-food self-edit; applied with Rex's explicit OK.
- `BACKLOG.md` — logged the new domain-layer skill-injection item; marked group 5 DONE; groups 1–5 now shipped.

## Verified — with evidence

- **Dry-run flat substitution diffs clean.** Processed the template through the flat-shape rules (drop `agents_read_step` block, keep parking-lot since `include_parking_lot == true`, strip template header + OPTIONAL markers, renumber) and `diff`'d against the committed `output-small` example → clean, "flat substitution reproduces the example exactly."
- **Modular path unverified by diff but inspected.** Template still carries `1. AGENTS.md` as the first step; the marker is true for modular so the read is preserved. No modular example exists in `examples/` to diff against, so this rests on inspection, not a substitution diff. (Standing gap: there is no modular-shape example output tree to regression against.)
- **Self-edit confirmed** by grep: our `session-start.md` no longer contains an AGENTS.md line; steps are contiguous 1–3.
- **BACKLOG cross-references** to template/decisions/example paths re-checked against the edited files.

## Misses / deviations / honesty

- **Scope of group 5 vs. the source brief.** `agent-process-brief.md` §1.1 / Appendix A argues a broader redesign of `/session-start` (don't re-read CLAUDE.md *or* AGENTS.md in any shape; scale heavy reads; make ROADMAP/DECISIONS conditional on resuming feature work). Group 5 as tracked was narrower — just the rule-shape conditioning of the AGENTS.md read — so I deliberately did *not* do the full Appendix-A rewrite. Surfaced this to Rex rather than silently expanding scope. The broader rewrite remains un-logged; if it's wanted it should become its own BACKLOG item.
- **Modular shape may also be redundant.** By §1.1's logic, in modular shape CLAUDE.md is `@AGENTS.md`, so AGENTS.md auto-loads via the import too — meaning the read is arguably wasted there as well. Group 5 (and the new decisions.md rule) keep the modular read on the conservative reading that AGENTS.md is canonical there and worth an explicit orient. Not re-litigated; flagged here as a known open question if anyone revisits.
- No tests/build in this repo; verification is the dry-run-diff contract only.

## Handoff

**Gated on Rex / open:**
- The new **skill-injection-by-project-type** BACKLOG item — domain-layer capability for `context-engineering`. Do **not** build until the plugin-vs-vendor promotion mechanic is designed (the §4 flow only solves the vendored case; most candidate skills now arrive as marketplace plugins where active/parked is enable/disable, not a filesystem move). Large (>300-line gate) + new artifact type.
- Whether to do the **broader Appendix-A session-start rewrite** (see Misses above) — currently un-logged.
- Standing gap: **no modular-shape example output tree** to regression-test modular template changes against.

**Single next thing to pick up:** none forced. The agent-process/context-harness upgrade item is now fully shipped (groups 1–5). Natural next candidates are the gated prd-creator intake.md fixes (aggregated in BACKLOG) or designing the skill-injection mechanic.
