---
slug: mine
status: next
seq: 2
title: /mine — codify the source-agnostic mining process
---

# /mine

Mines **any source** — a repo (URL or local path), a dumped-docs pile, a design export, a research dump — for value and saves the findings into our system. Codifies the refined mining `Workflow`: stage source → inventory (+ license for repos) → triage fan-out → adversarial-verify every integrate/implement pick → synthesize into a source-organized tracker (**lens A** → cribs/roadmap) or the project's own surfaces (**lens B** → its BACKLOG/context). The name is deliberately broader than the old `/repo-miner` — the engine is source-agnostic.

## Current state

- **Rule-of-Two met** (Steinberger ×3 rounds + Pocock/designer ×2 passes, 2026-06-17). Past the codify threshold.
- **A-vs-B fork RESOLVED** (devils-advocate 2026-06-18): A (crib lens — "what should I steal into my tooling?") and B (project lens — "what does this project need?") are two *lenses* on one shared **engine** (stage → fan-out read → triage → adversarial-verify → tracker + amend one plan), not competing skills. Only the triage lens and output home differ.

## Next

Settle the **form fork first** (see Open), then build the engine: stage → fan-out read → triage → adversarial-verify → tracker + amend one plan. Wire **lens A** (proven, 3 real mines) now. **Defer lens B** until the next real dumped-content pile exists, then run the engine into that project — zero new structure built. **Authoring goes through `/furnace-plan`** — a real authoring task; the plan is presented for approval before any edit.

## Open

- **Form fork (settle in the furnace-plan):** a lightweight playbook the roadmap points to **vs.** an explicit-invoke `/mine` skill (like `furnace-plan`). The ticket originally leaned playbook to avoid invocation surface — but [D-034](../docs/DECISIONS.md#d-034) says an explicit-invoke skill (`disable-model-invocation: true`) costs **nothing** in-window, which removes the playbook's main rationale and makes a runnable `/mine` skill the stronger candidate. Lean: the skill, unless the plan surfaces a reason not to.
- B likely resolves into a `context-engineering` *extension* + a convention (broader source-type intake + an "append actionable items to BACKLOG" step), not a new skill — probably avoiding the `CF-22`/`CF-23` router cost entirely.
- Design inputs to honor **only IF the hand-run proves them needed** (do not pre-build): a per-mine staging folder `mines/<date>-<source>/`; heterogeneous source readers (repos = shallow-clone-to-scratch, never commit raw; dumped docs/designs = staged/pointed-to); a mine index/log; amend the *one* plan, pointer-not-copy (`C-19`).

## Engine gotchas (the encoded scar tissue — the real value, not the mechanics)

Surgical-not-blanket depth ([D-022](../docs/DECISIONS.md#d-022) — full 6-lens pass only on skill-authoring/governance skills, single-lens whole-skill triage for the off-domain mass); adversarial-verify every integrate/implement pick; dedup against existing `C`/`CF`/`DG` cribs (cite overlap, don't re-mint); **synthesis agents must RETURN drafts, never Write product** (the gate that failed 2026-06-17 — a synth agent wrote 23 cribs straight into the doc); don't-merge-trackers (D-022); consolidate skeptically (watch rubric inflation/fragmentation); tracker FORMAT (failure-it-prevents · surface · tier · status · parked); scratch cleanup.

## Why (pointers)

[2026-06-17-pocock-designer-cribs-and-roadmap](../docs/retros/2026-06-17-pocock-designer-cribs-and-roadmap.md); [cribs-adoption-roadmap](../docs/cribs-adoption-roadmap.md).
