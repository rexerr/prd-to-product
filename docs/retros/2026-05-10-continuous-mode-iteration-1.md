# Retro — 2026-05-10 — Continuous-mode iteration 1

Phase 4 closed the planned skill-refinement work; the skill entered continuous-mode maintenance per [ROADMAP.md "Continuous mode after Phase 4"](../../ROADMAP.md). This is the first continuous-mode iteration, kicked off by an option-2 audit (read `principles.md` and `decisions.md` directly against the project's existing context, no skill invocation) of `the-council`, a hand-built project that predates the skill.

This iteration is **analysis-only**: the audit was performed and synthesized in-conversation, but no skill changes shipped this session. Action queued for follow-up sessions, captured below.

## What was done this session

- Drafted an option-2 audit prompt (the "read principles directly, no skill invocation" path).
- Ran the audit in a separate session on `the-council`. Output saved to `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` (external repo).
- Synthesized findings against continuous-mode promotion criteria.
- Queued three follow-up sessions (A, B, C below) with self-contained prompts.

No code, no template edits, no skill changes. This session is the analysis-and-cache-transfer step before acting.

## What surfaced

Audit findings sorted by promotion status against the [ROADMAP "Continuous mode" criteria](../../ROADMAP.md) (real failure mode in dog-fooded session work; pattern requires second instance unless single-instance evidence is high-conviction).

### Promoted (act-now)

1. **DECISIONS_ACTIVE per-decision-criterion violations.** Both `prd-to-product` (own-validation, logged in `skills/context-engineering/generator/decisions.md:336-338`) and `the-council` mirror all decisions rather than applying the skill's per-decision "follow now / not visible from code / not superseded" criterion. The skill is self-aware of the first violation and hasn't acted. Two real projects in a row do the same thing → second-instance threshold met. **Resolution direction:** either sharpen the per-decision criterion's framing in the template (so users actually apply it), or relax it (concede that conservative mirroring is fine and simplify the rule). Decision on which lives in session C.

2. **Hooks-defaults-as-forcing-function principle.** `the-council`'s `git-and-deploy.md` cites recurring failure modes (env commit, deploy CLI, worktree) by name, but the project has no `.claude/settings.json` and no `.claude/hooks/` directory. The author *knew* the failure modes were recurring and still hand-built only the prose layer. The skill's default is `enforce_rules_as_hooks: true`, so a skill-scaffolded project would have faced the question; a hand-built project never did. **One instance, but high-conviction** — the data is unambiguous (failure modes documented in the project's own prose; hook layer absent), and the principle is the skill's central claim. **Resolution direction:** add a paragraph to `skills/context-engineering/principles.md` documenting "defaults as forcing function" with `the-council` cited as the empirical evidence. Lands in session C.

### Open as design question (not act-immediately)

3. **Workflows-with-PRD-pointer middle path.** Current PRD-redundancy guard in `decisions.md` is binary: PRD-pointer shape (when PRD exists) vs full inline description (when it doesn't). `the-council` demonstrates a third shape that's actually useful: one-line tagline → "See `docs/PRD.md`" → keep the workflow bullet list, drop the description paragraph. Workflows-at-orientation are concrete enough to earn their tokens; the description paragraph is the actual redundancy. The current rule is over-strict. **Open as a design question** — not promoted to act-now because the third shape's edge cases (when does the workflow list belong in AGENTS vs only in PRD; what counts as a "workflow" worth listing) aren't cooked. Lands in session B. **Resolved 2026-05-10 in session B** — see [`2026-05-10-workflows-prd-third-shape.md`](2026-05-10-workflows-prd-third-shape.md). Three-way guard on `len(workflows)`: 0–1 pointer-only, 2–5 pointer-plus-workflows, 6+ pointer-only (list lives in PRD).

### Watch (one instance, awaiting pattern)

4. **`session-discipline.md` canonical-section coverage.** `the-council`'s hand-built file is missing three canonical sections (Read before you write, Checkpoint between phases, Session management). Likely accidental from manual transcription, but one instance only. Promotes to act-now if a second hand-built project shows the same gap. The audit's open-question 3 makes this the highest-priority project-side fix for `the-council` itself, separate from the skill question.

5. **Recency-block dilution.** `the-council`'s "Before you respond" block has 7 items, with 3 (direct-on-main, no deploy CLI, reproduce-before-fixing) duplicating body content. `principles.md` explicitly says not to do this; the project did it anyway, possibly intentional given documented failure history. One instance, possibly project-specific. Promotes if a second project does the same — would mean the rule's framing isn't strong enough. Stays in watch.

6. **Audit-skill template.** The option-2 audit produced cleaner structure than the skill's own Phase 2 self-validation: inferred intake → missing files (load-bearing vs cosmetic) → drifted (intentional vs accidental) → present and correct → open questions for follow-up. One use of this structure. If session A produces the same shape on a different project, that's the audit-skill template — promotes to a continuous-mode skill candidate.

## Key decisions made this session

- **No "Phase 5."** Continuous mode doesn't have phases — it has evidence-gated edits. Promoted items act now; design questions open; watch items wait. The roadmap explicitly transitioned to this mode at the end of Phase 4; this iteration is the first proof that the discipline works.
- **Retro before next-action.** Three reasons for ending this session and writing the retro now: (a) this conversation is ~30k tokens of analysis chatter, exactly the cache-rot zone the Phase 4 retro flagged; (b) per the session-management rules shipped in Phase 2 (Thariq), "start a new session for a new task" — acting on the audit *is* a new task; (c) the retro is the cache transfer — next sessions load this file + the audit + AGENTS/CLAUDE and start cold-fresh.
- **Three follow-up sessions queued, ordering user-decided.** Sessions A (second audit), B (workflows-PRD design), and C (act on promoted items). C could land before A (act on what's promoted), after A (act on union of evidence including newly-promoted watch items), or after both (act on full picture). User choice. Prompts for A and B are appended below; C's prompt depends on whether A surfaces additional promotions and is therefore deferred.

## Next sessions queued

### Session A — Second-project audit

Run the same option-2 audit on a different hand-built project. Goal: sharpen the three watch items by gathering a second instance (or ruling them out). Output: a second `context-audit-*.md` in that project's `docs/`. Discussion of findings happens after that session lands.

Prompt is in this retro's appendix-A below.

### Session B — Workflows-PRD middle-path design

Design the third shape for "What this project is" so `decisions.md` can encode it. Inputs: `the-council`'s pattern, the current binary in `decisions.md`, the audit's proposed middle-path text. Output: a proposed `decisions.md` update (or a brief in `docs/` if the design isn't ready to land in templates).

Prompt is in this retro's appendix-B below.

### Session C — Act on promoted items (DECISIONS_ACTIVE + hooks-defaults principle)

Small commit applying items 1 and 2. Timing: user decides whether to do this before A (act on what's already promoted), after A (act on union of evidence), or after both A and B (act on full picture). Prompt is deferred until the ordering question is decided — A may promote watch items 4–6 to act-now, in which case C's scope expands.

## References

- `the-council` audit: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` (external repo, link will not resolve from prd-to-product).
- Continuous-mode discipline: [ROADMAP.md](../../ROADMAP.md) "Continuous mode after Phase 4."
- DECISIONS_ACTIVE first-violation log: `skills/context-engineering/generator/decisions.md:336-338`.
- Source-of-truth precedence rule (project wins over skill for that project's own files): applied throughout the audit.
- Phase 4 retro flagging session-size as a watch pattern: [`docs/retros/2026-05-10-phase-4-regenerate-examples.md`](2026-05-10-phase-4-regenerate-examples.md).

---

## Appendix A — Session A prompt (second-project audit)

Paste into a fresh Claude Code session opened in the target project's directory. **First, choose the target project.** Best evidence value comes from:

- **Hand-built, not scaffolded by `context-engineering`** (otherwise the audit only confirms the skill emits what it emits).
- **Different shape from `the-council`** if possible — `the-council` is modular + Next.js + 3 AI surfaces + voice-and-tone + UI. A flat-shape project, a no-AI project, or a non-Vercel stack would test whether the watch items are shape-specific or universal.
- **Mature enough to have real context files** — at least an `AGENTS.md` or `CLAUDE.md` plus some structure. Greenfield projects produce a "nothing exists" audit, which is less useful for sharpening the watch items.

Prompt body:

> Audit this project's AI-context structure (`CLAUDE.md`, `AGENTS.md`, `.claude/`, `docs/`) against the standards in the `context-engineering` skill at `/Users/rexc/Sites/prd-to-product/skills/context-engineering/`.
>
> **Background:** `context-engineering` is a skill that scaffolds AI-context for new AI-assisted coding projects. Its principles, templates, and decision logic encode an opinionated standard. This project wasn't scaffolded by the skill, so I want to see where it diverges from the standard and whether the divergences are intentional (project-specific choices) or accidental drift. This is the second audit of its kind; the first was on `the-council`, written up at `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` — read that first to understand the structure I want.
>
> **Read in this order:**
> 1. The `the-council` audit at `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` — for the audit shape and the watch items I'm trying to sharpen.
> 2. `/Users/rexc/Sites/prd-to-product/skills/context-engineering/SKILL.md` — what the skill does and when it triggers.
> 3. `/Users/rexc/Sites/prd-to-product/skills/context-engineering/principles.md` — the standards behind every template choice. Each rule cites the failure mode it prevents.
> 4. `/Users/rexc/Sites/prd-to-product/skills/context-engineering/generator/decisions.md` — the decision logic.
> 5. `/Users/rexc/Sites/prd-to-product/skills/context-engineering/examples/output-small/` — a complete worked example for the flat shape.
> 6. Then look at this project: `CLAUDE.md`, `AGENTS.md`, `.claude/`, `docs/`, plus enough of the source tree to infer stack and shape.
>
> **Produce a drift report** with the same structure as `the-council` audit:
> 1. Inferred intake answers (table format).
> 2. Missing files (load-bearing vs cosmetic).
> 3. Present but drifted (intentional vs accidental, with judgment).
> 4. Present and correct.
> 5. Open questions for the post-audit discussion.
> 6. Notes on what was *not* checked.
>
> **Pay specific attention to three watch items from the first audit** (these are what I'm trying to sharpen):
> - Does this project's `session-discipline.md` (if it has one) match the canonical section coverage, or is it missing canonical sections?
> - Does this project's "Before you respond" recency block (if it has one) duplicate body content?
> - Are the audit's findings on this project the same shape as `the-council`'s, or does this project surface a class of drift the first audit didn't?
>
> **Do not write any fixes.** I want the report first; we'll decide what to fix in a follow-up.
>
> **Project autonomy clause:** if this project's files contradict the skill's recommendation, treat the project's file as the source of truth for that project. Flag the divergence so I see it; don't recommend overwriting without asking.
>
> Save the report to `docs/context-audit-2026-05-10.md` (or whatever this project's `docs/` directory is called). If the project has no `docs/`, save it to the project root and we'll move it later.

---

## Appendix B — Session B prompt (workflows-PRD middle-path design)

Paste into a fresh Claude Code session opened in `/Users/rexc/Sites/prd-to-product`.

> Design the third shape for AGENTS.md's "What this project is" section in the `context-engineering` skill, and propose the `decisions.md` update that encodes it.
>
> **Background:** the current `decisions.md` "PRD redundancy guard" is binary. When `source_prd_present == true`, "What this project is" becomes a one-line tagline + `See docs/PRD.md`. When false, the section gets a full inline description. The audit on `the-council` (at `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`, line 99-105 of the drift section) demonstrates a useful third shape: one-line tagline → `See docs/PRD.md` → workflow bullet list → drop the description paragraph. Workflows are concrete and useful at orientation; the description paragraph is the actual redundancy. The retro at [`docs/retros/2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md) item 3 captures this as an open design question.
>
> **Read in this order:**
> 1. This retro: [`docs/retros/2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md). Item 3 is the design question.
> 2. The audit excerpt: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` lines 99–105 (the "What this project is" drift section).
> 3. Current rule: [`skills/context-engineering/generator/decisions.md`](../../skills/context-engineering/generator/decisions.md) "PRD redundancy guard" (search for `source_prd_present`).
> 4. The reasoning behind the rule: [`skills/context-engineering/principles.md`](../../skills/context-engineering/principles.md) — search for "redundancy" and the AGENTS.md paper's "2.7% improvement when README is removed" finding.
> 5. The relevant template: [`skills/context-engineering/templates/AGENTS.md.template`](../../skills/context-engineering/templates/AGENTS.md.template) — find the "What this project is" section.
>
> **Design questions to answer:**
> 1. **When does the workflow list belong in AGENTS vs only in PRD?** the-council's workflows are short, concrete user flows. A project with 12 workflows might want the list in PRD only. What's the threshold?
> 2. **What counts as a "workflow" worth listing in AGENTS?** PRD has user stories, use cases, scenarios — which of those promote to AGENTS-level orientation?
> 3. **Does the redundancy argument from the AGENTS.md paper still apply when the workflows are in AGENTS but the description isn't?** The paper found 2.7% degradation from README+CLAUDE.md duplication — does workflow-list-only avoid the same failure mode, or just reduce it?
> 4. **What's the intake question that surfaces the new shape?** Currently the skill asks `source_prd_present` (yes/no). Does it now also need `include_workflow_list_in_agents` (yes/no), or is that derivable from existing answers (e.g., if `len(workflows) > 1`)?
> 5. **Does this change anything about the flat-shape projects?** Or is it modular-only?
>
> **Output:** a proposed update to `decisions.md` "PRD redundancy guard" that encodes the third shape, plus any necessary updates to `intake.md` (new question or renamed existing one), plus a one-line addition to `principles.md` if the principle changes. If the design isn't ready to land in templates, write it as a brief at `docs/workflows-prd-redundancy-brief.md` and queue the implementation for a follow-up session.
>
> **Hard scope:** ≤ 3 files for the design pass; ≤ 100 lines of edits. If the design balloons beyond that, halt and surface the conflict — likely means the design isn't cooked and needs more shape from real-project evidence.
