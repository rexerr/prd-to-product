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
| `autonomy_gate_override` | Q27b | string | Non-default human-gate boundary for the "Autonomy — run to done" section. Usually empty (the section renders from `uses_visual_confirmation_gate` + `visual_confirmer_name`). Set only when the user names an exception to the default gated-surface split. |
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
| `include_decisions_active` | Q23 | bool | |
| `backlog_include_v2` | Q24 | bool | Default false. Gates the optional `Later / V2` section in `BACKLOG.md`. Mid-session deferrals are not gated — they always have a home in BACKLOG's In progress / Backlog sections. |
| `codex_usage` | Q25 | enum | `regular`, `occasional`, `none`. |
| `canonical_workflow_doc_name` | Q26 | string or null | |
| `include_product_rules` | Q27 | bool | |
| `artifact_skills_list` | Q24a | list of enum | Subset of `{llm-council, brainstorms}` the project will run regularly. Drives `docs/README.md`'s opt-in rows and the routing rule's `artifact_routing_block`. Empty → no artifact rows/block. `retros/` is **not** in this list (it is always-on, unconditional). |
| `artifact_routing_lines` | derived | string (markdown block) | Built from `artifact_skills_list`: one bullet per opted-in skill (`- \`<skill>\` → \`docs/<folder>/\` (name: <pattern>)`). See "Doc-routing pre-seed" below. Empty when `artifact_skills_list` is empty (the `artifact_routing_block` OPTIONAL gate drops it). |
| `include_synthesis_rule` | Q35a | bool | Default false. Gates the modular-only `synthesis-even-coverage.md` rule. Only asked when `rule_shape == "modular"` (Cluster 6, after rule-shape determination). |
| `workflows` | Q30 | list of `{name, description}` | |
| `phase_user_name`, `phase_user_goal`, `phase_user_task_placeholder`, `phase_user_done_when` | Q31 | strings | The user's first chunk of real work. Composed into `board_seed_rows` (see "Board seeding" below), not template phase parameters. |
| (all other content fills) | Q28–Q35 | strings | Used as direct substitutions. |

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

When `deploy_target_has_cli_conflict == true`, the flat-AGENTS template's "Code rules" emits a "Never use the <deploy_cli_name> CLI" line, and the recency block's primary-constraints anchor (item 3) appends "No <deploy_cli_name> CLI." When false, both are suppressed.

`stack_summary_one_line` is built from stack + deploy_target. Examples:

| `stack` | `deploy_target` | `stack_summary_one_line` |
|---|---|---|
| `nextjs` | `vercel` | `Next.js (App Router) on Vercel` |
| `nextjs` | `netlify` | `Next.js (App Router) on Netlify` |
| `react-vite` | `cloudflare` | `React + Vite on Cloudflare Pages` |
| `node-cli` | `fly` | `Node CLI on Fly.io` |
| `python` | `manual` | `Python (deployed manually)` |

## Board seeding (`board_seed_rows` + `backlog_tags_block`)

The kanban `BACKLOG.md.template` carries two `<!-- PARAMETERIZE -->` markers the generator **composes from the intake answers** — the same way it fills PRD/ARCHITECTURE content, *not* from a fixed stack table. The board is the project's actual near-term work, tagged with the project's actual subsystems; `stack`/`deploy_target` supply only a small generic base, everything else is read from the user's answers (workflows, data flow, folder structure, phase tasks, out-of-scope list). *Failure it prevents:* a generic stack table can't name a project's real surfaces (a contact form's `form`/`api`/`email`), so the seeded board would be inert boilerplate the user must rewrite.

Implements the "Smallest deployable first" opinion from [`docs/build-defaults-brief.md`](../../../docs/build-defaults-brief.md) item 1: when a deploy target exists, the first seeded row ships a deployable production shell before feature work — catching production-environment surprises (env loading, build step, framework adapter, CDN config) on day one rather than month six. The user edits any seeded row after generation; the board is the default starting point, not a lock.

### `backlog_tags_block`

Emit the vocabulary comment in this exact shape (the render tool validates rows against it; the axis lines read `axis:  <prose> — value · value · …`):

```
<!-- TAGS · max 2 per row · two axes only — the render validates rows against this list:
gate:  what must happen before it moves — <gate values>
area:  which part of the system — <area values>
-->
```

- **`gate:` axis (generic).** Always `needs-decision · blocked-on-<dep> · review`. Append `visual-confirm` **iff `uses_visual_confirmation_gate == true`** (the "generic-vs-visual-confirm" logic). No other gate values.
- **`area:` axis (project-derived).** The project's own subsystems, read from `main_workflow_steps`, `primary_data_flow_steps`, `folder_structure_summary`, and `external_integrations_list_or_none`. Always include `infra` (deploy / tooling / CI) and `docs`. Include `api` when the project exposes a server surface (`stack_has_client_server_split == true`, or a backend/CLI with routes). Keep it to ~4–6 short, lowercase, single-word values — starter values the user edits. *Example (contact form with a `/contact` page, a `/api/contact` route, Resend email): `form · api · email · infra · docs`.*

### `board_seed_rows`

