# Generator decisions

The mapping logic from intake answers to template choices, file outputs, and substitutions. Read this after `intake.md` has produced a complete answer set, before writing files.

## State map (from intake)

The generator should hold answers in a state map with these keys:

| Key | Source question | Type | Notes |
|---|---|---|---|
| `project_name` | Q1 | string | |
| `project_description` | Q2 | string (paragraph) | |
| `project_tagline_one_line` | Q2a | string | One-line tagline used when `source_prd_present == true` and "What this project is" becomes a pointer to PRD.md. |
| `repo_local_path` | Q3 | absolute path | |
| `github_repo_url` | Q4 | URL | |
| `visual_confirmer_name` | Q5 | string | Default: user's first name. |
| `stack` | Q5a | enum | `nextjs`, `react-vite`, `node-cli`, `python`, `other`. |
| `deploy_target` | Q5b | enum | `vercel`, `netlify`, `cloudflare`, `fly`, `railway`, `manual`, `none`. |
| `deploy_target_name` | derived | string | Display name (e.g., "Vercel", "Netlify"). |
| `deploy_target_has_cli_conflict` | derived | bool | True for Vercel and Netlify (CLI deploys conflict with auto-deploy via GitHub). False for Cloudflare Pages, Fly, Railway, manual, none. |
| `deploy_cli_name` | derived | string | "Vercel" / "Netlify" / etc. — only used if `deploy_target_has_cli_conflict`. |
| `stack_summary_one_line` | derived | string | E.g., "Next.js (App Router) on Vercel", "React + Vite on Cloudflare Pages". |
| `stack_has_client_server_split` | derived | bool | True for `nextjs`, `react-vite` (with backend), false for `node-cli`, `python`. Drives the server-only AI call rule. |
| `stack_has_ui` | derived | bool | True for `nextjs`, `react-vite`, false for `node-cli`, `python`. Drives whether visual confirmation gates commits. |
| `uses_visual_confirmation_gate` | derived | bool | True when `stack_has_ui == true` *and* `visual_confirmer_name` is set. Drives the worktree restriction (worktrees break visual confirmation in single-dev-server workflows). False suppresses worktree-restriction rules and the visual-confirmation recency item. |
| `enforce_rules_as_hooks` | Q5f | bool | When true, emit `.claude/settings.json` and `.claude/hooks/*.sh` to enforce load-bearing rules as actual blocks rather than prose. Default true; user can opt out. |
| `deploy_cli_lower` | derived | string | Lowercased deploy CLI name for use in shell command matchers (`vercel`, `netlify`). Empty when `deploy_target_has_cli_conflict == false`. |
| `install_cmd`, `dev_cmd`, `check_cmd`, `test_cmd`, `build_cmd` | Q5c | string | Commands. Defaults inferred from stack. |
| `env_pattern` | Q5d | string | E.g., "`.env.local` locally; Vercel project env vars in production". |
| `ai_surface_count` | Q6 | int | 0, 1, 2-3, or 4+. |
| `ai_surfaces` | Q7–Q15 | list of dicts | One dict per surface. |
| `model_split_table` | Q16 | string (markdown table) | |
| `ai_client_path`, `ai_prompts_path` | Q17–Q18 | string paths | |
| `design_shape` | Q19 | enum | `tokens_with_linter`, `basic_styling`, `none`. |
| `apply_design_heuristics` | Q20 | bool | |
| `voice_and_tone` | Q21 | bool | |
| `include_parking_lot`, `include_decisions_active`, `include_future` | Q22–Q24 | bool | |
| `codex_usage` | Q25 | enum | `regular`, `occasional`, `none`. |
| `canonical_workflow_doc_name` | Q26 | string or null | |
| `include_product_rules` | Q27 | bool | |
| `workflows` | Q30 | list of `{name, description}` | |
| (all content fills) | Q28–Q35 | strings | Used as direct substitutions. |

## Stack and deploy-target defaults

Defaults inferred from `stack` × `deploy_target`. The user can override any value during intake.

