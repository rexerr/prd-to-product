# Retro — 2026-06-21 07:08 CDT — G-19 adoption (positioning anchor + falsifiable rationale → DSB)   (1st session of the day, crib 1 of 2)

First of the two Wave-2 cleanup cribs Rex sequenced before opening CF-29 as the furnace-trial calibration vehicle. Decision: [D-050](../DECISIONS.md).

## What was completed

- **G-19 adopted into `design-system-bootstrap`** — see [D-050](../DECISIONS.md) for the rule and the 4 landing files; the crib + adversarial verdict are in [`cribs/cribs-from-gstack.md`](../cribs/cribs-from-gstack.md) (G-19 row, now `Adopted`). Not restating here (CF-06).
- **Scope corrected mid-flight, twice — both down.** Sold to Rex as "small"; reading the real surfaces showed it was a 5-file template change (intake capture is load-bearing — part (a) is explicitly "at intake"). Surfaced that honestly and got the nod before editing (crossed the >2-file gate). Then on inspection trimmed 5→4: a plain `PARAMETERIZE`-from-a-question registers in `intake.md`'s marker map, so `generator/decisions.md` needed **no** edit (it only registers OPTIONAL/derived markers). Net: 4 product files.
- **Bookkeeping:** D-050 logged (not mirrored — visible-by-reading, like D-036–D-038); `DECISIONS_ACTIVE.md` marker bumped to D-050; gstack tracker G-19 → `Adopted` (both the adoption table and the adversarial-verification row); roadmap sync marker updated (Wave-2 remaining = solo CF-07 + G-18-blocked).

## Verification (T-class)

Structural assertions, not byte-diff (2026-06-08 council): `positioning_anchor` marker traces to Q1e in the marker map · section present in template + fixture · **zero** leftover `PARAMETERIZE` markers in the fixture · rationale rule in both the emitted doc and `principles.md`. Fixture is a condensed faithful rendering of the template section. `Self-verified — independent sub-task not spawned` (a sub-50-line prose/template crib with a mechanical check; no oracle warranted).

## Failure this session

- **Tag: none.** The "small" mis-estimate was caught and disclosed *before* any edit (the scope gate did its job), and the 5→4 trim was a correct read, not a miss. No goal/scope/context/substitution failure.

## Durable work unit

D-050 (binding via the DSB skill files, not mirrored). No BACKLOG line — G-19 was a roadmap-sequenced crib, tracked in the gstack tracker + roadmap marker, both updated.

## Open / next

- **CF-07 next** — its landing is broader than "small" (5 candidate surfaces, heavy overlap with the D-005/D-006 write guard + the D-018 reload-before-write carve-out). Needs its own scope read before editing — likely collapses to 1–2 genuinely net-new surfaces. That read is the next action.
- Then CF-29 (Wave 3) as the furnace-trial calibration vehicle, per the [furnace-trial ticket](../../tickets/furnace-trial.md).
