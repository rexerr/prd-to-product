---
slug: session-start-rewrite
status: backlog
title: Broader Appendix-A /session-start rewrite
---

# Broader /session-start rewrite

Easy, low value — do only if session-start bloat bites.

## Current state

Group 5 (shipped 2026-06-08) fixed one redundant read (AGENTS.md in flat shape). [agent-process-brief.md](../docs/agent-process-brief.md) §1.1 / Appendix A proposed the fuller redesign we only partially did: restructure the command from "read 3–4 files every time" into tiers — don't re-read *anything* that auto-loads; **always** read just the latest retro (carries the handoff); read ROADMAP + `DECISIONS_ACTIVE` **only when resuming feature work**, skip for a trivial one-off.

## Why deferred, not done

Group 5 already captured the high-value slice; the rest is marginal token savings traded against asking the agent to judge "am I resuming feature work," which can misfire. Pure markdown template rewrite, target wording already exists in Appendix A; ~3 files + a gated self-edit to this repo's own copy; ≈half a session. Promote only if `/session-start` weight becomes a real problem.

## Baseline-check candidate (2026-06-12 harness batch)

The scaffolded `/session-start` should run the project's `check`/`test_cmd` before any work and reject a broken starting state — compounding bugs across sessions is the named failure (both Anthropic long-running-agent posts; celesteanders/harness implements it as a session-protocol step). Gated on the project actually having such a command (this repo has none). Fold into the next incidental edit of the template or this rewrite, whichever comes first.