| `stack` | `install_cmd` | `dev_cmd` | `check_cmd` | `test_cmd` | `build_cmd` |
|---|---|---|---|---|---|
| `nextjs` | `npm install` | `npm run dev` | `npm run check` | `npm test` (or "not configured") | `npm run build` |
| `react-vite` | `npm install` | `npm run dev` | `npm run lint && npm run typecheck` | `npm test` | `npm run build` |
| `node-cli` | `npm install` | (none — not a server) | `npm run lint && npm run typecheck` | `npm test` | `npm run build` |
| `python` | `uv sync` | (varies) | `ruff check . && mypy .` | `pytest` | (varies) |
| `other` | (ask user) | (ask user) | (ask user) | (ask user) | (ask user) |

`env_pattern` defaults:

| `deploy_target` | Default `env_pattern` |
|---|---|
| `vercel` | .env.local locally; Vercel project env vars in production. Never commit .env.local. |
| `netlify` | .env.local locally; Netlify site env vars in production. Never commit .env.local. |
| `cloudflare` | .dev.vars locally; Cloudflare Pages env vars in production. Never commit .dev.vars. |
| `fly` | .env locally; fly secrets in production. Never commit .env. |
| `railway` | .env locally; Railway project env vars in production. Never commit .env. |
| `manual` | (ask user — depends on host) |
| `none` | .env locally only. |

**Convention: `env_pattern` is a plain string** — no markdown formatting in the value itself. Markdown consumers (template lines that render this in `.md` output) are responsible for wrapping the substituted value in backticks at the substitution site (e.g., `` `<!-- PARAMETERIZE: env_pattern --> ` `` in the template). Shell consumers (`block-env-commit.sh.template`) substitute the plain value into a double-quoted `echo` without backticks, so command-substitution can't fire. This avoids context-dependent stripping logic in the generator and avoids parameter doubling. Same rule applies to any future parameter that needs to appear in both markdown and shell contexts.

`deploy_target_has_cli_conflict` truth table:

| `deploy_target` | `deploy_target_has_cli_conflict` | `deploy_cli_name` (when conflict) |
|---|---|---|
| `vercel` | true | `Vercel` |
| `netlify` | true | `Netlify` |
| `cloudflare` | false | (no CLI gate; Wrangler is the standard deploy path for Workers) |
| `fly` | false | (Fly CLI is the standard deploy path) |
| `railway` | false | (Railway CLI is the standard deploy path) |
| `manual` | false | |
| `none` | false | |

When `deploy_target_has_cli_conflict == true`, the flat-CLAUDE template's "Code rules" emits a "Never use the <deploy_cli_name> CLI" line, and the recency block's primary-constraints anchor (item 3) appends "No <deploy_cli_name> CLI." When false, both are suppressed.

`stack_summary_one_line` is built from stack + deploy_target. Examples:

| `stack` | `deploy_target` | `stack_summary_one_line` |
|---|---|---|
| `nextjs` | `vercel` | `Next.js (App Router) on Vercel` |
| `nextjs` | `netlify` | `Next.js (App Router) on Netlify` |
| `react-vite` | `cloudflare` | `React + Vite on Cloudflare Pages` |
| `node-cli` | `fly` | `Node CLI on Fly.io` |
| `python` | `manual` | `Python (deployed manually)` |

## Server-only AI call rule (conditional)

The `ai-shared.md` rule template carries a "never call AI from a client component" rule. This is only meaningful when `stack_has_client_server_split == true`. For `node-cli` and `python` stacks, suppress the rule (or replace with a stack-appropriate analogue if the project has one — e.g., "AI keys never in user-facing config" for a CLI). When suppressed, also suppress the corresponding recency-block item.

## Redundancy guards

The paper's redundancy finding (LLM context files improve by 2.7% when README is removed) means the practical risk is overlap inside our own outputs. PRD.md, ARCHITECTURE.md, and CLAUDE.md should not all describe the project.

