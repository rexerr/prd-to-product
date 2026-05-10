# Roadmap — prd-to-product

What's left, in priority order. Read this at the start of every session alongside the most recent retro in `docs/retros/`.

Check off tasks as they are completed. Mark phases done only when all tasks are checked and the done-when criteria is met.

This roadmap covers refinement of the `context-engineering` skill, applying it to this repo (eat the dog food), and entering continuous-maintenance mode. A separate scope — HTML-over-Markdown investigation — is captured in [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md) and runs in parallel.

## Phasing principles

- **One phase = one session.** End every phase with a retro in `docs/retros/`. Start the next phase fresh.
- **Direct-on-main, no branches.** Skill-refinement phases are sequential and touch the same files; branches add friction. Branches only for genuinely parallel work (e.g., the HTML investigation if it edits skill files).
- **Each phase passes the failure-mode test.** Before starting, name the specific mistake the phase prevents. If you can't, defer.
- **Each phase delivers something committable.** No half-finished phases on `main`.

---

## Phase A: Skill quick wins (session-management + on-demand hooks)

**Goal:** close the high-confidence gaps surfaced from Thariq's *Lessons from Building Claude Code* articles. Concrete edits, ~20 lines total.

**Failure modes prevented:**

- Re-prompting "that didn't work, try X" instead of `/rewind` — wastes context, accumulates failed attempts in the prefix.
- Autocompact firing during a long debug session and producing a bad summary because the model is at peak context-rot.
- Treating all hooks as "always-on," missing the on-demand `/careful`-style pattern for risky operations.
- Not knowing the context-rot threshold (~300–400k tokens) and missing the moment to compact proactively.

**Tasks:**

- [ ] Add three bullets to `skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template` and the flat-CLAUDE template: rewind > re-prompt; new session for new task; compact proactively during long debug.
- [ ] Add one paragraph to `skills/context-engineering/principles.md` "Always-on patterns" section describing always-on vs on-demand hooks. Don't try to make every hook always-on; on-demand is for risky operations you don't want enforced all the time (e.g., `/careful` blocking `rm -rf`, `DROP TABLE`, force-push only when invoked).
- [ ] Add one line to `principles.md` (in "Position-aware placement" or a new "Context budget" subsection) noting the ~300–400k token rot threshold from Anthropic's own published observations.
- [ ] Update `skills/context-engineering/examples/output-small/CLAUDE.md` to reflect the new bullets.
- [ ] Write the phase retro before closing the session.

**Done when:** new bullets and paragraph are in templates, the small example is updated, retro is written, all changes committed and pushed.

**Out of scope:** new templates, new on-demand hook scaffolds (those become Phase F+ if a real failure mode lands).

---

## Phase B: Eat the dog food (run the skill on this repo)

