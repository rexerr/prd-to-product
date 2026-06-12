# CLAUDE.md — prd-to-product

This file is read automatically at the start of every Claude Code session. Follow these rules for every task in this project.

`AGENTS.md` is a thin pointer that tells Codex to read this file plus Codex-specific additions. `CLAUDE.md` is the single source of truth. If you change a rule here, no mirroring is needed.

See `README.md` for product overview and stack.

---

## What this project is

Skill-development workspace for the `context-engineering` skill (and sibling skills `prd-creator`, `design-system-bootstrap`). The "product" here is a set of installable Claude Code / Codex skills that scaffold AI-assisted coding projects. No deployed application; output is consumed by Claude Code via symlinks in `~/.claude/skills/`. Single developer.

---

## Primary constraints (read before doing anything)

The full set is at the bottom of this file in "Before you respond." Read this block first if attention is short.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.

---

## Commands

The actual commands a session needs. Use these; do not invent alternatives.

- Install: (none — no package manifest, this is a docs/skills repo)
- Dev server: (none — no server)
- Type / lint check: (none — manual review and dry-run validation per skill conventions)
- Test: (none — regression is the hand-written `skills/context-engineering/examples/` output trees plus live-fire of emitted hooks)
- Build: (none)
- Env vars: no env files in this repo. `.env*` in any form should not be committed.

---

## Architecture rules (non-negotiable)

1. **Skills are markdown-only.** Per [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md), the skills in this repo stay markdown unless the brief's investigation concludes otherwise. Do not introduce HTML output paths in `context-engineering` without that decision being recorded in `docs/DECISIONS.md`.
2. **Every rule cites its failure mode.** Rules in `skills/context-engineering/principles.md`, in scaffolded `.claude/rules/`, and in skill SKILL.md files must name the specific failure they prevent. "Be thoughtful" is not a rule.
3. **The generator scaffolds shape, not content.** The `context-engineering` skill writes context files (rules, docs, slash commands, settings, hooks). It never writes product code (`app/`, `lib/`, `components/`, design tokens, etc.). See `skills/context-engineering/generator/decisions.md` "What the generator never writes."

---

## Session discipline

These rules prevent scope creep, hallucinated success, and lost context between sessions.

### Hard limits

- **Bug fix or small tweak:** ≤ 3 files, ≤ 50 lines.
- **Feature work:** ≤ 300 lines per session.
- **File size:** ≤ 500 lines before extraction.
- If a task would exceed these limits, stop before writing code. State the full scope and wait for confirmation.

### Read before you write

Before adding code in a file, read the file's exports, the immediate caller(s), and any obvious shared utilities. If the file is part of a pattern (route handlers, hooks, model adapters), skim a sibling that already works. If you do not understand why existing code is structured the way it is, ask before adding to it. "Looks orthogonal to me" is the most dangerous phrase in this codebase.

### Scope check before coding

Before writing code, state which files you will touch, what you will change and why, and estimated scope (small / medium / large). If the plan touches more than 2 files or scope is uncertain, wait for confirmation before beginning.

### Autonomy — run to done, then report

Default to finishing the work, not asking permission to finish it — but **the scope check above is the outer gate.** Within the scope limits, run the whole loop (edit → dry-run substitution/diff per "Verification before claiming done" → retro if warranted → commit → push when the task asked for it) and report — don't stop to ask "want me to commit?" on work that was always in scope. If a task would exceed the limits, stop and confirm first. "Run to done" governs only what is inside the scope gate. Always gated on Rex, never self-cleared: product / architecture / scope decisions; anything irreversible or outward-facing (public release, deleting work, force-push); and per the existing rules, self-modification of agent config (`.claude/` commands, settings, CLAUDE.md startup behavior).

### Non–Claude-Code agents are read-only here

Distinct from the self-modification gate above (which governs Claude Code editing its own agent config): any other agent surface (Cowork, claude.ai, etc.) does not write to this repo without explicit per-task permission from Rex — propose the change and wait. **Failure it prevents:** out-of-band edits from a tool whose context and discipline rules differ from a Claude Code session; silent divergence from the direct-on-main, scope-gated workflow.

### Checkpoint between phases of multi-step work

For any task with more than one distinct phase, pause between phases and restate: what was done, what was verified, what remains. Do not continue from a state you cannot describe. Prevents phase 4 of a 6-step refactor going wrong while phases 5 and 6 pile on top of broken state.

### Recommend a council at genuine forks

When a decision is **both costly to get wrong and hard to reverse** — changing the markdown-only invariant, a stack/architecture choice, a build-vs-don't call (a `D-NNN` decision), or adjudicating whether a Claude Design bundle re-introduces deliberately-cut scope — recommend running an LLM Council (or equivalent multi-perspective stress-test) *before* committing, rather than shipping a first instinct. Recommend it; do not auto-run it. **Failure it prevents:** a plausible-but-wrong first instinct surviving solo review on a fork that's expensive to unwind — twice on 2026-06-09 a council killed exactly such an instinct that had passed my own review. **Do not** recommend it for routine or reversible work (prose edits, single-file fixes, choosing between equivalent phrasings) — over-applying it turns judgment into ritual, atrophies the adjudication muscle, and leans on a non-deterministic external plugin the repo can't assume is installed. Decided in [`docs/DECISIONS.md`](docs/DECISIONS.md) D-009; council that set the threshold: [`docs/council/council-report-2026-06-09-reconcile.html`](docs/council/council-report-2026-06-09-reconcile.html).