- **PRD redundancy guard.** When `source_prd_present == true` *or* the generator is producing `docs/PRD.md`, "What this project is" takes one of three shapes based on `len(workflows)`. In all three the `project_description_pointer` block replaces the `project_description_section` block, and `project_tagline_one_line` (Q2a) is asked.
  - `len(workflows) <= 1`: pointer-only. One-line tagline + `See docs/PRD.md`. Suppress `workflows_list`. (Flat shape lands here by construction — flat projects have 0–1 workflows.)
  - `2 <= len(workflows) <= 5`: pointer-plus-workflows — the orientation shape. Tagline + `See docs/PRD.md` + the workflow bullet list. This is the shape `the-council` arrived at by hand (audit 2026-05-10); workflows are concrete enough to earn their tokens at session start, the paragraph is the actual redundancy.
  - `len(workflows) >= 6`: pointer-only, list lives in PRD only. Past five bullets the list defeats the compact-pointer goal and belongs in PRD. Suppress `workflows_list`.

  Reason: the paper's 2.7% finding targets duplicated prose descriptions. A bulleted workflow list is structurally distinct from a narrative paragraph — an orientation index, not a duplicate — and is cheap to keep at AGENTS-level when there are 2–5 named flows. When `source_prd_present == false` and PRD.md is not being generated, fall back to the inline `project_description_section` paragraph; `workflows_list` still gates on `len(workflows) > 1` per the existing template comment.
- **Architecture pointer guard.** When `docs/ARCHITECTURE.md` is being generated, the flat CLAUDE template's "Architecture rules (non-negotiable)" stays (those are behavioral rules, not layout description), but any prose paragraph that restates the layout, folder structure, or data model is dropped. The flat template does not currently include such prose; this guard is documented here so future template edits do not introduce duplication.
- **Decisions guard.** When `include_decisions_active == true`, constraints already in `DECISIONS_ACTIVE.md` are not restated in the body of CLAUDE.md/AGENTS.md. They may still appear in the recency block if they meet the bar (the recency block is intentionally short and rules already in DECISIONS_ACTIVE are unlikely to clear that bar).

## Rule shape: flat vs modular

Modular if **any** of the following are true:

- `ai_surface_count >= 2`
- `design_shape == "tokens_with_linter"`
- `len(workflows) > 1`
- `voice_and_tone == true`

Otherwise flat.

The token-plus-linter wording matters. A project with `lib/styles.js` and `app/globals.css` but no token file and no linter is `basic_styling`, not `tokens_with_linter`, and stays flat. A project with `design-system/colors_and_type.css` plus an `npm run check:tokens` linter is `tokens_with_linter` and goes modular.

## Paired-write rule for the flat shape

When `rule_shape == "flat"`, the generator writes two files together:

- `CLAUDE.md` from `claude-rules-flat-CLAUDE.md.template`. This is canonical.
- `AGENTS.md` from `claude-rules-flat-AGENTS.md.template`. This is the thin pointer plus the Codex-specific override paragraph.

Do not write the modular-shape `AGENTS.md.template` or `CLAUDE.md.template` when rule_shape is flat. The pairing is not obvious from the templates alone; this rule is what binds them.

## Paired-write rule for the modular shape

When `rule_shape == "modular"`:

- `AGENTS.md` from `AGENTS.md.template`. This is canonical.
- `CLAUDE.md` from `CLAUDE.md.template`. One line: `@AGENTS.md`.

Do not write the flat-shape templates when rule_shape is modular.

## Per-template inclusion table

Each row names a conditional template, the answer that triggers it, and the output path.