Compose the table body — one row per concrete near-term unit — in `Seq` order within the `next` lane. Each row is `Item · Type · Lane · Seq · Tags · Gloss · Refs`; `Refs` points to `docs/PRD.md` (the seed source). The `Gloss` is one plain-English line; operational detail stays in the PRD. Tags obey the `area:`/`gate:` vocabulary above (max 2).

1. **Deploy-shell row** — emit **only when `deploy_target != "none"`**, as `Seq` 1: Item `Ship deployable shell to <deploy_target_name>`, Type `chore`, Lane `next`, Tag `area:infra`. `Gloss` = one line compressing the deploy steps + the day-one rationale, per `deploy_target` (gist table below). For a UI stack (`stack_has_ui == true`) the gloss ends "…the URL serves an `<h1>`"; for a non-UI stack, "…a root/health route returns the project name."
2. **User's first work** — from Q31 (`phase_user_*`). Split `phase_user_task_placeholder` into one row per discrete task (a "deploy" sub-task folds into the deploy-shell row above, not its own row), `Seq` continuing 2, 3, …, Type `feature` (or `chore`/`fix` as fits), Lane `next`. Tag each with its `area:`, plus `gate:visual-confirm` when it touches UI and the visual gate is on. `Gloss` = the task in one plain line.
3. **Deferred items** — from `out_of_scope_list` / `deferred_capabilities_list_or_none`, only those that are genuine *future* work (not hard exclusions): emit as `icebox` rows, `Seq —`, tagged by `area:`, gloss naming what would un-park them.

**Deploy-step gist for the shell-row gloss** (compressed, per `deploy_target`):

| `deploy_target` | Gloss gist |
|---|---|
| `vercel` / `netlify` | Push to GitHub, connect <deploy_target_name>, confirm auto-deploy fires on push, and the URL serves the project name. |
| `cloudflare` | Push to GitHub, connect Pages (or `wrangler deploy` for Workers), confirm the `*.pages.dev` / `*.workers.dev` URL serves it. |
| `fly` | `fly launch` then `fly deploy`; confirm the `*.fly.dev` URL responds with the project name. |
| `railway` | Connect the repo / `railway up`; confirm the generated URL responds. |
| `manual` | Document the deploy command in Commands, run it once, record the production URL. |

## Server-only AI call rule (conditional)

The `ai-shared.md` rule template carries a "never call AI from a client component" rule. This is only meaningful when `stack_has_client_server_split == true`. For `node-cli` and `python` stacks, suppress the rule (or replace with a stack-appropriate analogue if the project has one — e.g., "AI keys never in user-facing config" for a CLI). When suppressed, also suppress the corresponding recency-block item.

## Even-coverage synthesis rule (conditional)

The `synthesis-even-coverage.md` rule guards multi-source synthesis against primacy/recency bias (over-weighting first/last sources, fabricating a pattern only a few support). It is **modular-only and off by default**, gated `rule_shape == "modular" and include_synthesis_rule`. It is **always-on when emitted** — no `paths:` frontmatter, like `git-and-deploy.md` and `session-discipline.md`; it is therefore **not** part of `path_scoped_rule_list`.

Its intake question (**Q35a**) lives in **Cluster 6, after rule-shape determination**, framed as the modular-only mirror of the flat-only Q34/Q35. It cannot live in Cluster 5: `rule_shape` is not computable there because one of its triggers (`len(workflows) > 1`) depends on workflow capture at Q30 (Cluster 6). A flat project is never asked Q35a — consistent with the modular-only emission gate, so there is no flat answer-but-no-landing dead-end. The failure it prevents: a project that routinely synthesizes N sources silently under-covering the middle inputs.

## Doc-routing pre-seed (the "Where new docs go" rule + the `docs/README.md` map)

The generator installs a **doc-routing convention** so a scaffolded project starts tidy instead of sprawling, and so artifact-emitting skills (council, brainstorm, deep-research) land their output well on run #1 instead of dumping at the repo root. Three pieces:

1. **The routing rule** — a `## Where new docs go` section, **unconditional in both shapes** (it is not gated on any answer): inline in `claude-rules-flat-AGENTS.md.template` and in `claude-rules-modular/session-discipline.md.template` (always-on rule), with **identical** prose. It names the root anchors and routes every other doc to a typed subfolder by name, lazily created on first write. It cites the root-sprawl failure mode (per "every rule cites its failure mode").

2. **The `docs/README.md` map** — emitted **always** (inclusion table), a human-facing index (doc type → folder → one-line why). It cross-references the routing rule as canonical; it does **not** restate the routing logic (DRY). The map and the rule use **one canonical folder set** and may not diverge.

3. **The artifact-skill opt-in** — intake **Q24a** captures `artifact_skills_list`. For each opted-in skill, build a **filename-pattern deference line** into `artifact_routing_lines` (substituted as a multi-line markdown block, like `architecture_rules_numbered_list` — **not** the inline `path_scoped_rule_list`). The `<!-- OPTIONAL: artifact_routing_block -->` gate (true when `len(artifact_skills_list) > 0`) shows these lines in the rule; matching opt-in rows render in the map. **Pre-seed = the steering line only; never an empty folder or `.gitkeep`** — the folder materializes when the skill first writes.

