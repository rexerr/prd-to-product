---
slug: client-work-os
status: backlog
title: Research-design engagement OS — a mode/sibling of context-engineering
---

# Research-design engagement OS

## Current state

Run **design-research client engagements** (calls, sessions, synthesis, prototypes, dev handoff, client comms) as Claude Code projects, so context compounds across sessions instead of restarting from memory. Originally a secondhand backlog row from the Every mine; **now evidence-backed** by a real engagement — **Theragen ActaStim Sync 3.0**, a five-month design+validation retainer, live (Align phase starts ~2026-07-01) — run through today's `context-engineering` tooling. **Build-bespoke-then-harvest:** you can't abstract a reusable harness from zero runs, so run a real engagement, capture where the harness fits and misfits, and let that evidence define the reusable pattern. The engagement is the forcing function; the system is the byproduct.

**Sources (durable, in-repo):**
- Harvest (first-party evidence) → [`research-design-os-theragen-harvest.md`](../docs/product-briefs/research-design-os-theragen-harvest.md)
- PRD-ready brief → [`research-design-os-prd-brief.md`](../docs/product-briefs/research-design-os-prd-brief.md)
- Orienting brief + build sequence → [`research-design-os-build-sequence-brief.md`](../docs/product-briefs/research-design-os-build-sequence-brief.md)
- System brief (routines + the ADHD design spine) → [`research-design-os-system-brief.md`](../docs/product-briefs/research-design-os-system-brief.md)
- Skill-gaps self-instrumenting mechanism → [`research-design-os-skill-gaps-brief.md`](../docs/product-briefs/research-design-os-skill-gaps-brief.md)

## Two tracks (the load-bearing distinction)

The council fork is **downstream** of the incremental path, not upstream of everything. Collapsing the two is the framing error to avoid.

### Track B — incremental, reversible, no-council, **already live**
Runs now on Theragen; generates the evidence Track A will later weigh. None of this waits on the council.
- **Scaffold Theragen with `context-engineering` for the disciplined shell** (CLAUDE.md, doc structure, context-thrift), hand-fill the content, and log every place the code-built harness misfits a research project. That gap list *is* the spec for the harness.
- **Engagement routines** (project-local `.claude/skills/`, manual-invoke): `/ingest-call`, `/ingest-session`, `/synthesize`, `/prototype-brief`; later `/standup`, `/postcard` when the friction is felt.
- **Personal routines** (user-level, travel to every project, manual-invoke): `/capture`, `/next`, `/smallest-step`, `/focus`, `/welcome-back`. **Build `/capture` + `/next` first** — they attack the real bottleneck (starting) and prove the habit fastest. *(These are not prd-to-product product — they're Rex's personal user-level skills; noted here for the whole-system picture.)*
- **Skill-gaps self-instrumenting mechanism** — see its own board row; **now unblocked** (its hard dependency, the context-lifecycle ticket, landed 2026-06-20).

