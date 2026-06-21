# Retro — 2026-06-21 07:08 CDT — CF-07 adopted narrowly (co-edited-file reload-before-write)   (1st session of the day, crib 2 of 2)

Second of the two Wave-2 cleanup cribs this session (after [G-19](2026-06-21-g19-positioning-anchor.md)). Decision: [D-051](../DECISIONS.md).

## What was completed

- **CF-07 adopted narrowly** — one new CLAUDE.md rule ("Reload a co-edited file before writing it"), the write-side complement of the D-018 ledger-sweep. The scope read, the rule-by-rule verdict, and the three parked rules are in [D-051](../DECISIONS.md); not restating here (CF-06).
- **Bookkeeping:** D-051 logged (not mirrored — CLAUDE.md-self-evident + redundant with already-mirrored D-018); `DECISIONS_ACTIVE.md` marker → D-051; pocock tracker CF-07 → `Adopted-narrowly`; roadmap marker updated (Wave 2 effectively complete bar the blocked G-18).

## The finding — "small one" was mostly already-held

CF-07 was billed (by me, at sequencing time) as a small Wave-2 crib with a 5-surface landing. The scope read collapsed it: rule 1 redundant (C-30 + never-writes), rule 3 no live referent, rule 4 *tensions with a deliberate decision* (generators default to skip-not-merge by design). Only rule 2 was net-new, and even it is ~90% enforced already — the Edit tool rejects stale-buffer writes within a session; D-018 names the one cross-agent case. Net adoption: **1 file, <15 lines**, closing only the general cross-agent residual (Cowork co-editing — the surface that's actually growing).

This is the value of the scope read the lifecycle mandates: a faithful crib adoption can be *one line + three documented declines*, and that's a complete outcome, not a half-job. The declines (CF-04 concept-keyed) are the durable part — they stop a future mine re-litigating CF-07's redundant rules.

## Failure this session

- **Tag: none.** The over-scoped initial framing ("small, 5 surfaces") was corrected by the mandated scope read *before* editing and surfaced to Rex with a recommendation; he chose adopt-narrow. The gate worked as designed. No goal/scope/context/substitution failure reached an edit.

## Durable work unit

D-051 (binding via CLAUDE.md prose; not mirrored). No BACKLOG line — roadmap-sequenced crib, tracked in the pocock tracker + roadmap marker.

## Open / next

- **Wave 2 effectively complete** — only G-18 remains, blocked on the unbuilt C-24 oracle prompt (Wave 3). Next leverage is **Wave 3** (`/furnace-plan` each); **CF-29** is the planned furnace-trial calibration vehicle per the [furnace-trial ticket](../../tickets/furnace-trial.md) — the next real furnace plan, calibrated pre-build.
