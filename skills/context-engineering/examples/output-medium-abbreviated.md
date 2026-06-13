# Output sketch: medium project (abbreviated)

Companion to [`transcript-medium.md`](transcript-medium.md). The medium case lands in **modular** shape via the voice-and-tone trigger, with one AI surface, basic styling, no token system. This sketch describes the file tree, the regression checks, and the suppressions that are visible in the emitted output. No full file tree.

## File tree

```
/Users/maya/Sites/craft-letters/
├── AGENTS.md                          # canonical, modular shape
├── CLAUDE.md                          # one line: @AGENTS.md
├── BACKLOG.md
├── .codex/
│   └── config.toml                    # codex_usage == "occasional"
├── .claude/
│   ├── settings.json                  # block-env-commit + block-worktree only
│   ├── commands/
│   │   └── session-start.md
│   ├── hooks/
│   │   ├── README.md
│   │   ├── block-env-commit.sh        # always emitted
│   │   └── block-worktree.sh          # uses_visual_confirmation_gate == true
│   └── rules/
│       ├── git-and-deploy.md          # always-on
│       ├── session-discipline.md      # always-on
│       ├── voice-and-tone.md          # path-scoped — the modular trigger
│       ├── ai-shared.md               # path-scoped (stack_has_client_server_split == true)
│       └── ai-draft-generator.md      # path-scoped (one surface)
└── docs/
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── DECISIONS.md
    ├── DECISIONS_ACTIVE.md            # empty, awaiting first promotion
    └── retros/
        └── README.md
```

No `.agents/skills/` (codex_usage is `occasional`, not `regular`). No `product-rules.md` (`include_product_rules == false`). No `design-system.md` or `design-heuristics.md` (`design_shape == "basic_styling"`). No `Later / V2` section in `BACKLOG.md` (`backlog_include_v2 == false`). No surface-specific frontmatter pollution.

## Stack parameterization (visible in output)

The medium case exercises the non-Vercel parameterization path. Spot-checks across emitted files:

| Where | Value | Why |
|---|---|---|
| `AGENTS.md` "Tech stack" line | React + Vite on Cloudflare Pages | `stack_summary_one_line` derived from `stack=react-vite, deploy_target=cloudflare` |
| `AGENTS.md` Commands → Env vars | `` `.dev.vars locally; Cloudflare Pages env vars in production. Never commit .dev.vars.` `` | `env_pattern` Cloudflare default + markdown re-wrap convention |
| `git-and-deploy.md` credentials line | Same `.dev.vars` plain-string value, wrapped at substitution site | Convention check: plain string + markdown re-wrap (see [`decisions.md`](../generator/decisions.md) "env_pattern defaults") |
| `block-env-commit.sh` echo | "Credentials follow this project's env pattern: .dev.vars locally; ... Never commit .dev.vars. If you need..." | Shell consumer substitutes plain value, no backticks (single sentence period, no doubling) |
| `AGENTS.md` "Code rules" deploy line | **(no `block-deploy-cli` line)** | `deploy_target_has_cli_conflict == false` for Cloudflare; the deploy-CLI restriction is dropped from prose and from hooks |

## Hooks scaffold (modular + Cloudflare deltas)

Only two hooks emit because `deploy_target_has_cli_conflict == false`:

| Hook | Emitted | Why |
|---|---|---|
| `block-env-commit.sh` | yes | Always emitted (when `enforce_rules_as_hooks == true`) |
| `block-deploy-cli.sh` | **no** | Wrangler is the standard Cloudflare deploy path; no CLI conflict |
| `block-worktree.sh` (Bash + EnterWorktree) | yes (both matchers) | `uses_visual_confirmation_gate == true` |

`.claude/settings.json` has three `PreToolUse` hook entries (env + worktree-bash + worktree-tool), not four. The `block-deploy-cli` block is dropped along with its trailing comma per JSON-aware substitution.

## Recency block

`AGENTS.md` "Before you respond" has three items:

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.
2. **Visual confirmation gates the commit.** Do not commit UI changes until Maya confirms in a running dev server.
3. **Never call the AI layer from a client component.**

Item 4 (vocabulary lock) is dropped because the project has no canonical/forbidden vocabulary list (separate from voice-and-tone, which is about positioning and characteristics, not term lockdown). Renumbering rule keeps the list contiguous.

## Voice-and-tone rule (the modular trigger)

`.claude/rules/voice-and-tone.md` is the load-bearing file for this project. Its `paths:` frontmatter scopes the rule to files where customer-facing copy is generated or stored:

```yaml
---
paths:
  - "lib/ai/draft.js"
  - "lib/ai/prompts.js"
  - "functions/api/draft.js"
---
```

Body covers the source hierarchy, brand position, primary brand line, voice characteristics, preferred and forbidden term lists, positioning risks, and the project-specific rule that AI cannot invent client facts (every draft must cite the specific brief detail it draws from; gaps surface as `[REVIEW: ...]` placeholders).

## AI rule shape (1 surface, client/server split)

Because `stack_has_client_server_split == true`, `ai-shared.md` emits with the "Never call AI from a client component" rule active. The one surface-specific rule (`ai-draft-generator.md`) has substituted `paths:`:

```yaml
---
paths:
  - "lib/ai/draft.js"
  - "functions/api/draft.js"
  - "lib/ai/prompts.js"
---
```

## Path-scoped rule list

`AGENTS.md` "Path-scoped rules" section reads:

> `voice-and-tone.md`, `ai-shared.md`, `ai-draft-generator.md`.

Always-on rules: `git-and-deploy.md`, `session-discipline.md`.

## What's not present

- `.agents/skills/README.md` (codex_usage occasional, not regular).
- `product-rules.md` (`include_product_rules == false`).
- `design-system.md`, `design-heuristics.md` (`design_shape == "basic_styling"`).
- `Later / V2` section in `BACKLOG.md` (`backlog_include_v2 == false`).
- `block-deploy-cli.sh` and its `settings.json` entry (`deploy_target_has_cli_conflict == false`).
- Vocabulary lock section in AGENTS.md (no canonical/forbidden lists).

## Regression checks

The medium-case test passes if:

1. **Modular shape via voice-and-tone trigger.** [`decisions.md`](../generator/decisions.md) "Rule shape" criterion fires on `voice_and_tone == true` even with `ai_surface_count == 1` and `design_shape != "tokens_with_linter"`. If the generator drops to flat shape, the criterion is misreading "modular if **any** of the following" as "modular if all".
2. **AGENTS canonical, CLAUDE thin.** `AGENTS.md` is the full rule set; `CLAUDE.md` is one line: `@AGENTS.md`.
3. **Hooks parameterization on deploy target.** `block-deploy-cli.sh` is NOT emitted (Cloudflare); `block-worktree.sh` IS emitted (visual-confirmation gate); `block-env-commit.sh` IS emitted (always).
4. **env_pattern convention.** The Cloudflare default substitutes as a plain string into shell echo (no command substitution risk) and gets backtick-wrapped at markdown consumption sites.
5. **Recency block has three items.** Item 4 (vocabulary lock) is dropped; renumbering rule fires.
6. **Voice-and-tone frontmatter substituted.** `paths:` lines in `voice-and-tone.md` and `ai-draft-generator.md` are plain string entries with no `<!-- PARAMETERIZE: ... -->` markers.

If any check fails, the bug is in the generator (`decisions.md` or substitution rules), not in the templates.
