# Example transcript: large project

The large-shape regression test. Modeled on `epost-intelligence-feed` (the feed project audited in `findings.md`). Lands in the **modular shape** because every modular threshold is crossed: three AI surfaces, token system with linter, multiple workflows, voice-and-tone rule.

This case exercises the regression test definition in `NOTES.md`: the generator must reproduce feed's structure plus the two corrections (AGENTS canonical direction, `DECISIONS_ACTIVE.md` present). If the generator reproduces feed exactly, the criterion has not been applied.

This is a transcript only. Output sketch follows.

---

## Cluster 1: project basics

- `project_name`: `intelligence-feed`
- `project_description_one_paragraph`: A private internal workflow tool. Monitors international shipping and customs sources, surfaces relevant items for human review, and supports content production with three workflows (Sources, Feed Review, Content) and a draft-only publishing model.
- `repo_local_path`: `/Users/rexc/Sites/intelligence-feed`
- `github_repo_url`: `https://github.com/rex-org/intelligence-feed`
- `visual_confirmer_name`: Rex

## Cluster 2: AI surfaces

- `ai_surface_count`: 3
- **Surface 1: `feed-enrichment`**
  - `surface_implementation_path`: `lib/ai/enrich.js`
  - `surface_api_route_path`: `app/api/feeds/[id]/enrich/route.js`
  - `surface_system_prompt_constant`: `AI_TAKE_SYSTEM`
  - `surface_purpose_paragraph`: Background system that enriches every ingested feed item: categorization, Important flag, and AI Take generation. Runs in Inngest, never client-side.
  - `surface_audience`: internal reviewer
  - `surface_model_choice`: Haiku primary, Gemini fallback (enrichment only)
  - `surface_prompt_rules_list`: Keep AI Take short. State what changed and why it may matter to ePost. Note uncertainty. No public copy. No customer action. No reviewer workflow direction.
  - `surface_output_schema_or_none`: AI Take Schema (canonical in `docs/PRD.md`): WHAT CHANGED, WHY IT MATTERS TO EPOST, RELEVANCE, URGENCY, CROSS-SOURCE NOTE, CONFIDENCE.
- **Surface 2: `feed-assistant`**
  - `surface_implementation_path`: `lib/ai/assistant.js`
  - `surface_api_route_path`: `app/api/feeds/ai-assist/route.js`
  - `surface_system_prompt_constant`: `ASSISTANT_SYSTEM`
  - `surface_purpose_paragraph`: Streaming conversational helper inside the Feed Review surface. Triggered from a feed item or selected items, not a standalone page.
  - `surface_audience`: internal reviewer
  - `surface_model_choice`: Sonnet
  - `surface_prompt_rules_list`: Ambient, not chatbot. Reference items in context. No invented facts. No customer guidance without `[REVIEW: ...]` placeholder.
  - `surface_output_schema_or_none`: streaming text
- **Surface 3: `content-generation`**
  - `surface_implementation_path`: `lib/ai/generate.js`
  - `surface_api_route_path`: `app/api/content/generate/route.js`
  - `surface_system_prompt_constant`: `CONTENT_ASSISTANT_SYSTEM`
  - `surface_purpose_paragraph`: Editorial draft generation for INTERNAL, NEWSLETTER, BLOG output types. LINK is excluded; LINK never uses AI generation.
  - `surface_audience`: customer-facing through reviewer-edited drafts
  - `surface_model_choice`: Sonnet
  - `surface_prompt_rules_list`: Follow voice-and-tone rules. Source facts override brand messaging. Customer guidance requires reviewer approval; emit `[REVIEW: ...]` placeholders. No invented metrics. INTERNAL/NEWSLETTER/BLOG produce drafts. LINK skips this surface entirely.
  - `surface_output_schema_or_none`: per-output-type templates
- `model_split_table`:
  | Client   | Model ID                    | Used for |
  | -------- | --------------------------- | -------- |
  | `haiku`  | `claude-haiku-4-5-20251001` | Background enrichment |
  | `sonnet` | `claude-sonnet-4-6`         | Assistant + editorial generation |
- `ai_client_path`: `lib/ai/client.js`
- `ai_prompts_path`: `lib/ai/prompts.js`

## Cluster 3: design system

- `design_shape`: `tokens_with_linter`. Token CSS at `design-system/colors_and_type.css`, linter `npm run check:tokens` wired into `npm run check`.
- `apply_design_heuristics`: yes
- Token-system fills include: typography (Geist sans, Chivo Mono for UI labels), motion (`--dur-fast` + `--ease-out`), icons (Material Icons Outlined only), layout (240px sidebar plus scrollable main), indicator vocabulary (status chip / type badge / category tag / relevance chip / output history chip / alert / banner / badge), naming taboo (no pill, no label, no bubble), button hierarchy (primary, approve, secondary, tertiary, ghost, with destructive variants), forms, things to avoid (no gradients, no Tailwind, no shadcn, no Instrument Serif).
- Three load-bearing one-liners for AGENTS.md instant-recall block: every color/spacing/radius/shadow uses a CSS custom property; Geist for body, Chivo Mono for UI labels; Material Icons Outlined only.
- Design heuristics specifics: `action_ceiling_count` = 3 (Approve, Skip, Add to chat). `miller_application` = "no card body shows more than 7 distinct content blocks before requiring expansion." `aria_specific_rules` = ".btn-icon requires aria-label; aria-expanded on accordion toggles; aria-live=polite on assistant message thread."

## Cluster 4: voice and tone