| Template | Triggered when | Output path |
|---|---|---|
| `claude-rules-modular/git-and-deploy.md.template` | `rule_shape == "modular"` | `.claude/rules/git-and-deploy.md` |
| `claude-rules-modular/session-discipline.md.template` | `rule_shape == "modular"` | `.claude/rules/session-discipline.md` |
| `claude-rules-modular/product-rules.md.template` | `rule_shape == "modular" and include_product_rules` | `.claude/rules/product-rules.md` |
| `claude-rules-modular/voice-and-tone.md.template` | `rule_shape == "modular" and voice_and_tone` | `.claude/rules/voice-and-tone.md` |
| `claude-rules-modular/design-system.md.template` | `rule_shape == "modular" and design_shape == "tokens_with_linter"` | `.claude/rules/design-system.md` |
| `claude-rules-modular/design-heuristics.md.template` | `rule_shape == "modular" and apply_design_heuristics` | `.claude/rules/design-heuristics.md` |
| `claude-rules-modular/ai-shared.md.template` | `rule_shape == "modular" and ai_surface_count >= 1` | `.claude/rules/ai-shared.md` |
| `claude-rules-modular/ai-surface-stub.md.template` | `rule_shape == "modular" and ai_surface_count >= 1`. Instantiated **once per surface**. | `.claude/rules/ai-<surface_kebab_name>.md` |
| `docs/PRD.md.template` | always | `docs/PRD.md` |
| `docs/ARCHITECTURE.md.template` | always | `docs/ARCHITECTURE.md` |
| `docs/ROADMAP.md.template` | always | `ROADMAP.md` (root, default) or `docs/ROADMAP.md` if user prefers |
| `docs/DECISIONS.md.template` | always | `docs/DECISIONS.md` |
| `docs/DECISIONS_ACTIVE.md.template` | `include_decisions_active` | `docs/DECISIONS_ACTIVE.md` |
| `docs/PARKING_LOT.md.template` | `include_parking_lot` | `docs/PARKING_LOT.md` |
| `docs/FUTURE.md.template` | `include_future` | `docs/FUTURE.md` (or `FUTURE.md` at root) |
| `docs/retros/README.md.template` | always | `docs/retros/README.md` |
| `claude-commands/session-start.md.template` | always | `.claude/commands/session-start.md` |
| `codex-config.toml.template` | `codex_usage in ("regular", "occasional")` | `.codex/config.toml` |
| `agents-skills-README.md.template` | `codex_usage == "regular"` | `.agents/skills/README.md` |
| `claude-settings.json.template` | `enforce_rules_as_hooks == true` | `.claude/settings.json` |
| `claude-hooks/README.md.template` | `enforce_rules_as_hooks == true` | `.claude/hooks/README.md` |
| `claude-hooks/block-env-commit.sh.template` | `enforce_rules_as_hooks == true` | `.claude/hooks/block-env-commit.sh` (chmod +x) |
| `claude-hooks/block-deploy-cli.sh.template` | `enforce_rules_as_hooks == true and deploy_target_has_cli_conflict == true` | `.claude/hooks/block-deploy-cli.sh` (chmod +x) |
| `claude-hooks/block-worktree.sh.template` | `enforce_rules_as_hooks == true and uses_visual_confirmation_gate == true` | `.claude/hooks/block-worktree.sh` (chmod +x) |

The flat-shape templates (`claude-rules-flat-CLAUDE.md.template` and `claude-rules-flat-AGENTS.md.template`) and the modular entry-point templates (`AGENTS.md.template`, `CLAUDE.md.template`) are governed by the paired-write rules above, not by this table.

## Substitution rules

### General

For every `<!-- PARAMETERIZE: <key> -->` marker, substitute the corresponding value from the state map. Trim leading/trailing whitespace on substitution. Preserve indentation.

### YAML frontmatter substitution

Some templates carry `<!-- PARAMETERIZE: ... -->` markers inside YAML frontmatter blocks (between `---` lines). Specifically `claude-rules-modular/ai-surface-stub.md.template`:

```yaml
---
paths:
  - "<!-- PARAMETERIZE: surface_implementation_path -->"
  - "<!-- PARAMETERIZE: surface_api_route_path -->"
  - "<!-- PARAMETERIZE: ai_prompts_path -->"
---
```

Substitution must run before the file is written. If the YAML frontmatter contains an unsubstituted `<!--` block when written, downstream tools that parse frontmatter will fail. Verify by parsing the YAML after substitution; the `paths:` list should contain three plain string entries with no comment markers.

### OPTIONAL block handling

`<!-- OPTIONAL: <key> -->` markers gate the line or block immediately following. Each marker has a condition expressed in the comment (e.g., `include if include_parking_lot == true`).

Behavior:

- If the condition is true: keep the marker line itself removed from output, keep the gated block as-is.
- If the condition is false: drop the marker line **and** the gated block (the next line, or the next contiguous block ending at a blank line, depending on context).

Some markers gate inline cells in tables (e.g., `<!-- OPTIONAL: ux_row -->` in the flat CLAUDE "Where to look" table). For those, drop the entire row when the condition is false.

### KEEP AS-IS

