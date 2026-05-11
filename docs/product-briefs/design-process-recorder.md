# Working brief: Design Process Black Box Recorder

A passive-capture system that records the design process — prompts, references, iterations, reversals, decisions — and reconstructs the work afterward as a case-study-ready narrative.

This is the most ambitious idea in the bundle. It's parked here intentionally; the brief exists so the concept doesn't decay, not because it's actionable next.

## What it is

You design something — in Figma, in code, in your sketchbook, in conversation with Claude or ChatGPT or Midjourney. The system captures the trail: AI prompts you sent, references you pulled, design files at intervals, the moments you reversed direction. Later — when the work is done or a case study is due — the system reconstructs a timeline and drafts a chaptered narrative: *brief, exploration, reversal, decision, polish, ship*. You edit it. You export it. Suddenly your case study is real, not retrofitted.

## Who it's for

Designers (independent and in-house) whose *process* is part of the value being sold, not just the deliverable. Design leaders who want their team's work to be teachable. Agencies who pitch on craft and need to prove how they think. Anyone who has stared at a finished project and tried to remember why they made the calls they made.

## The core problem

When work ships, the artifact is visible but the journey isn't. Clients pay for the journey ("why did we end up here") and the designer's instinct ("what did you reject and why"). Reconstructing a case study after the fact takes hours and the memory is fuzzy within a week. Most case studies on designer portfolios are partial fiction — not from dishonesty but from forgetting. There's no mechanism that captures the truth as it happens.

## Rough shape of the experience

- Capture layer running in the background — somewhere between an MCP tool, a browser extension, a desktop app, or all three.
- Captures: AI prompts (Claude, ChatGPT, Midjourney), screenshots at intervals, Figma file states, conversational snippets from the user.
- Timeline view: scroll through the project chronologically. See the prompts you ran. See the references you pulled. See the moment you changed direction.
- AI synthesis: "draft a case study from this project" → Claude reads the timeline and produces a chaptered narrative.
- Editor: designer cleans up, redacts sensitive client content, restructures, exports.
- Output: markdown case study, slide deck, portfolio page, or video walkthrough script.

## What this is NOT

- Not full screen-recording video — too heavy, privacy-invasive, hard to synthesize.
- Not audio transcription — V1 at least. Calls and voice memos are a V2 capture surface.
- Not multi-designer team capture. Solo designer first.
- Not auto-publishing. Designer is always in the edit-and-approve loop.
- Not real-time client dashboards. Output is artifact, not surveillance.

## Open questions

This is where the brief gets honest about how big the project is.

- **Capture surface.** Browser extension? Desktop daemon? Figma plugin? Claude Code MCP? Each has different scope, privacy properties, and engineering cost. Probably some combination, but which first?
- **Privacy.** Sensitive client work, NDAs, redaction-before-publishing. The designer has to trust the capture is local-first or has a hard delete. This is the trust gate — without it, the product is dead.
- **AI tool coverage.** Claude, ChatGPT, Midjourney, Figma — which to integrate with first? Each integration is a real engineering lift.
- **Storage architecture.** Local-first? Cloud? Hybrid? Has direct cost and trust implications.
- **Synthesis quality.** "Draft a case study" is easy to do badly (boring, generic, AI-uniformed). It has to feel like the designer wrote it. Probably needs heavy stylistic priming from the user's existing case studies.
- **The smallest useful version.** What's the V0 that's actually worth shipping? Possibly: "snapshot my Figma + my Claude / ChatGPT prompts every 30 minutes, give me a browsable timeline, skip the synthesis entirely." Let the designer reconstruct the narrative themselves but from a real timeline. Synthesis is V2.
- **Business model.** Tool the designer runs (one-time / subscription) vs service that does the synthesis (per-case-study fee).

## Why park it

It's the most distinctly *you*-shaped idea in the bundle — directly mirrors the retro / continuous-mode / process-as-product discipline already in this repo. But it's also the hardest: passive capture + storage + timeline + synthesis is a four-system product, not a three-session validation. Promote when there's appetite for a multi-month build.

## Source

This conversation, 2026-05-11. Ranked #20 (hardest to prototype) by the other Claude. Worth keeping warm. Possibly the eventual destination of the prd-to-product ecosystem itself, applied to design work.
