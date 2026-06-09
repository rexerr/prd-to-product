# Retro — 2026-06-09 10:04 CDT — prd-creator intake fix pass (ask-anyway → draft-and-present + vocab/temporal scrub + Gotchas) (D-010)   (5th session of the day)

## What this session did

Aggregated four accumulated prd-creator findings (unblocked 2026-06-08) into one pass on the front-door skill of the chain. Outcome: **D-010 logged; ask-anyway shifted to draft-and-present; internal-scaffolding vocabulary scrubbed from all user-facing copy and from the spec that prescribed it; a preventive no-temporal-claims guardrail added; the `## Gotchas` section backfilled.** 206 changed lines across 10 files, under the 300-line gate.

## The crux that the planning caught

The headline finding ("ask anyway overcorrects on thorough briefs") looked like "revert to pre-fill," which would have reopened exactly what the skill deliberately banned. The real fix is a **third** behavior the old rule collapsed away:

- ❌ **silent absorption** — fill answers unseen (Pass 1.7 banned this; kept banned verbatim at `principles.md:34` / `SKILL.md:32`)
- ❌ **ask cold** — ignore the brief, make the user re-state it (the overcorrection)
- ✅ **draft-and-present** — draft from the brief, show it, get confirm/edit (not silent, not wasteful)

Draft-and-present honors the Pass 1.7 lesson *because* it was a lesson against *silent* absorption — every draft is surfaced and signed off. The mandate to change lived at exactly one line (`intake.md:25`); the silent-absorption ban was the part to **keep and augment**, not rewrite.

## What two review rounds added (the value of planning before editing)

The plan went through two reviewer rejections before approval; both caught real gaps:

1. **`generator/output-summary.md` was missing from the change set.** It is the *spec source* of the worst leak — its Format block + rule 43 prescribe the `(from cluster N)` provenance tags rendered in the examples, and it already contradicted its own line 60. Scrubbing transcripts without fixing the spec would have let a real run re-inject the leak immediately.
2. **The hand-enumerated leak list was a floor, not a spec.** It missed `small` summary openers (9/75/101/131) and the entire "Captured as D-00N" synonym class (`medium:39/43`, `large:43`) — same leak as "D-001 candidate," different surface string. Fix: scrub and verify by **category grep** (`[Cc]luster [0-9]`; `D-0\d\d` outside the read-back/output blocks), not literal strings, so verification can actually fail on a miss. The category approach then caught a *third* missed instance during execution — `output-summary.md:44`'s skipped-reason example "cluster 6 not run" — which no hand list had flagged.

The lesson reinforced: present enumerations as floors under category rules; bind verification to the category, not the instances.

## What landed (D-010)

- **Behavior:** `intake.md` (draft-and-present + 3-way distinction at cluster 0, user-facing-copy rule, no-temporal-claims guardrail, line-29/125 phrasing); `principles.md` (augmented line 34 + new "Interview conduct" section); `SKILL.md:32` augmented.
- **Vocab scrub at the spec source:** `output-summary.md` Format block + rules 43/44 (dropped `(from cluster N)` tags and the cluster-named skipped-reason example).
- **Gotchas:** three bullets on `SKILL.md` matching the sibling-skill convention, each citing a documented failure.
- **Examples:** all three transcripts scrubbed; `medium` + `large` de-abbreviated to *show* draft-and-present (medium = user edits the draft, large = user confirms unchanged); `small` kept as the no-brief ask-cold baseline.
- **Bookkeeping:** `NOTES.md` (reconciled the parked "pre-fill-then-confirm" item — its gate was met by the Squirreled negative result; build-state + regression tests 11-12 on broadened patterns); `DECISIONS.md` D-010 + `DECISIONS_ACTIVE.md` mirror.

## Verification

- Test 12a: zero `[Cc]luster [0-9]` in transcripts. ✓
- Test 12b: `D-0\d\d` only inside cluster-5 read-back + output blocks (all three). ✓
- Spec↔example: `output-summary.md` no longer prescribes the tag; transcripts render none. The four residual `(cluster N)` hits are model-facing prose (SKILL Gotchas *quoting* the anti-pattern, NOTES, README), not user-facing tags. ✓
- Output invariance: `examples/small/PRD.md` byte-identical (not in the diff). ✓
- Tests 1-10 hold (output PRD unchanged; cluster-0-first and confirm-before-write present). ✓
- Scope containment: only `skills/prd-creator/*` + `docs/DECISIONS*` touched; 206 lines < 300 gate; no split needed.

## Decisions / notes

- **No council** — the reversal is reversible prose backed by a real validation failure (below the D-009 threshold); considered and declined, recorded in D-010.
- **Scope: prd-creator only.** Sibling propagation (context-engineering + design-system-bootstrap share the patterns) is a backlogged fast-follow. The vocab/temporal halves propagate mechanically; the **ask-anyway behavioral half does not** — context-engineering's Q0a *is* the source-material question, which stays.
- **Verification ceiling (honest):** this is a static walk of updated transcripts against the regression tests, not a live skill run. The draft-and-present behavior is demonstrated in the examples, not yet observed on a fresh real project.

## Handoff — for a future session

- **Backlog fast-follow:** propagate vocab-leak + temporal fixes to the two sibling skills' `intake.md` (do NOT propagate ask-anyway blindly).
- **Still open from earlier (unchanged):** `block-deploy-cli.sh` / `block-worktree.sh` stdin fix; the bundle-PRD on-ramp is intentionally not built (D-008).
- **D-010 revisit-if:** a real run shows draft-and-present over-absorbs (users rubber-stamp wrong drafts) → tighten to per-field confirmation.

## Commit / push

prd-creator intake fix (intake/output-summary/principles/SKILL/3 transcripts/NOTES) + D-010 in both decision files + this retro, committed together. No push unless asked.
