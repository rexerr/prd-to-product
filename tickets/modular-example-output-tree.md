---
slug: modular-example-output-tree
status: backlog
title: Modular-shape example output tree for regression
---

# Modular-shape example output tree

## Current state

The verification contract diffs dry-run output against [`examples/output-small/`](../skills/context-engineering/examples/output-small/) — but that's the **only** example and it's **flat** shape. There is no **modular** example (rules in `.claude/rules/*.md`, AGENTS.md canonical, CLAUDE.md = `@AGENTS.md`). Consequence, seen live in group 5: changes to the modular path can't be diff-verified, only inspected.

## Next

Build a committed `examples/output-modular/` from a representative modular input (e.g. tokens-plus-linter design, or ≥1 AI surface). **Council caveat ([council-report-2026-06-08](../docs/council/council-report-2026-06-08.html)):** do NOT build it as a golden-tree **byte-diff** — generation is LLM-driven and non-deterministic, so a byte-diff fires false positives on legitimate run-to-run variation and trains the operator to ignore it. Build it as **structural/invariant assertions**: required files exist, required sections present, cross-references resolve, OPTIONAL gates evaluated correctly.

## Open

Cost: the baseline must be trustworthy (a wrong baseline is worse than none), and every future template change then updates *two* trees. Promote when modular-affecting changes become routine — flat is the common case, modular rarer, and one good baseline beats two half-maintained ones.