**Goal:** scaffold `AGENTS.md`, `CLAUDE.md`, `.claude/rules/`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/retros/` (with this repo's existing retro migrated), `ROADMAP.md` (replacing this file's content via the generator), and optional `PARKING_LOT.md` / `FUTURE.md` for `prd-to-product/` itself.

**Failure modes prevented:**

- Future sessions re-derive context every time (already paying this cost).
- Skill changes ship without being road-tested in real usage.
- Inconsistency between the skill's recommendations and the repo authoring it ("the cobbler's children have no shoes" antipattern).

**Tasks:**

- [ ] Run `context-engineering` skill on this repo. Stack: probably `other` or `node-cli` (this is a skill-development workspace, not a deployed app). Deploy target: `none`. Visual confirmer: user. Visual-confirmation gate: probably `false` since there's no UI.
- [ ] Confirm hooks-emission logic produces only the appropriate hooks for this repo type. The deploy-CLI hook should NOT emit (no deploy target). The worktree-blocker hook should NOT emit (no visual confirmation gate). The env-commit hook still emits.
- [ ] Migrate `docs/retros/2026-05-10-context-engineering-skill-refinement.md` into the new scaffolded structure if the location changes.
- [ ] Decide on conditional patterns: include `PARKING_LOT.md` and `FUTURE.md` (skill is genuinely evolving). Include `DECISIONS_ACTIVE.md` if there are binding constraints not visible from code.
- [ ] Confirm `ROADMAP.md` content from this file is preserved or merged with the generator's output.
- [ ] Confirm `docs/html-over-markdown-brief.md` is preserved.
- [ ] Run `/session-start` (if scaffolded) and confirm the orientation flow makes sense.
- [ ] Write the phase retro.

**Done when:** repo has working `AGENTS.md`/`CLAUDE.md`/`.claude/rules/` consistent with the skill's current state. `/session-start` produces useful orientation. All changes committed and pushed.

**Out of scope:** building any new product code. This is a docs/rules scaffold only. The generator does not write to `app/`, `lib/`, `components/`, etc.

---

## Phase C: Open items from prior retro (regression + verification)

**Goal:** clear validation items left in `docs/retros/2026-05-10-context-engineering-skill-refinement.md` that are not new features.

**Failure modes prevented:**

- Stack-parameterization changes silently break the modular shape (only the small/flat shape was validated previously).
- Hook contract assumptions drift from upstream Claude Code without notice.

**Tasks:**

- [ ] Generator dry-run on a hypothetical non-Vercel modular project (e.g., React Vite SPA on Cloudflare Pages with 2 AI surfaces). Confirm: paired-write rules emit modular templates, recency renumbering still works for items 3–4, `paths:` frontmatter substitution produces parseable YAML, `OPTIONAL` blocks gate cleanly.
- [ ] Live-test each emitted hook in a throwaway session. Try `vercel deploy`, `git add .env.local`, `git worktree add ../foo`. Confirm each blocks with the expected message. If a block does not fire, debug and fix.
- [ ] Generator dry-run on the original Vercel/Next.js case to confirm no regressions vs the current small example.
- [ ] Write the phase retro.

**Done when:** all three dry-runs produce expected output, all hooks fire as designed, retro is written.

**Out of scope:** regenerating the medium/large abbreviated examples (Phase E).

---

## Phase D: Skill ecosystem audit

**Goal:** apply Thariq's 9-category skill framework as a triage tool. Identify gaps; do not fill them.

**Failure modes prevented:**

- Skill descriptions don't trigger reliably ("the description field is for the model, not a summary" — Thariq).
- Missing skill categories where the user routes through prose every time. Most likely candidate: a verification skill, given the visual-confirmation gate is core to the workflow.

**Tasks:**

- [ ] Read SKILL.md of every skill in `skills/`: `context-engineering`, `prd-creator`, `design-system-bootstrap`, `brand-voice` and any others. Audit each `description` field against the "describes when to trigger this" standard. Edit if descriptions are summary-shaped instead of trigger-shaped.
- [ ] Categorize each skill against Thariq's 9 categories: Library/API Reference, Product Verification, Data Fetching, Business Process Automation, Code Scaffolding, Code Quality/Review, CI/CD, Runbooks, Infrastructure Ops.
- [ ] Document the category gaps in `docs/FUTURE.md` (or `PARKING_LOT.md` if mid-session). Identify the one or two gaps that map to a real, repeated failure the user has hit.
- [ ] Write the phase retro.

**Done when:** all skill descriptions are trigger-shaped, gaps are documented in `FUTURE.md`, retro is written.

**Out of scope:** building any new skill. This is triage only.

---

## Phase E: Regenerate medium and large abbreviated examples

**Goal:** the abbreviated example outputs (`skills/context-engineering/examples/output-medium-abbreviated.md`, `output-large-abbreviated.md`) reflect pre-refinement output. Bring them current.

**Failure modes prevented:**

- Users reading the examples see stale patterns (Vercel hardcoded, 5-item recency block, no Commands section, no hooks scaffold). They scaffold projects that don't match what the skill now produces.

**Tasks:**

- [ ] Regenerate `output-medium-abbreviated.md` reflecting current state.
- [ ] Regenerate `output-large-abbreviated.md` reflecting current state.
- [ ] Pick a different stack for at least one example (e.g., medium = Next.js + Vercel as today; large = something non-Vercel like Python ML on Fly, to demonstrate parameterization).
- [ ] Confirm small/medium/large form a coherent progression in scale.
- [ ] Write the phase retro.

**Done when:** both abbreviated examples reflect current skill state, at least one demonstrates non-Vercel parameterization, retro is written.

---

## Continuous mode (after Phase E)

The skill enters maintenance mode. Triggers for new edits:

- A real failure mode lands during dog-fooded session work. Capture in `docs/PARKING_LOT.md`. Fix when the second instance hits (one-off failures may not be the rule's fault; patterns are).
- A Claude Code feature ships that obsoletes a current pattern (e.g., agent teams become non-experimental, `/init` interactive flow becomes default, hook contract changes).
- A new piece of evidence appears (peer-reviewed paper, Anthropic insider article, etc.). Apply the same hype-vs-substance discipline used in the initial refinement: trace each adoption to a specific failure mode the skill should prevent.

Do not edit the skill on speculation. The discipline is the skill's own principle: every paragraph earns its tokens, every rule names a specific failure mode.

---

## Open decisions

Decisions deferred until more information is available. Move into `docs/DECISIONS.md` when resolved.

- **Should `prd-creator` and `design-system-bootstrap` switch to HTML output?** Pending HTML-over-Markdown investigation in [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md). Do not pre-decide.
- **Verification skill: build, defer, or skip?** Phase D documents the gap. The decision to build comes in continuous mode if real failures pile up. For now, the visual-confirmation gate plus hooks covers most of the safety surface.
- **When does `agent teams` move from experimental to standard, and what does that change for the skill?** Watch upstream Claude Code releases.

## Parallel work

- The HTML-over-Markdown investigation ([`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md)) is parallel-eligible. Run in its own session whenever convenient. Branch only if it produces edits to skill files that overlap with main-branch skill-refinement work.
- Phases A through E are sequential. Each builds on prior state in the same files. Branches and parallel agents do not help.

## Cross-references

- Skill source: [`skills/context-engineering/`](skills/context-engineering/).
- Most recent session retro: `docs/retros/` (read at session start before doing any work).
- Mid-session deferred items: `docs/PARKING_LOT.md` (created in Phase B).
- Decisions log: `docs/DECISIONS.md` (created in Phase B).
- Long-horizon items: `docs/FUTURE.md` (created in Phase B if Phase D surfaces gaps).
- HTML-over-Markdown investigation: [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md).
