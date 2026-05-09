# CLAUDE.md — simple-form

This file is read automatically at the start of every Claude Code session. Follow these rules for every task in this project.

`AGENTS.md` is a thin pointer that tells Codex to read this file plus Codex-specific additions. `CLAUDE.md` is the single source of truth. If you change a rule here, no mirroring is needed.

See `README.md` for product overview and stack.

---

## What this project is

A single-page contact form for a freelance designer's portfolio site. Visitors fill a name, email, and message; the form posts to an API route that emails the designer via Resend. No database, no auth, no logged-in state.

---

## Architecture rules (non-negotiable)

1. **Validate before sending.** The API route validates name, email format, and message length before calling Resend. Never forward an unvalidated payload.
2. **No client-side Resend.** The Resend SDK only runs in `app/api/contact/route.js`. Never import it from a client component.
3. **Honeypot field stays.** The hidden `website` field is the spam filter. Never remove it without a replacement.

---

## Session discipline

These rules prevent scope creep, hallucinated success, and lost context between sessions.

### Hard limits

- **Bug fix or small tweak:** ≤ 3 files, ≤ 50 lines.
- **Feature work:** ≤ 300 lines per session.
- **File size:** ≤ 500 lines before extraction.
- If a task would exceed these limits, stop before writing code. State the full scope and wait for confirmation.

### Scope check before coding

Before writing code, state which files you will touch, what you will change and why, and estimated scope (small / medium / large). If the plan touches more than 2 files or scope is uncertain, wait for confirmation before beginning.

### Verification before claiming done

Never claim success based on "the code looks correct."

- UI changes: run `npm run dev`, describe what to look for and on which page, wait for Jordan's visual confirmation.
- Logic or data changes: run `npm run check`, report results.

### Reproduce before fixing

For any bug, write the failing reproduction first, then the fix, then verify the same reproduction now passes.

### Commit gate — mandatory for UI changes

**Do not commit until Jordan visually confirms the change looks correct.** Workflow: apply changes → `npm run dev` → confirm no build errors → tell Jordan what to look for and on which page → wait for confirmation → commit and push.

### Session retros

Write a retro at the end of every non-trivial session: `docs/retros/YYYY-MM-DD-topic.md`. At the start of a new session, read the most recent retro before doing anything else.

---

## Code rules

- Never hardcode secrets. Credentials live in `.env.local` (local) and Vercel env vars (production). Never commit `.env.local`.
- Never use the Vercel CLI. Pushes to `main` deploy automatically.
- Always work directly on `main` in `/Users/jordan/Sites/simple-form`. Never create branches or use `git worktree`. Worktrees create isolated copies the dev server can't see, breaking visual verification. Do not invoke worktree-creating tools (`EnterWorktree`, `Agent` with `isolation: "worktree"`).
- Do not push to GitHub unless the task explicitly says to commit and push. After every push, paste the commit URL (`https://github.com/jordan-d/simple-form/commit/<sha>`) and state "waiting for Vercel deploy." Do not declare the session task complete until Jordan confirms the deploy reached production.
- Never preemptively pass `-c` config overrides to `git` without asking first.

---

## Decisions log

Log significant decisions in `docs/DECISIONS.md` per its own instructions.

---

## Where to look

Read at start of every session: this file, `AGENTS.md`, the most recent file in `docs/retros/`.

Then read the doc that governs what you're about to touch. Source of truth on conflict is the right-hand column:

| Touching | Doc → conflict source of truth |
|---|---|
| Product behavior, copy | `docs/PRD.md` |
| Architecture, data model | `docs/ARCHITECTURE.md` |
| Status, current phase | `ROADMAP.md` |

If a conflict isn't covered above, surface it as an open question. Don't pick silently.

---

## Before you respond — load-bearing constraints

These are the rules that must not be lost mid-session. Read this block last so it stays in attention.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines.
2. **Visual confirmation gates the commit.** Do not commit UI changes until Jordan confirms in a running dev server.
3. **Direct on `main`. No branches. No worktrees.**
4. **No Vercel CLI.**
5. **Reproduce before fixing.**

If any constraint above conflicts with a request, surface the conflict before acting.
