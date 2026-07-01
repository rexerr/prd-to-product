---
slug: pressure-test-behavior-prose
status: watching
title: Pressure-test behavior-shaping prose before shipping
---

# Pressure-test behavior-shaping prose

## Current state

The verification contract covers template *substitution* (dry-run diff) and hooks (live-fire), but nothing tests whether **behavior-shaping prose** (principles, session-discipline rules, scaffolded `.claude/rules/`) actually changes agent behavior — we ship those on inspection. Superpowers' `writing-skills` treats skill prose as code: baseline-test a subagent *without* the rule, document its failure/rationalizations verbatim, write the rule to counter them, re-test.

**Counter: 0/2.** Trigger fired 2026-06-11 (A/F/G discipline rules written), test deliberately skipped — an n=1-per-condition run can't attribute a behavior delta to the rule (the run-to-run-variation confound), and the load-bearing assumption (Task-tool subagents auto-load CLAUDE.md in this harness) is unverified.

## Next (preconditions before any slice)

Verify the auto-load assumption first; run **≥3 trials per condition**; only a consistent delta touches the counter. Record per-scenario **flips**, not aggregate deltas (arXiv 2603.25723 — harness effects concentrate on boundary instances; aggregate deltas at n=3 read as noise). Aim scenarios at boundary cases. A noisy 1/2 would be manufactured evidence — the ceremony-accretion the failure-tag instrument exists to catch.

## Method (for a future slice)

Pressure scenarios combine 3+ pressures (time, sunk cost, authority, social) and force a concrete A/B/C choice with no "I'd ask the user" exit. Meta-test the violator: "how could the rule have been written to make the right answer unambiguous?" (ignored-it → foundational principle; should-have-said-X → add X verbatim; didn't-see-Y → surface earlier). Bulletproof = complies under max pressure AND cites the rule AND acknowledges the temptation. **Adopt the method, not superpowers' persuasion-heavy tone.**

**Measured counterpart (CE-plugin mine, 2026-07-01)** — Every's plugin runs the same idea as a working eval discipline; fold these into any slice:

- **Paired blind old-vs-new injection** — run both prose versions blind against the same fixtures; outcomes classify as *improvement* / *no-regression* / **already-emergent-at-this-tier** (an honest third bucket our plan lacked: the rule may be a no-op because the model already does it).
- **Fixtures must be discriminating** — a scenario both versions pass proves nothing; design the case where old fails and new succeeds, or conclude "no demonstrated improvement."
- **Variance is the headline metric, not the pass rate** — their 60-trial eval found the real defect was one fixture giving 3 different answers in 4 trials; two confidently-wrong N=1 reads are documented in the same doc. Confirms this ticket's ≥3-trials precondition with field data.
- **Grade from the transcript, never the model's self-report.**

**Harness design (TanStack/intent remainder mine, 2026-07-01)** — `evals/intent-discovery/` is a shipping instance of this exact experiment (does ambient guidance prose change agent behavior?). The methodology is now design-complete; what remains is instantiating a runner on scripted Claude Code sessions. Lift these structures ([mined doc IR-1](../docs/mined/2026-07-01-tanstack-intent-remainder.md) has citations):

- **Condition lattice + diagnostic ceiling arm** — no-prose / current-prose / candidate-prose conditions scored; an explicit-instruction arm runs as a ceiling check but is *excluded from the headline score*. Prompt explicitness is a separate controlled dimension, not mixed into the conditions.
- **Materialize the prose from the product** — the harness injects the actual SKILL.md/rules file under test (imported/copied at run time), never a paraphrase, so measured prose can't drift from shipped prose.
- **Calibrate the grader first** — hand-written known-outcome transcripts (including expected *failures*) regression-test the grading before any live run is trusted; a grader that can't reproduce known verdicts invalidates the run, not the rule.
- **Two failure channels** — harness-integrity failures fail the experiment; behavioral failures are diagnostic data. Never let a broken harness read as a behavioral result.
- **pass@k AND pass^k over ≥3 runs** — pass^k (every run complies) is the reliable-not-lucky metric; report per-condition rates + a failure-class histogram.
- **Judge quarantine** — any LLM judge annotates subjective residue only, with a mandated "unknown"; it never touches deterministic scores.
- **Anti-contamination guards** — a *mention* of the behavior must not grade as the behavior (their parser requires command-position forms); the rule text itself must not be parseable as compliance evidence.
- **Failure taxonomy** — their corpus names 13 classes; the host-relevant ones beyond pass/fail: `reference-only` (talked about the rule, didn't apply it), `late-load` (applied after the harmful act), `instruction-ignored`, `context-saturation`.

## Why (pointers)

[superpowers handoff brief](../docs/superpowers-context-engineering-handoff.md); github.com/obra/superpowers `writing-skills`; [CE-plugin mine](../docs/mined/2026-07-01-compound-engineering-plugin.md) P-3 (`safe-auto-rubric-calibration.md`, `paired-old-vs-new-injection-skill-evals.md`, `fake-cli-harness-for-skill-judgment-evals.md` in the clone). Promotion = Rule of Two (two real prose defects caught). Complements the 2026-06-08 council's "structural assertions, not byte-diffs" on the behavioral side.
