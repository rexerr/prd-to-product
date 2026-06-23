# Retro — 2026-06-23 08:11 CDT — Scaffold port + belt/suspenders scan   (1st session of the day)

Executed [`docs/briefs/scaffold-port-candidates-brief.md`](../briefs/scaffold-port-candidates-brief.md) end to end: ported the two known generic gaps into the `context-engineering` scaffold, ran the belt+suspenders scan, and adopted the two candidates that cleared the n≥2 bar. Dogfood of the new CLAUDE.md "Port self-improvements back to the skill" rule.

## What was completed

- **Ported two generic process gaps** into the scaffold (both shapes + the rendered fixture): the self-modification-of-config gate (autonomy never-self-clear list) and the delegate-to-subagent + engineered-blindness verifier rule (session-management). Generic wording per [D-013](../DECISIONS.md)/[D-019](../DECISIONS.md), each citing its failure mode. Commit `41bb0b3`.
- **Ran the belt+suspenders scan in two passes** (each a fresh subagent): the process layer first, then — after Rex caught the gap (see Failure) — the shipped skills as surfaces.
- **Adopted the two n≥2 candidates** (commit `9817fdd`): prd-creator standing scaffolding-leak category grep at the pre-write confirm step; context-engineering "never product code" banned-path list turned into a Write-time allowlist assertion. Both repo-internal; neither ports to the scaffold.
- **Deferred the rest** under the anti-guardrail stance: the ledger-sweep hook (n=1) recorded as a `watching` tripwire row (commit `3cc7566`); four other n<2 candidates left in the brief.
- **Retired** the board row + stamped the brief executed (commit `96a2f82`).

## Failure this session

- **Tag:** goal drift (delivered scope drifted narrower than the ask; caught by Rex, not by me).
- **Name the artifact:** the brief's headline says scan "this repo **AND the skills it ships**," but its method *step 1* lists only `skills/context-engineering/templates/` for the skills portion. My first subagent prompt scoped to step 1 literally, so the first scan never swept prd-creator / DSB / mine / plan-review / furnace-plan / CE-proper for their own belt-only disciplines. Rex asked "did you actually do this?" and I had to run a second pass — which found the two candidates that were actually adopted. The narrow scope would have shipped a "nothing to adopt" verdict that was wrong.
- **Tool or agent?** Agent judgment — I failed to reconcile the brief's broad headline against its narrower enumerated method before delegating, and wrote the delegation to the letter of the list.
- **Does it generalize?** Plausibly a class: when a spec's headline scope is broader than its enumerated steps, the enumeration is often illustrative, not exhaustive — taking it as a closed list under-delivers. Distinct from ordinary scope-creep (this was scope-*shortfall*).
- **→ The change it demands:** none yet (n=1). Candidate one-liner if it recurs (Rule-of-Two): *when a brief's headline scope is broader than its enumerated method, scope to the headline (or surface the gap), don't silently execute the narrower list.* Watch for a 2nd instance.

## Verification — what it did and didn't cover

- **Port:** confirmed the new content present in all 5 expected locations, both autonomy `OPTIONAL` blocks still fence-balanced, only the 3 intended files touched (grep + `git diff --stat`). This was a targeted-grep check, **not** a full generator dry-run substitution rendered and diffed against `output-small` (class T) — lighter than the CLAUDE.md contract's strongest form.
- **prd-creator suspenders:** *ran* the category greps live against the example PRDs — `[Cc]luster [0-9]` returns zero; `D-0[0-9]` matches only the sanctioned "Decisions already made" block ([examples/small/PRD.md:56–59](../../skills/prd-creator/examples/small/PRD.md)); `output-summary.md` carries no `(from cluster N)` tags. Red-capable: returns clean because the 2026-06-09 scrub fixed the fixtures; would return matches on a real leak.
- **CE suspenders:** prose-instruction assertion (per-write, no runtime fire possible) — self-verified by read + consistency with the existing banned-path list and the D-005/D-006 write guard.
- **Evidence claims:** verified both subagents' n=2 counts against source myself ([decisions.md:559](../../skills/context-engineering/generator/decisions.md), [2026-06-09 intake-fix retro](2026-06-09-prd-creator-intake-fix.md)). This spot-check caught a subagent overreach — it marked the CE check "port: YES"; I corrected it (scaffolded projects write product code by design, so there is no scaffold-side analog).

## Key decisions made

- **No `D-NNN` for the two adopted suspenders** (retro-only). Both are visible by reading the two skill files (fail the `DECISIONS_ACTIVE` "not visible in code" bar), and the direct precedent — push-state belt+suspenders — was retro-logged, not decision-logged. A decision would be warranted only if this became a cross-skill mandate ("every shipped skill carries a deterministic leak-grep"); it didn't.
- **Adopt 2, defer 4** against the n≥2 bar (precedent: push-state n=3, decision-number n=2).

## Open items

- Four deferred belt+suspenders candidates (DSB raw-hex n=1, mine synth-write n=1, write-guard arm-forgotten n=0, furnace sentinel n=0) — recorded in the brief; promote only on a 2nd instance.
- Ledger-sweep hook — `watching` row; build the pre-commit hook only if a 2nd accidental sweep lands.

## Next session

- Wave-3 CF-29 remaining: the scoped `context-engineering` subset (Rule-of-Two now met by prd-creator + DSB) — its own `/furnace-plan` pass, council-gated if it reopens the shape-vs-content fork (carried from the 2026-06-22 retro).
