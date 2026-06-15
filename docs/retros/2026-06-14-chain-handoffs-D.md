# Retro — 2026-06-14 ~10:45 CDT — chain orchestration fix-candidate D shipped   (1st session of the day)

Triggered by a discussion of Addy Osmani's "loop engineering" piece, which routed into the creator-vs-checker question, the furnace-plan grading refinement, and then the first real planning task run through the full furnace → Cowork loop.

## What was completed

- **Furnace-plan grading refined (committed `2e33a51`, earlier this session):** the trial's raw Cowork Must-fix count was replaced with a three-bucket classification (no-read / read-but-wrong / judgment) so an unchanged catch rate can be diagnosed instead of guessed. Came out of the loop-engineering creator-vs-checker discussion — Addy's "distinct agents prevent self-grading" maps onto Cowork being the distinct checker, and the furnace preflight being a forcing function that defeats one failure sub-type but not the other.
- **Chain orchestration fix-candidate D shipped ([D-014](../DECISIONS.md)):** context-engineering's `generator/output-summary.md` §3 now names `design-system-bootstrap` as a conditional successor with an inline skip condition; DSB's `SKILL.md` gained an "unrequested collision" decline-gate (the qventus lesson promoted from a buried gotcha), worded to distinguish it from the adjacent "migrate" bullet. prd-creator needed no edit — its output-summary already hardcodes the context-engineering handoff and forbids inventing other next steps (verified, not assumed).
- **Fix-candidate C (repo rename) held** as a separate Rex-gated decision. Authoring verification refuted the backlog's cost estimate: 112 refs across 36 files (not ~15, mostly historical record), a local-dir rename breaks the 3 skill symlinks *and* the context-engineering-audit skill's 6 hardcoded absolute paths, and it touches gated agent-config files.

## Failure this session

- **Tag: bad substitution (planning-stage unverified assertions — both caught pre-commit by the furnace → Cowork loop).** The furnace ledger I authored carried two wrong facts: (1) "the new decision is D-013" — asserted without ever reading `docs/DECISIONS.md`, where D-013 was already taken (the `/audit-context` decline). Furnace Check 1 ("every count traces to a read this session") *should* have forced that read and I skipped it — a **bucket-1** miss, the "tighten the preflight, do not kill" signal. (2) "DSB is never named anywhere in either file" — false; `context-engineering/SKILL.md:59` names it. I had read that file in full and still misread it — a **bucket-2** miss, the confident-misread class our morning discussion argued self-review structurally cannot catch. Cowork caught both. Net: nothing wrong reached commit, and the first live furnace ledger produced exactly the bucketed data the grading instrument was built for the same session.

## Files changed

- `skills/context-engineering/generator/output-summary.md` — §3 conditional DSB successor step (modified)
- `skills/design-system-bootstrap/SKILL.md` — body decline-gate; frontmatter description left byte-identical (modified)
- `docs/DECISIONS.md` — D-014 appended, five-field format (modified)
- `BACKLOG.md` — chain-orchestration item marked D-shipped / C-held; furnace grading entry refined earlier (modified)
- `docs/retros/2026-06-14-chain-handoffs-D.md` — this retro (new)

## Key decisions made

- **D-014** — chain skills name their successor with a skip condition. Not mirrored to DECISIONS_ACTIVE.md (Rex's call): effects are visible by reading the two skill files, matching the D-011/D-012 skip precedent.
- **C and D decoupled.** D is reversible additive prose and the real architectural fix; C is irreversible/outward-facing with underestimated cost. Shipping D alone and gating C corrects the backlog's "C is the cheapest first move" framing — D was the cheaper, safer, higher-value move.
- **DSB routing description left unchanged.** The harness routes on the frontmatter description (already ~478 chars near a possible truncation cap), so the gate is a decline-after-consideration, not route-prevention — recorded explicitly in D-014 so it is not a silent gap.

## Open items

- **Furnace trial signal accumulating.** This was the first ledger attacked by Cowork: 1 bucket-1 + 1 bucket-2 + three bucket-3 refinements across two rounds. The bucket-1 (D-013 number) is a "tighten the preflight" signal — the furnace should more rigorously force the read-the-decisions-log step before asserting any `D-NNN`. Worth watching whether that recurs.
- **Fix-candidate C** remains a live Rex decision: rename-at-all, operative-vs-historical boundary, GitHub redirect (UNVERIFIED). Held in BACKLOG.
- Stale `ROADMAP.md` cross-ref in the audit skill (Cowork confirmed it absent) — unrelated to D, left for a future incidental edit.

## Next session

- Keep using `/furnace-plan` on real planning work to grow the Cowork-graded signal. If bucket-1 misses recur (asserting facts without the forcing-function read), tighten the furnace preflight's read-enforcement before considering the hook promotion.
- C is teed up if Rex wants it; the verified scope and hazards are in the plan + BACKLOG.
