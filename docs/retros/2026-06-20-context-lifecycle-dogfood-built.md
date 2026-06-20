# Retro — 2026-06-20 09:57 CDT — Context-lifecycle dogfood (built)   (4th session of the day)

Builds what [`2026-06-20-context-lifecycle-dogfood-planned.md`](2026-06-20-context-lifecycle-dogfood-planned.md) planned. Decision: [D-048](../DECISIONS.md). Commits `1705412` (dogfood) + `acf7780` (ledger sweep).

## What was completed

- The lean-plus dogfood from the approved plan (`~/.claude/plans/foamy-scribbling-thimble.md`): `tickets/` mechanism + README, furnace-trial extracted to a ticket, `BACKLOG.md` restructured (`## Active` thin index / `## Legacy`), ~9 dead items swept, `## Format` rewritten as the lifecycle rule.
- `DECISIONS_ACTIVE.md` thinned from 17 paragraph entries to one-line binding-rule index entries; D-048 mirrored; marker reconciled through D-048.
- `/end-session` retirement ritual; D-048 logged; living-document-lifecycle parent brief; one-line CLAUDE.md graduation-trigger rule.
- **Measured result:** `BACKLOG.md` 31.5K→11.5K tokens, `DECISIONS_ACTIVE.md` 3.5K→1.6K tokens — both return whole, well under the 25K cap. BACKLOG landed under the 18K threshold, so the second mega-item (`plan-review`) correctly stayed deferred to thin-on-touch.

## Failure this session

- **Tag:** none (no failure landed in the build), but two near-misses worth recording.
- **Near-miss 1 — the plan-as-approved carried a latent execution trap.** Precondition 0d gated header-collapse on a raw `grep "BACKLOG.md#"` being empty; that grep matches `trial-ledger.md` prose, so run literally it would have *wrongly preserved* the fat headers and under-delivered the thin index. Caught by Cowork `/plan-review` Round 2 (after plan approval, before building) and fixed in-plan (link-form gate `](.*#`).
  - **Tool or agent?** Agent judgment at plan-authoring — asserted "grep empty" without the link-form precision; the furnace preflight + blind reviewer both missed it (the blind reviewer is read-only and didn't re-run the grep).
  - **Does it generalize?** It's the furnace bucket-1 class (assert from a grep without exact form). The existing Check 1a covers string-equality; this is an adjacent "substring vs. precise-pattern grep" sub-case. **n=1** — do not edit the furnace yet (Rule of Two); log it. If a second precise-grep miss appears, extend 1a to "greps used as gates must match the precise target form, not a substring."
- **Near-miss 2 — process ordering.** Committed the code before writing this retro, contrary to the retro README's "write the retro before the code commit." No double-*push* resulted (nothing pushed), so the waste that rule prevents didn't land — but the ordering was wrong. Tool-or-agent: agent. Change: none beyond noting it; the discipline already exists.

## Files changed

See commit `1705412`. New: `tickets/README.md`, `tickets/furnace-trial.md`, `tickets/archive/`, `docs/briefs/living-document-lifecycle-brief.md`. Edited: `BACKLOG.md`, `docs/DECISIONS_ACTIVE.md`, `docs/DECISIONS.md`, `.claude/commands/end-session.md`, `CLAUDE.md`.

## Key decisions made

- [D-048](../DECISIONS.md) — the full record. Settled this session: decisions tier needs no ADR status-field (narrowed the brief); ACTIVE-thinning is in-scope (the `/devils-advocate` finding that Rex's "ever-growing ACTIVE" worry targets); per-file `DECISIONS.md` split + skill port deferred.

## Post-retro update (this section added after the retro was first committed)

This retro was committed at `5a9b545` and then **more work landed in the same session** — the retro froze before the session truly ended. Corrections, so the next session doesn't inherit a stale picture:

- **The retirement ritual IS now exercised** (the "UNEXERCISED" item below is superseded). The first live test ran: link-depth rewrite tested red→green, and a real decision-demotion + marker reconcile happened this session. The test surfaced an edge — `git mv` refuses an untracked ticket (one created and resolved in a single session) — now hardened by commit [`5ba52ec`](https://github.com/rexerr/prd-to-product/commit/5ba52ec) ("Guard the retirement ritual's git mv against same-session untracked tickets"). All pushed.
- **The one genuinely-unexercised piece left is thin-on-touch** — self-testing the first time a `## Legacy` entry is edited.

## Open items — verification gaps (honest)

- ~~**The retirement ritual is written but UNEXERCISED.**~~ **Superseded — see Post-retro update above.** (Original note: no ticket archived yet, so `git mv` + link-depth steps unproven.)
- **Thin-on-touch is a stated rule, untested.** First time a `## Legacy` fat entry is edited, watch whether it actually gets converted.
- **The proven shape has NOT been ported to `context-engineering`** — the deferred leverage rock. This dogfood exists to de-risk that port; it is now the next-highest foundational item.
- `plan-review` rehost stays a fat `## Legacy` entry (deferred, not parked) — converts on next touch.

## Next session

- The skill port: carry the proven thin-index + tickets + retirement shape into `context-engineering` so new projects are born with it. Its own scope-gate + likely `D-NNN`; sibling to the parked docs-structure rock ([`docs/briefs/docs-structure-and-artifact-routing-brief.md`](../briefs/docs-structure-and-artifact-routing-brief.md)).
- Watch for the first live exercise of the retirement ritual; treat it as the ritual's red/green test.
