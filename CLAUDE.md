# CLAUDE.md — prd-to-product

This file is read automatically at the start of every Claude Code session. Follow these rules for every task in this project.

`AGENTS.md` is a thin pointer that tells Codex to read this file plus Codex-specific additions. `CLAUDE.md` is the single source of truth. If you change a rule here, no mirroring is needed.

See `README.md` for product overview and stack.

---

## What this project is

Skill-development workspace for the `context-engineering` skill (and sibling skills like `prd-creator`, `design-system-bootstrap`, `brand-voice`). The "product" here is a set of installable Claude Code / Codex skills that scaffold AI-assisted coding projects. No deployed application; output is consumed by Claude Code via symlinks in `~/.claude/skills/`. Single developer.

---

## Primary constraints (read before doing anything)

The full set is at the bottom of this file in "Before you respond." Read this block first if attention is short.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.
2. **Direct on `main`. No branches.**

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

### Checkpoint between phases of multi-step work

For any task with more than one distinct phase, pause between phases and restate: what was done, what was verified, what remains. Do not continue from a state you cannot describe. Prevents phase 4 of a 6-step refactor going wrong while phases 5 and 6 pile on top of broken state.

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
- **`/compact` proactively, with a description, during long debug sessions before autocompact fires.** A user-triggered `/compact "what we're investigating and what we've ruled out"` produces a much better summary than the automatic one, which often fires when the model is at peak context-rot.

### Session retros

Write a retro at the end of every non-trivial session: `docs/retros/YYYY-MM-DD-topic.md`. At the start of a new session, read the most recent retro before doing anything else.

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

## Where to look

Read at start of every session: this file, `AGENTS.md`, `docs/DECISIONS_ACTIVE.md`, the most recent file in `docs/retros/`.

Then read the doc that governs what you're about to touch. Source of truth on conflict is the right-hand column:

| Touching | Doc → conflict source of truth |
|---|---|
| Product behavior, copy | `docs/PRD.md` |
| Architecture, data model | `docs/ARCHITECTURE.md` |
| Status, current phase | `ROADMAP.md` |
| Recent binding decisions | `docs/DECISIONS_ACTIVE.md` |

If a conflict isn't covered above, surface it as an open question. Don't pick silently.

---

## Before you respond — load-bearing constraints

These are the rules that must not be lost mid-session. Read this block last so it stays in attention. Items here meet the bar: violating them damages product, loses work, or burns a stakeholder. Other rules (direct-on-main, reproduce-before-fixing) live in the body of this file; do not duplicate them here.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines.

If any constraint above conflicts with a request, surface the conflict before acting.