**Canonical portable folder set** (identical in rule and map):

| Type | Folder | Always or opt-in |
|---|---|---|
| `*-brief.md` | `docs/briefs/` | always (rule lists it; folder lazy) |
| `*-handoff.md` | `docs/handoffs/` | always |
| `*-reference.md` / domain notes | `docs/reference/` | always |
| research output (e.g. `deep-research`) | `docs/research/` | always (rides the rule — **no** opt-in checkbox) |
| dated retros | `docs/retros/` | always (folder pre-seeded with its README — the one folder that ships content) |
| audits | `docs/audits/` | always |
| `llm-council` output | `docs/council/` | opt-in via Q24a |
| `brainstorm` output | `docs/brainstorms/` | opt-in via Q24a |

**Root anchors:** `PRD.md`, `ARCHITECTURE.md`, `DECISIONS.md`, and `DECISIONS_ACTIVE.md` **only when `include_decisions_active == true`** — gated by `decisions_active_anchor` (inline compressed form in the rule; a gated table row in the map). A Q23=No project must not name a `DECISIONS_ACTIVE.md` it never emitted.

**Repo-specific types are NOT scaffolded.** `cribs/` and `product-briefs/` are idiosyncratic to the meta-repo that hosts this skill; shipping them into every generated project seeds unused-convention noise — the exact sprawl this rule fights. They are deliberately absent from both the rule and the map.

**Scope boundary:** this installs the *project's* convention (its context files declare landing zones). It does **not** edit the global council/brainstorm/deep-research skills — they write to their generic default and defer to a project convention if one exists. At build, read each opted-in skill's actual default output naming for the deference line; **if a skill is unreachable, emit the folder route only (`<skill> → docs/<folder>/`), never an invented filename pattern.**

## Redundancy guards

The paper's redundancy finding (LLM context files improve by 2.7% when README is removed) means the practical risk is overlap inside our own outputs. PRD.md, ARCHITECTURE.md, and CLAUDE.md should not all describe the project.

- **PRD redundancy guard.** When `source_prd_present == true` *or* the generator is producing `docs/PRD.md`, "What this project is" takes one of three shapes based on `len(workflows)`. In all three the `project_description_pointer` block replaces the `project_description_section` block, and `project_tagline_one_line` (Q2a) is asked.
  - `len(workflows) <= 1`: pointer-only. One-line tagline + `See docs/PRD.md`. Suppress `workflows_list`. (Flat shape lands here by construction — flat projects have 0–1 workflows.)
  - `2 <= len(workflows) <= 5`: pointer-plus-workflows — the orientation shape. Tagline + `See docs/PRD.md` + the workflow bullet list. This is the shape `the-council` arrived at by hand (audit 2026-05-10); workflows are concrete enough to earn their tokens at session start, the paragraph is the actual redundancy.
  - `len(workflows) >= 6`: pointer-only, list lives in PRD only. Past five bullets the list defeats the compact-pointer goal and belongs in PRD. Suppress `workflows_list`.

  Reason: the paper's 2.7% finding targets duplicated prose descriptions. A bulleted workflow list is structurally distinct from a narrative paragraph — an orientation index, not a duplicate — and is cheap to keep at AGENTS-level when there are 2–5 named flows. When `source_prd_present == false` and PRD.md is not being generated, fall back to the inline `project_description_section` paragraph; `workflows_list` still gates on `len(workflows) > 1` per the existing template comment.
- **Architecture pointer guard.** When `docs/ARCHITECTURE.md` is being generated, the flat AGENTS template's "Architecture rules (non-negotiable)" stays (those are behavioral rules, not layout description), but any prose paragraph that restates the layout, folder structure, or data model is dropped. The flat template does not currently include such prose; this guard is documented here so future template edits do not introduce duplication.
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

- `AGENTS.md` from `claude-rules-flat-AGENTS.md.template`. This is canonical and carries all rules inline, plus a Codex-specific section when `uses_visual_confirmation_gate == true`.
- `CLAUDE.md` from `claude-rules-flat-CLAUDE.md.template`. One line: `@AGENTS.md`.

