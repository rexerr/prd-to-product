# Example transcript: medium project

A medium-shape project taken through the generator. Lands in the **flat shape** because the project does not cross any of the four modular thresholds (one AI surface, no token file or linter, single workflow, no voice rule). This is the case the per-template inclusion table and the flat-vs-modular criterion in `decisions.md` need to handle correctly.

**Project shape (per phase-1-prd.md validation):** Next.js app with three pages and two API routes, one AI surface, basic styling without a token file or linter, single developer, Vercel deploy, Codex used occasionally.

This is a transcript only — no full output tree. Output sketch follows after the transcript.

---

## Cluster 1: project basics

- `project_name`: `prompt-coach`
- `project_description_one_paragraph`: A small tool that helps technical writers refine their prompts for LLM-assisted drafting. Three pages: a workspace where the writer pastes a draft prompt and sees a critique, a library of saved prompts, and a settings page. One API route generates the critique; a second API route saves prompts to local storage on the server side via a small Postgres table.
- `repo_local_path`: `/Users/sam/Sites/prompt-coach`
- `github_repo_url`: `https://github.com/sam-w/prompt-coach`
- `visual_confirmer_name`: Sam

## Cluster 2: AI surfaces

- `ai_surface_count`: 1
- Surface 1: `prompt_critic`
  - `surface_implementation_path`: `lib/ai/critique.js`
  - `surface_api_route_path`: `app/api/critique/route.js`
  - `surface_system_prompt_constant`: `PROMPT_CRITIC_SYSTEM`
  - `surface_purpose_paragraph`: Reads the writer's draft prompt and returns a structured critique covering clarity, specificity, and example coverage.
  - `surface_audience`: writer (the user of the tool)
  - `surface_model_choice`: Sonnet
  - `surface_prompt_rules_list`: Keep critique short (no more than 6 bullets). Cite the specific phrase or section being critiqued. No rewriting; offer suggestions only. Never invent a missing context detail; flag the gap instead.
  - `surface_output_schema_or_none`: `{ clarity: bullets, specificity: bullets, examples: bullets }`
- `model_split_table`: single client, `sonnet` only.
- `ai_client_path`: `lib/ai/client.js`
- `ai_prompts_path`: `lib/ai/prompts.js`

## Cluster 3: design system

- `design_shape`: `basic_styling` (`globals.css` plus a small `lib/styles.js`, no token file, no linter)
- `apply_design_heuristics`: skipped (gated on tokens-with-linter)

## Cluster 4: voice and tone

- `voice_and_tone`: no (output is internal critique, not customer-facing copy)

## Cluster 5: conditional patterns

- `include_parking_lot`: yes
- `include_decisions_active`: yes
- `include_future`: no
- `codex_usage`: occasional → emit `.codex/config.toml`, skip `.agents/skills/`
- `canonical_workflow_doc_name`: none
- `include_product_rules`: no

## Cluster 6: content fills

(condensed)

- PRD content captures the three-page workspace, the writer audience, the prompt-critique problem, and the seven-step workflow.
- Architecture captures the critique flow, the saved-prompts flow, Postgres as the only persistence, and the AI-layer overview.
- `additional_stack_summary`: Neon Postgres for saved prompts. Anthropic SDK for the critic.
- Architecture rules (flat shape):
  1. **Critique runs server-side only.** `lib/ai/critique.js` is imported only from `app/api/critique/route.js`. Never from a client component.
  2. **No critique caching.** Every request hits the model. The prompt is short and quality matters more than cost.
  3. **Saved prompts are user-scoped via session cookie.** No cross-user reads.

## Confirmation

> **Skill:** Rule shape: **flat**. The project has one AI surface, no token-plus-linter design system, one workflow, and no voice rule. None of the four modular thresholds is crossed.
>
> **Files to write:**
> - `AGENTS.md` (thin pointer to CLAUDE)
> - `CLAUDE.md` (canonical, all rules inline including the AI server-only rule)
> - `ROADMAP.md`
> - `.claude/commands/session-start.md`
> - `.codex/config.toml`
> - `docs/PRD.md`
> - `docs/ARCHITECTURE.md`
> - `docs/DECISIONS.md`
> - `docs/DECISIONS_ACTIVE.md`
> - `docs/PARKING_LOT.md`
> - `docs/retros/README.md`
>
> Proceed?

**User:** yes

## Output sketch

This is the structural sketch, not the full file tree. The small case in `output-small/` shows the full file shape; this case shares the same shape with these deltas:

- `CLAUDE.md` includes architecture rule about the AI server-only constraint.
- `CLAUDE.md` "Before you respond" block has item 6 enabled (AI client-component constraint).
- `.codex/config.toml` is present at the repo root.
- `docs/DECISIONS_ACTIVE.md` is present (and starts empty, awaiting first promotion).
- `docs/PARKING_LOT.md` is present.
- No `.claude/rules/` folder. No `design-system.md`, no `voice-and-tone.md`, no `ai-shared.md`, no surface-specific AI rule. The flat CLAUDE.md is doing all the rule work.

The medium-case test passes if (1) `decisions.md`'s flat-vs-modular criterion lands this on flat, (2) the AI architecture rule appears in CLAUDE.md, (3) the recency safeguard renumbering rule includes item 6, and (4) `.codex/config.toml` is emitted but `.agents/skills/README.md` is not.

If the criterion mistakenly pushes this case to modular, the criterion is wrong. The fix is in `decisions.md`, not in the templates.
