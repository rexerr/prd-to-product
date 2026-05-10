# Product requirements: prd-to-product

## Product summary

`prd-to-product` is a development workspace for a small set of installable Claude Code / Codex skills that scaffold AI-assisted coding projects:

- `context-engineering` — scaffolds `AGENTS.md`, `CLAUDE.md`, `.claude/rules/`, `.claude/settings.json`, `.claude/hooks/`, and the `docs/` shape (PRD, ARCHITECTURE, DECISIONS, ROADMAP, retros).
- `prd-creator` — interview-driven PRD generation.
- `design-system-bootstrap` — token-first design-system scaffolding.

The "product" is the markdown content of these skills. They are consumed locally by Claude Code via symlinks in `~/.claude/skills/` and by Codex via `~/.codex/skills/` (when applicable). There is no deployed runtime application.

## Target users

- Single developer (the author) — primary.
- Other Claude Code / Codex users who install the skills from this repo.

## Core problem

A new AI-assisted coding project starts in a state where the agent re-derives "what is this project, what conventions apply, what is canonical when docs disagree" every session. The fix is a small set of files at known paths, plus harness-level hooks that turn load-bearing rules into actual blocks. This repo develops the skills that scaffold those files.

## Main workflow

The skill-refinement cycle (see `ROADMAP.md` for current phase and prior retros for context):

1. **Validate** — dry-run the generator against synthetic project shapes; live-fire emitted hooks in throwaway sessions.
2. **Refine** — apply changes to templates, decisions logic, principles. Each change traces to a named failure mode.
3. **Dog-food** — run the skill on this repo (and the author's other projects). Capture mismatches.
4. **Audit** — categorize the skill ecosystem against the 9-category framework. Fix description fields that don't trigger reliably.
5. **Regenerate examples** — bring the abbreviated medium/large example outputs current.

After Phase 4, enter continuous mode: edit only on real failures or upstream Claude Code feature changes.

## Out of scope

- Multi-developer workflows (branch policies, PR review templates).
- Build-system-specific rules (Turbo, Nx, monorepo layouts).
- Generating product code (the generator scaffolds shape; it never writes `app/`, `lib/`, `components/`, design tokens).
- Hosting or distributing skills as a package — installation is via local symlinks.

## Deferred capabilities

Tracked in [`docs/FUTURE.md`](FUTURE.md) once Phase 3 surfaces real category gaps.

## Cross-references

- Architecture: [`docs/ARCHITECTURE.md`](ARCHITECTURE.md).
- Roadmap: [`ROADMAP.md`](../ROADMAP.md).
- Decisions log: [`docs/DECISIONS.md`](DECISIONS.md).
- Active decisions: [`docs/DECISIONS_ACTIVE.md`](DECISIONS_ACTIVE.md).
- HTML-over-Markdown investigation: [`docs/html-over-markdown-brief.md`](html-over-markdown-brief.md).
