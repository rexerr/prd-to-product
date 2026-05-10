# Generator intake

The question flow Claude runs when the context-engineering skill is invoked. Seven clusters, asked sequentially. Cluster boundaries matter. Do not interleave.

## Question contract

- One cluster at a time. Do not dump every question at once.
- Per call: 2 to 4 options for branching questions; up to 3 questions per call.
- Free-text questions (content fills) ask one at a time and accept open answers.
- Branching questions return a label the generator can match against `decisions.md`.
- After every cluster, summarize what was captured before moving on. The user can correct before the next cluster begins.
- **Source material first.** Cluster 0 captures any existing PRD, decisions, or external skills. When source material is provided, downstream clusters run as confirm-or-correct against extracted answers, not fill-from-scratch.

## Cluster 0: Source material (always — runs before anything else)

The user often arrives with a drafted PRD or other source material. This cluster captures it before the question flow begins, so downstream clusters can extract proposed answers rather than fill from scratch.

**Always ask Q0a explicitly, even if a PRD or other source is already visible in conversation context.** Do not silently absorb material because it appeared earlier. Asking out loud forces the user to confirm intent and tells the user that downstream extraction is about to happen. Silent absorption is the failure mode that makes the user wonder later "did the agent actually use my PRD or guess?"

Ask in one call:

0a. **Existing PRD.** Do you have a drafted PRD for this project? Paste, link, or say "no." (If a PRD is already in context, name it explicitly: "I see a PRD at `<path>` in context — use it as cluster 0 source? Y/N." Wait for an answer. Do not proceed on assumption.)
0b. **Other source material.** Anything else relevant? (Decisions list, V2/V3 ideas, related global skills, design-system reference, brand book, etc. Optional.)

If a PRD is provided:

- Read it before proceeding.
- Extract proposed answers for cluster 1 (project name, description), cluster 2 (AI surfaces if the PRD describes them), cluster 6 (PRD content fills, architecture content, workflows, deferred capabilities, vocabulary lock if listed).
- For each downstream cluster where extraction yielded proposed answers, present them as "I extracted X from your PRD — confirm or correct" rather than asking the question cold.
- For clusters where the PRD has no relevant content (cluster 3 design system, cluster 4 voice and tone, cluster 5 conditional patterns), ask the user normally — these are workflow questions, not product facts.

If no PRD is provided, run all downstream clusters as cold-start fill flows (the original behavior).

State map keys set by cluster 0:

- `source_prd_present` — bool
- `source_prd_content` — string (the PRD text, if pasted)
- `source_other_material` — string (decisions, V2 list, skills, etc.)

## Cluster 1: Project basics (always)

**If PRD provided:** extract `project_name` and `project_description_one_paragraph` from the PRD. Present as "I extracted from your PRD: name=X, description=Y. Confirm or correct." Then ask Q3, Q4, Q5 normally (these are not in PRDs).

**If no PRD:** ask all five questions as cold-start fills.

Ask in one batch:

1. **Project name.** Free text. → `project_name`.
2. **One-paragraph description.** What this project is, who it's for, what it does. → `project_description_one_paragraph`.
3. **Local repo path.** Absolute path on disk. → `repo_local_path`.

Then in a second call:

4. **GitHub repo URL.** Format `https://github.com/<org>/<repo>`. → `github_repo_url`.
5. **Visual confirmer name.** The human who confirms UI changes in a running dev server. Default: the user's first name. → `visual_confirmer_name`.

If `source_prd_present == true`, also extract a one-line tagline from the PRD's first paragraph (or ask if extraction fails):

5a. **Project tagline (one line).** Used when CLAUDE.md/AGENTS.md "What this project is" becomes a pointer to PRD.md. Free text. → `project_tagline_one_line`.

## Cluster 1.5: Stack and commands

