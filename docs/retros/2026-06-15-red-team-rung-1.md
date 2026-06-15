# Retro — 2026-06-15 ~11:30 CDT — red-team Rung 1 shipped (D-016)   (1st session of the day)

Session-start oriented on the 2026-06-14 chain-handoffs retro; Rex picked the BACKLOG "red-team sibling skill" item. The work resolved into a critique-before-locking handoff in prd-creator, authored via `/furnace-plan` and routed through Cowork across two rounds.

## What was completed

- **Red-team Rung 1 shipped ([D-016](../DECISIONS.md)).** prd-creator's `output-summary.md` gained a "When to recommend a pressure-test pass" subsection: when a PRD locks an **identity-defining bet in tension with a V1 cut**, the terminal "Next step" emits one optional, tool-agnostic critique line before the context-engineering pointer; omitted for routine/low-stakes/conventional PRDs. Reuses the D-014/D-015 successor-handoff pattern. The `examples/large` transcript was updated to show it firing (its advice-tone differentiator meets the bar); `small`/`medium` stay terse — the example set now demonstrates selectivity (2 omit, 1 fires).
- **Escalation ladder recorded, not just a point fix.** Rung 1 (handoff) shipped; Rung 2 (build the `/red-team` sibling) stays parked with a promotion trigger (handoff observed dropped in a real run); Rung 3 (fold critique work into prd-creator) rejected as a single-purpose violation. context-engineering's scaffolded ROADMAP critique was scoped out (no observed-failure evidence — Rule of Two).
- **Pre-decision orientation caught that the niche may already be covered.** Before committing, surfaced that the ecosystem has grown thick with adversarial tooling (devil's-advocate, plan-review, llm-council) since the 2026-05-11 evidence, which is why Rung 1 (cheap handoff) was chosen over building the skill — and Rex confirmed the direction.

## Failure this session

- **Tag: bad substitution (planning-stage internal contradiction, caught pre-commit by furnace → Cowork).** The rev. 1 plan placed the conditional critique copy inside `output-summary.md`'s always-printed Format block while simultaneously claiming the example transcripts stayed valid *because* the step was conditional — the two cannot both hold. A **bucket-2** miss (all relevant facts were read; the synthesis was internally inconsistent — the confident-misread class self-review structurally cannot catch). The same round also carried an over-broad trigger ("any V1/V2 cut") that fired on every PRD, collapsing "conditional" into "mandatory." Cowork caught both as must-fixes. Round 2, after the fix, produced only bucket-3 refinements (fill-slot instantiation, a sharper identity-defining-and-in-tension cue, a verification-scope clarification) — no bucket-1 or bucket-2. Net: nothing wrong reached commit.

## Files changed

- `skills/prd-creator/generator/output-summary.md` — new "When to recommend a pressure-test pass" subsection + relaxed "Next step" rule (modified)
- `skills/prd-creator/examples/large/transcript.md` — terminal "Next step" shows the critique line firing, fill-slot instantiated (modified)
- `docs/DECISIONS.md` — D-016 appended, five-field, no ACTIVE mirror (modified)
- `BACKLOG.md` — red-team item marked Rung 1 shipped / sibling parked, escalation ladder recorded (modified)
- `docs/retros/2026-06-15-red-team-rung-1.md` — this retro (new)

## Key decisions made

- **D-016** — prd-creator terminal state conditionally recommends a critique pass before the context-engineering handoff. Not mirrored to DECISIONS_ACTIVE.md (effect visible by reading the skill files; D-011/D-012/D-014/D-015 precedent).
- **Rung 1 over Rung 2/3.** A soft handoff is cheaper than a new skill and doesn't duplicate ecosystem critique tooling; the sibling stays parked behind an observed-drop trigger.
- **Two deliberate non-edits recorded in D-016** so they're not later flagged as drift: `SKILL.md:38` keeps "typically run context-engineering" (the hedge stays accurate); `principles.md:104` council principle left unchanged (reference-only, rarely co-occurs with the summary — the rev.-1 bridge sentence was dropped as low-value, per Cowork).

## Furnace trial signal (accumulating)

Third real ledger attacked by Cowork. Round 1: 1 bucket-2 (the Format-block contradiction) + 1 over-broad-trigger design flaw; round 2: bucket-3 only. The bucket-1 class from the 06-14 Part-1 miss (asserting a `D-NNN` without reading the log) did **not** recur — D-016 was confirmed as next-free by grepping the header list before claiming it, applying the prior lesson. Consistent with the 06-14 reading: the forcing function holds when honored; the residual misses are the read-but-wrong class that a distinct reviewer, not self-review, must catch.

## Open items

- **Furnace promotion watch unchanged.** Still no bucket-1 recurrence; the hook-promotion question stays gated on the content proving out (council's "earn the hook" caveat). One more bucket-2 caught this session reinforces that the distinct-verifier role (Cowork) remains load-bearing.
- **Fix-candidate C (repo rename)** still a live Rex-gated decision (carried from 06-14).
- **Rung 2 trigger:** promote the parked `/red-team` sibling only if the soft handoff is observed dropped in a real run.

## Next session

- The handoff is shipped but unexercised — like DSB and the build-defaults deploy-shell, its real validation needs a live prd-creator run on a PRD that meets the bar. Watch for one.
- Nothing pushed this session (no push requested).
