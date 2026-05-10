# Example transcript: large project

The large-shape regression test for structural parameterization. **Modular shape** via the `ai_surface_count >= 2` trigger, but the project is a no-UI Python service on Fly.io — a stack-and-deploy combination that exercises **four distinct suppressions** and a recency-block shrink that the prior Next.js+Vercel large example could not.

**Project shape:** Python service on Fly.io, three LLM surfaces in a classification pipeline, no UI (HTTP service consumed by upstream support tooling), single developer, no voice-and-tone (output is internal routing data, not user-facing copy), Codex used regularly for backend pairing.

This is a transcript only. Output sketch follows.

---

## Cluster 0: source material

- `source_prd_present`: no
- `source_other_material`: none

## Cluster 1: project basics

- `project_name`: `triage-classifier`
- `project_description_one_paragraph`: A Python service that ingests customer-support tickets, classifies them by topic and urgency, and produces a routing summary for handoff. Three LLM surfaces work in a pipeline: topic classification → urgency detection → handoff summary. Consumed by the existing support tooling over HTTP; no UI of its own.
- `repo_local_path`: `/Users/devon/Sites/triage-classifier`
- `github_repo_url`: `https://github.com/devon-ops/triage-classifier`
- `visual_confirmer_name`: Devon (named for the intake, but `uses_visual_confirmation_gate` resolves false because `stack_has_ui == false`)

## Cluster 1.5: stack and commands

- `stack`: `python`
- `deploy_target`: `fly`
- `install_cmd`: `uv sync`
- `dev_cmd`: `uv run uvicorn app.main:app --reload`
- `check_cmd`: `ruff check . && mypy .`
- `test_cmd`: `pytest`
- `build_cmd`: (none — Fly builds the Docker image at deploy time)
- `env_pattern`: `.env locally; fly secrets in production. Never commit .env.` (Fly default; not overridden.)
- `enforce_rules_as_hooks`: yes

Derived:

- `deploy_target_name`: `Fly.io`
- `deploy_target_has_cli_conflict`: **false** (Fly CLI is the standard deploy path)
- `stack_summary_one_line`: `Python service on Fly.io`
- `stack_has_client_server_split`: **false** (Python service; no client-side execution context)
- `stack_has_ui`: **false**
- `uses_visual_confirmation_gate`: **false** (no UI to confirm)

This combination is the structural parameterization demo. Four derived flags resolve false; each gates a distinct suppression downstream.

## Cluster 2: AI surfaces

- `ai_surface_count`: 3

**Surface 1: `topic-classifier`**
- `surface_implementation_path`: `app/ai/topic.py`
- `surface_api_route_path`: `app/api/classify.py`
- `surface_system_prompt_constant`: `TOPIC_CLASSIFIER_SYSTEM`
- `surface_purpose_paragraph`: Reads a support ticket and assigns one of a fixed topic taxonomy (Billing, Account, Product, Technical, Other). Used to route the ticket to the right team queue.
- `surface_audience`: internal support routing (not customer-visible)
- `surface_model_choice`: Haiku
- `surface_prompt_rules_list`: Topic must be from the fixed taxonomy. No invented categories. If a ticket genuinely doesn't fit, choose `Other` rather than guessing. Confidence threshold: low-confidence routing falls back to Other plus a flag for human review.
- `surface_output_schema_or_none`: `{ topic: enum, confidence: float }`

**Surface 2: `urgency-detector`**
- `surface_implementation_path`: `app/ai/urgency.py`
- `surface_api_route_path`: `app/api/classify.py` (same route — composes the two classifiers)
- `surface_system_prompt_constant`: `URGENCY_DETECTOR_SYSTEM`
- `surface_purpose_paragraph`: Reads the ticket and assigns one of four urgency levels (Critical, High, Normal, Low) based on explicit signals (system down, blocked, time-sensitive) — not on the customer's tone.
- `surface_audience`: internal support routing
- `surface_model_choice`: Haiku
- `surface_prompt_rules_list`: Score on explicit signals only. Do not infer urgency from emotional tone. Default to Normal when signals are ambiguous. Reasoning trace required (one short sentence citing the signal that justifies the level).
- `surface_output_schema_or_none`: `{ urgency: enum, reasoning: string }`

**Surface 3: `summary-generator`**
- `surface_implementation_path`: `app/ai/summary.py`
- `surface_api_route_path`: `app/api/summarize.py`
- `surface_system_prompt_constant`: `SUMMARY_GENERATOR_SYSTEM`
- `surface_purpose_paragraph`: Produces a two-sentence handoff summary for the support agent who will own the ticket: what the customer reported, what's been tried, and what the suggested next action is.
- `surface_audience`: internal support agents (the receiving team)
- `surface_model_choice`: Sonnet
- `surface_prompt_rules_list`: Two sentences maximum. Cite specific ticket details, not paraphrase. Flag any ticket where the customer's request is genuinely unclear; never invent a "what's been tried" if the ticket doesn't say.
- `surface_output_schema_or_none`: `{ summary: string }`

- `model_split_table`:
  | Client | Model ID | Used for |
  | --- | --- | --- |
  | `haiku` | `claude-haiku-4-5-20251001` | topic + urgency classification |
  | `sonnet` | `claude-sonnet-4-6` | handoff summary |