- `voice_and_tone`: yes
- Source hierarchy: approved brand book → strategic positioning → public website → discovery summaries → general practice.
- Brand position, primary brand line ("Global shipping. Zero surprises."), voice characteristics (calm confidence, problem-first, concrete, advisory, plainspoken, active, efficient, human), preferred terms (resilience, orchestration, infrastructure, predictability, DDP, landed cost, customs, etc.), forbidden terms (seamless, end-to-end, streamlined, best-in-class, simplify, leverage, cutting-edge, scalable, innovative, disruptive, revolutionary), positioning risks (do not sound like only a carrier reseller, do not overstate automation, etc.).

## Cluster 5: conditional patterns

- `include_parking_lot`: yes
- `include_decisions_active`: **yes** (this is one of the two corrections; feed had only `decisions-history.md`)
- `include_future`: yes
- `codex_usage`: regular → emit both `.codex/config.toml` and `.agents/skills/README.md`
- `canonical_workflow_doc_name`: `CONTENT_SYSTEM` → `docs/CONTENT_SYSTEM.md` is the canonical tiebreaker
- `include_product_rules`: yes

## Cluster 6: content fills

(condensed)

- PRD content captures the three workflows, the reviewer audience, the AI Take Schema, the output type taxonomy with vocabulary lock.
- Architecture content captures the ingestion → enrichment → review → content production pipeline, Neon Postgres, Inngest, WordPress draft publishing.
- Workflows: 1) Sources (manage and monitor RSS), 2) Feed Review (primary daily review), 3) Content (publishing workspace).
- `additional_stack_summary`: Neon Postgres, Inngest for background jobs, Tiptap, TanStack Table.
- Vocabulary lock: canonical `INTERNAL`, `NEWSLETTER`, `BLOG`, `LINK`, `ALERT`. Forbidden `internal-brief`, `customer-newsletter`, `weekly-news-roundup`, `news-update`, `breaking-alert`.
- Product rules: 17 rules sourced from PRD and CONTENT_SYSTEM (every status answers "what next," Feed Review is daily triage, two actions only, no auto drafts, no auto publish, INTERNAL/NEWSLETTER/BLOG create drafts, LINK direct-publish, fallbacks over failures, vocabulary lock applies, do not build ALERT, etc.).

## Confirmation

> **Skill:** Rule shape: **modular**. Three AI surfaces, token-system-with-linter design, three workflows, voice-and-tone rule. All four modular thresholds crossed.
>
> **Direction:** AGENTS canonical, CLAUDE.md is `@AGENTS.md`. (Correction 1: feed had this direction already.)
>
> **Decisions split:** `DECISIONS.md` plus `DECISIONS_ACTIVE.md` present. (Correction 2: feed had only `decisions-history.md`.)
>
> **Files to write:**
> - `AGENTS.md` (canonical, with recency safeguard items 1–7 including AI and vocabulary)
> - `CLAUDE.md` (one line: `@AGENTS.md`)
> - `ROADMAP.md`
> - `FUTURE.md` (or `docs/FUTURE.md`)
> - `.claude/commands/session-start.md`
> - `.claude/rules/git-and-deploy.md`
> - `.claude/rules/session-discipline.md`
> - `.claude/rules/product-rules.md`
> - `.claude/rules/voice-and-tone.md`
> - `.claude/rules/design-system.md`
> - `.claude/rules/design-heuristics.md`
> - `.claude/rules/ai-shared.md`
> - `.claude/rules/ai-feed-enrichment.md`
> - `.claude/rules/ai-feed-assistant.md`
> - `.claude/rules/ai-content-generation.md`
> - `.codex/config.toml`
> - `.agents/skills/README.md`
> - `docs/PRD.md`
> - `docs/ARCHITECTURE.md`
> - `docs/CONTENT_SYSTEM.md` (named canonical workflow doc; the user fills the body)
> - `docs/DECISIONS.md`
> - `docs/DECISIONS_ACTIVE.md`
> - `docs/PARKING_LOT.md`
> - `docs/retros/README.md`
>
> Proceed?

**User:** yes

## Output sketch

Structural sketch only. The full file shapes follow the modular templates with all conditional sections enabled.

Key checks for the regression test:

- `AGENTS.md` is canonical. `CLAUDE.md` is one line. (Correction 1.)
- `docs/DECISIONS_ACTIVE.md` exists with the assessment-shape promotion criteria. (Correction 2.)
- `AGENTS.md` "Before you respond" block has all seven items (AI client-component constraint, vocabulary lock both included).
- `path_scoped_rule_list` in AGENTS.md "Path-scoped rules" section reads: `voice-and-tone.md`, `design-system.md`, `design-heuristics.md`, `ai-shared.md`, `ai-feed-enrichment.md`, `ai-feed-assistant.md`, `ai-content-generation.md`.
- Each `ai-<surface>.md` file has substituted `paths:` frontmatter — no `<!-- PARAMETERIZE: ... -->` markers remain inside YAML.
- The "When in doubt" table in AGENTS.md includes the workflow row pointing at `docs/CONTENT_SYSTEM.md`.
- The vocabulary lock section in AGENTS.md carries both the canonical and forbidden lists.
- The Codex section at the bottom of AGENTS.md is present.

If any of these checks fail, the generator has a bug. If the file list matches but the corrections are missing (CLAUDE canonical, no `DECISIONS_ACTIVE.md`), the regression test framing is wrong and the generator is reproducing feed exactly instead of applying the corrections.