`<!-- KEEP AS-IS: <reason> -->` markers do not require substitution and should not be removed. They are documentation for the user that the line they precede is intentionally fixed.

## Hooks enforcement (parallel to prose rules)

When `enforce_rules_as_hooks == true`, the generator emits `.claude/settings.json` and supporting scripts under `.claude/hooks/`. The rationale is the AGENTS.md study finding that prose rules are interpreted as guidelines; for load-bearing constraints, the right enforcement layer is a hook from the harness, not a sentence in CLAUDE.md.

Hooks emitted:

| Hook script | Always or conditional | Blocks |
|---|---|---|
| `block-env-commit.sh` | Always (when `enforce_rules_as_hooks == true`) | `Bash(git add .env*)` — prevents staging env files. |
| `block-deploy-cli.sh` | When `deploy_target_has_cli_conflict == true` | `Bash(<deploy_cli_lower> *)` — prevents deploy-CLI usage that conflicts with auto-deploy. |
| `block-worktree.sh` | When `uses_visual_confirmation_gate == true` | `Bash(git worktree *)` and `EnterWorktree` tool — prevents worktree creation that would break visual confirmation. |

The hooks coexist with the prose rules in CLAUDE.md/AGENTS.md. The prose explains *why*; the hook guarantees *that*. Removing one without the other breaks either orientation or enforcement. The prose rules are not removed when hooks are emitted.

Scripts must be `chmod +x` after writing. The generator handles this as part of file emission; users adding new hooks manually must remember to do it themselves.

## JSON-aware substitution

`claude-settings.json.template` carries `<!-- PARAMETERIZE: -->` markers and `"//OPTIONAL"` keys, but the file itself is JSON, not Markdown. The substitution rules are slightly different:

- `<!-- PARAMETERIZE: <key> -->` inside JSON string values: replace as normal (the marker syntax inside a string does not break JSON parsing).
- `"//OPTIONAL": "<condition>"` keys: gate the JSON object containing them. If the condition is false, drop the *entire enclosing object* (not just the key). When dropping an object inside an array, also drop the trailing comma if it would create a syntax error.
- `"//"` keys (without `OPTIONAL`): pure documentation. Claude Code ignores keys starting with `//`. Keep them as-is in the output; they are harmless and useful for the user.

After substitution, the generator must validate the output is parseable JSON. If validation fails, the generator reports the file path and the parse error and stops; do not emit a syntactically broken `settings.json`.

## Recency safeguard renumbering rule

The recency safeguard block in `AGENTS.md.template` and the equivalent in `claude-rules-flat-CLAUDE.md.template` carries item 1 always present and items 2 (visual confirmation), 3 (AI), 4 (vocabulary) conditional.

Always-on item:

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.

Conditions for optional items:

- Item 2 (visual confirmation gates the commit) included if `uses_visual_confirmation_gate == true`. Suppressed for no-UI projects (`node-cli`, `python`, `other` without UI). Same gate also drops the visual-confirmation line from "Primary constraints (read before doing anything)" near the top, the "Commit gate" body section, the "UI changes" bullet under "Verification before claiming done", and the "No worktrees" suffix in primary-constraints item 3.
- Item 3 (AI client-component constraint) included if `ai_surface_count >= 1` *and* `stack_has_client_server_split == true`. Suppressed for `node-cli` and `python` stacks even if AI surfaces exist.
- Item 4 (vocabulary lock) included if vocabulary lock applies (any of `canonical_vocabulary_list` is non-empty).

When optional items are skipped, renumber the remaining items so the list is contiguous (1 — not 1, 2; or 1, 2 — not 1, 3).

## No-UI project handling

When `uses_visual_confirmation_gate == false`, the following content is dropped from the flat-CLAUDE template, the modular AGENTS template, the modular session-discipline template, and the flat-AGENTS Codex-override paragraph:

- Primary-constraints item 2 ("Visual confirmation gates the commit") — both templates.
- The "No worktrees." suffix on primary-constraints item 3 — both templates.
- Recency-block item 2 — both templates.
- Body "Commit gate" section — flat CLAUDE and modular session-discipline.
- "UI changes" bullet under "Verification before claiming done" — flat CLAUDE and modular session-discipline.
- The Codex-override paragraph in flat-AGENTS.md.template (the entire override is about visual confirmation).
- The worktree-restriction code rule (already gated by the same flag — confirm it stays gated).
- The block-worktree.sh hook and its two `settings.json` entries (already gated).

