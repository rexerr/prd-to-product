# CLAUDE.md — prd-to-product

Read automatically at the start of every Claude Code session; follow these rules for every task. `AGENTS.md` is a thin pointer to this file — CLAUDE.md is the single source of truth, no mirroring needed. Product overview and stack: `README.md`.

---

## What this project is

Skill-development workspace for the `context-engineering` skill (and siblings `prd-creator`, `design-system-bootstrap`). The "product" is installable Claude Code / Codex skills consumed via symlinks in `~/.claude/skills/`. No deployed application. Single developer. The repo also hosts two **non-chain** skills: `furnace-plan` (an explicit-invoke plan-authoring discipline, symlinked like the chain skills) and `context-engineering-audit` (a design record, deliberately **not** symlinked per [D-019](docs/DECISIONS.md)).

---

## Primary constraints (read before doing anything)

The full set is at the bottom in "Before you respond." Read this block first if attention is short.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.

---

## Commands

None — no package manifest, server, linter, or test runner. Regression is the hand-written `skills/context-engineering/examples/` output trees plus live-firing emitted hooks. No `.env*` in any form should be committed.

---

## Architecture rules (non-negotiable)

1. **Skills are markdown-only.** No HTML output paths without a decision recorded in `docs/DECISIONS.md` (see [D-001](docs/DECISIONS.md); brief: [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md)).
2. **Every rule cites its failure mode.** In `skills/context-engineering/principles.md`, scaffolded `.claude/rules/`, and SKILL.md files. "Be thoughtful" is not a rule.
3. **The generator scaffolds shape, not content.** `context-engineering` writes context files, never product code (`app/`, `lib/`, `components/`, design tokens, etc.). See `skills/context-engineering/generator/decisions.md` "What the generator never writes."

---

## Session discipline

Prevents scope creep, hallucinated success, and lost context between sessions.

### Hard limits

- **Bug fix or small tweak:** ≤ 3 files, ≤ 50 lines. **Feature work:** ≤ 300 lines per session. **File size:** ≤ 500 lines before extraction.
- If a task would exceed these, stop before writing code, state full scope, wait for confirmation.

### Read before you write

Read a file's exports, callers, and shared utilities before adding to it; skim a working sibling if it's part of a pattern. If you don't understand why existing code is structured as it is, ask. "Looks orthogonal to me" is the most dangerous phrase in this codebase.

### Scope check before coding

State files to touch, the change and why, and estimated scope (small / medium / large). More than 2 files or uncertain scope → wait for confirmation.

### Autonomy — run to done, then report

The scope check is the outer gate; inside it, run the whole loop (edit → verify → retro if warranted → commit → push when asked) without stopping to ask permission. Always gated on Rex, never self-cleared: product / architecture / scope decisions; anything irreversible or outward-facing (public release, deleting work, force-push); self-modification of agent config (`.claude/` commands, settings, CLAUDE.md startup behavior). Rationale: [`docs/agent-process-brief.md`](docs/agent-process-brief.md).

### Non–Claude-Code agents: no product writes (one measurement-data carve-out)