### Track A — the costly, hard-to-reverse fork (**council-gated**)
- **Does `context-engineering` get a dedicated research-design MODE, or is it a standalone product?** This is the mode-vs-standalone fork. Recommend an LLM council before any implementation ([D-009](../docs/DECISIONS.md#d-009) threshold); do not auto-run, do not skip. It is decided *from Theragen evidence*, after the harvest — Phase 3, not now.

## What the engagement proved (the evidence upgrade)

- **Flagship = cross-source synthesis + contradiction detection, not filing.** ⭐ Holding a whole corpus at once (SOW, charter, project plan, call transcript, two research decks, a data-science deck) and surfacing where they *disagree* / what *no single source says* — the SOW-vs-charter conflict over device-retention ownership; the auto-sync-removes-the-behavior-that-predicts-retention paradox. The flagship is a `/synthesize`/`/reconcile` pass over the corpus, **not** `/ingest` (storage).
- **The artifact model needs a 4th lane.** Starter had **Research** (rigor; cite the source, evidence≠interpretation, one-shot, durable) / **Stimulus** (speed; disposable test props) / **Handoff** (precision; versioned paid deliverable). Theragen produced a category none cover: **Comms / Alignment** — workshop agendas, decision dockets, client emails, status "postcards." Audience-tuned, sent-not-stored, voice-sensitive. Collapsing the lanes is the main design error.
- **Visibility / sensitivity is a first-class dimension — genuinely new vs. code projects.** Near-miss: almost published a client's proprietary retention numbers to a public web page. Every artifact sits on a *private / client-shared / public* axis, plus a de-identification rule (patient data stays de-identified and out of the tool until stripped — medical client, real people).
- **Draft-first ("kill the blank page") is the actual engine.** Every useful output was a draft to react to; never a blank page. Validated empirically.
- **Verify-the-artifact is domain-general.** The HTML prototype shipped blank twice because "done" was claimed without running it; a red-capable check ("does it actually render?") caught it. Bake a verify step into any routine that emits runnable/renderable output.
- **Client-roster-with-bios** context file (role, owns-what, relationship, comms preference, bio, pronouns) — richer than a flat `people.md`. Prevents mis-attribution / misgendering a stakeholder (happened this session).
- **Keep harvest separate from engagement content** — the "Theragen OS" folder blurred system-thinking with client content; the mode's scaffold should make that seam explicit.

## The design spine (why it's built this way)

Tuned for an ADHD-pattern of working where the hard part is the cost of *starting*, not the task. These shape every routine and are the reason a board-of-twelve-cards is the wrong default surface: **kill the blank page** (draft-first) · **one next action, not a board** · **push, not pull** (briefings come to you) · **make time visible** (elapsed/remaining) · **re-entry over guilt** ("welcome back, here's the one thing," never a scold). Ship thin; add a routine only after feeling the friction it removes.

## Rejected spine alternatives (kept for the "why not")
The Twin (voice/taste corpus — fun-trap, premature) · The Pipeline (state machine — overkill for early object counts) · The Standing Coworker (autonomous overnight — biggest fun-trap, nothing to run on) · The Front Desk (its one live piece, per-stakeholder registers, folds into Comms) · The Film Crew (a lens, not a structure). Detail: [PRD brief](../docs/product-briefs/research-design-os-prd-brief.md) §"Rejected alternatives."

## Gates

- **Council gate (Track A, open).** Mode-vs-standalone is costly + hard-to-reverse; council before implementation, decided from Theragen evidence (Phase 3). Do not auto-run, do not skip.
- **Context-lifecycle gate — CLEARED.** In-repo lifecycle work landed 2026-06-20 ([D-048](../docs/DECISIONS.md#d-048); [dogfood-built retro](../docs/retros/2026-06-20-context-lifecycle-dogfood-built.md)). This unblocks the skill-gaps mechanism, which is its child. *(The harvest's "harness-skill-gaps queued behind the context-lifecycle ticket" sequencing was written in the Theragen workspace; in this repo the parent has landed.)*
- **Governance.** Cowork advises; Claude Code implements under Rex's scope gate; self-modification of agent config is gated on Rex regardless. Reversible prose changes need no council; the costly forks (the context-engineering port / a heavier harvest loop) are where a council is recommended.
- **Port-back / vocabulary.** Anything that changes what the generator emits (the visibility/sensitivity convention especially) → `DECISIONS.md` (+ `DECISIONS_ACTIVE.md` mirror if binding) and update the `output-small` fixture. Don't import Theragen-specific vocabulary into the generic scaffold ([D-013](../docs/DECISIONS.md#d-013)/[D-019](../docs/DECISIONS.md#d-019)).

## Children (hang off this anchor)

1. **friday-postcard** — recurring client-status artifact in the Comms lane (own board row, iced).
2. **Skill-gaps self-instrumenting mechanism** — generator change (own board row, **now unblocked**).
3. Add **Comms/Alignment** as the 4th artifact lane in the mode's model + scaffold (Track A; DECISIONS entry at build time).
4. Emit a **visibility/sensitivity convention** (private/client-shared/public) + de-id rule (Track A; DECISIONS entry at build time).
5. **Verify-the-artifact** step for routines that emit runnable output (cheap; reinforces existing rule).
6. **Client-roster-with-bios** context file for the mode (cheap).

## Next

Track B is live and needs no gate — the near-term actionable is the **skill-gaps mechanism** (own row, unblocked). Track A waits for the **LLM council** on mode-vs-standalone, run from Theragen evidence at harvest time. `/prd-creator` can take the [PRD brief](../docs/product-briefs/research-design-os-prd-brief.md) directly when Rex chooses to advance the mode question.

## Why (pointers)

The five source briefs (above); council threshold [D-009](../docs/DECISIONS.md#d-009); lifecycle gate [D-048](../docs/DECISIONS.md#d-048); don't-import-vocabulary [D-013](../docs/DECISIONS.md#d-013)/[D-019](../docs/DECISIONS.md#d-019); prior gated-direction-without-D-NNN precedent: [project-setup retro](../docs/retros/2026-07-01-project-setup-investigation-council-spec.md).
