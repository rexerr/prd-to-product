# Roadmap — prd-to-product

What's left, in priority order. Read this at the start of every session alongside the most recent retro in `docs/retros/`.

Check off tasks as they are completed. Mark phases done only when all tasks are checked and the done-when criteria is met.

This roadmap covers refinement of the `context-engineering` skill, applying it to this repo (eat the dog food), and entering continuous-maintenance mode. A separate scope — HTML-over-Markdown investigation — is captured in [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md) and runs in parallel.

## Phasing principles

- **One phase = one session.** End every phase with a retro in `docs/retros/`. Start the next phase fresh.
- **Direct-on-main, no branches.** Skill-refinement phases are sequential and touch the same files; branches add friction. Branches only for genuinely parallel work (e.g., the HTML investigation if it edits skill files).
- **Each phase passes the failure-mode test.** Before starting, name the specific mistake the phase prevents. If you can't, defer.
- **Each phase delivers something committable.** No half-finished phases on `main`.
- **Each phase has an abort criterion.** If the phase surfaces a structural regression in earlier work, halt and re-scope. Do not paper over it to keep the schedule.
- **Phase N runs against the skill state at the end of Phase N−1.** Validate, then refine, then dog-food, then audit, then regenerate. Order matters.

---

## Phase 1: Validation (regression + hook contract)

**Goal:** confirm the skill's current state — paper alignment, stack parameterization, hook scaffold — is structurally sound before applying it to this repo or doing further refinement. This is throwaway work that catches problems cheaply, before they land in artifacts that are expensive to rebuild.

**Failure modes prevented:**

- Stack-parameterization changes silently break the modular shape (only the small/flat shape was validated previously).
- Hook contract assumptions (input via stdin JSON, exit 2 to block, `if: "Bash(...)"` permission syntax inside the `if` field, `EnterWorktree` as exact tool name) drift from upstream Claude Code without notice.
- The dog-food scaffold (Phase 2) gets built on a broken foundation, requiring re-runs.

**Tasks:**

- [x] Generator dry-run on a hypothetical non-Vercel modular project (e.g., React Vite SPA on Cloudflare Pages with 2 AI surfaces). Confirm: paired-write rules emit modular templates, recency renumbering still works for items 3–4, `paths:` frontmatter substitution produces parseable YAML, `OPTIONAL` blocks gate cleanly, no syntax-broken `settings.json` files.
- [x] Generator dry-run on the original Vercel/Next.js case. Compare against `skills/context-engineering/examples/output-small/` as the canonical regression target. Diff should be minimal and explainable.
- [x] Live-test each emitted hook in a **throwaway session**: start a fresh Claude Code session in a tmp directory outside this repo, copy the emitted `.claude/settings.json` and `.claude/hooks/` files in, then attempt each blocked operation: `vercel deploy`, `git add .env.local`, `git worktree add ../foo`, and the `EnterWorktree` Claude Code tool. Confirm each blocks with the expected message. If a block does not fire, debug — likely culprits: `chmod +x` not applied, `if:` permission syntax wrong, `EnterWorktree` not the actual tool name, JSON shape mismatched. (All four fired — PASS. See retro.)
- [x] Write the phase retro to `docs/retros/YYYY-MM-DD-phase-1-validation.md`.

**Done when:** all three dry-runs produce expected output, all hooks fire as designed, retro is written and committed.

**Abort criterion:** if validation surfaces a structural regression in the skill (e.g., the modular shape is genuinely broken, or the hook contract documented in `decisions.md` does not match what Claude Code actually does), halt. Do not proceed to Phase 2 until the regression is fixed in the skill itself. Update this roadmap to add a remediation phase before continuing.

**Out of scope:** regenerating the medium/large abbreviated examples (Phase 4). Adding new features or rules.

---

## Phase 2: Skill quick wins + eat the dog food

**Goal:** apply pending Thariq-derived quick wins to the skill (warm-up), then run the skill on this repo to scaffold `AGENTS.md`, `CLAUDE.md`, `.claude/rules/`, `.claude/settings.json`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and consolidate the existing roadmap and retros under the scaffolded structure.

Pre-work and dog-food run in the same session because the quick wins are ~20 lines of edits and the dog-food scaffold immediately tests them in real usage. Splitting them creates an artificial phase boundary.

**Failure modes prevented:**