Outside agent surfaces (Cowork, claude.ai, Codex, etc.) may not author or edit **product** — skills, code, docs, decisions — which must go through the Claude-Code scope-gated workflow; they propose and wait for per-task permission instead. **Exception:** a designated, append-only **measurement artifact** an outside agent owns may be written by that agent — currently only the furnace trial ledger (Cowork's `/plan-review` writes it; see [D-018](docs/DECISIONS.md)). The test: *product, or the agent's own measurement output?* Product is banned; own-measurement-data is permitted. **Failure it prevents:** out-of-band edits from tools whose discipline rules differ, and silent divergence from the scope-gated workflow — without forcing a reviewer's own findings out of the repo where they inform improvement. **Committing the carve-out's writes:** the outside agent appends to the working tree but cannot commit, so a Claude-Code session that finds an unstaged change to **`skills/furnace-plan/trial-ledger.md`** it did not make should sweep it into a dedicated commit (e.g. "Sweep Cowork ledger append"). Scope this strictly to that one file — never generalize it to "commit any working-tree change you didn't make."

### Checkpoint between phases of multi-step work

Between phases, restate: done / verified / remaining. Do not continue from a state you cannot describe. **Failure it prevents:** phase 4 going wrong while 5 and 6 pile on top.

### Recommend a council at genuine forks

When a decision is **both costly to get wrong and hard to reverse** — changing the markdown-only invariant, a stack/architecture choice, a build-vs-don't `D-NNN` call, adjudicating whether a Claude Design bundle re-introduces cut scope — recommend an LLM Council (or equivalent multi-perspective stress-test) before committing; never auto-run it. Do **not** recommend it for reversible work (prose edits, single-file fixes) — over-applying turns judgment into ritual. **Failure it prevents:** a plausible-but-wrong first instinct surviving solo review on an expensive-to-unwind fork. Threshold and rationale: [D-009](docs/DECISIONS.md).

### Verification before claiming done

Never claim success because "the code looks correct."

- Skill template / rule / decision changes: dry-run substitution, diff against `skills/context-engineering/examples/output-small/`. Hook changes: copy emitted scripts to `/tmp/<test>/` and live-fire each blocked operation in a fresh session ([contract](docs/retros/2026-05-10-phase-1-validation.md)).
- Doc / retro / roadmap changes: re-read after editing; confirm cross-references resolve.

### Reproduce before fixing

Failing reproduction first, then the fix, then the same reproduction passing.

### Session management

- **Prefer `/rewind` to re-prompting** — re-prompting leaves the failed attempt in the prefix; `/rewind` reverts both conversation and working tree.
- **New session for a new task** — carried-over context burns tokens and imports stale assumptions.
- **`/compact` proactively with a description during long debug sessions** — autocompact fires at peak context-rot; `/clear` + a fresh brief when you want full control of what carries forward. **Failure it prevents:** losing edge-case context to a bad autocompact.
- **Delegate to a subagent when you need the conclusion, not the artifact** — keeps verbose intermediates out of the prefix, and a fresh subagent verifying work is not the model grading its own output.

### Session retros

End every non-trivial session with `docs/retros/YYYY-MM-DD-topic.md`; read the most recent retro at session start. Each retro tags the dominant failure (bad substitution / scope creep / lost context / goal drift / none — template: `docs/retros/README.md`). **Failure it prevents:** accreting guardrails against failures that never occur — the tag log answers "adopt this?" with evidence.

---

## Code rules

- Never hardcode secrets; no `.env*` committed.
- Work directly on `main` in `/Users/rexc/Sites/prd-to-product`; no branches.
- Push only when the task explicitly says to; after every push, paste the commit URL (`https://github.com/rexerr/prd-to-product/commit/<sha>`).
- Never preemptively pass `-c` config overrides to `git` without asking.
- Do not silently change SKILL.md trigger phrases or the markdown-only invariant. Document material changes in `docs/DECISIONS.md`; mirror binding ones into `docs/DECISIONS_ACTIVE.md`.

---

## Decisions log

Log significant decisions in `docs/DECISIONS.md` per its own instructions. If a decision imposes a binding constraint not visible in code, mirror a one-liner into `docs/DECISIONS_ACTIVE.md`.

---

## Where facts live — memory vs. repo

The cut: **survives a tool switch vs. doesn't.** Repo (`CLAUDE.md`, `AGENTS.md`, `docs/`) holds anything load-bearing or cross-tool — it binds every agent (Codex and Cursor can't read Claude's machine-local auto-memory). Auto-memory is Claude-local scratch only. When a rule moves into the repo, delete any duplicate memory; if a memory contradicts this file, this file wins — reconcile and delete the memory.

---

## Where to look

Read at session start: this file, `BACKLOG.md`, `docs/DECISIONS_ACTIVE.md`, the most recent file in `docs/retros/`. Then the doc governing what you're touching — right-hand column is source of truth on conflict:

| Touching | Doc |
|---|---|
| Product behavior, copy | `docs/PRD.md` |
| Architecture, data model | `docs/ARCHITECTURE.md` |
| Open work, in progress, next | `BACKLOG.md` |
| Recent binding decisions | `docs/DECISIONS_ACTIVE.md` |

If a conflict isn't covered above, surface it as an open question. Don't pick silently.

---

## Before you respond — load-bearing constraints

Read this block last so it stays in attention. Items here meet the bar: violating them damages product, loses work, or burns a stakeholder. Other rules live in the body; do not duplicate them here.

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines.

If any constraint above conflicts with a request, surface the conflict before acting.
