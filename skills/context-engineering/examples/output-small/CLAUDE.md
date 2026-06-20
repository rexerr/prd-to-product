# CLAUDE.md — simple-form

This file is read automatically at the start of every Claude Code session. Follow these rules for every task in this project.

`AGENTS.md` is a thin pointer that tells Codex to read this file plus Codex-specific additions. `CLAUDE.md` is the single source of truth.

## What this project is

A single-page contact form for a freelance designer's portfolio site. See `docs/PRD.md`.

---

## Primary constraints

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.
2. **Visual confirmation gates the commit.** Do not commit UI changes until Jordan confirms in a running dev server.
3. **Direct on `main`. No branches. No worktrees. No Vercel CLI.**

---

## Commands

The actual commands a session needs. Use these; do not invent alternatives.

- Install: `npm install`
- Dev server: `npm run dev`
- Type / lint check: `npm run check`
- Test: not configured (this project has no test suite)
- Build: `npm run build`
- Env vars: `.env.local locally; Vercel project env vars in production. Never commit .env.local.`

---

## Architecture rules (non-negotiable)

1. **Validate before sending.** The API route validates name, email format, and message length before calling Resend. Never forward an unvalidated payload.
2. **No client-side Resend.** The Resend SDK only runs in `app/api/contact/route.js`. Never import it from a client component.
3. **Honeypot field stays.** The hidden `website` field is the spam filter. Never remove it without a replacement.

---

## Session discipline

- **Hard limits:** bug fix ≤ 3 files / ≤ 50 lines, feature ≤ 300 lines, file ≤ 500 lines. If a task would exceed, stop and state full scope before writing code.
- **Read before you write.** Read the file's exports, immediate callers, and obvious shared utilities before adding code. "Looks orthogonal to me" is the most dangerous phrase in this codebase.
- **Scope check before coding.** State files, intended changes, scope estimate. If > 2 files or scope uncertain, wait for confirmation.
- **Autonomy — run to done, then report.** The scope check is the outer gate: within the scope limits, run the whole loop (edit → `npm run check` → retro if warranted → commit → push) and report — don't stop to ask "want me to commit?"; over the limits, stop and confirm first. Always gated on Jordan, never self-cleared: UI/visual changes, product/architecture/scope decisions, anything irreversible or outward-facing.
- **Checkpoint between phases of multi-step work.** Pause between phases and restate what was done / verified / left. Don't continue from a state you can't describe.
- **Recommend a structured review at genuine forks.** When a decision is costly to get wrong AND hard to reverse (architecture/stack choice, core-invariant change, build-vs-don't), recommend a multi-perspective review (LLM-council-style, if available) before committing — don't ship a first instinct. Not for routine/reversible work. Prevents a plausible-but-wrong instinct surviving solo review.
- **Verification before claiming done.** UI: run `npm run dev`, tell Jordan what to look for and on which page, wait for visual confirmation. Logic: run `npm run check`, report results. Wired-up behavior (hook, command, script): fire it once and observe — a file looking right is not the behavior firing.
- **Reproduce before fixing.** Failing reproduction first, then fix, then verify. A repro that passes without asserting the symptom (a unit test of logic, a simulator happy-path) is theater — what counts as red-capable depends on the project type:

  | Project type | A red-capable repro is… |
  |---|---|
  | Web | a failing component render or visual diff — not a green unit test of the handler underneath |
  | Mobile | exercised against real OS / network / permission state, not a simulator happy-path |
  | Backend | an HTTP-layer integration or contract test, or a deploy-window metric query — not a logic unit test |
  | CLI | a shell invocation asserting the exact exit code + stdout/stderr |
  | Data | re-derive the number a second way and watch the cross-check reconcile |
- **Session management** (Source: Thariq Shihipar, *Lessons from Building Claude Code: Session Management & 1M Context*, Anthropic 2025):
  - Prefer `/rewind` to re-prompting when an approach fails — reverts conversation and working tree instead of accumulating dead-end context.
  - Start a new session for a new task. The orientation cost is one retro read.
  - `/compact` proactively, with a description, during long debug sessions before autocompact fires at peak context-rot.
- **Commit gate (UI changes).** Do not commit until Jordan visually confirms.
- **Session retros.** Write a retro at the end of every non-trivial session: `docs/retros/YYYY-MM-DD-topic.md`. Read the most recent retro at session start.

---

## Code rules

- Never hardcode secrets. Credentials live in `.env.local locally; Vercel project env vars in production. Never commit .env.local.`. Never commit local env files.
- Never use the Vercel CLI. Pushes to `main` deploy automatically.
- Always work directly on `main` in `/Users/jordan/Sites/simple-form`. Do not create branches.
- Do not use `git worktree` while the visual-confirmation commit gate is in effect. The dev server points at the main checkout; a worktree has its own working copy, so changes "made" in the worktree are not what `npm run dev` is rendering. Do not invoke worktree-creating tools (`EnterWorktree`, `Agent` with `isolation: "worktree"`) for this project.
- After every push, paste the commit URL (`https://github.com/jordan-d/simple-form/commit/<sha>`) and state "waiting for Vercel deploy." Do not declare done until Jordan confirms production.

Decisions log in `docs/DECISIONS.md`.

---

## Where facts live — memory vs. repo

The operative cut is **survives a tool switch vs. doesn't.** Claude's auto-memory is machine-local and Claude-only — Codex and Cursor can't read it.

- **Repo** (`CLAUDE.md`, `docs/`): anything load-bearing, *and* any cross-tool working preference — it must bind every agent, not just Claude on this machine. The repo is the source of truth.
- **Auto-memory:** Claude-local scratch only — agent-discovered notes (build quirks, debugging insights) that are fine to lose on a tool switch. Claude writes these itself.
- When a rule belongs in the repo, put it here and **delete any duplicate memory.** If a memory ever contradicts this file on a work rule, this file wins; reconcile and delete the memory.

---

## Before you respond — load-bearing constraints

Read this block last so it stays in attention. Items here meet the bar: violating them damages product, loses work, or burns a stakeholder. Other rules (direct-on-main, no Vercel CLI, reproduce-before-fixing) live in the body above; do not duplicate them here.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines.
2. **Visual confirmation gates the commit.** Do not commit UI changes until Jordan confirms in a running dev server.

If any constraint above conflicts with a request, surface the conflict before acting.
