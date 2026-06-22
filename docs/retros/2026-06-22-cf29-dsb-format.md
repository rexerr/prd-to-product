# Retro — 2026-06-22 ~12:45 CDT — CF-29 Wave 3: DESIGN_SYSTEM-FORMAT.md on DSB   (4th session of the day)

Propagated the CF-29 per-artifact FORMAT-file pattern (piloted on prd-creator, [D-052](../DECISIONS.md#d-052)) to `design-system-bootstrap`, authored via `/furnace-plan`. New decision: [D-057](../DECISIONS.md#d-057).

## What was completed

- New [`skills/design-system-bootstrap/DESIGN_SYSTEM-FORMAT.md`](../../skills/design-system-bootstrap/DESIGN_SYSTEM-FORMAT.md) — single diffable shape-contract for the `DESIGN_SYSTEM.md` doc, mirroring `PRD-FORMAT.md`. Doc-only artifact scope; all-three-shapes shape scope (core skeleton + shape-gated OPTIONALs from NOTES).
- Moved the reference-side bodies (positioning anchor + falsifiable rationale, progressive-disclosure placement) out of `principles.md` → thinned to *why* + pointer. Operative echoes left untouched in the loaded template; prepended a standalone authority-pointer comment above its existing block.
- Wired FORMAT into `SKILL.md` (Files-in-skill) and `NOTES.md` (regression shape source-of-truth pointer).
- Logged D-057 (not mirrored to `DECISIONS_ACTIVE` — craft-structure, same call as D-052); updated CF-29 status in the pocock tracker, the roadmap sync marker, and the BACKLOG Wave-3 row.

## Failure this session

- **Tag:** none of the four canonical types (not bad-substitution / scope-creep / lost-context / goal-drift) — but one real near-miss, recorded as a candidate class.
- **Name the artifact:** the plan asserted "the `#### Backgrounds`-style entries are bold table labels, not headings." They are **real H4 headings** (`grep -nE '^#{1,4} '` on the fixture shows 8 of them). The blind cc-subagent *saw* `#### Backgrounds` and still mislabeled it; my preflight propagated it; Cowork didn't flag it either. The `^#{1,3} ` grep had been masking H4 the whole time.
- **Tool or agent?** Agent judgment — the bucket-2 "read it and still misread" class the furnace explicitly says it cannot fully catch. All three review passes (preflight, blind subagent, Cowork) shared the same blind spot.
- **What caught it:** build-time re-verification (re-running the heading grep with `^#{1,4}` before writing FORMAT). The "reproduce/verify before claiming done" discipline did its job — the plan's stated verification step was itself wrong, and executing it for real surfaced the error.
- **Does it generalize?** Mildly: when a verification step hinges on a regex/tool invocation, run the invocation at authoring time rather than reasoning about what it would match. `^#{1,3}` "excludes H4" was true *and* misleading — it hid the H4 rather than proving their absence. Candidate one-liner if it recurs (Rule-of-Two, n=1): *a heading/structure grep used as a shape check must match one level deeper than the deepest level it asserts, so absence is proven not assumed.*
- **→ The change it demands:** none yet (n=1). Watch for a second "verification-grep masked the thing it should have caught" instance.

## Files changed

- New: `skills/design-system-bootstrap/DESIGN_SYSTEM-FORMAT.md`.
- `skills/design-system-bootstrap/principles.md` — two sections thinned to why + pointer.
- `skills/design-system-bootstrap/templates/DESIGN_SYSTEM.md.template` — prepended authority-pointer comment (line 1); body untouched.
- `skills/design-system-bootstrap/SKILL.md`, `NOTES.md` — pointers to FORMAT.
- `docs/DECISIONS.md` (D-057), `docs/cribs-from-pocock-craft.md`, `docs/cribs-adoption-roadmap.md`, `BACKLOG.md`.
- Swept separately: `skills/furnace-plan/trial-ledger.md` (Cowork `/plan-review` append, D-018 carve-out) — dedicated commit.

## Verification

- **V1 skeleton diff:** FORMAT core skeleton matches fixture H1–H4 by name + order, with two documented small-shape variances (`#### Families` collapses to prose for a single family; `#### Type scale` carries a density parenthetical). GREEN with explained deltas.
- **V2 move-not-duplicate:** `principles.md` thinned to why + pointer; full failure-cited bodies live only in FORMAT; the template line-25 operative echo is the sanctioned exemption, not drift.
- **V3 nothing-operative-moved:** template body +1 comment only (operative echoes intact at 17/19/25); `intake.md` not in the diff; `SKILL.md` binding contracts untouched (only the Files-in-skill list gained a line).
- **V4 cross-refs:** all FORMAT links resolve; the one repo-docs link uses `../../docs/` (correct depth).
- **V5 decision-number freshness:** re-grepped max = D-056 immediately before writing → D-057.
- **Independence note:** verification self-run (build-time greps), plus the upstream blind cc-subagent + Cowork passes on the plan. Not a fresh independent verifier on the *landed tree* — self-verified there.

## Key decisions made

- **D-057** logged. Doc-only artifact scope + all-three-shapes shape scope, both ratified by Rex at plan approval.
- Surfaced (did not fix) a pre-existing template/NOTES gap: the large-shape accessibility-notes section is a NOTES expectation the template never emits. FORMAT flags it; closing it (adding generation behavior) is a separate future ticket if the large shape is exercised.

## Next session

- Push gated on Rex (not yet pushed; two commits staged locally — product + the ledger sweep).
- Wave-3 CF-29 remaining: the scoped context-engineering subset (Rule-of-Two now met by prd-creator + DSB) — its own `/furnace-plan` pass, council-gated if it reopens the shape-vs-content fork.
- If the large DSB shape is ever exercised: the template/NOTES accessibility-notes gap becomes a real ticket.
