# Retro — 2026-06-18 07:05 CDT — Retro-convention cluster: C-09 + CF-06 (D-024)   (1st session of the day)

*(First retro written under the convention it adopts — lesson→change prompts + reference-don't-restate.)*

## What was completed

- Adopted the **first tight same-surface cluster** (C-09 + CF-06, both → `docs/retros/README.md`, both class D) — the sanctioned non-batch form under D-022. Decision + full rationale: [D-024](../DECISIONS.md). Edits, verification, and the deferred-backport reasoning: [the plan](../../../.claude/plans/sleepy-dreaming-hollerith.md) (not restating here).
- All 7 class-(D) verify steps green, including the deliberate **empty diff** on `.claude/commands/end-session.md` (it inherits CF-06 by reference).

## Failure this session

- **Tag:** none — no bad substitution, scope creep, lost context, or goal drift.
- A near-miss did land, so forcing the lesson→change jump:
  - **Tool or agent?** Agent. The draft plan under-specified two bookkeeping edits (the sync-marker as a "date refresh" rather than an appended adoption record; the tracker-cell flips quoted as whole-cell replacements rather than fragment edits). Cowork caught both.
  - **Does it generalize?** Yes — a recurring *plan-precision* class: when an edit must preserve surrounding text, the plan should say "edit only fragment X," not quote a partial cell as the replacement. Same family as CF-03's path-imprecision, one rung up (cell-fragment vs string-form).
  - **→ The change it demands:** None minted now. Both were **bucket-3** refinements (Cowork's job, caught and applied pre-execution); the furnace's own *string/equality-claim* trigger (logged at [D-023](../DECISIONS.md) / the [furnace BACKLOG item](../../BACKLOG.md)) already names the adjacent class. If fragment-preservation misses recur as **bucket-1**, fold "quote the fragment to change, not the whole cell" into furnace Check 1 — not before (Rule of Two; don't contaminate the mid-trial instrument).

## Furnace trial signal (link, not restate)

- Cowork wrote **2 live rows** for this review, **both bucket-3** (no bucket-1, no bucket-2) — see [`skills/furnace-plan/trial-ledger.md`](../../skills/furnace-plan/trial-ledger.md). Against CF-03's 1 bucket-1 + 1 bucket-3, this is movement toward the **mostly-bucket-3** state that is D-022's promotion-trigger direction (consider the `ExitPlanMode` hook). Two data points; not a verdict. Trial-grading stays Rex's per the [furnace BACKLOG item](../../BACKLOG.md).

## Files changed

- `docs/retros/README.md` — C-09 lesson→change prompts (`## Failure this session`) + CF-06 "Reference, don't restate" (`## Discipline`) + suggested-skills atom (`## Next session`).
- `docs/cribs-from-steinberger-ecosystem.md`, `docs/cribs-from-pocock-craft.md` — C-09 / CF-06 Status cells → `Adopted (→ D-024)`.
- `docs/DECISIONS.md` — **D-024**. `docs/cribs-adoption-roadmap.md` — rows 15/16 + sync marker.
- `skills/furnace-plan/trial-ledger.md` — Cowork's 2 rows (**separate dedicated commit**, D-018 sweep).

## Key decisions made

- **D-024** (see DECISIONS.md — not restating). Establishes the worked example of D-022's "one tight cluster per pass."

## Open items

- **Deferred (T) follow-up:** backport C-09 + CF-06 into the scaffolded retro template (`skills/context-engineering/templates/docs/retros/` + the `examples/output-small/` fixture) — distinct surface + class, promote when an emitted project needs it.
- **Noticed-in-passing (not fixed):** `docs/retros/README.md`'s `## Open items` template line still references `PARKING_LOT.md`/`ROADMAP.md`, stale for this repo (uses `BACKLOG.md`/`DECISIONS.md`). Out of scope for this cluster; flag for a future incidental touch.

## Next session

- Next Wave-1 crib from [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md): **CF-02** (durable-PRD rules → prd-creator) — the queued (T) pass, or another cheap (D) win (C-14/C-10). Open with `/furnace-plan` for CF-02 (it's class T, touches a skill).