Do not write the modular-shape `AGENTS.md.template` or `CLAUDE.md.template` when rule_shape is flat. The pairing is not obvious from the templates alone; this rule is what binds them. **Both shapes are AGENTS-canonical** (CLAUDE.md is always the `@AGENTS.md` pointer); flat and modular differ only in whether the rules live inline (flat) or under `.claude/rules/` (modular).

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
| `claude-rules-modular/synthesis-even-coverage.md.template` | `rule_shape == "modular" and include_synthesis_rule` | `.claude/rules/synthesis-even-coverage.md` |
| `docs/PRD.md.template` | always | `docs/PRD.md` |
| `docs/ARCHITECTURE.md.template` | always | `docs/ARCHITECTURE.md` |
| `docs/BACKLOG.md.template` | always | `BACKLOG.md` (root) — the single work-tracking surface (build plan + in-progress + backlog + open decisions + done). Optional `Later / V2` section gated on `backlog_include_v2`. |
| `docs/DECISIONS.md.template` | always | `docs/DECISIONS.md` |
| `docs/DECISIONS_ACTIVE.md.template` | `include_decisions_active` | `docs/DECISIONS_ACTIVE.md` |
| `docs/retros/README.md.template` | always | `docs/retros/README.md` |
| `docs/README.md.template` | always | `docs/README.md` (the doc-routing map — see "Doc-routing pre-seed" below) |
| `claude-commands/session-start.md.template` | always | `.claude/commands/session-start.md` |
| `claude-commands/end-session.md.template` | always | `.claude/commands/end-session.md` |
| `claude-scripts/render-backlog-kanban.py.template` | always | `.claude/scripts/render-backlog-kanban.py` (chmod +x) — generic kanban renderer for `BACKLOG.md`. Ships always: the board ships always, so does its view tool. Emitted under `.claude/scripts/` (inside the allowlist, same category as the `.sh` hooks under `.claude/hooks/`), **not** `scripts/` (off-allowlist). Trigger precedent: the `always` command rows above; `chmod +x` mechanics: the hook rows below. |
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

`<!-- OPTIONAL: <key> -->` markers gate the line or block immediately following. Each marker has a condition expressed in the comment (e.g., `include if backlog_include_v2 == true`).

Behavior:

- If the condition is true: keep the marker line itself removed from output, keep the gated block as-is.
- If the condition is false: drop the marker line **and** the gated block (the next line, or the next contiguous block ending at a blank line, depending on context).

Some markers gate inline cells in tables (e.g., `<!-- OPTIONAL: ux_row -->` in the flat AGENTS "Where to look" table). For those, drop the entire row when the condition is false.

### Inline compressed OPTIONAL form (content inside the marker)

A fourth form handles **mid-sentence conditional text** — a substring that must appear or vanish without the open/close span or next-line behaviors above reaching it. The content to conditionally insert lives **inside** the marker body:

`<!-- OPTIONAL: <key> — include if <cond>; inline content: <text> -->`

Behavior:

- **Condition true:** replace the entire marker with `<text>` (the part after `inline content:`), trimmed of its leading/trailing space.
- **Condition false:** drop the entire marker, emitting nothing in its place.

The surrounding line is otherwise untouched, so punctuation must be authored to read correctly in **both** states. Precedent: the bare-content form already in use at `claude-rules-flat-AGENTS.md.template` "Where to look" (`… this file, <!-- OPTIONAL: \`docs/DECISIONS_ACTIVE.md\`, --> the most recent …`), where the inserted text carries its own trailing comma. The labeled `inline content:` variant is the same mechanism made explicit. Used by `decisions_active_anchor` in the "Where new docs go" routing rule (both shapes): author the `DECISIONS.md` list item so it ends with a period when the gated `, \`DECISIONS_ACTIVE.md\`` is dropped and reads as a clean two-item list when kept. **Failure it prevents:** a template relying on an undocumented drop behavior — a stray `<!-- /OPTIONAL -->` leaking into output or mangled mid-sentence punctuation.

### session-start AGENTS.md read is unconditional

`claude-commands/session-start.md.template` reads `AGENTS.md` as step 1 in **both** shapes. AGENTS.md is canonical in flat and modular alike (CLAUDE.md is just `@AGENTS.md`), so the explicit orientation read is always worthwhile. No `rule_shape` gating applies — keep the step as written, do not drop or renumber it.

> Historical note: flat shape used to drop this read because flat was CLAUDE-canonical and AGENTS.md was a thin pointer. The flat shape is now AGENTS-canonical (matching modular), so that exception is gone.

### KEEP AS-IS

`<!-- KEEP AS-IS: <reason> -->` markers do not require substitution and should not be removed. They are documentation for the user that the line they precede is intentionally fixed.

## Generated-file provenance banner

Every file the generator emits leads with a one-line **provenance banner** so a reader or agent knows the file was scaffolded — and that it is safe to hand-edit. *Failure it prevents:* a human or agent hand-edits (or reasons about) a generated file in ignorance of its provenance. This is **not** clobber-safety — the non-destructive write guard already owns that — so the wording is deliberately **"safe to hand-edit," not "do not edit."**

**Canonical text** (one wording; only the comment syntax varies by format):

> Generated by the context-engineering skill — safe to hand-edit. Re-running the skill regenerates the scaffold shape and asks before overwriting your changes.

**Per-format syntax and placement:**

| Emitted format | Comment syntax | Banner position |
|---|---|---|
| Markdown `.md`, no frontmatter | `<!-- … -->` | First line, before the H1 / `@import`. |
| Markdown `.md` with YAML frontmatter (path-scoped rules; slash commands carry a `description`) | `<!-- … -->` | The line **directly after the closing `---`** (no blank between), then a blank line, then the H1 or body. A comment *before* `---` breaks frontmatter parsing. |
| Shell `.sh` | two `# …` lines | After the `#!/usr/bin/env bash` shebang, before the `# Hook:`/`# Reason:` lines. |
| Python `.py` | two `# …` lines | After the `#!/usr/bin/env python3` shebang, before the module docstring. Carries no authoring block (like the shell hooks), so the strip step is a no-op and the banner is emitted verbatim from template source. |
| TOML `.codex/config.toml` | two `# …` lines | First emitted lines (replaces the stripped authoring block as the top). |
| JSON `.claude/settings.json` | n/a — JSON has no comments | Carried by the existing top `"//"` documentation key; **no separate banner**. |