When `deploy_target == "none"`, the push-protocol body bullet drops the "waiting for `<deploy_target_name>` deploy" wording and the production-confirmation requirement; the user still pastes the commit URL but the agent declares done after the push.

The block is intentionally short. Items previously in the block (direct-on-main, no deploy CLI, reproduce-before-fixing) live in the body of the template and are not duplicated in the recency block. The principle: items belong in the recency block only if violating them damages product, loses work, or burns a stakeholder, and only if duplicating them genuinely changes agent behavior under attention pressure.

## Path-scoped rule list (AGENTS.md "Path-scoped rules" section)

The `path_scoped_rule_list` parameter is derived from the per-template inclusion decisions, not asked of the user. Build the list from the rule files actually emitted.

For example, if the modular set includes `voice-and-tone.md`, `design-system.md`, `ai-shared.md`, and `ai-feed-enrichment.md`, the value is:

> `voice-and-tone.md`, `design-system.md`, `ai-shared.md`, `ai-feed-enrichment.md`.

If only one is included, the value is just that one filename. If none are included, the entire "Path-scoped rules" sentence in AGENTS.md is omitted via the OPTIONAL marker that gates it.

## UX row content for the flat CLAUDE template

The `ux_row_doc_names` parameter is only relevant when `rule_shape == "flat"` and the project has UX or styling docs. If `design_shape == "none"`, drop the row entirely (the `<!-- OPTIONAL: ux_row -->` marker handles this). If `design_shape == "basic_styling"` and the user named UX or styling docs, fill with those doc paths in the format `\`docs/UX_HEURISTICS.md\` (canonical), \`docs/UI_SYSTEM.md\` (styling)` or whatever the project actually has.

## PRD-driven generation behaviors

When `source_prd_present == true`, the generator applies four documented defaults during file generation. These are not improvisation; they are spec.

### PRD-as-tiebreaker fallback

If `canonical_workflow_doc_name` is null and `source_prd_present == true`, mark the PRD as the workflow tiebreaker in two places:

- In `AGENTS.md` "Before writing any code" section, under "Read when relevant," append "**Tiebreaker on conflicts.**" to the `docs/PRD.md` line.
- In `AGENTS.md` "When in doubt" table, the "Product behavior, copy" row reads `docs/PRD.md` (canonical, tiebreaker)`.

If a `canonical_workflow_doc_name` is named, it owns the tiebreaker role and the PRD does not.

### V2/V3 extraction from PRD into FUTURE.md

If `source_prd_present == true` and `include_future == true`, scan the PRD for sections named `## V2`, `## V3`, `## Future`, `## Deferred capabilities`, `## Roadmap V2`, or similar. Lift the items into `FUTURE.md` under the appropriate "V2" or "V3" subsection.

If `include_future == false` but the PRD has a deferred-capabilities section, leave the items in the PRD's "Deferred capabilities" subsection (which `PRD.md.template` already provides for via `deferred_capabilities_list_or_none`).

### Decisions seeding from PRD

If `source_prd_present == true` and the PRD contains a `## Decisions`, `## Decisions made`, `## Architecture decisions`, or similar section, extract each decision as a candidate for `DECISIONS.md` seeding.

For each candidate:

1. Format it per the `DECISIONS.md` template structure (Title / Date / Context / Decision / Reason / Revisit if).
2. Number it D-001, D-002, etc. in the order it appears in the PRD.
3. Append to `docs/DECISIONS.md`.

**Do not bulk-mirror to `DECISIONS_ACTIVE.md`.** See "DECISIONS_ACTIVE promotion is per-decision, not bulk" below.

### External-skill cross-link in agents-skills README

If `external_skill_references` is non-empty (Q27a in cluster 5 captured at least one), add the cross-link to `.agents/skills/README.md`:

