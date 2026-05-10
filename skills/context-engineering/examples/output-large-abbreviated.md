# Output sketch: large project (abbreviated)

Companion to [`transcript-large.md`](transcript-large.md). The large case is the **structural parameterization regression test**: a no-UI Python service on Fly.io with three AI surfaces. Lands in modular shape via `ai_surface_count >= 2`, but the no-UI + no-CLI-conflict + no-voice-and-tone combination forces a four-flag suppression cascade visible across the file tree, hooks scaffold, recency block, and rule directory.

## File tree

```
/Users/devon/Sites/triage-classifier/
├── AGENTS.md                          # canonical, modular shape, minimal recency
├── CLAUDE.md                          # one line: @AGENTS.md
├── ROADMAP.md
├── FUTURE.md                          # V2 list
├── .codex/
│   └── config.toml
├── .agents/
│   └── skills/
│       └── README.md                  # codex_usage == "regular"
├── .claude/
│   ├── settings.json                  # block-env-commit only
│   ├── commands/
│   │   └── session-start.md
│   ├── hooks/
│   │   ├── README.md
│   │   └── block-env-commit.sh        # the only hook emitted
│   └── rules/
│       ├── git-and-deploy.md          # always-on
│       ├── session-discipline.md      # always-on (no UI bullet, no Commit gate)
│       ├── ai-topic-classifier.md     # path-scoped (one of three surfaces)
│       ├── ai-urgency-detector.md     # path-scoped
│       └── ai-summary-generator.md    # path-scoped
└── docs/
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── DECISIONS.md
    ├── DECISIONS_ACTIVE.md
    ├── PARKING_LOT.md
    └── retros/
        └── README.md
```

**Not emitted** (each absence has a specific suppression flag — see cascade table below):

- `voice-and-tone.md` — `voice_and_tone == false`.
- `design-system.md`, `design-heuristics.md` — `design_shape == "none"`.
- `product-rules.md` — `include_product_rules == false`.
- `ai-shared.md` — `stack_has_client_server_split == false` (Python service has no client/server boundary; the "never call AI from a client component" rule has no analogue).
- `block-deploy-cli.sh` (+ `settings.json` entry) — `deploy_target_has_cli_conflict == false` (Fly CLI is the standard deploy path).
- `block-worktree.sh` (+ `settings.json` entries × 2) — `uses_visual_confirmation_gate == false` (no UI; worktrees do not break a non-existent visual-confirmation gate).

## Suppression cascade (the demo)

This is what the large case exists to prove: the generator suppresses real content based on four orthogonal flags, not just one. Each row is a separate suppression, traceable to a specific line in [`decisions.md`](../generator/decisions.md).

| Flag | Value | Drops in output |
|---|---|---|
| `uses_visual_confirmation_gate` | false | • Recency item 2 (visual confirmation gates the commit)<br>• "No worktrees." inline suffix on primary-constraints item 3<br>• Body Commit gate section in `session-discipline.md`<br>• UI bullet under Verification before claiming done<br>• Codex visual-confirmation override paragraph in `AGENTS.md`<br>• `block-worktree.sh` hook<br>• Two `settings.json` PreToolUse entries (Bash + EnterWorktree) |
| `stack_has_client_server_split` | false | • `ai-shared.md` rule file<br>• Recency item 3 (AI client-component constraint) |
| `deploy_target_has_cli_conflict` | false | • "Never use the X CLI" line in Code rules<br>• "No X CLI" inline suffix on primary-constraints item 3<br>• `block-deploy-cli.sh` hook<br>• One `settings.json` PreToolUse entry |
| `voice_and_tone` | false | • `voice-and-tone.md` rule file<br>• `path_scoped_rule_list` entry for voice-and-tone |

If any of these suppressions does not fire, the generator has a regression. The most likely culprit: the OPTIONAL gating logic in [`decisions.md`](../generator/decisions.md) misreading one of the flags.

## Hooks scaffold (the minimal case)

`.claude/settings.json` has a single `PreToolUse` hook block. This is the floor — the simplest hooks scaffold the generator can emit when `enforce_rules_as_hooks == true`.

| Hook | Emitted | Why |
|---|---|---|
| `block-env-commit.sh` | yes | Always emitted (when `enforce_rules_as_hooks == true`) |
| `block-deploy-cli.sh` | **no** | `deploy_target_has_cli_conflict == false` |
| `block-worktree.sh` (Bash matcher) | **no** | `uses_visual_confirmation_gate == false` |
| `block-worktree.sh` (EnterWorktree matcher) | **no** | `uses_visual_confirmation_gate == false` |

