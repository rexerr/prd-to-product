# Generator decisions

The mapping logic from intake answers to template choices, file outputs, and substitutions. Read this after `intake.md` has produced a complete answer set, before writing files.

## State map (from intake)

The generator should hold answers in a state map with these keys:

| Key | Source question | Type | Notes |
|---|---|---|---|
| `project_name` | Q1 | string | |
| `project_description` | Q2 | string (paragraph) | |
| `repo_local_path` | Q3 | absolute path | |
| `github_repo_url` | Q4 | URL | |
| `visual_confirmer_name` | Q5 | string | Default: user's first name. |
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

`<!-- KEEP AS-IS: <reason> -->` markers do not require substitution and should not be removed. They are documentation for the user that the line they precede is intentionally fixed (e.g., the "Vercel + Next.js" line in AGENTS.md).

## Recency safeguard renumbering rule

The recency safeguard block in `AGENTS.md.template` and the equivalent in `claude-rules-flat-CLAUDE.md.template` carries items 1–5 always present and items 6 (AI), 7 (vocabulary) conditional.

Conditions:

- Item 6 (AI client-component constraint) included if `ai_surface_count >= 1`.
- Item 7 (vocabulary lock) included if vocabulary lock applies (any of `canonical_vocabulary_list` is non-empty).

When optional items are skipped, renumber the remaining items so the list is contiguous (1, 2, 3, 4, 5 — not 1, 2, 3, 4, 5, 7).

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
