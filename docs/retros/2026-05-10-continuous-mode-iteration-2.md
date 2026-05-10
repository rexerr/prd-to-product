# Retro — 2026-05-10 — Continuous-mode iteration 2

Second iteration of continuous-mode. Triggered by completion of session A (second-project audit on `field-society-demo`) from [iteration-1](2026-05-10-continuous-mode-iteration-1.md)'s queued sessions. Synthesizes audit results, updates promotion status of all six items from iteration 1, queues two follow-up sessions (C with expanded scope; new D for audit-skill design).

Analysis-only session. No skill changes ship in this commit; session B's separate commit (workflows-PRD third shape) lands in parallel.

## What was done this session

- Reviewed second audit at `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md` (external repo).
- Synthesized findings against iteration-1's six items (2 promoted, 1 design-question, 3 watch).
- Updated promotion status: 2 watch items promoted to act-now, 1 design question resolved (in session B), 1 promoted item course-corrected to lower-urgency, 1 newly opened design question for the audit skill itself.
- Drafted updated prompts for session C (expanded scope, 4 act-now items now) and new session D (audit-skill design).

## What surfaced in the second audit

Six iteration-1 items, status after audit 2:

### Originally promoted, status updates

1. **DECISIONS_ACTIVE per-decision criterion** — *course corrected.* Field-society-demo correctly curated 3 of 9 decisions per the criterion; the-council bulk-mirrored. So the criterion *works* when applied carefully; the-council was the failure, not the rule. Resolution direction shifts from "sharpen-or-relax" to "sharpen template framing only" — small change, lower urgency. Stays in session C.

2. **Hooks-defaults-as-forcing-function principle** — *evidence strengthened.* Field-society-demo also has prose-cites-failures + hooks-absent. Two instances now of identical shape. Conviction was already high; now incontrovertible. Stays in session C.

### Originally a design question, now resolved

3. **Workflows-with-PRD-pointer middle path** — *resolved in session B.* Three-way guard on `len(workflows)` landed in `decisions.md` and `principles.md`. See [`2026-05-10-workflows-prd-third-shape.md`](2026-05-10-workflows-prd-third-shape.md). Field-society-demo (which has 0 workflows in pointer position; sits at the lower threshold edge) didn't change session B's design but reinforces that the binary collapse was the right thing to fix.

### Originally watch, now promoted

4. **`session-discipline.md` three-section gap** — *promoted to act-now.* Same three sections (Read before you write / Checkpoint / Session management) absent in both projects. Identical hand-copy pattern. Two instances → systematic. *Resolution direction:* the canonical template *has* all three sections; the issue is that hand-builders systematically miss them. The fix is not a template change but a `principles.md` paragraph documenting the pattern, plus enforcement landing in session D's audit skill. Lands in session C.

5. **Recency-block dilution** — *promoted to act-now.* Same items 3–5 (direct-on-main / no deploy CLI / reproduce-before-fixing) duplicated in both projects. Two instances of the *same* items in the *same* positions. *Resolution direction:* either sharpen the existing template comment to call these three items out by name with reasoning, or concede that catastrophic-failure-mode items earn dual placement and update the principle. Recommend sharpening first; if a third project drifts the same way, change the principle. Lands in session C.

6. **Audit-skill template** — *promoted; gets its own session D.* Second use produced cleaner, comparable structure. Pattern is repeatable. Field-society-demo's audit explicitly suggests "the skill could expose a 'minimum required sections' checklist or a validator that runs against an existing project" (audit line 178) — natural starting design for the audit skill.

## Newly surfaced

- **Positive divergence on DECISIONS_ACTIVE.** Field-society-demo demonstrates the per-decision criterion works without skill scaffolding when carefully applied. First audited project where the discipline held without intervention. Useful empirical anchor — the discipline can be learned and held, isn't strictly hook-dependent. Worth one sentence in the session-C principles addition.
- **`codex_usage` divergence between projects.** The-council had `.codex/config.toml` + `.agents/skills/README.md`; field-society-demo doesn't. Probably project-specific (different stage of work). Not a skill issue.
- **Internal forward references at scaffold stage are fine.** Field-society-demo's `ARCHITECTURE.md` says `Stack: see package.json` but `package.json` doesn't yet exist. Audit correctly classified this as expected pre-Phase-1 state, not drift. Worth noting that the skill's emit-with-forward-refs pattern works.