- Re-prompting "that didn't work, try X" instead of `/rewind` — wastes context, accumulates failed attempts in the prefix.
- Autocompact firing during a long debug session and producing a bad summary because the model is at peak context-rot.
- Treating all hooks as "always-on," missing the on-demand `/careful`-style pattern for risky operations.
- Not knowing the context-rot threshold (~300–400k tokens) and missing the moment to compact proactively.
- Future sessions in this repo re-derive context every time (already paying this cost).
- Skill changes ship without being road-tested in real usage.
- Inconsistency between the skill's recommendations and the repo authoring it ("the cobbler's children have no shoes" antipattern).

**Tasks (warm-up — quick wins to skill, ~20 lines total):**

- [x] Add three bullets to `skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template` and `templates/claude-rules-flat-CLAUDE.md.template`: (a) prefer `/rewind` to re-prompting when an approach fails; (b) start a new session for a new task; (c) `/compact` proactively with a description during long debug sessions before autocompact fires. Cite source inline in the comment header: "Source: Thariq Shihipar, *Lessons from Building Claude Code: Session Management & 1M Context*, Anthropic 2025."
- [x] Add one paragraph to `skills/context-engineering/principles.md` "Always-on patterns" section describing always-on vs on-demand hooks. Always-on = rules that must hold every session (the three already scaffolded). On-demand = invoked only when needed for risky operations (e.g., `/careful` blocking `rm -rf`, `DROP TABLE`, force-push for the duration of a session). Don't try to make every hook always-on; the surface area gets noisy. Cite source inline.
- [x] Add a short note in `principles.md` (in "Position-aware placement" or a new "Context budget" subsection) that context rot starts ~300–400k tokens for the 1M-context model, **task-dependent**, with inline citation to Thariq's *Session Management & 1M Context* article. Frame as: "the threshold is approximate and likely to drift as models change — re-verify when consulting."
- [x] Update `skills/context-engineering/examples/output-small/CLAUDE.md` to mirror the new bullets.
- [x] Commit the quick wins as their own commit before starting the dog-food scaffold (so the dog-food commit is reviewable independently).

**Tasks (main — dog-food the skill on this repo):**

- [x] Run `context-engineering` skill on this repo. Stack: `other` (skill-development workspace, not a deployed app). Deploy target: `none`. Visual confirmer: user. `uses_visual_confirmation_gate`: false (no UI). **Hit the abort criterion on first run** — templates assumed UI exists. Skill fix landed in commit `a30d008` (gate visual-confirmation content on `uses_visual_confirmation_gate`); re-ran cleanly.
- [x] Confirm hooks-emission logic produces only the appropriate hooks for this repo type. Verified: `block-deploy-cli.sh` not emitted (`deploy_target_has_cli_conflict=false`), `block-worktree.sh` not emitted (`uses_visual_confirmation_gate=false`), `block-env-commit.sh` emitted (universal). `.claude/settings.json` parses; hook chmod +x.
- [x] Preserve and integrate existing files: `docs/retros/2026-05-10-*.md`, this `ROADMAP.md`, `docs/html-over-markdown-brief.md` — all untouched. Templated ROADMAP staged to `/tmp/dogfood-prd-to-product/ROADMAP.md.template-output` for reference.
- [x] Decide on conditional patterns: included `PARKING_LOT.md` (env_pattern doubled-period + output-small staleness from Phase 1 already captured), `FUTURE.md` (Phase 3 will populate), `DECISIONS_ACTIVE.md` (D-001 markdown-only, D-002 direct-on-main, D-003 no-UI gate).
- [x] Run `/session-start` and confirm the orientation flow makes sense for this repo. Walked the steps; orientation is coherent (AGENTS.md → ROADMAP → latest retro → PARKING_LOT → DECISIONS_ACTIVE).
- [x] Write the phase retro to `docs/retros/2026-05-10-phase-2-quick-wins-and-dogfood.md`.

**Done when:**
1. Quick-wins commit landed and pushed.
2. Repo has working `AGENTS.md`/`CLAUDE.md`/`.claude/rules/`/`.claude/settings.json` consistent with the skill's current state.
3. `/session-start` produces useful orientation.
4. Existing roadmap, retros, and HTML brief are preserved.
5. Phase retro is written and the dog-food commit is pushed.

**Abort criterion:** if the dog-food scaffold reveals that the skill's intake or decision logic does not handle the "skill-development workspace" project shape (e.g., it assumes UI exists, requires a deploy target, breaks on `stack: other`), halt. Update the skill to handle the shape, then re-run. Do not hand-edit the scaffolded output to make it work.

