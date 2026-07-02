# Harvest from the Theragen engagement → prd-to-product backlog

**What this is:** learnings from a working session that did real prep for a live design-research client engagement (Theragen ActaStim Sync 3.0), captured to be fed into a fresh prd-to-product Claude Code session and turned into BACKLOG rows / DECISIONS through the normal scope-gated workflow.

**How to use it (for the new session):** don't auto-commit. Read this, propose BACKLOG rows and any DECISIONS entries, and *recommend a council* on the one big fork flagged below before building it. Then commit under the usual gate. Where a change touches the `context-engineering` scaffold, remember the "port self-improvements back to the skill + output-small fixture" rule.

**Cold-reader context:** the session explored the standing idea of *running a design-research client engagement as a Claude Code project* (the "OS"). Rather than design the harness up front, we did real Theragen work — workshop prep, data review, client-comms drafts, a prototype — and let the gaps in today's context-engineering reveal themselves. That's the build-bespoke-then-harvest strategy already written up in the working folder (`Theragen OS/building-out-the-system-brief.md`, `design-research-system-brief.md`, `harness-skill-gaps-brief.md`). This doc is the first real harvest from it. These learnings belong in prd-to-product; the Theragen deliverables stay in Theragen (keep the two separate — mixing them was itself a small lesson).

---

## 1. The flagship capability is cross-source synthesis + contradiction detection (not filing) ⭐
**Learning:** the highest-value work all session was holding many sources at once — SOW, client charter, project plan, call transcript, two research decks, a data-science deck — and surfacing where they *disagree*: the SOW vs. charter conflict over who owns device-retention outcomes; the chosen design focus areas vs. what the data says actually drives retention; the auto-sync-removes-the-behavior-that-predicts-retention paradox. None of that is visible in any single source.

**Why it matters:** this is the spec for the "research-and-design mode" of context-engineering that's been circling in the briefs. The flagship routine of that mode isn't `/ingest` (storage) — it's a `/reconcile`-style pass that reads the whole corpus and reports contradictions, gaps, and what no single source says. (This is the same instinct as Rex's "personas/avenues" idea: read one corpus through a design lens vs. research-question lens vs. comms lens.)

**Proposed action:** treat "does context-engineering get a dedicated research-design mode, built around synthesis" as the central fork. **This is council-worthy** (costly + hard to reverse, per the CLAUDE.md council rule) — recommend a council before building. Backlog it as the anchor item the smaller ones hang off.

## 2. The artifact model is missing a lane: client comms / alignment
**Learning:** the starter's three modes were Research / Stimulus / Handoff. But most of this session produced a fourth category none of those cover — **stakeholder communication and alignment**: a workshop agenda, a decision-confirmation docket, a data-response email, a private side-ping, a client status "postcard." It has its own discipline: audience-tuned, sent-not-stored, voice-sensitive.

**Proposed action:** add a comms/alignment lane to the research-design mode's model and scaffold. Cheap add once mode #1 exists.

## 3. Visibility / sensitivity is a first-class dimension — genuinely new vs. code projects
**Learning:** near-miss — almost helped publish the client's proprietary retention numbers to a public-web Notion page. A client engagement has a sharing axis a code repo doesn't: every artifact is *private / client-visible / public*, and the patient de-identification rule already in the Theragen starter is one instance of it.

**Proposed action:** the research-design scaffold should emit a **visibility/sensitivity tagging convention** (private / client-shared / public) + a de-identification rule, and routines should respect it. This is the clearest "context-engineering assumes software, this isn't software" gap of the session. Warrants a DECISIONS entry since it changes what the generator emits. (This is exactly the kind of logged failure → guardrail the repo's doctrine wants.)

## 4. Verification discipline is domain-general — it caught a real bug, and was failed first
**Learning:** the HTML prototype shipped blank twice because "done" was claimed without running it; a Node-with-DOM-shim repro caught the crash (and a weak-data problem). The repo's "reproduce before fixing / verify before claiming done" rule proved it isn't code-specific — even a design deliverable needs a red-capable check ("does it actually render?").

**Proposed action:** bake a "verify the artifact actually works" step into design-OS routines that emit anything runnable/renderable. Reinforces the existing rule; low cost. (Also a self-note: the agent asserted done before verifying — the exact failure the rule prevents.)

## 5. Draft-first ("kill the blank page") is the actual engine
**Learning:** every useful output was a draft to react to or redirect — never a blank page. That design principle from the briefs is what moved the work.

**Proposed action:** confirm/strengthen "every routine drafts first" as a hard principle of the research-design mode (it's already in the briefs; the session validated it empirically).

## 6. Smaller port-backs
- **Client-roster-with-bios** as a real context file (richer than a flat `people.md`: role, owns-what, relationship, comms preference, bio, pronouns). Failure it prevents: mis-attribution / misgendering a stakeholder (happened this session). Candidate scaffold file for the mode.
- **Keep harvest separate from engagement content.** The "Theragen OS" folder blurred system-thinking with client content; that blur is a small lesson in itself — the mode's scaffold should make the seam explicit.

---

## Suggested backlog framing (adapt to prd-to-product's thin-index style)
- ⭐ **Research-design mode for context-engineering — synthesis-first.** Big fork; run a council before building. Anchor item; #2–#6 depend on it. Cross-ref the three `Theragen OS` briefs + the `harness-skill-gaps` ticket (which is queued behind the context-lifecycle ticket and part of this same thread).
- **Add comms/alignment as a 4th artifact lane** in the mode's model + scaffold. (child of the anchor)
- **Emit a visibility/sensitivity convention** (private/client/public) + de-id rule; DECISIONS entry. (child)
- **Verify-the-artifact step** for design-OS routines that emit runnable output. (cheap)
- **Client-roster-with-bios** context file for the mode. (cheap)

## Guardrails for the porting session
- Scope-gated workflow; state files-to-touch and scope before writing.
- The anchor item (#1) is the council fork — recommend it, don't auto-run, don't skip it.
- Anything that changes what the generator emits → DECISIONS.md (+ DECISIONS_ACTIVE mirror if binding) and update the `output-small` fixture per the port-back rule.
- Don't import Theragen-specific vocabulary into the generic scaffold (the don't-import-internal-vocabulary line).