## Updated session plan

Session A done. Session B done (separate commit). Two sessions queued.

### Session C — Act on four promoted items

Scope expanded from 2 to 4. All small. Single commit applying all four; total target ~50 lines across `principles.md` and `AGENTS.md.template`. Prompt in Appendix C below.

### Session D — Audit-skill design (new)

Design (or design-and-implement, scope-decision-first) the `context-engineering-audit` skill. Two real audits demonstrate the pattern is repeatable; field-society-demo's audit explicitly suggests the validator capability. Prompt in Appendix D below.

Either order is fine for C and D. They're independent.

## Key decisions made this session

- **DECISIONS_ACTIVE criterion isn't broken.** Field-society-demo proves it works when carefully applied. Resolution shifts from "decide direction" to "sharpen framing only." Lower-urgency, lower-cost.
- **Two-instance threshold met for session-discipline-three-section + recency-block-dilution.** Both promoted. Iteration-2 closes with zero items in watch — promote-or-act-or-rule-out, nothing dangling.
- **Audit-skill is a real continuous-mode candidate.** Two instances of the pattern producing comparable output → promotion criterion met. Session D queued.
- **Resolution direction for session-discipline-three-section is documentation, not template change.** Canonical template already has all three sections. The systematic miss is by hand-builders, not by the skill. Document the pattern; enforce in the audit skill.

## References

- Field-society-demo audit: `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md` (external repo).
- The-council audit: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` (external repo).
- Iteration-1 retro: [`2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md).
- Session B retro: [`2026-05-10-workflows-prd-third-shape.md`](2026-05-10-workflows-prd-third-shape.md).

---

## Appendix C — Session C prompt (act on four promoted items)

Paste into a fresh Claude Code session opened in `/Users/rexc/Sites/prd-to-product`.

> Act on four promoted items from continuous-mode iteration 2. Single small commit applying all four; total target ~50 lines across `principles.md` and `AGENTS.md.template`.
>
> **Read in this order:**
> 1. This iteration's retro: [`docs/retros/2026-05-10-continuous-mode-iteration-2.md`](docs/retros/2026-05-10-continuous-mode-iteration-2.md). Items 1, 2, 4, 5 are the four to act on.
> 2. Iteration-1 retro: [`docs/retros/2026-05-10-continuous-mode-iteration-1.md`](docs/retros/2026-05-10-continuous-mode-iteration-1.md). For original framing of items 1 (DECISIONS_ACTIVE) and 2 (hooks-defaults).
> 3. Both audits — the empirical evidence each item cites:
>    - `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`
>    - `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md`
> 4. Current files to edit: [`skills/context-engineering/principles.md`](skills/context-engineering/principles.md) and [`skills/context-engineering/templates/AGENTS.md.template`](skills/context-engineering/templates/AGENTS.md.template). Possibly also the modular template `skills/context-engineering/templates/claude-rules-modular/decisions-log.md.template` if it carries DECISIONS_ACTIVE framing.
>
> **The four items, in commit order:**
>
> 1. **Hooks-defaults-as-forcing-function** in `principles.md`. Add a paragraph documenting that the skill's `enforce_rules_as_hooks: true` default is a forcing function: scaffolded projects face the question, hand-built projects skip it. Cite both audits as evidence. ~15 lines.
> 2. **DECISIONS_ACTIVE template framing** in `AGENTS.md.template` (and modular template equivalent if it exists). Sharpen the per-decision criterion's framing so users actually apply it. Add a one-sentence positive example: field-society-demo's correct 3-of-9 curation as proof the criterion works without skill enforcement. ~10 lines.
> 3. **Session-discipline three-section gap** in `principles.md`. Add a paragraph noting that the three canonical sections (Read before you write / Checkpoint / Session management) are systematically missed by hand-builders (two-of-two audited projects). No template fix needed — canonical template has all three. This documents the pattern for session D's audit-skill design to enforce. ~10 lines.
> 4. **Recency-block dilution framing** in `AGENTS.md.template`. Sharpen the existing comment near the recency block to call out the three items by name (direct-on-main, no deploy CLI, reproduce-before-fixing) and explain why they belong in the body, not the recency block. Both audits show the same three items duplicated. ~15 lines.
>
> **Hard scope:** ≤ 3 files. ≤ 100 lines total. Single commit message naming all four items.
>
> **Verification:** re-read each edited file end-to-end. Confirm cross-references resolve. No code paths to dry-run.
>
> **Push:** do not push without asking.
>
> **Retro:** write a session-C retro at `docs/retros/2026-05-10-continuous-mode-session-c.md` summarizing what landed and any decisions made between the two-options framing for item 4 (sharpen-framing vs allow-dual-placement).