**Strip-vs-banner discriminator (the load-bearing rule — do not confuse the two top-of-file comments).** Every template carries an **authoring-metadata block** that is template-only and **stripped at emit**: `<!-- Template: … -->` in markdown (body has `Template:` / `Purpose:` / `Related principles:` / `Use this template when:` lines) and the equivalent `# Template:`/`# Purpose:`/… block in `codex-config.toml.template`. The provenance banner is a *separate* comment that is **emitted verbatim**. Tell them apart **by text, not position**:

- **(a) Banner** — body begins `Generated by the context-engineering skill`. **Keep; emit verbatim.**
- **(b) Authoring block** — body carries `Template:` / `Purpose:` / `Use this template when:`. **Strip; never emit.**
- **(c) Source ordering** — in template source the banner is placed **immediately after the authoring block** (for frontmatter, after the closing `---` + block; for shell, after the shebang; for TOML, after the `# Template:` block), so stripping the block leaves the banner as the leading line of the emitted body — no positional guessing.
- **(c′) Blank-line consumption (frontmatter only)** — a frontmatter template separates the authoring block from the closing `---` by one blank line; the strip **consumes that blank along with the block**, so the emit is `---` then banner with no blank between (matching the placement table). Plain-markdown templates have the block at line 1 with no leading blank, so this clause does not apply to them.

**Templates without an authoring block.** Not every template has one. The shell hooks (`block-*.sh.template`) and `claude-hooks/README.md.template` carry no `Template:`/`Purpose:` block — so for them the strip step is a **no-op**: the banner is simply prepended (markdown → line 1; shell → line 2, after the shebang) and **all existing content is kept**. In particular a shell hook's `# Hook:` / `# Reason:` comments are *functional content*, not an authoring block (they lack the `Template:`/`Purpose:` text rule (b) keys on), so they are never stripped.

This section also documents, for the first time, that the authoring-metadata block is **stripped at emit** — previously done by inference, now load-bearing because a banner comment sits adjacent to it.

## Hooks enforcement (parallel to prose rules)

When `enforce_rules_as_hooks == true`, the generator emits `.claude/settings.json` and supporting scripts under `.claude/hooks/`. The rationale is the AGENTS.md study finding that prose rules are interpreted as guidelines; for load-bearing constraints, the right enforcement layer is a hook from the harness, not a sentence in CLAUDE.md.

Hooks emitted:

| Hook script | Always or conditional | The script blocks |
|---|---|---|
| `block-env-commit.sh` | Always (when `enforce_rules_as_hooks == true`) | `git add/stage … .env*` at command-word position — prevents staging env files. |
| `block-deploy-cli.sh` | When `deploy_target_has_cli_conflict == true` | `<deploy_cli_lower> …` / `npx <deploy_cli_lower> …` at command-word position — prevents deploy-CLI usage that conflicts with auto-deploy. |
| `block-worktree.sh` | When `uses_visual_confirmation_gate == true` | `git worktree …` commands (Bash matcher) and the `EnterWorktree` tool (own matcher) — prevents worktree creation that would break visual confirmation. |

The hooks coexist with the prose rules in CLAUDE.md/AGENTS.md. The prose explains *why*; the hook guarantees *that*. Removing one without the other breaks either orientation or enforcement. The prose rules are not removed when hooks are emitted.

### Scoping is script-side; the `if` filter is not used (decided 2026-06-12)

Every hook entry uses a bare tool matcher (`"Bash"`, `"EnterWorktree"`); the script reads the stdin JSON payload and decides. Two decisions recorded here:

1. **The documented inner `if` filter is dropped.** The original templates scoped unconditional `exit 2` scripts with `if` (e.g. `"if": "Bash(git add .env*)"`). The field is officially documented and usually works (verified by negative-case live-fire, 2026-06-12), but it was twice observed letting the hook run on non-matching complex compound commands (2026-06-08: `git rev-list … && ls …`; 2026-06-12: a multi-heredoc fixture command). The 2026-05-10 validation missed this because it tested positive cases only. Since the script must therefore scope itself anyway, keeping `if` adds only a drift hazard: a stale `if` after a script-pattern change **silently disarms the guard** (fail-open) — the worst failure mode for a blocking hook. With unconditional scripts the original defect's true severity was total-Bash-blockage in any project emitting the conditional hooks (observed: the-council).
2. **Command matching is jq-extraction with raw-payload fallback, anchored at command-word position.** `jq -r '.tool_input.command // empty'` when jq exists; raw payload otherwise (coarser, but a blocking guard must never disarm because a dependency is missing). Matching anchors at line start or after `|` `&` `;` so prose/data merely *mentioning* a pattern doesn't block — chosen over raw-payload word-boundary grep after a live false positive (2026-06-12: a command embedding `git add .env*` as JSON data was blocked). Deliberate trade-offs, documented in each script: subshell-wrapped invocations `(git add .env)` are not caught (`(` is not an anchor, to let embedded `Bash(git add .env*)` strings pass); a heredoc/data line *beginning* with a guarded command still matches (fails toward blocking).