- `ai_client_path`: `app/ai/client.py`
- `ai_prompts_path`: `app/ai/prompts.py`

## Cluster 3: design system and UX

- `design_shape`: `none` (Python service, no UI)
- `apply_design_heuristics`: skipped

## Cluster 4: voice and tone

- `voice_and_tone`: **no** (output is internal routing data and internal handoff summaries; no brand voice concern)

## Cluster 5: conditional patterns

- `include_parking_lot`: yes
- `include_decisions_active`: yes
- `include_future`: yes (V2 list: switch from API LLM to fine-tuned classifier for high-volume topics; add streaming summary for real-time agent UI; per-team confidence thresholds)
- `codex_usage`: regular → emit both `.codex/config.toml` and `.agents/skills/README.md`
- `canonical_workflow_doc_name`: none
- `include_product_rules`: no (PRD plus per-surface AI rules carry the load)
- `external_skill_references`: none

## Cluster 6: content fills

(condensed)

- PRD content captures the three-surface pipeline, the internal-support audience, the "tickets routed late + summaries inconsistent" problem, and the five-step workflow (ingest → classify topic → detect urgency → generate summary → write back to support tool).
- Architecture content captures the FastAPI service, async LLM calls with retry, Postgres for ticket state and classification audit log, no caching of LLM responses (audit trail must reflect real model output), structured JSON logging.
- `additional_stack_summary`: FastAPI, Postgres (Fly Postgres add-on), Anthropic SDK, structlog for JSON logs.
- Workflows: single primary workflow (classification pipeline). The three AI surfaces are pipeline stages, not parallel workflows.
- Vocabulary lock: none. Topic and urgency taxonomies live in `docs/PRD.md` and the prompt constants; no project-wide vocabulary lockdown across docs.

## Rule shape determination

| Trigger | Value | Triggers modular? |
|---|---|---|
| `ai_surface_count >= 2` | **3** | **yes** |
| `design_shape == "tokens_with_linter"` | none | no |
| `len(workflows) > 1` | 1 | no |
| `voice_and_tone == true` | no | no |

**Result: modular**, driven entirely by the AI-surface count.

## Suppression cascade (the demo)

The combination `stack=python + deploy_target=fly + design_shape=none + voice_and_tone=no` triggers four distinct suppressions in the emitted output. Each suppression is documented in [`decisions.md`](../generator/decisions.md) and gates real content drops.

| Flag | Value | Suppresses |
|---|---|---|
| `uses_visual_confirmation_gate` | false | Recency item 2, "No worktrees." suffix on primary-constraints item 3, body Commit gate section, UI bullet under Verification, Codex visual-confirmation override paragraph in AGENTS.md, `block-worktree.sh` hook + 2 `settings.json` entries |
| `stack_has_client_server_split` | false | `ai-shared.md` rule file, recency item 3 (AI client-component constraint) |
| `deploy_target_has_cli_conflict` | false | "Never use the X CLI" line in Code rules, "No X CLI" inline suffix on primary-constraints item 3, `block-deploy-cli.sh` hook + its `settings.json` entry |
| `voice_and_tone` | false | `voice-and-tone.md` rule file |

## Confirmation

> **Skill:** Rule shape: **modular**. Three AI surfaces; the other three triggers are not crossed.
>
> **Direction:** AGENTS canonical, CLAUDE.md is `@AGENTS.md`.
>
> **Hooks scaffold:** `block-env-commit.sh` only. Both other hooks suppressed by `uses_visual_confirmation_gate == false` and `deploy_target_has_cli_conflict == false`. The minimal hook scaffold case.
>
> **Recency block:** one item (hard scope limits). Items 2–4 all suppressed by the flag cascade above.
>
> **Files to write:**
> - `AGENTS.md` (canonical, modular, minimal recency)
> - `CLAUDE.md` (one line: `@AGENTS.md`)
> - `ROADMAP.md`
> - `FUTURE.md` (V2 list)
> - `.claude/commands/session-start.md`
> - `.claude/settings.json` (one hook only)
> - `.claude/hooks/block-env-commit.sh` + `README.md`
> - `.claude/rules/git-and-deploy.md`
> - `.claude/rules/session-discipline.md`
> - `.claude/rules/ai-topic-classifier.md`
> - `.claude/rules/ai-urgency-detector.md`
> - `.claude/rules/ai-summary-generator.md`
> - `.codex/config.toml`
> - `.agents/skills/README.md`
> - `docs/PRD.md`
> - `docs/ARCHITECTURE.md`
> - `docs/DECISIONS.md`
> - `docs/DECISIONS_ACTIVE.md`
> - `docs/PARKING_LOT.md`
> - `docs/retros/README.md`
>
> **Not written:** `voice-and-tone.md`, `design-system.md`, `design-heuristics.md`, `product-rules.md`, `ai-shared.md`, `block-deploy-cli.sh`, `block-worktree.sh`. Each absence traces to a specific suppression flag, not to a forgotten template.
>
> Proceed?

**User:** yes

## Output sketch

See `output-large-abbreviated.md` for the structural sketch and the regression checks this case verifies.