JSON output is one PreToolUse object inside the array. The OPTIONAL gating must correctly drop the other three objects **and** the trailing comma that would otherwise produce invalid JSON.

## Stack parameterization (visible in output)

| Where | Value | Why |
|---|---|---|
| `AGENTS.md` "Tech stack" line | Python service on Fly.io | `stack_summary_one_line` derived |
| `AGENTS.md` Commands → Install | `uv sync` | Python stack default |
| `AGENTS.md` Commands → Check | `ruff check . && mypy .` | Python stack default |
| `AGENTS.md` Commands → Test | `pytest` | Python stack default |
| `AGENTS.md` Commands → Env vars | `` `.env locally; fly secrets in production. Never commit .env.` `` | `env_pattern` Fly default + markdown re-wrap |
| `block-env-commit.sh` echo | "Credentials follow this project's env pattern: .env locally; fly secrets in production. Never commit .env. If you need..." | Shell consumer substitutes plain value |

## Recency block

`AGENTS.md` "Before you respond" has **one item**:

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.

Items 2, 3, and 4 are all suppressed by the flag cascade. This is the minimum recency block — three of the four conditional items dropped — and it tests the renumbering rule's contiguous-list invariant in the degenerate case.

If the emitted recency block has more than one item, one of the suppression conditions misread.

## AI rules (3 surfaces, no shared)

Three surface-specific rule files, no `ai-shared.md`. Each has substituted `paths:` frontmatter with three plain string entries (no remaining markers).

```yaml
# ai-topic-classifier.md
---
paths:
  - "app/ai/topic.py"
  - "app/api/classify.py"
  - "app/ai/prompts.py"
---
```

```yaml
# ai-urgency-detector.md
---
paths:
  - "app/ai/urgency.py"
  - "app/api/classify.py"
  - "app/ai/prompts.py"
---
```

```yaml
# ai-summary-generator.md
---
paths:
  - "app/ai/summary.py"
  - "app/api/summarize.py"
  - "app/ai/prompts.py"
---
```

The surface-specific files emit per [`decisions.md`](../generator/decisions.md) "Per-template inclusion table"; `ai-shared.md` is suppressed per the "Server-only AI call rule (conditional)" section because `stack_has_client_server_split == false`. If `ai-shared.md` is emitted anyway with the server-only rule active, the conditional logic was not read.

## Path-scoped rule list

`AGENTS.md` "Path-scoped rules" section reads:

> `ai-topic-classifier.md`, `ai-urgency-detector.md`, `ai-summary-generator.md`.

(No `voice-and-tone.md`, no `design-system.md`, no `ai-shared.md` — each absence traces to a flag.)

Always-on rules: `git-and-deploy.md`, `session-discipline.md`. (No `product-rules.md`.)

## Two corrections still apply

The two structural corrections from prior validation work still apply to this case:

1. **AGENTS canonical, CLAUDE thin.** `AGENTS.md` is the full rule set; `CLAUDE.md` is one line: `@AGENTS.md`. Direction not inverted.
2. **`DECISIONS_ACTIVE.md` present.** With promotion criteria and an empty body awaiting first promotion.

## Regression checks

The large-case test passes if:

1. **Four suppressions fire.** Each of the four flag values in the suppression cascade drops the content listed in its row. Spot-check: `ai-shared.md` absent, `voice-and-tone.md` absent, both worktree-block entries absent from `settings.json`, only `block-env-commit.sh` in `.claude/hooks/`.
2. **Recency block has one item.** Renumbering rule fires correctly in the degenerate case; output is `1.` alone, not an empty list and not items 1+something with broken numbering.
3. **AGENTS canonical, CLAUDE thin.** Direction not inverted from the modular paired-write rule.
4. **`settings.json` JSON validity.** With three of four hook objects dropped, the remaining JSON parses (trailing-comma cleanup fired).
5. **Hook script substitution.** `block-env-commit.sh` echo includes the substituted Fly `env_pattern` as a plain string (single trailing period, no command-substitution backticks).
6. **Surface-specific frontmatter substituted.** All three `ai-<surface>.md` files have plain `paths:` entries with no remaining `<!-- PARAMETERIZE: ... -->` markers.
7. **No `ai-shared.md`.** Suppressed because `stack_has_client_server_split == false`; this is the harder check because the generator must read the conditional in [`decisions.md`](../generator/decisions.md) "Server-only AI call rule (conditional)" rather than treating `ai-shared.md` as unconditional for any project with AI.

If any check fails, the bug is in the generator (`decisions.md` or substitution rules), not in the templates.
