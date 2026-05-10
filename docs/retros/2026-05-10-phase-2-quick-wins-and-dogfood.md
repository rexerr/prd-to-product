# Retro — 2026-05-10 — Phase 2 quick wins + dog-food

Phase 2 of [ROADMAP.md](../../ROADMAP.md). Two parts in one session: (1) Thariq-derived quick wins to the `context-engineering` skill (~20 lines, committed independently), then (2) running the skill on this repo to produce its own context scaffold. Outcome: both parts shipped. The dog-food run hit the abort criterion mid-flight (templates assumed UI exists for a no-UI project), the skill was fixed, and the dog-food was re-run cleanly.

## What was completed

### Part 1 — Skill quick wins (commit [ab0cd77](https://github.com/rexerr/prd-to-product/commit/ab0cd77))

- Three session-management bullets added to both `templates/claude-rules-modular/session-discipline.md.template` and `templates/claude-rules-flat-CLAUDE.md.template`: (a) prefer `/rewind` to re-prompting when an approach fails; (b) start a new session for a new task; (c) `/compact` proactively with a description during long debug sessions before autocompact fires. Cited inline: Thariq Shihipar, *Lessons from Building Claude Code: Session Management & 1M Context*, Anthropic 2025.
- One paragraph added to `principles.md` "Always-on patterns" describing always-on vs on-demand hooks. Always-on = the three scaffolded hooks. On-demand = `/careful`-style for risky operations like `rm -rf`, `DROP TABLE`, force-push — invoked per-session, not blanket. Generator does not currently scaffold an on-demand example; the principle is enough until a real failure mode justifies one.
- Short note added to `principles.md` (new "Context budget" subsection) on context rot starting ~300–400k tokens for the 1M-context model, task-dependent, with the "approximate, will drift" framing.
- Mirrored the new bullets in `skills/context-engineering/examples/output-small/CLAUDE.md` so the canonical example reflects current template output.
- ROADMAP Part 1 tasks checked off in the same commit.

### Skill fix mid-flight (commit [a30d008](https://github.com/rexerr/prd-to-product/commit/a30d008))

The dog-food on this repo (no UI, no deploy, `stack=other`) hit the abort criterion: templates hardcoded "Visual confirmation gates the commit" as primary-constraints item 2 and recency-block item 2, with no `OPTIONAL` gate. Codex override and body Commit gate sections were also UI-only. Per the brief, halted the dog-food and fixed the skill before continuing.

Surgical gates added (~40 lines, mostly OPTIONAL-marker insertions):

- `templates/AGENTS.md.template` — primary-constraints item 2, recency-block item 2, "No worktrees" suffix on item 3 → all gated on `uses_visual_confirmation_gate`.
- `templates/claude-rules-flat-CLAUDE.md.template` — same three positions, plus body Commit gate section, Verification "UI changes" bullet (which also got switched from hardcoded `npm run dev` / `npm run check` to the parameterized `dev_cmd` / `check_cmd`), and a two-form push protocol (`with_deploy` vs `no_deploy`) so `deploy_target=none` doesn't ask the user to wait for a deploy that doesn't exist.
- `templates/claude-rules-flat-AGENTS.md.template` — Codex visual-override paragraph (entire override is UI-only) gated.
- `templates/claude-rules-modular/session-discipline.md.template` — Commit gate section, Verification "UI changes" bullet gated.
- `generator/decisions.md` — recency-renumbering rule updated (item 2 is now conditional on `uses_visual_confirmation_gate`); new "No-UI project handling" section enumerating everything that drops when the flag is false; new no-deploy clause for push-protocol wording.

This is a real skill improvement, not a one-off patch — any `stack: other` or `node-cli` or `python` project would have had the same dead text.

### Part 2 — Dog-food on this repo (commit pending — this commit)

Ran `context-engineering` skill on this repo with the inputs in the brief (stack=other, deploy_target=none, no UI, include PARKING_LOT/FUTURE/DECISIONS_ACTIVE). Files produced:

- `AGENTS.md` (1 line — `@CLAUDE.md` plus the introductory pointer; the Codex override gated out as it should be).
- `CLAUDE.md` (~120 lines — flat shape; primary constraints item 1 only; no worktree restriction; no Commit gate body section; push protocol uses the no-deploy form; Verification UI bullet absent; session-management bullets present from Part 1's edits).
- `docs/PRD.md`, `docs/ARCHITECTURE.md` — minimal scaffolds reflecting the skill-development workspace nature of the repo.
- `docs/DECISIONS.md` — seeded with three decisions: D-001 markdown-only (from `html-over-markdown-brief.md`), D-002 direct-on-main (from ROADMAP phasing principles), D-003 no-UI gate added to `context-engineering` (the skill fix this session).
- `docs/DECISIONS_ACTIVE.md` — same three as binding constraints. Each genuinely fits the criteria (rule the agent must follow now; not visible from code; not superseded).
- `docs/PARKING_LOT.md` — seeded with the four open items from Phase 1 retro and from this run (env_pattern doubled-period, output-small staleness, stack=other defaults, missing stack_summary_one_line row for `other + none`).
- `docs/FUTURE.md` — empty; Phase 3 ecosystem audit will populate.
- `docs/retros/README.md` — retro template.
- `.claude/commands/session-start.md` — orientation slash command including the parking-lot and DECISIONS_ACTIVE steps.
- `.claude/settings.json` — only `block-env-commit` registered. Both `block-deploy-cli` and `block-worktree` correctly suppressed via OPTIONAL gates (the dog-food's central hook-emission verification).
- `.claude/hooks/block-env-commit.sh` (chmod +x), `.claude/hooks/README.md`.

ROADMAP.md, the two existing retros, and `docs/html-over-markdown-brief.md` all untouched. The would-be templated `ROADMAP.md` was staged to `/tmp/dogfood-prd-to-product/ROADMAP.md.template-output` and confirmed to be a placeholder shell (unsurprising — the template can't know about Phase 1–4 of skill refinement).

`/session-start` orientation walked manually: AGENTS → CLAUDE → ROADMAP → most recent retro (`2026-05-10-phase-1-validation.md`) → PARKING_LOT → DECISIONS_ACTIVE. Coherent. The agent can resume cleanly.

## Files changed

### Part 1 (commit ab0cd77)
- `skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template` — added Session management section.
- `skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template` — added Session management section.
- `skills/context-engineering/principles.md` — added Always-on vs on-demand paragraph and Context budget subsection.
- `skills/context-engineering/examples/output-small/CLAUDE.md` — mirrored bullets.
- `ROADMAP.md` — Part 1 tasks checked off.

### Skill fix (commit a30d008)
- `skills/context-engineering/templates/AGENTS.md.template`
- `skills/context-engineering/templates/claude-rules-flat-AGENTS.md.template`
- `skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template`
- `skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template`
- `skills/context-engineering/generator/decisions.md`

### Part 2 (this commit)
- `AGENTS.md` (new)
- `CLAUDE.md` (new)
- `.claude/settings.json` (new)
- `.claude/commands/session-start.md` (new)
- `.claude/hooks/block-env-commit.sh` (new, chmod +x)
- `.claude/hooks/README.md` (new)
- `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/DECISIONS_ACTIVE.md`, `docs/PARKING_LOT.md`, `docs/FUTURE.md`, `docs/retros/README.md` (all new)
- `ROADMAP.md` — Part 2 tasks checked off.
- This retro.

## Key decisions made

- **D-003 (no-UI gate added to `context-engineering`).** Logged in `docs/DECISIONS.md` and mirrored to `DECISIONS_ACTIVE.md`. The hardcoded always-on item 2 was a real skill bug, not a one-off. Surfacing it via dog-food is exactly what the abort criterion is for.
- **Skill fix as its own commit, separate from dog-food output.** Reviewable independently. Matches the brief's pattern of Part 1 quick wins also being their own commit.
- **`stack=other + deploy_target=none` synthesis** — `stack_summary_one_line` derived as "Skill-development workspace (markdown only, no runtime)" by hand because the table in `decisions.md` doesn't cover this combination. Captured in `PARKING_LOT.md` for Phase 3 or 4 to address.

## Open items / next session

- **Phase 3 ecosystem audit starts next.** Read each skill's SKILL.md, audit description fields against the trigger-shaped standard, categorize against Thariq's 9 categories, document gaps in `docs/FUTURE.md`, drain `docs/PARKING_LOT.md`.
- **Parking lot grew this session.** Four items now: env_pattern doubled-period (Phase 1), output-small staleness (Phase 1), `stack=other` defaults all-asked (this session, may not need action), missing `stack_summary_one_line` row for `other + none` (this session). Phase 3 should drain.
- **The skill fix worked but covers only the flat shape and modular session-discipline.** The modular shape's other rule files (`product-rules.md`, `voice-and-tone.md`, etc.) were not audited for UI assumptions — they are unlikely to have any (none of them mention visual confirmation in the templates I've read), but a sweep during Phase 4 example regeneration would confirm.
- **`/session-start` was walked manually, not invoked as a slash command.** It's the same content either way; live invocation in a fresh session would be a nicer test. Pick up at session start of Phase 3 — first thing should be running `/session-start` for real.
- **`docs/handoff.md`, `docs/prd-creator-brief.md`, `docs/design-system-bootstrap-brief.md`** were preserved (not touched) but never wired into the new context structure. Phase 3 audit can decide whether they belong in `FUTURE.md`, in `PARKING_LOT.md`, or stay as standalone briefs.