### Seeded `permissions.allow`

`settings.json` also carries a seeded `permissions.allow` allowlist (read-only inspection commands + the project's `check_cmd`/`build_cmd`). Rationale: cut permission prompts for safe commands the agent runs constantly, without granting write/commit/push (those stay under the Autonomy charter and any commit-blocking hooks). Real-project evidence: qventus grew a hand-written `settings.local.json` allowlist (`git rev-list`, `git ls-remote`) because the scaffold seeded none (post-mortem 2026-06-08).

- The universal read-only core is always emitted: `git status/diff/log/show/branch/rev-parse`, `grep`, `rg`, `find`, `ls`, `cat`, `date`.
- The two command entries (`Bash(<check_cmd>:*)`, `Bash(<build_cmd>:*)`) are emitted only when those commands exist; **drop any whose value resolved to `none`/`not configured`** (e.g. this repo and other no-build projects get the core only).
- **Emit even when `enforce_rules_as_hooks == false`:** in that case still write a `settings.json` containing only the `permissions` block (no `hooks`). The allowlist is independent of hook enforcement.
- Grow the list per project with the `fewer-permission-prompts` skill; the seed is a floor, not a ceiling.

Scripts must be `chmod +x` after writing. The generator handles this as part of file emission; users adding new hooks manually must remember to do it themselves.

## JSON-aware substitution

`claude-settings.json.template` carries `<!-- PARAMETERIZE: -->` markers and `"//OPTIONAL"` keys, but the file itself is JSON, not Markdown. The substitution rules are slightly different:

- `<!-- PARAMETERIZE: <key> -->` inside JSON string values: replace as normal (the marker syntax inside a string does not break JSON parsing).
- `"//OPTIONAL": "<condition>"` keys: gate the JSON object containing them. If the condition is false, drop the *entire enclosing object* (not just the key). When dropping an object inside an array, also drop the trailing comma if it would create a syntax error.
- `"//"` keys (without `OPTIONAL`): pure documentation. Claude Code ignores keys starting with `//`. Keep them as-is in the output; they are harmless and useful for the user.

After substitution, the generator must validate the output is parseable JSON. If validation fails, the generator reports the file path and the parse error and stops; do not emit a syntactically broken `settings.json`.

## Recency safeguard renumbering rule

The recency safeguard block in `AGENTS.md.template` (modular) and the equivalent in `claude-rules-flat-AGENTS.md.template` (flat) carries item 1 always present and items 2 (visual confirmation), 3 (AI), 4 (vocabulary) conditional.

Always-on item:

1. **Hard scope limits.** Bug fix: ≤ 3 files, ≤ 50 lines. Feature: ≤ 300 lines per session.

Conditions for optional items:

- Item 2 (visual confirmation gates the commit) included if `uses_visual_confirmation_gate == true`. Suppressed for no-UI projects (`node-cli`, `python`, `other` without UI). Same gate also drops the visual-confirmation line from "Primary constraints (read before doing anything)" near the top, the "Commit gate" body section, the "UI changes" bullet under "Verification before claiming done", and the "No worktrees" suffix in primary-constraints item 3.
- Item 3 (AI client-component constraint) included if `ai_surface_count >= 1` *and* `stack_has_client_server_split == true`. Suppressed for `node-cli` and `python` stacks even if AI surfaces exist.
- Item 4 (vocabulary lock) included if vocabulary lock applies (any of `canonical_vocabulary_list` is non-empty).

When optional items are skipped, renumber the remaining items so the list is contiguous (1 — not 1, 2; or 1, 2 — not 1, 3).

## No-UI project handling

When `uses_visual_confirmation_gate == false`, the following content is dropped from the flat-AGENTS template (the rule-carrying canonical file), the modular AGENTS template, the modular session-discipline template, and the flat-AGENTS Codex-specific section:

- Primary-constraints item 2 ("Visual confirmation gates the commit") — both templates.
- The "No worktrees." suffix on primary-constraints item 3 — both templates.
- Recency-block item 2 — both templates.
- Body "Commit gate" section — flat AGENTS and modular session-discipline.
- "UI changes" bullet under "Verification before claiming done" — flat AGENTS and modular session-discipline.
- The Codex-specific section in flat-AGENTS.md.template (the entire section is the visual-confirmation override).
- The worktree-restriction code rule (already gated by the same flag — confirm it stays gated).
- The block-worktree.sh hook and its two `settings.json` entries (already gated).

When `deploy_target == "none"`, the push-protocol body bullet drops the "waiting for `<deploy_target_name>` deploy" wording and the production-confirmation requirement; the user still pastes the commit URL but the agent declares done after the push.

The block is intentionally short. Items previously in the block (direct-on-main, no deploy CLI, reproduce-before-fixing) live in the body of the template and are not duplicated in the recency block. The principle: items belong in the recency block only if violating them damages product, loses work, or burns a stakeholder, and only if duplicating them genuinely changes agent behavior under attention pressure.

## Path-scoped rule list (AGENTS.md "Path-scoped rules" section)

The `path_scoped_rule_list` parameter is derived from the per-template inclusion decisions, not asked of the user. Build the list from the rule files actually emitted.

For example, if the modular set includes `voice-and-tone.md`, `design-system.md`, `ai-shared.md`, and `ai-feed-enrichment.md`, the value is:

> `voice-and-tone.md`, `design-system.md`, `ai-shared.md`, `ai-feed-enrichment.md`.

If only one is included, the value is just that one filename. If none are included, the entire "Path-scoped rules" sentence in AGENTS.md is omitted via the OPTIONAL marker that gates it.

## UX row content for the flat AGENTS template

The `ux_row_doc_names` parameter is only relevant when `rule_shape == "flat"` and the project has UX or styling docs. If `design_shape == "none"`, drop the row entirely (the `<!-- OPTIONAL: ux_row -->` marker handles this). If `design_shape == "basic_styling"` and the user named UX or styling docs, fill with those doc paths in the format `\`docs/UX_HEURISTICS.md\` (canonical), \`docs/UI_SYSTEM.md\` (styling)` or whatever the project actually has.

## PRD-driven generation behaviors

When `source_prd_present == true`, the generator applies four documented defaults during file generation. These are not improvisation; they are spec.

### PRD-as-tiebreaker fallback

If `canonical_workflow_doc_name` is null and `source_prd_present == true`, mark the PRD as the workflow tiebreaker in two places:

- In `AGENTS.md` "Before writing any code" section, under "Read when relevant," append "**Tiebreaker on conflicts.**" to the `docs/PRD.md` line.
- In `AGENTS.md` "When in doubt" table, the "Product behavior, copy" row reads `docs/PRD.md` (canonical, tiebreaker)`.

If a `canonical_workflow_doc_name` is named, it owns the tiebreaker role and the PRD does not.

### V2/V3 extraction from PRD into the BACKLOG `Later / V2` section

If `source_prd_present == true` and `backlog_include_v2 == true`, scan the PRD for sections named `## V2`, `## V3`, `## Future`, `## Deferred capabilities`, `## Roadmap V2`, or similar. Lift the items as one-line entries into the `Later / V2` section of `BACKLOG.md` (the optional section gated on `backlog_include_v2`).

If `backlog_include_v2 == false` but the PRD has a deferred-capabilities section, leave the items in the PRD's "Deferred capabilities" subsection (which `PRD.md.template` already provides for via `deferred_capabilities_list_or_none`); they reach the backlog only as a Backlog entry if and when one becomes real.

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

## Non-destructive write guard

Before writing any file in the inclusion table, check whether the target path already exists on disk.

- **Does not exist** → write normally.
- **Exists and is a recognizable unfilled scaffold** (contains an unresolved `<!-- PARAMETERIZE:` or `<!-- OPTIONAL:` marker) → safe to overwrite after a one-line confirm; don't make the user diff a never-customized scaffold.
- **Exists and differs** → **do not overwrite.** Show a diff against the existing file, state it already exists, and ask **overwrite / skip**. **Default to skip.** These are whole-file scaffold artifacts (AGENTS.md, CLAUDE.md, rules, docs, commands, settings) with no merge operation — do not offer merge. Never overwrite hand-authored work without explicit consent.

Report skipped/overwritten files in the post-generation summary with the standard markers `(skipped — already exists; not overwritten)` and `(overwritten with consent)`. Because generation is non-deterministic, a re-run sees most prior files as "differs" and prompts (default skip) on each — expected; the guard prioritizes never-clobber over silent re-runs.

**Enforced (D-005).** This guard is now backed by the global `write-guard.sh` PreToolUse hook ([`hooks/README.md`](../../../hooks/README.md)) when installed and this run is armed. (`enforce_rules_as_hooks` emits hooks *into the scaffolded project*; this is a separate hook that guards the **generator's own writes**.) A write to a file that **existed before this run** is gated — interactive → a non-forgeable permission dialog (`ask`), headless → auto-skip (`deny`, never clobbers/hangs). Files this run *creates* are auto-tracked as run-owned and stay editable. Still honor the prose: the hook may be absent or bypassed, and does nothing unless this run armed it. The field-society-demo run caught a `PRD.md` collision this way — this section makes that behavior systematic rather than ad hoc.

**Arm at run start (before writing any file), disarm at run end** — via Bash, so it bypasses the guard's own `Write|Edit` matcher:

```bash
# run start
mkdir -p ~/.claude/state/write-guard
: > ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel
# run end
rm -f ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel \
      ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".owned
```

Where the hook isn't installed this is a harmless no-op. A forgotten arm = no enforcement for that run (the prose is the backstop); a forgotten disarm is harmless.

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
- Any file outside `.claude/`, `.codex/`, `.agents/`, `docs/`, `AGENTS.md`, `CLAUDE.md`, `BACKLOG.md`.

**Treat the list above as an allowlist and assert against it before every `Write` — do not rely on remembering the ban.** For each file the generator is about to write, check the literal target path: it must sit under `.claude/`, `.codex/`, `.agents/`, or `docs/`, or be one of `AGENTS.md` / `CLAUDE.md` / `BACKLOG.md`. If the target is off the allowlist, refuse the write and surface it in the output summary ("source material implied `<path>` — not scaffolded; consider a follow-up skill or hand-bootstrap") rather than improvising the file. Test the path mechanically; do not reason about whether a path "feels like" product code — the allowlist is the test. This is distinct from the D-005/D-006 write guard, which gates writes to *pre-existing* files; the allowlist catches *net-new* product-code paths the generator should never create at all. **Why an assertion, not just the prose ban:** the ban below was in force during the `the-council` and `epost-assessment` runs and the agent improvised product code from source material anyway — an invariant that must be re-applied correctly on every write is fragile, while a path-allowlist check fails objectively on the first off-list target.

**Templates may reference paths to product files** — `design-system.md` rule references the token file path via `<!-- PARAMETERIZE: token_file_path -->`, `ai-shared.md` references the AI client and prompts paths, etc. These references are targets, not commands to create. The path being unresolved at scaffold time is fine; the user creates the file when they are ready.

**The `docs/tickets/` graduation layer is runtime-created, not generator-written.** The scaffolded `BACKLOG.md` ships thin and lean; the session-discipline graduation rule + the `/end-session` retirement ritual tell a project to split it into a thin index + on-demand `docs/tickets/<slug>.md` parts (archived to `docs/tickets/archive/`) *only when it outgrows the session-start read*. The generator never emits a `tickets/` folder at scaffold time — the project creates it at graduation. `docs/tickets/` sits under `docs/`, so the allowlist above already admits it (no amendment). There is no inclusion-table row for it. The ticket-file convention (slug naming, `slug`/`status`/`title` frontmatter, archive + `+1-../` link-depth rules) is carried **inline in the scaffolded `/end-session` ritual** — a graduating project has it without re-running the skill, so there is no separate `tickets/README.md.template` (a template in the skill's `templates/` would be unreachable by the already-scaffolded project).

**If source material contains product-code-shaped content** (a brand book describing colors and typography, a tech spec describing module structure), the generator surfaces this in the output summary as "your tokens/components/etc. are not yet scaffolded — the source material had relevant content; consider a follow-up skill or hand-bootstrap." The generator does not improvise the file because the source material implied it.

This rule is non-negotiable. The validation run on `the-council` and on the `epost-assessment` retrospective both surfaced violations where the agent improvised product code from source material. Any deviation requires user-explicit instruction ("yes, write the tokens file") and even then should be a separate session, not folded into context scaffolding.

## Scaffolding-leak scan before finalizing

Before writing the scaffolded files, run a **mechanical category grep** over the about-to-be-written content for internal interview/generator machinery that must never reach a user's repo. This is deterministic — run the grep and read its output, do not eyeball. It is the independent backstop to the "Internal scaffolding stays internal" prose rule in `principles.md`: the prose prevents the leak being *written*; this grep catches it if the rule is forgotten on any one run. Mirrors the same scan in `prd-creator` ([generator/decisions.md](../../prd-creator/generator/decisions.md)).

**Use category patterns, never a literal word-list** — a literal test re-encodes the blind spot it is meant to catch:

- `grep -niE '[Cc]luster [0-9]'` → expect **zero** (interview-stage machinery).
- `grep -niE 'Q[0-9][a-z]'` → expect **zero** (state-map question labels, e.g. `Q0a`).
- `grep -niE 'state.?map'` → expect **zero** (the generator-state map is internal).
- `grep -niE '<!-- *(PARAMETERIZE|OPTIONAL)|PARAMETERIZE:'` → expect **zero** unsubstituted template markers. Match the **comment-marker form**, never the bare word — "optional" is ordinary English and must not flag.
- `grep -niE 'D-0[0-9]'` → scope **by content region**, not a blanket zero. `D-NNN` is sanctioned deliverable content **inside the project's own decisions-log file** (its `Numbered D-001, D-002, etc.` guidance and, in a mature project, real `### D-001` entries). It is a leak **only outside that file**: a *this-repo* decision ID (`D-010`, `D-063`…) cited as a failure mode in a rule/`AGENTS.md`, or any `D-NNN` narration in prose. (Mirrors prd-creator's "where confirmed IDs are part of the deliverable; never as narration.")

Any hit outside its sanctioned region → fix before writing; do not ship the file with the leak in it.

**Failure it prevents:** internal machinery (`cluster N`, `Q0a` labels, `state map`, unsubstituted `PARAMETERIZE`/`OPTIONAL` markers, or a this-repo `D-NNN` cited as a failure mode) reaching a user's scaffolded files — the [D-010](../../../docs/DECISIONS.md) leak class, mechanically backstopped.

## After writing

After all files are written, hand off to `output-summary.md` for the post-generation report.
