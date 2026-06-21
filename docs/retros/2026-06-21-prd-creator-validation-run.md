# Retro — 2026-06-21 14:24 CDT — prd-creator validation run (CF-29 PRD-FORMAT, partial)   (4th session of the day)

Ran prd-creator as a live validation of the CF-29 / [D-052](../DECISIONS.md) `PRD-FORMAT.md` consolidation — the prd-creator pilot is the "live evidence for whether the consolidation earns propagation" the [CF-29 retro](2026-06-21-cf29-prd-format-pilot.md) named. No product changed; this is a measurement session.

## What the run validated

- **Format loads as designed.** `PRD-FORMAT.md` loaded cleanly as the *reference* authority and `templates/PRD.md.template` as the *boot* artifact — the CF-29 split is structurally intact at load time, no broken pointer observed.
- **Interview path works.** Drafted-and-presented each cluster from the supplied brief instead of asking cold; pushed on the real forks (V1-user narrowing, `/next` ranking logic); correctly parked two "I'm not sure" answers as open questions with a thin default rather than forcing decisions.
- **Self-skip check fires correctly.** When Rex narrowed the request to a single `/capture` skill, the skill bailed out of the heavyweight clustered interview — the intended behavior for a trivial single-feature ask.

## What it did NOT validate — the gap that matters

- **The PRD *write* against `PRD-FORMAT.md` was never exercised.** Every approach to it pivoted (brief swap → narrowing → self-skip), so the 12-section skeleton render, the move-out-of-`principles.md` pointers resolving in a written doc, and the closed 11/12/14 section-count drift remain **unconfirmed in output**. That write step is exactly the part CF-29 changed.
- **Consequence for [D-052](../DECISIONS.md):** the "pilot proving out" gate on propagating the FORMAT pattern to DSB / context-engineering is **not yet met end-to-end**. Loading + interview + self-skip pass; the write artifact does not exist. Do not treat CF-29 as output-validated. The gate closes on Rex's next real prd-creator run, which he chose as the honest test (clean session, empty project, no carried context).

## Failure this session

- **Tag: goal drift (near-miss — caught by Rex, no product touched).**
- **Name it.** Mid-run I slid from *running the validation* to *proposing to build the `/capture` skill* — staged location, inbox shape, "tell me where it lives and I'll build it." Rex caught it: "you make it sound like we are building this right now." The session's goal was to exercise the skill flow, not ship a tool; I drifted from measurement into execution.
- **Tool or agent?** Agent judgment. The self-skip check did its job (correctly refused the heavyweight PRD); the drift was me filling the freed space with a build proposal instead of holding the validation frame.
- **Does it generalize?** Plausibly — a validation/measurement session is a soft frame with no artifact gate, so it's easy to wander into "let's just build it" when the input gets concrete. n=1 here; logging as a watch, not a rule.
- **The check that would have held:** state the session's success condition at the top ("produce a written PRD to inspect the format render") and test each next move against it. A concrete buildable sub-task is not the goal unless it serves that condition.

## Files changed

- This retro only. No product, no docs beyond this record. The two candidate briefs (`ai-research-synthesizer`, the Desktop design-research-engagements brief) were inputs, not edited.

## Open / next

- **prd-creator write-path validation is still open**, deferred to Rex's next real project (clean session). That run is the live evidence that closes the [D-052](../DECISIONS.md) propagation gate — until it lands, CF-29 → DSB propagation stays ungated.
- No BACKLOG line added: this is a measurement result on an existing deferred item, recorded here, not new work.

## Update — 2026-06-21 (write path validated; style gap found + fixed → D-053)

Rex ran prd-creator clean in a fresh session on a new project (`~/Sites/cat-tracker`, a stray-cat tracking app, "Strays") and brought the output back for review. This **closes the write-path gap** the run above left open.

**Structural pass (the part CF-29 changed) — clean.** All 12 core sections in canonical order; optional-section logic correct (Brand-and-voice omitted in favor of a sibling `BRAND.md`, Supporting-documents included and linking it); `D-001..D-009` decision seed list well-formed with one-line rationales; no 11/12/14 section-count regression; H1 name-only, sentence-case headers, no colons in titles. Content quality genuinely strong — the interview caught a real hole (cutting both voting and login removed the only abuse defense) and flagged it as the top pilot risk. **So the principles.md → PRD-FORMAT.md move did not break the structural render.**

**House-style fail — and it was pre-registered.** The emitted `PRD.md` had **33 em dashes** (+6 in `BRAND.md`) and Oxford-comma violations, against a canonical `examples/small/PRD.md` with zero — so this is drift, not a misread rule. Verified mechanism by reading the firing path: the house-style rules live only in reference-not-boot `PRD-FORMAT.md`, never loaded at generation; the loaded template carried content cues but no style cue, so the rules never entered context. [D-052](../DECISIONS.md)'s own "Revisit if" predicted exactly this ("a PRD house-style regression is observed → hoist the Camp-B rules into the loaded template, fork (a)").

**Fix shipped ([D-053](../DECISIONS.md)).** Hoisted the Camp-B house-style rules into the loaded `templates/PRD.md.template` as an operative `KEEP-AS-IS` cue at the top. The general lesson — **any rule that must fire at generation needs a thin operative echo in the loaded artifact, not just a home in the reference FORMAT file** — now binds the pending CF-29 propagation to DSB + context-engineering (carried in D-053 + D-052's revisit). The behavioral confirmation (a clean re-generation with zero em dashes) is left to the next real prd-creator run, since it can't be verified without re-running the generator.

**Net for [D-052](../DECISIONS.md):** the *structural* propagation gate is met; the propagation now also inherits a required design constraint (operative-echo for write-time rules). Files changed this update: `templates/PRD.md.template` (prd-creator), `docs/DECISIONS.md` (D-053), `docs/DECISIONS_ACTIVE.md` (marker), this retro.
