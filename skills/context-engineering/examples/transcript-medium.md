# Example transcript: medium project

A medium-shape project taken through the generator. Lands in the **modular shape** because the project crosses one of the four modular thresholds: `voice_and_tone == true`. The other three thresholds are not crossed (one AI surface, basic styling, single workflow), so the modular split is driven entirely by the voice-and-tone trigger. This is the case that exercises voice-and-tone as a modular-shape pivot and the non-Vercel parameterization path.

**Project shape:** React + Vite SPA on Cloudflare Pages, one AI surface, basic styling without a token file or linter, single developer, voice-and-tone enabled (the product *is* the developer's brand voice), Codex used occasionally.

This is a transcript only — no full output tree. Output sketch follows after the transcript.

---

## Cluster 0: source material

- `source_prd_present`: no
- `source_other_material`: none

All downstream clusters run cold-start.

## Cluster 1: project basics

- `project_name`: `craft-letters`
- `project_description_one_paragraph`: A single-page web tool for a freelance copywriter (Maya) to generate first-draft email campaigns from client briefs in her established voice. The user pastes a client brief, sees a generated draft (subject lines, body, CTA options) tailored to her voice profile, and edits before delivering to the client. No accounts, no saved drafts beyond local storage.
- `repo_local_path`: `/Users/maya/Sites/craft-letters`
- `github_repo_url`: `https://github.com/maya-w/craft-letters`
- `visual_confirmer_name`: Maya

## Cluster 1.5: stack and commands

- `stack`: `react-vite`
- `deploy_target`: `cloudflare`
- `install_cmd`: `npm install`
- `dev_cmd`: `npm run dev`
- `check_cmd`: `npm run lint && npm run typecheck`
- `test_cmd`: `npm test`
- `build_cmd`: `npm run build`
- `env_pattern`: `.dev.vars locally; Cloudflare Pages env vars in production. Never commit .dev.vars.` (Cloudflare default; not overridden.)
- `enforce_rules_as_hooks`: yes

Derived:

- `deploy_target_name`: `Cloudflare Pages`
- `deploy_target_has_cli_conflict`: **false** (Wrangler is the standard deploy path; no CLI gate)
- `stack_summary_one_line`: `React + Vite on Cloudflare Pages`
- `stack_has_client_server_split`: **true** (Vite + Cloudflare Pages Functions for the backend route)
- `stack_has_ui`: true
- `uses_visual_confirmation_gate`: **true**

## Cluster 2: AI surfaces

- `ai_surface_count`: 1
- Surface 1: `draft-generator`
  - `surface_implementation_path`: `lib/ai/draft.js`
  - `surface_api_route_path`: `functions/api/draft.js` (Cloudflare Pages Functions)
  - `surface_system_prompt_constant`: `DRAFT_GENERATOR_SYSTEM`
  - `surface_purpose_paragraph`: Reads a client brief plus Maya's voice profile and produces a first-draft email campaign in three sections: three subject-line options, one body draft, two CTA variants.
  - `surface_audience`: end customer (Maya's client's recipient list), through Maya's edits
  - `surface_model_choice`: Sonnet
  - `surface_prompt_rules_list`: Follow Maya's voice characteristics (calm, specific, plainspoken). No invented client facts; flag gaps with `[REVIEW: ...]` placeholders. No generic marketing phrases from the forbidden list. Keep body under 200 words unless brief explicitly requests more. Subject lines under 60 characters.
  - `surface_output_schema_or_none`: `{ subject_lines: string[3], body: string, cta_options: string[2] }`
- `model_split_table`: single client, `sonnet` only.
- `ai_client_path`: `lib/ai/client.js`
- `ai_prompts_path`: `lib/ai/prompts.js`

## Cluster 3: design system and UX

- `design_shape`: `basic_styling` (`src/index.css`, no token file, no linter)
- `apply_design_heuristics`: skipped (gated on `tokens_with_linter`)

## Cluster 4: voice and tone

- `voice_and_tone`: **yes**
- `voice_source_hierarchy`: Maya's portfolio writing samples → her positioning brief → general copywriting craft principles.
- `brand_position_paragraph`: Maya writes copy that respects the reader's intelligence. Her work converts because it sounds like one careful person talking to another — not a brand, not a department.
- `primary_brand_line`: "Copy that respects the reader."
- `voice_characteristics_list`: calm, specific, plainspoken, active voice, concrete examples over abstractions, comfortable with silence (no filler).
- `preferred_terms_list`: campaign, brief, draft, reader, send, open rate (when actually measured).
- `forbidden_terms_list`: blast, audience, leverage, unlock, seamless, journey, ecosystem, game-changing, revolutionary, best-in-class, world-class.
- `positioning_risks_list`: do not sound like a marketing agency; do not promise outcomes the brief doesn't support; do not write copy that could be any brand.
- `project_specific_writing_rule`: Every draft must cite the specific brief detail it draws from. AI cannot invent client facts.

## Cluster 5: conditional patterns

- `include_decisions_active`: yes
- `backlog_include_v2`: no (V2 items arrive as `BACKLOG.md` Backlog entries when they become real)
- `codex_usage`: occasional → emit `.codex/config.toml`, skip `.agents/skills/`
- `canonical_workflow_doc_name`: none
- `include_product_rules`: no
- `external_skill_references`: none

## Cluster 6: content fills

(condensed)

- PRD content captures the single workspace page, Maya's audience (herself, then her clients via drafts), the "AI drafts that don't sound like AI" problem, and the four-step workflow (paste brief → review draft → edit → deliver).
- Architecture content captures the draft-generation flow (brief → API route → Anthropic SDK → structured response), localStorage for voice-profile persistence, no database, Cloudflare Pages Functions for the API route.
- `additional_stack_summary`: Anthropic SDK for draft generation. localStorage for voice-profile and recent-drafts cache. No database.
- Architecture rules: not asked (modular shape — architecture lives in `docs/ARCHITECTURE.md` and per-surface rules; `architecture_rules_numbered_list` is flat-shape only).

## Rule shape determination

Applying the criterion at [`decisions.md`](../generator/decisions.md) "Rule shape: flat vs modular":

| Trigger | Value | Triggers modular? |
|---|---|---|
| `ai_surface_count >= 2` | 1 | no |
| `design_shape == "tokens_with_linter"` | basic_styling | no |
| `len(workflows) > 1` | 1 | no |
| `voice_and_tone == true` | **yes** | **yes** |

**Result: modular**, driven entirely by the voice-and-tone trigger. This is the case the modular criterion exists to catch — a project that would otherwise be flat but has a load-bearing voice rule that earns its own path-scoped rule file.

## Confirmation

> **Skill:** Rule shape: **modular**. The voice-and-tone trigger crosses the threshold; the other three are not crossed.
>
> **Direction:** AGENTS canonical, CLAUDE.md is `@AGENTS.md`.
>
> **Hooks scaffold:** `block-env-commit.sh` (always), `block-worktree.sh` (uses_visual_confirmation_gate=true). **No `block-deploy-cli.sh`** — Wrangler is the standard Cloudflare deploy path, not a CLI conflict.
>
> **Files to write:**
> - `AGENTS.md` (canonical, modular)
> - `CLAUDE.md` (one line: `@AGENTS.md`)
> - `BACKLOG.md`
> - `.claude/commands/session-start.md`
> - `.claude/settings.json`
> - `.claude/hooks/block-env-commit.sh` + `block-worktree.sh` + `README.md`
> - `.claude/rules/git-and-deploy.md`
> - `.claude/rules/session-discipline.md`
> - `.claude/rules/voice-and-tone.md`
> - `.claude/rules/ai-shared.md`
> - `.claude/rules/ai-draft-generator.md`
> - `.codex/config.toml`
> - `docs/PRD.md`
> - `docs/ARCHITECTURE.md`
> - `docs/DECISIONS.md`
> - `docs/DECISIONS_ACTIVE.md` (empty, awaiting first promotion)
> - `docs/retros/README.md`
>
> Proceed?

**User:** yes

## Output sketch

See `output-medium-abbreviated.md` for the structural sketch and the regression checks this case verifies.
