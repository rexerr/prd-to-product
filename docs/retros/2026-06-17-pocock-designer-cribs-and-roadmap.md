# Retro — 2026-06-17 20:23 CDT — Pocock + designer crib mining, 6-lens re-mine, adoption roadmap   (3rd session of the day)

## What was completed

- **Mined three external repos as candidate cribs** via `Workflow` fan-out (conclusions, not artifacts): `mattpocock/skills` (33 skills, MIT), `mattpocock/agent-rules-books` (Maciej Ciemborowicz, MIT), `Owl-Listener/designer-skills` (MC Dean, MIT). Two new source-organized trackers: [`cribs-from-pocock-craft.md`](../cribs-from-pocock-craft.md) (`CF-01`–`CF-29`) and [`cribs-from-designer-skills.md`](../cribs-from-designer-skills.md) (`DG-01`–`DG-02`). First pass: adversarial-verify on every integrate/implement pick → 6 craft + 2 design keepers, 0 implement-straight survived.
- **Corrected a wrong-comparand decline (`CF-06`).** Rex flagged Pocock's `handoff` skill; re-read showed the workflow had dismissed it as "weaker than C-16" — a category error (C-16 = decision-escalation; handoff = session-continuity). Promoted the de-dup-by-reference rule to `CF-06`.
- **6-lens primitive re-mine of all 34 Pocock skills** (one agent per skill; `wf_4e227677-89e`, 35 agents, ~1.8M tokens) after Rex observed the first pass lacked rigor. Raw 23 keepers → **consolidated to 16** (fragments merged: source-immutability 4→`CF-07`, interview 3→`CF-18`, disclosure 2→`CF-25`; `CF-28` folded into `CF-01`). Added a **Parked** bucket (10 investigates + 9 future-useful atoms) as the CF-04 declined-ledger applied to ourselves.
- **Built the unifying layer:** [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md) — one cross-source strategy (6-step lifecycle, T/H/D verification playbook, Waves 1–3 + Big Rocks), pointer-based (no merge). Wired one standing `BACKLOG.md` row naming the current wave; bidirectional pointers added to the steinberger + designer trackers; ratified as **D-022**.

## Failure this session

- **Dominant tag: none landed** — no bad substitution shipped, no unauthorized scope creep (each expansion was Rex-directed), no lost context, no goal drift. But two honest process observations:
  1. **A workflow synthesis subagent wrote product directly**, bypassing the return-markdown-then-I-write gate I'd designed into the run (it wrote `CF-07`–`CF-29` straight into the doc, and placed the section after Provenance). It worked out, but the control gate didn't hold — when a workflow is meant to *return* a draft for review, the agent prompt must forbid Write, not just describe the return value.
  2. **Rubric permissiveness is a real dial, observed live.** The first pass's single-lens whole-skill triage under-evaluated (false-negatives — handoff). The 6-lens primitive pass over-corrected (false-positives — 23 fragmented from ~16 real ideas). The standing rule banked into D-022: run the deep pass *surgically* (on-domain skills only), not as a blanket.

## What verification covered — and what it didn't

- **Covered (D-class):** ran a `grep`/`awk` check confirming the consolidated keeper table has exactly **16 rows**, the merged ids (`CF-08/09/10/17/19/24/28`) are **absent**, and all four crib-doc link targets **exist on disk**. Commit verified: 6 files, `49f98b2..1778fc2` pushed.
- **Did NOT cover:** I did not re-read the fully-assembled `cribs-from-pocock-craft.md` end-to-end after all 11 surgical edits — table structure was grep-verified, prose flow was not. I verified the four crib docs exist but did **not** click-test every inline cross-ref inside the roadmap (e.g. the `examples/output-small/` and `retros/2026-05-10-phase-1-validation.md` paths cited in the verification playbook). Low risk (those paths are load-bearing elsewhere and known-good), but it's an honest gap, not a clean re-read.

## Files changed

- `docs/cribs-from-pocock-craft.md` — new, then Round-2 consolidation (23→16, merges, parked bucket, Provenance reorder).
- `docs/cribs-from-designer-skills.md` — new.
- `docs/cribs-adoption-roadmap.md` — new (the unifying strategy).
- `docs/cribs-from-steinberger-ecosystem.md` — back-pointer to the roadmap.
- `BACKLOG.md` — one standing crib-adoption row (current wave: Wave 1).
- `docs/DECISIONS.md` — **D-022** (not mirrored to ACTIVE; visible-by-reading skip precedent).

## Key decisions made

- **D-022** — crib adoption runs through one pointer-roadmap; the three trackers stay source-organized inventories (no merge — C-19); BACKLOG points, never lists (C-12); status lives in the source tracker, not the roadmap.
- **Standing rule (in D-022):** future deep re-mines are surgical (skill-authoring/governance skills only). agent-rules-books + designer-skills do **not** warrant a 6-lens re-run (designer was thin; the rule-books method is already `CF-05`).

## Open items / gated on Rex

- **Wave 1 is ready** — `CF-03`, `CF-02`, `CF-06`, `CF-04` + the steinberger cheap batch (`C-14`/`C-15`/`C-09`/`C-10`), each a sub-50-line edit. **Starting in a new session** (Rex's call).
- **Big rocks** (each own plan, gated): AGENTS.md-canonical flip (decided, not executed); build the `solutions/` scar-tissue library (unblocks `CF-05`).
- At-most-once consideration: a full end-to-end re-read of the consolidated pocock-craft tracker before adopting from it, since this session only grep-verified its structure.

## Next session

- Pick the top open Wave 1 crib from [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md), adopt via its lifecycle (edit → verify per class → flip status in the source tracker → log `D-NNN`). Recommended first: `CF-03` (red-capable-repro gate into CLAUDE.md) — smallest, closes a live failure, single surface.
