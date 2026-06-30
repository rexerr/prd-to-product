# Retro — 2026-06-30 16:26 CDT — Slice 2c: provenance-grounded output check (Option B) — (2nd session of the day)

Picked up board Seq 1 ("Invariant/semantic output checks") after the morning's agent-process row reconcile. Scoped the one remaining slice (2c, provenance-grounded), chose the mechanism with Rex, planned it via `/furnace-plan`, and shipped it. This **completes** the council's three-check sequence (write-guard → no-jargon-leak → provenance-grounded) and retires the Seq-1 row. Plan: [`~/.claude/plans/kind-strolling-catmull.md`](../../../.claude/plans/kind-strolling-catmull.md).

## What was completed

- **Mechanism decided with Rex before planning.** Option B (slot-scoped trace check) over Option C (structural source-binding). The dig-in established that the real grounding surface is the D-070 *agent-composed* slots (board rows/glosses), not the boilerplate banner; and that C is strongest where fabrication is rare and weakest/harmful where it's common, so it parks behind the chain-auto-composer trigger (not Rule-of-Two).
- **`context-engineering` provenance scan** — new `## Provenance-grounded scan before finalizing` in [`generator/decisions.md`](../../skills/context-engineering/generator/decisions.md), sibling to the leak scan at the same pre-write gate. A bounded *semantic* check (not a grep), scoped to an enumerated composed-fact slot list with explicit structural exemptions (lanes/`Seq`/boilerplate), backstopping the Board-seeding "compose from intake" rule.
- **`prd-creator` source-attribution rule** — extended the temporal-provenance rule in [`principles.md`](../../skills/prd-creator/principles.md) and the two age-scoped [`SKILL.md`](../../skills/prd-creator/SKILL.md) mentions to bar inventing *where a fact came from* ("based on your research" with no research named). Prose-only — its draft-and-confirm human loop is the independent catch (Rex's call); no parallel scan.
- **[D-071](../DECISIONS.md#d-071)** logged (B shipped; C parked on the auto-composer; prd-creator prose-only; DSB excluded as deterministic+copy-only); `DECISIONS_ACTIVE.md` marker bumped to D-071 (evaluated-and-skipped — implementation discipline visible by reading the skills).
- **Seq-1 board row retired** — all three council slices now shipped; the row leaves the board (no card to archive — it referenced council + D-064).

## Verification

Per the no-runner contract (dry-run substitution against `output-small/`): **RED** — a fabricated `Set up PostgreSQL contacts table` row (in-vocabulary `area:api`, so only provenance is wrong) flags against `data_persistence_paragraph` ("No persistence…"). **GREEN** — all 4 real fixture rows trace clean; fixture unedited. **Boundary (2b)** — invented audit-DB step (`primary_data_flow_steps`) and `lib/db.js` (`folder_structure_summary`) both flag. **prd-creator** — "based on your research" with none named flags; a faithful "the brief describes X" passes. No `templates/`/`examples/` output touched (no leak surface); new section leak-pattern clean; `check-live-links` 0/115 broken; board renders 0 tag warnings.

## Failure this session

- **Tag: none** — no failure reached the commit. But the layered review earned its keep: the plan as first drafted carried **four real defects**, each caught pre-ship — (1) a *derived* slot (`stack_summary_one_line`) wrongly listed as composed [blind Opus reviewer]; (2) two genuinely-composed slots missing from scope [blind reviewer]; (3) a RED test using an off-vocabulary `area:db` tag that would let the tag-validator fire instead of the provenance scan [blind reviewer]; (4) a non-sequitur rationale ("not greppable") for prd-creator's prose-only choice, when the real reason is the human-confirm loop [Cowork]. Plus a stale D-065-vs-D-064 subagent miscite I caught by re-grep, and a 3-vs-5 file-count undercount [Cowork]. The furnace preflight + blind reviewer + Cowork pipeline did exactly its job: catch authoring imperfections before they ship. n=1 datum that the three-layer review converts plan-authoring slips into pre-ship catches.

## Key decisions

- **Option B, not C** (Rex) — bounded slot-scoped trace check; C parked behind building the chain auto-composer, explicitly not Rule-of-Two. Rationale in [D-071](../DECISIONS.md#d-071).
- **prd-creator prose-only** (Rex) — human-confirm loop is the independent catch; no parallel scan.
- **DSB excluded** — no fact-slot surface (deterministic-transform + copy-only, D-044).

## Open items

- **Residual design bet (2b boundary-completeness):** whether the ~13-slot list is the *complete* fabrication-risk surface is the one thing the dry-run can't fully settle. Revisit trigger: a fabrication slips through a composed slot not in the list during real use → widen the list or the trace rule.
- **Port-to-scaffold:** none needed — the CE scan lives in the shipped generator and the prd-creator rule ships with that skill; both travel to users already.
- Cowork's `/plan-review` append to `skills/furnace-plan/trial-ledger.md` swept in its own dedicated commit (D-018 carve-out), separate from the 2c work.

## Next session

- Board `next` lane is now **empty** (Seq-1 retired). Next work is Rex's pick from `backlog` — the `Generator skips seeded allowlist when hooks are off` fix (logged this morning) is a small ≤1-file candidate.