This cluster drives the Commands block in AGENTS.md/CLAUDE.md (the paper's strongest empirical positive on context files: tools mentioned in context get used; tools not mentioned almost never do). It also drives stack-conditional rules (server-only AI calls, deploy-CLI restrictions).

Branching first:

5b. **Stack.** Pick the closest:
   - **Next.js** — App Router, Pages Router, or either.
   - **React + Vite** — SPA, no Next.js.
   - **Node CLI** — command-line tool, no UI.
   - **Python** — Python project (data, ML, CLI, or service).
   - **Other** — describe in free text.

→ `stack` enum.

5c. **Deploy target.** Where production runs:
   - **Vercel** — auto-deploy on push to `main`.
   - **Netlify** — auto-deploy on push to `main`.
   - **Cloudflare Pages or Workers** — Wrangler is the standard deploy path.
   - **Fly.io** — Fly CLI is the standard deploy path.
   - **Railway** — Railway CLI or auto-deploy.
   - **Manual** — host varies; user describes.
   - **None** — local-only, no production target.

→ `deploy_target` enum. Drives `deploy_target_has_cli_conflict`, `deploy_cli_name`, `env_pattern` defaults.

After branching, default the commands per stack from the table in `decisions.md`. Show the defaults to the user in one batch and ask "confirm or override":

5d. **Commands.** Confirm or override the inferred defaults:
- `install_cmd` — install dependencies.
- `dev_cmd` — start dev server (or "(none — not a server)" for non-server stacks).
- `check_cmd` — type/lint check.
- `test_cmd` — run tests (or "not configured" if there's no test suite).
- `build_cmd` — production build.

5e. **Env vars pattern.** Confirm or override the deploy-target default. Free text. → `env_pattern`.

5f. **Enforce load-bearing rules as hooks?** (Recommended.)
   - **Yes** — emit `.claude/settings.json` and `.claude/hooks/*.sh` to block load-bearing rule violations at the harness level (deploy CLI, env-file commits, worktree creation when applicable). Prose in CLAUDE.md explains *why*; hooks guarantee *that*. The AGENTS.md study found prose rules get interpreted as guidelines under attention pressure; hooks do not.
   - **No** — keep enforcement to prose only. Choose this if you do not want any harness-level blocking, or if you plan to write your own hooks separately.

→ `enforce_rules_as_hooks` bool. Default `true`.

State map keys set by cluster 1.5:

- `stack` — Q5b
- `deploy_target` — Q5c
- `install_cmd`, `dev_cmd`, `check_cmd`, `test_cmd`, `build_cmd` — Q5d
- `env_pattern` — Q5e
- `enforce_rules_as_hooks` — Q5f

Derived (computed by `decisions.md`, not asked):

- `deploy_target_name`, `deploy_target_has_cli_conflict`, `deploy_cli_name`, `stack_summary_one_line`, `stack_has_client_server_split`.

## Cluster 2: AI surfaces

**If PRD provided:** scan the PRD for AI mentions (model names, prompt files, AI surfaces, agentic patterns). If found, propose surface count and per-surface answers (name, purpose, audience, model). Present as "I found N AI surfaces in your PRD: [list]. Confirm or correct." Then ask the remaining per-surface fills (paths, prompt constants, prompt rules, output schema) as confirm-or-correct against extraction.

**If no PRD:** ask all questions cold.

Branching question first:

6. **AI surfaces.** How many distinct AI surfaces does this project have?
   - 0 — no AI in the product.
   - 1 — one surface (one prompt, one purpose).
   - 2 to 3 — a few surfaces with different audiences or models.
   - 4+ — large AI footprint.

If 0: skip the rest of this cluster.

If 1+: for each surface, free-text:

7. **Surface name** (kebab-case, used in filename `ai-<name>.md`). → `surface_display_name`, `surface_kebab_name`.
8. **Implementation file path.** → `surface_implementation_path`.
9. **API route path.** → `surface_api_route_path`.
10. **System prompt constant name.** Convention: `<SURFACE>_SYSTEM`. → `surface_system_prompt_constant`.
11. **What this surface does** (one paragraph). → `surface_purpose_paragraph`.
12. **Audience.** Internal reviewer, customer-facing, both. → `surface_audience`.
13. **Model choice.** Free text or selection. → `surface_model_choice`.
14. **Prompt rules** (3–5 bullets). → `surface_prompt_rules_list`.
15. **Output schema if any.** → `surface_output_schema_or_none`.

Then once for the project:

16. **Model split table.** All clients, model IDs, and what each is used for. → `model_split_table`, `model_split_rule_1`, `model_split_rule_2`.
17. **AI client file path.** Default `lib/ai/client.js`. → `ai_client_path`.
18. **AI prompts file path.** Default `lib/ai/prompts.js`. → `ai_prompts_path`.

## Cluster 3: Design system and UX

Branching first:

19. **Design system shape.** Pick the closest:
   - **Token system with linter.** Project has a token CSS file (custom properties) and a no-hardcoded-values linter. Examples: `design-system/colors_and_type.css` plus `npm run check:tokens`.
   - **Basic styling.** `globals.css`, maybe `lib/styles.js`. No token file. No linter.
   - **None.** No styling rules to capture.

If "Token system with linter": follow up with token-system fills (typography, motion, icon set, layout rules, indicator vocabulary, button tiers, form rules, things to avoid, three load-bearing one-liners for the AGENTS.md instant-recall block, design heuristics specifics like action ceiling count and Miller-law application).

If "Basic styling": skip the design system rule template. The flat CLAUDE template carries minimal styling rules inline.

If "None": skip both.

20. **Apply design heuristics rule?** Only ask if "Token system with linter" was chosen.
   - Yes — add `design-heuristics.md` with named-law section.
   - No — skip the rule.

## Cluster 4: Voice and tone

Branching:

21. **Voice and tone rule needed?**
   - **Yes.** Project produces user-facing copy, especially AI-generated copy.
   - **No.** Internal-only output, or copy is not a load-bearing concern.

If yes, fill:

- `voice_source_hierarchy`, `brand_position_paragraph`, `primary_brand_line`, `voice_characteristics_list`, `preferred_terms_list`, `forbidden_terms_list`, `positioning_risks_list`, `project_specific_writing_rule`.

If no, skip the voice-and-tone template.

## Cluster 5: Conditional patterns

Six branching questions. Group three per call.

First call:

22. **Include `PARKING_LOT.md`?**
   - Yes (recommended) — surface for mid-session deferrals.
   - No — small project, deferrals fit in retros.
23. **Include `DECISIONS_ACTIVE.md`?**
   - Yes (recommended) — curated subset of binding decisions.
   - No — project is small enough that `DECISIONS.md` alone is fine.
24. **Include `FUTURE.md`?**
   - Yes — project has a clear V2-and-beyond list.
   - No — V2 items live in `ROADMAP.md` for now.

Second call:

25. **Codex used in the workflow?**
   - Yes, regularly — emit `.codex/config.toml` and `.agents/skills/README.md`.
   - Yes, occasionally — emit `.codex/config.toml` only.
   - No — skip both.
26. **Tiebreaker doc.** Does the project have a single canonical doc that decides workflow conflicts (like `CONTENT_SYSTEM.md` in feed)?
   - Yes — name it. → `canonical_workflow_doc_name`.
   - No — the "Where to look" table covers conflicts on its own. **If `source_prd_present == true`, `decisions.md` will mark the PRD as the tiebreaker by default.**
27. **`product-rules.md` always-on rule needed?**
   - Yes — project has product invariants the agent must enforce on every feature decision.
   - No — `PRD.md` alone covers it.

Third call (only if `codex_usage in ("regular", "occasional")`):

27a. **External skills.** Any global skills (in `~/.claude/skills/` or `~/.codex/`) that this project is built on or interacts with? Free text. → `external_skill_references` (list of `{name, path, relationship}`). The generator cross-links these from `.agents/skills/README.md` so future sessions know where to find the related skill.

## Cluster 6: Naming and parameterization

**If PRD provided:** extract proposed answers for as many of Q28–Q35 as the PRD covers. Most PRDs include product summary, target users, core problem, main workflow, out of scope, deferred capabilities. Many include vocabulary (terminology section) and architecture content. Present each cluster-6 fill as "I extracted from your PRD: [content]. Confirm, edit, or replace." Skip extraction for fills the PRD does not cover; ask those normally.

**If the PRD has a `## Decisions` or `## Decisions made` section:** extract decisions as candidates for `DECISIONS.md` seeding. See `decisions.md` "Decisions seeding from PRD" for the per-decision criteria check before any are mirrored to `DECISIONS_ACTIVE.md`.

**If the PRD has a `## V2`, `## Future`, or `## Deferred capabilities` section:** extract for `FUTURE.md` if `include_future == true`.

**If no PRD:** ask all questions cold.

Free-text fills for the docs templates:

28. **PRD content.** `product_summary_paragraph`, `target_users_list`, `core_problem_paragraph`, `main_workflow_steps`, `out_of_scope_list`, `deferred_capabilities_list_or_none`.
29. **Architecture content.** `primary_data_flow_name`, `primary_data_flow_steps`, optional `secondary_flow_name`/`secondary_flow_steps`, `data_persistence_paragraph`, `external_integrations_list_or_none`, `folder_structure_summary`.
30. **Workflow names.** Up to N. → `workflow_<n>_name`, `workflow_<n>_description`.
31. **Roadmap Phase 1.** `phase_1_name`, `phase_1_goal`, `phase_1_task_placeholder`, `phase_1_done_when`.
32. **Stack additions beyond the framework + deploy target captured in cluster 1.5.** Database, jobs runner, AI provider, external integrations. → `additional_stack_summary`.
33. **Vocabulary lock.** Canonical names and forbidden old values, if any. → `canonical_vocabulary_list`, `forbidden_vocabulary_list`, `vocabulary_lock_rule`.
34. **Architecture rules** (only for flat shape). 3–5 numbered architecture rules. → `architecture_rules_numbered_list`.
35. **Product UX rules** (only for flat shape, if applicable). → `product_ux_rules_list`, `critical_invariants`.

## Confirm before writing

After all clusters are answered:

1. Summarize every captured answer in a structured block.
2. Show the file list the generator will produce, derived from `decisions.md` rules applied to the answers.
3. Wait for explicit user confirmation. Phrases that count: "yes", "go", "proceed", "looks good." Anything that asks a clarifying question or proposes a change resets to the relevant cluster.
4. Only after confirmation: produce files.

## Dry-run mode

If the user invokes the skill with a "dry run" flag (e.g., "use the context-engineering skill in dry-run mode"), run all clusters, run the confirmation summary, and stop without writing files. Output the summary as the final message.

## Notes

- Every PARAMETERIZE marker across templates must trace to a question or to a derivation in `decisions.md`. The marker map below is the audit trail.
- Branching questions write the answer into a generator-state map (e.g., `rule_shape`, `include_parking_lot`). `decisions.md` reads from that map to drive template inclusion.

## Marker map

Every PARAMETERIZE marker, its source question (or "derived"), and its cluster.

### Cluster 0: source material

State-map keys only (no PARAMETERIZE markers):

- `source_prd_present` — Q0a (state map)
- `source_prd_content` — Q0a (state map, raw PRD text)
- `source_other_material` — Q0b (state map, optional other source)

These keys gate downstream extraction behavior; they do not substitute into templates directly.

### Cluster 1: project basics

- `project_name` — Q1
- `project_description_one_paragraph` — Q2
- `project_tagline_one_line` — Q5a (only when `source_prd_present == true` or PRD redundancy guard fires)
- `repo_local_path` — Q3
- `github_repo_url` — Q4
- `visual_confirmer_name` — Q5

### Cluster 1.5: stack and commands

- `stack` — Q5b (state map)
- `deploy_target` — Q5c (state map)
- `install_cmd` — Q5d
- `dev_cmd` — Q5d
- `check_cmd` — Q5d
- `test_cmd` — Q5d
- `build_cmd` — Q5d
- `env_pattern` — Q5e
- `enforce_rules_as_hooks` — Q5f (state map; default true)
- `deploy_target_name` — derived from `deploy_target`
- `deploy_cli_lower` — derived from `deploy_target` (lowercased CLI name; empty when no CLI conflict)
- `deploy_target_has_cli_conflict` — derived from `deploy_target`
- `deploy_cli_name` — derived (only used when `deploy_target_has_cli_conflict == true`)
- `stack_summary_one_line` — derived from `stack` + `deploy_target`
- `stack_has_client_server_split` — derived from `stack`
- `stack_has_ui` — derived from `stack`
- `uses_visual_confirmation_gate` — derived from `stack_has_ui` and `visual_confirmer_name`

### Cluster 2: AI surfaces

- `ai_surface_count` — Q6 (state map only, not a marker)
- `surface_display_name` — Q7 (per surface)
- `surface_implementation_path` — Q8 (per surface)
- `surface_api_route_path` — Q9 (per surface)
- `surface_system_prompt_constant` — Q10 (per surface)
- `surface_purpose_paragraph` — Q11 (per surface)
- `surface_audience` — Q12 (per surface)
- `surface_model_choice` — Q13 (per surface)
- `surface_prompt_rules_list` — Q14 (per surface)
- `surface_output_schema_or_none` — Q15 (per surface)
- `model_split_table` — Q16
- `model_split_rule_1`, `model_split_rule_2` — Q16 (sub-fills)
- `ai_client_path` — Q17
- `ai_prompts_path` — Q18
- `ai_surface_kebab_name_list` — derived (built from per-surface answers in decisions.md)
- `ai_surfaces_summary` — derived (one-line summary built from per-surface answers)

### Cluster 3: design system

- `design_shape` — Q19 (state map only)
- `apply_design_heuristics` — Q20 (state map only)
- `token_file_path` — Q19 sub-fill (only if `tokens_with_linter`)
- `token_linter_command` — Q19 sub-fill
- `typography_rules` — Q19 sub-fill
- `motion_tokens` — Q19 sub-fill
- `icon_set` — Q19 sub-fill
- `layout_rules` — Q19 sub-fill
- `indicator_vocabulary_table` — Q19 sub-fill
- `forbidden_indicator_terms` — Q19 sub-fill
- `button_tier_list` — Q19 sub-fill
- `form_rules` — Q19 sub-fill
- `design_things_to_avoid_list` — Q19 sub-fill
- `design_rule_1`, `design_rule_2`, `design_rule_3` — Q19 sub-fill (three load-bearing one-liners for AGENTS.md instant-recall block)
- `action_ceiling_count` — Q20 sub-fill (only if `apply_design_heuristics`)
- `miller_application` — Q20 sub-fill
- `aria_specific_rules` — Q20 sub-fill

### Cluster 4: voice and tone

- `voice_and_tone` — Q21 (state map only)
- `voice_source_hierarchy` — Q21 sub-fill
- `brand_position_paragraph` — Q21 sub-fill
- `primary_brand_line` — Q21 sub-fill
- `voice_characteristics_list` — Q21 sub-fill
- `preferred_terms_list` — Q21 sub-fill
- `forbidden_terms_list` — Q21 sub-fill
- `positioning_risks_list` — Q21 sub-fill
- `project_specific_writing_rule` — Q21 sub-fill

### Cluster 5: conditional patterns

- `include_parking_lot` — Q22 (state map)
- `include_decisions_active` — Q23 (state map)
- `include_future` — Q24 (state map)
- `codex_usage` — Q25 (state map)
- `canonical_workflow_doc_name` — Q26 (only if user named one)
- `include_product_rules` — Q27 (state map)
- `skill_list` — Q25 sub-fill (only if `codex_usage == "regular"`)
- `external_skill_references` — Q27a (only if `codex_usage in ("regular", "occasional")`). State-map list, used by `decisions.md` to add cross-link block to `.agents/skills/README.md`.

### Cluster 6: content fills

- `product_summary_paragraph` — Q28
- `target_users_list` — Q28
- `core_problem_paragraph` — Q28
- `main_workflow_steps` — Q28
- `out_of_scope_list` — Q28
- `deferred_capabilities_list_or_none` — Q28
- `primary_data_flow_name` — Q29
- `primary_data_flow_steps` — Q29
- `secondary_flow_name` — Q29 (optional)
- `secondary_flow_steps` — Q29 (optional)
- `data_persistence_paragraph` — Q29
- `external_integrations_list_or_none` — Q29
- `folder_structure_summary` — Q29
- `workflow_1_name`, `workflow_1_description` — Q30 (per workflow)
- `workflow_2_name`, `workflow_2_description` — Q30 (per workflow, etc.)
- `phase_1_name`, `phase_1_goal`, `phase_1_task_placeholder`, `phase_1_done_when` — Q31
- `additional_stack_summary` — Q32
- `canonical_vocabulary_list`, `forbidden_vocabulary_list`, `vocabulary_lock_rule` — Q33
- `architecture_rules_numbered_list` — Q34 (only for flat shape)
- `product_ux_rules_list`, `critical_invariants` — Q35 (only for flat shape, if applicable)
- `numbered_product_rules_list` — only if `include_product_rules == true`. Free-text 3–10 rules.
- `open_decisions_list_or_none` — Q31 sub-fill (open decisions for the roadmap, free text)
- `ux_row_doc_names` — only for flat shape. Either drop the row (handled in decisions.md) or fill from project's UX docs.
- `path_scoped_rule_list` — derived (built from the per-template inclusion table in decisions.md)