- In the "Available skills" section, if `_None yet._` is the placeholder, replace with a paragraph noting that no repo-local skills exist but external skills inform the project, listing each from `external_skill_references` with its path.
- In the "Cross-references" section, add one bullet per external skill in the form `Methodology source skill (lives in user-global config): \`<path>\`.`

Example output for an external skill named `llm-council` at `~/.claude/skills/llm-council/`:

> _None yet._ Add a skill folder under `.agents/skills/<skill-name>/` and document it here when one is added. Until then, the global skill set in `~/.claude/skills/` and `~/.codex/` applies — most relevant for this project: `llm-council` (the methodology source skill that this product is built on).

## DECISIONS_ACTIVE promotion is per-decision, not bulk

When decisions are seeded into `DECISIONS.md` (whether from PRD extraction or from user-supplied lists in cluster 0's `source_other_material`), each one must pass the `DECISIONS_ACTIVE.md` three-condition criteria before it is mirrored:

1. **Imposes a rule the agent must follow now.**
2. **Not enforced or visible by reading the code itself.** A decision like "use Vercel KV" is visible from `package.json` and should not be in `DECISIONS_ACTIVE.md`. A decision like "BYOK only in V1; no accounts" is a product strategy that lives nowhere in code and should be in `DECISIONS_ACTIVE.md`.
3. **Has not been superseded by a later decision.**

Process:

- For each candidate decision, ask the user a literal Y/N question. Print the decision title, a one-line summary, and the three criteria above. Wait for an explicit response. Do not batch the candidates. Do not decide silently and report.
- The agent's recommendation is allowed and welcome ("D-002 looks like it qualifies because the fallback chain isn't visible from any single file") but the user's Y/N is the call.
- If the user is unsure, default to no. The decision still lives in `DECISIONS.md` and can be promoted later.
- Bulk-mirror is prohibited. The outcome of every promotion must trace to a recorded user response.

The validation run on `epost-assessment` decided 3 of 5 promotions silently. The outcome was defensible but the process violated this rule. Future runs must show the question-and-answer per decision.

Rationale: the validation run on `the-council` mirrored all four seeded decisions to `DECISIONS_ACTIVE.md` without per-decision check. At least one (D-001 BYOK) clearly qualified, but mirroring all four bypassed the curation logic. The whole point of `DECISIONS_ACTIVE.md` is being a curated subset; bulk-mirror collapses the distinction.

## What the generator never writes

The skill's scope is context files: rules, docs, slash commands, the AGENTS.md/CLAUDE.md pair, the codex/agents-skills config. **Never product code.** No matter what the user provides as source material (PRD, brand book, design spec, tech doc), the generator does not create files at any of the following paths:

- `app/**/*.{js,jsx,ts,tsx,css,scss}` — application code, including styles.
- `lib/**/*` — library code.
- `components/**/*` — UI components.
- `features/**/*` — feature modules.
- `pages/**/*` — page components.
- `styles/**/*` — global styles.
- `public/**/*` — static assets.
- `design-system/**/*.{css,js,jsx,ts,tsx}` — token files, even if the project's design system rule references them.
- Any file outside `.claude/`, `.codex/`, `.agents/`, `docs/`, `AGENTS.md`, `CLAUDE.md`, `ROADMAP.md`, `FUTURE.md`.

**Templates may reference paths to product files** — `design-system.md` rule references the token file path via `<!-- PARAMETERIZE: token_file_path -->`, `ai-shared.md` references the AI client and prompts paths, etc. These references are targets, not commands to create. The path being unresolved at scaffold time is fine; the user creates the file when they are ready.

**If source material contains product-code-shaped content** (a brand book describing colors and typography, a tech spec describing module structure), the generator surfaces this in the output summary as "your tokens/components/etc. are not yet scaffolded — the source material had relevant content; consider a follow-up skill or hand-bootstrap." The generator does not improvise the file because the source material implied it.

This rule is non-negotiable. The validation run on `the-council` and on the `epost-assessment` retrospective both surfaced violations where the agent improvised product code from source material. Any deviation requires user-explicit instruction ("yes, write the tokens file") and even then should be a separate session, not folded into context scaffolding.

## After writing

After all files are written, hand off to `output-summary.md` for the post-generation report.
