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

## Why (pointers)

[superpowers handoff brief](../docs/superpowers-context-engineering-handoff.md); github.com/obra/superpowers `writing-skills`. Promotion = Rule of Two (two real prose defects caught). Complements the 2026-06-08 council's "structural assertions, not byte-diffs" on the behavioral side.
