# Output sketch: large project (abbreviated)

Companion to `transcript-large.md`. The large case is the regression test against feed plus the two corrections from `NOTES.md`. No full file tree; structural sketch with the key checks.

## File tree

```
/Users/rexc/Sites/intelligence-feed/
├── AGENTS.md                              # canonical, modular shape
├── CLAUDE.md                              # one line: @AGENTS.md
├── ROADMAP.md
├── FUTURE.md                              # at root
├── .codex/
│   └── config.toml
├── .agents/
│   └── skills/
│       └── README.md
├── .claude/
│   ├── commands/
│   │   └── session-start.md
│   └── rules/
│       ├── git-and-deploy.md              # always-on
│       ├── session-discipline.md          # always-on
│       ├── product-rules.md               # always-on (17 rules)
│       ├── voice-and-tone.md              # path-scoped
│       ├── design-system.md               # path-scoped
│       ├── design-heuristics.md           # path-scoped
│       ├── ai-shared.md                   # path-scoped
│       ├── ai-feed-enrichment.md          # path-scoped (from ai-surface-stub)
│       ├── ai-feed-assistant.md           # path-scoped (from ai-surface-stub)
│       └── ai-content-generation.md       # path-scoped (from ai-surface-stub)
└── docs/
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── CONTENT_SYSTEM.md                  # canonical workflow doc; user fills body
    ├── DECISIONS.md
    ├── DECISIONS_ACTIVE.md                # CORRECTION 2: present, with promotion criteria
    ├── PARKING_LOT.md
    └── retros/
        └── README.md
```

## Correction checks

These are the two corrections from `NOTES.md`. The regression test passes only if both are present.

### Correction 1: AGENTS canonical, CLAUDE thin

`AGENTS.md` is the canonical entry point with the full rule set, instant-recall design lines, "When in doubt" table, "Path-scoped rules" section, Codex-specific section, and "Before you respond" recency block at the bottom.

`CLAUDE.md` is one line:

```
@AGENTS.md
```

If the generator inverts this (CLAUDE canonical, AGENTS thin), the correction has not been applied.

### Correction 2: DECISIONS_ACTIVE.md present

`docs/DECISIONS_ACTIVE.md` exists with the three-condition promotion criteria:

> A decision belongs here if **all** are true:
> - It imposes a rule the agent must follow now.
> - That rule is not enforced or visible by reading the code itself.
> - It has not been superseded by a later decision.

Feed had `decisions-history.md` only and pushed binding constraints into `.claude/rules/`. The generator must not reproduce that shape.

## Recency block check

`AGENTS.md` "Before you respond" block has all seven items:

1. Hard scope limits.
2. Visual confirmation gates the commit. (Confirmer: Rex.)
3. Direct on `main`. No branches. No worktrees.
4. No deploy CLI.
5. Reproduce before fixing.
6. **Never call the AI layer from a client component.** (Item 6 included because `ai_surface_count >= 1`.)
7. **Vocabulary lock applies.** (Item 7 included because the canonical/forbidden lists are non-empty.)

If only five or six items appear, the renumbering rule fired but the conditions were misread.

## Path-scoped rule list check

`AGENTS.md` "Path-scoped rules" section reads:

> Path-scoped rules: `voice-and-tone.md`, `design-system.md`, `design-heuristics.md`, `ai-shared.md`, `ai-feed-enrichment.md`, `ai-feed-assistant.md`, `ai-content-generation.md`.

Always-on rules: `git-and-deploy.md`, `session-discipline.md`, `product-rules.md`.

## Frontmatter substitution check

Each surface-specific AI rule (`ai-feed-enrichment.md`, `ai-feed-assistant.md`, `ai-content-generation.md`) has a `paths:` frontmatter with three plain string entries. Example for `ai-feed-enrichment.md`:

```yaml
---
paths:
  - "lib/ai/enrich.js"
  - "app/api/feeds/[id]/enrich/route.js"
  - "lib/ai/prompts.js"
---
```

If any entry contains `<!-- PARAMETERIZE: ... -->`, the substitution rule was not applied and the file will not parse as YAML downstream.

## Vocabulary lock check

`AGENTS.md` "Vocabulary lock" section lists both:

- Canonical: `INTERNAL`, `NEWSLETTER`, `BLOG`, `LINK`, `ALERT`.
- Forbidden: `internal-brief`, `customer-newsletter`, `weekly-news-roundup`, `news-update`, `breaking-alert`.

The forbidden list is what makes the rule work. Empty forbidden list = rule not doing its job.

## When in doubt table check

The "When in doubt" table in `AGENTS.md` includes the workflow row pointing at `docs/CONTENT_SYSTEM.md` because `canonical_workflow_doc_name` was set.

## What's not present

- `claude-rules-flat-CLAUDE.md.template` output (the flat shape templates are not used in modular shape).
- A `TECH_STACK.md` (the user did not opt in; AGENTS.md "Tech stack" section drops the doc reference via OPTIONAL marker, falls back to `package.json`).

## Test outcome

The large-case test passes if all four correction checks pass plus all four structural checks pass. If any check fails, fix the generator (`decisions.md` or the substitution rules), not the templates.