**Improvisation policy:** if during the dog-food run the user notices a file that would help (e.g., `CONVENTIONS.md`, a `.claude/agents/` directory) but is not part of the skill's current output, **do not add it ad-hoc**. Capture the observation in `docs/PARKING_LOT.md` for Phase 3 or later consideration. The principle is preserved: the generator scaffolds; observations during use feed the next iteration of the skill.

**Out of scope:** building any new product code. This is a docs/rules scaffold only. The generator does not write to `app/`, `lib/`, `components/`, etc.

---

## Phase 3: Skill ecosystem audit

**Goal:** apply Thariq's 9-category skill framework as a triage tool. Identify gaps, fix description fields. Do not fill skill gaps.

**Failure modes prevented:**

- Skill descriptions don't trigger reliably ("the description field is for the model, not a summary" — Thariq, *Lessons from Building Claude Code: How We Use Skills*).
- Missing skill categories where the user routes through prose every time. Most likely candidate: a verification skill, given the visual-confirmation gate is core to the workflow.

**Tasks:**

- [x] Read SKILL.md of every skill in `skills/`: `context-engineering`, `prd-creator`, `design-system-bootstrap` (and any others). For each, audit the `description` field against the "describes when to trigger this" standard. Edits land **directly in each skill's `SKILL.md` file** (replacing summary-shaped descriptions with trigger-shaped ones). Commit each edit with a short note on what was wrong. **Audit result (2026-05-10): all three descriptions were already trigger-shaped — verb phrases, "Use when…" exemplars, explicit negative cases. No edits needed.** (The `brand-voice` reference originally on this line was struck — see Phase 3 retro; the installed `brand-voice:*` plugins are upstream Anthropic, not this repo's work.)
- [x] Categorize each skill against Thariq's 9 categories: Library/API Reference, Product Verification, Data Fetching, Business Process Automation, Code Scaffolding, Code Quality/Review, CI/CD, Runbooks, Infrastructure Ops. **Result: all three skills land in Code Scaffolding; eight categories are uncovered.**
- [x] Document the category gaps in **`docs/FUTURE.md`** (created in Phase 2). For each gap, write one line: "Category X — gap exists / no real failure yet" or "Category X — gap exists, real failure: [specific moment]." Only the gaps with a real failure become candidates for future skill development.
- [x] Drain `docs/PARKING_LOT.md` items captured during Phase 2's dog-food. Each becomes either: (a) a Phase 4+ task, (b) a `FUTURE.md` entry, or (c) closed as "not a real concern."
- [x] Write the phase retro to [`docs/retros/2026-05-10-phase-3-ecosystem-audit.md`](docs/retros/2026-05-10-phase-3-ecosystem-audit.md).

**Done when:** all skill descriptions are trigger-shaped (or confirmed already are), gaps are documented in `FUTURE.md` with real-failure annotations where applicable, parking-lot is drained, retro is written.

