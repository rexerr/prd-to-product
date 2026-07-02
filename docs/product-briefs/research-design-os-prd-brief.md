# PRD brief — Research-Design Engagement OS (for prd-creator)

**How to use:** drop this file into the target project dir (recommend **prd-to-product** if this becomes a mode of `context-engineering`; a fresh dir if standalone), start a session there, run `/prd-creator` and point it at this file. It's a *brief*, not a spec — the interview should still draw out target user, exact workflow, stack, and success metrics. Open questions for the interview are flagged **[interview]**.

---

## One-line pitch
A way to scaffold and run **design-research client engagements** (calls, user sessions, synthesis, prototypes, dev handoff, client comms) as Claude Code projects — built around **cross-source synthesis and contradiction-detection**, not filing. Likely a new *mode* of `context-engineering`; possibly a standalone product. **[interview: mode vs. standalone]**

## The problem
`context-engineering` today assumes a *software* project — it emits architecture rules, line limits, code-shaped slots. A design-research engagement has different shapes and disciplines, so running one ad hoc means insight gets lost and every session restarts from memory. There's no disciplined shell for the non-code consulting work a designer actually does.

## The core insight (earned, not assumed)
This brief exists because a real engagement (Theragen, below) was run through today's tooling and the gaps revealed themselves. The single highest-value capability wasn't storage — it was holding *many* sources at once (SOW, client charter, project plan, call transcript, research decks, a data-science deck) and surfacing where they **contradict** each other and what **no single source says**. That synthesis/reconcile pass is the flagship, and it's the thing to design the product around.

## What it does — the artifact model
Four lanes, each with its own discipline (collapsing them is the main design error):
- **Research** (rigor) — calls, sessions, synthesis; cite the source, separate evidence from interpretation; capture is one-shot. Durable.
- **Stimulus** (speed) — storyboards / throwaway prototypes as test props. Disposable.
- **Handoff** (precision) — the dev-ready spec. Versioned. The paid deliverable.
- **Comms / Alignment** (NEW — discovered in the Theragen run) — workshop agendas, decision dockets, client emails, status "postcards." Audience-tuned, sent-not-stored, voice-sensitive. Today's three-mode model misses this entirely.

## Requirements surfaced by the real run
- **Synthesis / `reconcile` routine** as the flagship — read the corpus, report contradictions + gaps + what's missing. (Overlaps with, and may extend, the existing `/mine` skill — worth deciding.)
- **Visibility / sensitivity is first-class** — every artifact is *private / client-shared / public*, plus a de-identification rule for sensitive data. This is genuinely new vs. code projects (near-miss this session: almost published a client's proprietary data to a public web page).
- **Draft-first everywhere** — every routine drafts something to react to; never a blank page. (Validated empirically this session — it's what moved the work.)
- **Verify-the-artifact** — even design/runnable deliverables need a red-capable check ("does it actually render?"), not just "looks right."
- **Client-roster-with-bios** context file (role, owns-what, relationship, comms preference, pronouns) — richer than a flat people list. Prevents mis-attribution / misgendering a stakeholder.

## Scope
- **In:** the disciplined shell (CLAUDE.md, doc structure, context-thrift conventions) + named routines for the four lanes, for a *single designer/consultant* running client engagements. **[interview: only Rex, or other consultants too?]**
- **Out (for now):** a heavy self-improvement engine, autonomous/scheduled agents, eval tooling, a productized SaaS. Thin conventions now; proven mechanisms later.

## Rejected alternatives (from the brainstorm — kept so the PRD carries the "why not")
Converged on a **Chief-of-Staff spine** (ingest → tracked decisions/owners/blocked → surface the one next action), which in practice became the **synthesis engine** above. Rejected, and why:
- **The Twin** (voice/taste corpus, AI drafts everything) — fun-trap; premature before there's a body of work.
- **The Pipeline** (state machine over every artifact) — overkill for the object counts real engagements start with.
- **The Standing Coworker** (autonomous overnight runs) — the biggest fun-trap; nothing to run on autonomously yet.
- **The Front Desk** (client-facing-trust system) — half-real; its one live piece (per-stakeholder registers) folds into Comms.
- **The Film Crew** (production metaphor) — a nice lens, not a structure.

## Evidence it's real
The **Theragen ActaStim Sync 3.0** engagement (five-month design+validation retainer) was the bespoke instance. Running its prep through today's skills is what surfaced every gap above. Build-bespoke-then-harvest: this PRD *is* the harvest.

## Open questions for the interview
- **[interview]** Mode of `context-engineering` vs. standalone product?
- **[interview]** Target user — only Rex, or packaged for other design consultants?
- **[interview]** Success criteria — what makes this "worth it"? (e.g., a second engagement scaffolds in <1 hr; zero lost insights across sessions; N reconcile-catches per engagement.)
- **[interview]** Happy-path workflow — the first session of a new engagement, start to finish.
- **[interview]** Build sequence + what ships first (`reconcile`? the four-lane scaffold? the visibility model?).

## Governance note
"Does context-engineering get a dedicated research-design mode" is a **costly, hard-to-reverse fork** — recommend an **LLM council** before committing to build, per the prd-to-product council rule.
