---
slug: harness-batch-liftables
status: watching
title: Harness-batch liftables (2026-06-12)
---

# Harness-batch liftables

Trigger-gated candidates from the 2026-06-12 external-source batch (9 sources: 7 URLs + 2 Reddit posts) that fit no existing entry. Fold into incidental edits, no dedicated session. Source: [2026-06-12-harness-batch-review](../docs/retros/2026-06-12-harness-batch-review.md).

## Candidates

- **(a) Stale-assumption tagging** (Anthropic effective-harnesses) — rules additionally name the model-capability assumption they encode, making them retire-able when models improve (their sprint decomposition went obsolete on a model upgrade). A one-line extension to "every rule cites its failure mode." Trigger: next major model change in the harness, or first never-firing rule observed in retros.
- **(b) `docs/references/*-llms.txt` slot** (OpenAI harness-engineering) — scaffold a place to vendor load-bearing dependency docs into a project, plus an intake question for which dependencies qualify. Trigger: first observed dependency-API hallucination in a scaffolded project.
- **(c) Doc-gardening** (OpenAI) — a scaffolded `/doc-audit` command sweeping for stale docs + dead cross-references. Trigger: retro failure-tags show lost-context / stale-cross-reference recurring (the kill-watch instrument gates this — counter, not instinct).
- **(d) Feature ledger + never-weaken-tests rule** (Anthropic harness-design-long-running-apps) — a markdown (per the invariant, not JSON) per-item ledger with verification steps + explicit pass state, for projects expecting unattended runs; and a "never remove or weaken tests" rule (named failure: agent silently deletes failing checks to declare victory — a goal-drift instance). Triggers: a premature-completion retro tag / first observed test-editing instance.

## Honesty note

From celesteanders/harness: its advertised "append-only" task-list enforcement was prompt-only and its claimed lint hook is absent from the artifact — if (d) ever ships, enforcement claims must match mechanism.
