# Retro — 2026-06-09 10:39 CDT — sibling-skill propagation of the D-010 vocab + temporal fixes   (6th session of the day)

## What this session did

Executed the fast-follow backlogged at the end of the prd-creator pass (5th session): propagate the *mechanical* halves of D-010 (vocab-leak + temporal) to `context-engineering` and `design-system-bootstrap`. Outcome: **20 changed lines across 4 files** — far smaller than the prd-creator pass, because read-only investigation showed two of the three would-be cost centers were already handled.

## The finding that shrank it

What looked like "another prd-creator-sized pass" collapsed to a near-no-op once grepped:

1. **Behavioral half was already done.** Both siblings' cluster 0 already prescribe draft-and-present verbatim — context-engineering: *"present them as 'I extracted X from your PRD — confirm or correct' rather than asking the question cold"*; DSB the same for a brand book. prd-creator was the laggard, not the template. Nothing to change.
2. **Transcripts don't leak.** All `Cluster N` references in the six sibling transcripts are `## Cluster N: topic` **structural section headers** (plus a couple `(...)` annotations) — developer-facing documentation, not simulated user-facing dialogue. Left untouched, consistent with how the prd-creator pass left NOTES.md / principles.md / README.md cluster references. Rewriting them would have been ~48 cosmetic edits with zero leak-reduction and would make the examples harder to map cluster-by-cluster.

So the genuine leak surface was **one quoted prompt** (context-engineering `intake.md:22`, `"use it as cluster 0 source?"`). DSB had zero spoken leaks. The rest is preventive.

## What landed ("Aligned" scope, Rex's pick)

- **`context-engineering/generator/intake.md`** — fixed the line-22 quoted prompt (dropped "cluster 0 source" → "the source PRD for this scaffold"); added the preventive no-temporal-claims guardrail to the "Read it before proceeding" step.
- **`design-system-bootstrap/generator/intake.md`** — added the same temporal guardrail (no quoted-prompt fix needed; none existed).
- **Both `principles.md`** — added a shared `## Interview conduct: stay in natural language, stay grounded` section (internal-scaffolding-stays-internal + no-temporal-claims), each citing the prd-creator-observed failure, so all three skills now state the same rules.

**Left deliberately untouched:** the six transcripts (structural headers, not leaks), both `SKILL.md` Gotchas sections (their three bullets carry each skill's *own* top failures; vocab/temporal weren't observed failures there), all cluster-0 behavior (already extract-and-confirm), and the model-facing `0a/0b` labels + `Q0a` state-map vars.

## Verification

- No user-facing quoted prompt names a cluster: tighter grep (`(I see|use it as|do you have|paste|confirm).*cluster [0-9]`) → zero. The one greedy-regex "hit" (`dsb intake.md:286`) was confirmed model-facing ("run the cluster-8 preview step" in a dry-run instruction), not spoken copy.
- Draft-and-present behavior unchanged in both (the "confirm or correct rather than ask cold" lines are intact — the behavior must not regress).
- Temporal guardrail present in both cluster 0s; conduct section present in both principles.md.
- Scope: 20 lines / 4 files, well under the 300 gate.

## Misses / honest notes

- **Verification is static**, same ceiling as the prd-creator pass: greps + re-reads, not a live skill run. The siblings' draft-and-present is asserted from the intake spec, not observed on a fresh project.
- **The conduct-principle additions are preventive**, not fixing an observed failure in these two skills — justified by citing the prd-creator failure as the shared mode (CLAUDE.md architecture rule 2). A purist "minimal" scope would have skipped them; "Aligned" was chosen for cross-skill consistency.
- D-010 got a propagation note rather than a new D-NNN — it's the same decision propagated, not a new one.

## Handoff

- **No open sibling-propagation work remains.** If a real run ever surfaces a *spoken* cluster-N leak in a sibling transcript (not just a header), reopen the transcript question deferred here.
- Still open from earlier (unchanged): `block-deploy-cli.sh` / `block-worktree.sh` stdin fix; the auto-detect-input finding (BACKLOG); design-system-bootstrap from-scratch validation needs a real project.

## Commit / push

The 4 skill files + D-010 propagation note + BACKLOG removal + this retro, committed together. No push unless asked.