### Verification before claiming done

Never claim success based on "the code looks correct."

- Skill template / rule / decision changes: do a dry-run substitution against an example input set and diff against `skills/context-engineering/examples/output-small/`. For hook changes, copy emitted scripts into `/tmp/<test>/` and live-fire each blocked operation in a fresh Claude Code session (see [`docs/retros/2026-05-10-phase-1-validation.md`](docs/retros/2026-05-10-phase-1-validation.md) for the contract).
- Doc / retro / roadmap changes: re-read the file after editing and confirm the cross-references still resolve.

### Reproduce before fixing

For any bug, write the failing reproduction first, then the fix, then verify the same reproduction now passes.

### Session management

Built-in commands that keep the conversation prefix clean. Source: Thariq Shihipar, *Lessons from Building Claude Code: Session Management & 1M Context*, Anthropic 2025.

- **Prefer `/rewind` to re-prompting when an approach fails.** Re-prompting "that didn't work, try X" leaves the failed attempt in the prefix; `/rewind` reverts both conversation and working tree to a clean state.
- **Start a new session for a new task.** Carrying over an unrelated task's context burns tokens and risks the new task inheriting stale assumptions. The orientation cost is a single retro read.
- **`/compact` proactively, with a description, during long debug sessions before autocompact fires.** A user-triggered `/compact "what we're investigating and what we've ruled out"` produces a much better summary than the automatic one, which often fires when the model is at peak context-rot — its least intelligent moment. The cut: `/compact` is lossy and the model picks what survives (steer it with the hint); `/clear` plus a fresh session means you write the brief and control exactly what carries forward. **Failure it prevents:** losing edge-case context to a bad autocompact — a concrete instance of goal drift.
- **Delegate to a subagent when you need the conclusion, not the artifact.** Broad searches, doc sweeps, and verification runs produce verbose intermediates; a subagent returns the conclusion and the noise stays out of the main context. Verification especially: a fresh subagent checking the work is not the model grading its own output. **Failure it prevents:** intermediate tool output bloating the conversation prefix; self-preferential review.

### Session retros

Write a retro at the end of every non-trivial session: `docs/retros/YYYY-MM-DD-topic.md`. At the start of a new session, read the most recent retro before doing anything else.

Each retro tags the session's dominant failure — bad substitution / scope creep / lost context / goal drift / none (see the template in `docs/retros/README.md`). **Failure it prevents:** accreting tooling and ceremony against failures that never actually occur — the tag turns "should I adopt this guardrail?" into a question the log answers with evidence instead of instinct.

---

## Code rules

- Never hardcode secrets. No env files belong in this repo; `.env*` in any form should not be committed.
- Always work directly on `main` in `/Users/rexc/Sites/prd-to-product`. Do not create branches.
- Do not push to GitHub unless the task explicitly says to commit and push. After every push, paste the commit URL (`https://github.com/rexerr/prd-to-product/commit/<sha>`).
- Never preemptively pass `-c` config overrides to `git` without asking first.
- Do not silently change SKILL.md trigger phrases or the markdown-only invariant for the `context-engineering` skill. Document material changes in `docs/DECISIONS.md` and mirror binding ones into `docs/DECISIONS_ACTIVE.md`.

---

## Decisions log

Log significant decisions in `docs/DECISIONS.md` per its own instructions. If the decision imposes a binding constraint not visible in code, also mirror a one-liner into `docs/DECISIONS_ACTIVE.md`.

---

## Where facts live — memory vs. repo

The operative cut is **survives a tool switch vs. doesn't.** Claude's auto-memory is machine-local and Claude-only — Codex and Cursor can't read it.

- **Repo** (`CLAUDE.md`, `AGENTS.md`, `docs/`): anything load-bearing, *and* any cross-tool working preference — it must bind every agent, not just Claude on this machine. The repo is the source of truth.
- **Auto-memory:** Claude-local scratch only — agent-discovered notes (build quirks, debugging insights) that are fine to lose on a tool switch. Claude writes these itself.
- When a rule belongs in the repo, put it here and **delete any duplicate memory.** If a memory ever contradicts this file on a work rule, this file wins; reconcile and delete the memory.

---

## Where to look

Read at start of every session: this file, `AGENTS.md`, `BACKLOG.md`, `docs/DECISIONS_ACTIVE.md`, the most recent file in `docs/retros/`.

Then read the doc that governs what you're about to touch. Source of truth on conflict is the right-hand column:

| Touching | Doc → conflict source of truth |
|---|---|
| Product behavior, copy | `docs/PRD.md` |
| Architecture, data model | `docs/ARCHITECTURE.md` |
| Open work, in progress, next | `BACKLOG.md` |
| Recent binding decisions | `docs/DECISIONS_ACTIVE.md` |

If a conflict isn't covered above, surface it as an open question. Don't pick silently.

---

## Before you respond — load-bearing constraints

These are the rules that must not be lost mid-session. Read this block last so it stays in attention. Items here meet the bar: violating them damages product, loses work, or burns a stakeholder. Other rules (direct-on-main, reproduce-before-fixing) live in the body of this file; do not duplicate them here.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines.

If any constraint above conflicts with a request, surface the conflict before acting.