---

## Appendix D — Session D prompt (audit-skill design)

Paste into a fresh Claude Code session opened in `/Users/rexc/Sites/prd-to-product`.

> Design (or design-and-implement, scope decision first) the `context-engineering-audit` skill — a sibling to `context-engineering` that wraps the option-2 audit pattern.
>
> **Background:** two real audits used the same structure (inferred intake → missing → drifted → present → open questions, with explicit comparison to prior audit when applicable). The pattern is repeatable. Iteration-2 retro item 6 promotes this to a continuous-mode candidate.
>
> **Read in this order:**
> 1. Iteration-2 retro: [`docs/retros/2026-05-10-continuous-mode-iteration-2.md`](docs/retros/2026-05-10-continuous-mode-iteration-2.md). Item 6 is the rationale; "Session D" in the updated session plan is the scope.
> 2. Iteration-1 retro Appendix A: [`docs/retros/2026-05-10-continuous-mode-iteration-1.md`](docs/retros/2026-05-10-continuous-mode-iteration-1.md). The original audit prompt that produced both audits — encode this as the skill's procedure.
> 3. Both audits — the worked examples to reproduce:
>    - `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`
>    - `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md`
> 4. Sibling skill for naming and structure conventions: [`skills/context-engineering/SKILL.md`](skills/context-engineering/SKILL.md), [`skills/context-engineering/principles.md`](skills/context-engineering/principles.md).
>
> **Scope decision (decide first, then act):**
>
> - **Light (recommended for first pass):** `skills/context-engineering-audit/` as a sibling skill. `SKILL.md` (trigger phrases, when-to-use, when-not-to-use) + `procedure.md` (audit shape, reading order, output structure). The skill's job is to drive the option-2 pattern with no automation — same flow Claude follows when handed the prompt today, but triggerable as a skill. Output: drift report in the project's `docs/`.
> - **Heavy:** a real validator that programmatically reads `.claude/`, `docs/`, etc., and reports missing canonical sections + drift against templates. Tool, not pure skill. Larger surface — need to decide between Bash script, MCP wrapper, or Python.
>
> Recommend starting **light**. Document the heavier validator capability as future work in the new skill's `NOTES.md` or a brief, gated on real failure modes from skill use (third-instance discipline).
>
> **If light:** produce `skills/context-engineering-audit/SKILL.md` (trigger-shaped description: "Audit an existing project's AI-context structure against the context-engineering standard. Use when…"), plus `skills/context-engineering-audit/procedure.md` (the audit shape, reading order, output structure — reuse the iteration-1 Appendix A prompt as the backbone). Maybe a `principles.md` if the skill has its own opinions worth stating; maybe not.
>
> **If heavy:** write a brief at `docs/audit-skill-brief.md` first. Don't implement until the brief is reviewed.
>
> **Hard scope:**
> - Light path: ≤ 200 lines (small skill scaffold across SKILL.md + procedure.md).
> - Heavy path: ≤ 50 lines (brief only — defer implementation).
>
> **Push:** do not push without asking.
>
> **Retro:** write a session-D retro at `docs/retros/2026-05-10-continuous-mode-session-d.md` summarizing the scope decision (light vs heavy) and what landed.