**Abort criterion:** if the audit reveals that two or more skills have overlapping/conflicting trigger phrases (Claude can't tell them apart), halt. Resolve trigger ambiguity before continuing — that is a real failure mode that affects every session, not a future-work item.

**Out of scope:** building any new skill. This is triage only.

---

## Phase 4: Regenerate small, medium and large abbreviated examples

**Goal:** the example outputs (`skills/context-engineering/examples/output-small/`, `output-medium-abbreviated.md`, `output-large-abbreviated.md`) reflect pre-refinement output. Bring them current.

**Failure modes prevented:**

- Users reading the examples see stale patterns (Vercel hardcoded, 5-item recency block, no Commands section, no hooks scaffold, divergent `settings.json` "//" comment fields and hook-script bodies). They scaffold projects that don't match what the skill now produces.

**Tasks:**

- [x] Regenerate `output-small/` reflecting current parameterized template output: refresh the `"//"` comment fields in `settings.json` and the comment headers + echo bodies in the three hook scripts so they match what the templates emit today. In-phase scope expansion: surfaced a markdown-vs-shell `env_pattern` ambiguity (literal backticks would trigger command substitution); resolved by making `env_pattern` plain strings at the source with markdown consumers wrapping at the substitution site. Doubled-period [FUTURE.md](docs/FUTURE.md) watch item hit second instance and was fixed per continuous-mode discipline.
- [x] Regenerate `output-medium-abbreviated.md` reflecting current state. **Project replaced:** `craft-letters` (Vite+Cloudflare Pages, modular shape via the voice-and-tone trigger, one AI surface, basic styling). Transcript companion regenerated alongside.
- [x] Regenerate `output-large-abbreviated.md` reflecting current state. **Project replaced:** `triage-classifier` (Python service on Fly.io, modular via three AI surfaces, no UI, no voice-and-tone). Demonstrates the four-flag structural suppression cascade. Transcript companion regenerated alongside.
- [x] Pick a different stack for at least one example. **Both medium and large are non-Vercel** (Cloudflare and Fly). Result is stronger than the original ROADMAP suggestion of "at least one."
- [x] Confirm small/medium/large form a coherent progression in scale. Coverage map documented in [Phase 4 retro](docs/retros/2026-05-10-phase-4-regenerate-examples.md): small=flat-baseline, medium=modular+voice+UI+non-Vercel, large=modular+3-surfaces+no-UI+structural-suppressions. Deliberate uncovered shapes (modular+UI+Vercel, flat+non-Vercel) also recorded.
- [x] Write the phase retro to [`docs/retros/2026-05-10-phase-4-regenerate-examples.md`](docs/retros/2026-05-10-phase-4-regenerate-examples.md).

**Done when:** all three example outputs reflect current skill state, at least one of medium/large demonstrates non-Vercel parameterization, retro is written. **Met.**

**Abort criterion:** if regenerating a medium or large example surfaces a skill gap (e.g., the generator has no template for a pattern the example needs), halt and capture in `docs/PARKING_LOT.md`. Decide whether to add the template now (extending the phase scope) or skip the example shape until later. **Triggered once** (the `env_pattern` markdown-vs-shell ambiguity during task 1 regen); resolved in-phase per the criterion's "add the template now" branch. Resolution recorded in Phase 4 retro.

---

## Continuous mode (after Phase 4)

The skill enters maintenance mode. Triggers for new edits:

- A real failure mode lands during dog-fooded session work. Capture in `docs/PARKING_LOT.md`. Fix when the second instance hits (one-off failures may not be the rule's fault; patterns are).
- A Claude Code feature ships that obsoletes a current pattern (e.g., agent teams become non-experimental, `/init` interactive flow becomes default, hook contract changes).
- A new piece of evidence appears (peer-reviewed paper, Anthropic insider article, etc.). Apply the same hype-vs-substance discipline used in the initial refinement: trace each adoption to a specific failure mode the skill should prevent. Cite sources inline so future-you can re-check claims that age.

Do not edit the skill on speculation. The discipline is the skill's own principle: every paragraph earns its tokens, every rule names a specific failure mode.

---

## Open decisions

Decisions deferred until more information is available. Move into `docs/DECISIONS.md` when resolved (Phase 2 creates that file).

- **Should `prd-creator` and `design-system-bootstrap` switch to HTML output?** Pending HTML-over-Markdown investigation in [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md). Do not pre-decide.
- **Verification skill: build, defer, or skip?** Phase 3 documents the gap. The decision to build comes in continuous mode if real failures pile up. For now, the visual-confirmation gate plus hooks covers most of the safety surface.
- **When does `agent teams` move from experimental to standard, and what does that change for the skill?** Watch upstream Claude Code releases.
- **Should there be on-demand hook scaffolds in the skill?** Phase 2 documents the principle but does not scaffold an example. Pending a real failure mode (e.g., user repeatedly hits a moment where a scoped `/careful` would have helped). Until then, the principle is enough.

## Parallel work

- The HTML-over-Markdown investigation ([`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md)) is parallel-eligible. Run in its own session whenever convenient. Branch only if it produces edits to skill files that overlap with main-branch skill-refinement work.
- Phases 1 through 4 are sequential. Each builds on prior state in the same files. Branches and parallel agents do not help.

## Cross-references

- Skill source: [`skills/context-engineering/`](skills/context-engineering/).
- Most recent session retro: `docs/retros/` (read at session start before doing any work).
- Mid-session deferred items: `docs/PARKING_LOT.md` (created in Phase 2).
- Decisions log: `docs/DECISIONS.md` (created in Phase 2).
- Long-horizon items: `docs/FUTURE.md` (created in Phase 2 if Phase 3 surfaces gaps; otherwise unused).
- HTML-over-Markdown investigation: [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md).
