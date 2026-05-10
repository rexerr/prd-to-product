# Architecture

Stack: Skill-development workspace (markdown only, no runtime).

## Skill layout

Each skill lives under `skills/<skill-name>/` and follows a common shape:

- `SKILL.md` — frontmatter (name + description used for trigger matching) plus when-to-trigger and when-not-to-trigger guidance.
- `principles.md` (when applicable) — structural conventions and rationale. Reference, not boot.
- `templates/` — annotated template files the generator fills in.
- `generator/` — `intake.md` (question flow), `decisions.md` (mapping logic), `output-summary.md` (post-generation report).
- `examples/` — worked examples, often as full output trees plus abbreviated transcripts.
- `NOTES.md` (when applicable) — internal notes including regression-test definition.

The four skills currently in the repo:

- [`skills/context-engineering/`](../skills/context-engineering/) — full shape above.
- [`skills/prd-creator/`](../skills/prd-creator/) — interview-driven PRD generation.
- [`skills/design-system-bootstrap/`](../skills/design-system-bootstrap/) — token-first design-system scaffolding.
- [`skills/brand-voice/`](../skills/brand-voice/) — brand-voice discovery, guideline generation, enforcement.

## Distribution

Skills are not packaged. They are consumed locally via symlinks:

- `~/.claude/skills/<skill-name>` → `<repo>/skills/<skill-name>` (verified for the four current skills).
- `~/.codex/skills/<skill-name>` → similar, when the skill is Codex-relevant.

Editing a file in this repo is immediately live for the next Claude Code / Codex session.

## Repo top-level

- `AGENTS.md`, `CLAUDE.md` — entry-point pair for this repo (scaffolded from `context-engineering`, dog-food run).
- `ROADMAP.md` — phased plan for skill refinement.
- `docs/` — PRD, ARCHITECTURE (this file), DECISIONS, DECISIONS_ACTIVE, PARKING_LOT, FUTURE, retros, plus per-skill briefs (`prd-creator-brief.md`, `design-system-bootstrap-brief.md`, `html-over-markdown-brief.md`, `handoff.md`).
- `.claude/` — settings, hooks, slash commands for sessions in this repo (scaffolded from `context-engineering`).
- `skills/` — the actual product.

## External integrations

None at runtime. The skills consume MCP-provided platforms (Notion, Confluence, Drive, Slack, Gong, Granola, etc.) when invoked, but those integrations live in the consumer's environment, not in this repo.

## Cross-references

- Product requirements (canonical for product behavior): [`docs/PRD.md`](PRD.md).
- Roadmap and current phase: [`ROADMAP.md`](../ROADMAP.md).
- Decisions log: [`docs/DECISIONS.md`](DECISIONS.md).
