## Retro — 2026-05-10 — Continuous-mode session C: act on four promoted items

Acted on the four items promoted in [continuous-mode iteration 2](2026-05-10-continuous-mode-iteration-2.md). Single small commit applying all four. Two files touched: `skills/context-engineering/principles.md` and `skills/context-engineering/templates/AGENTS.md.template`. Total: 33 insertions, 1 deletion.

## What landed

1. **Hooks-defaults-as-forcing-function** (`principles.md`, new subsection after "Always-on hooks vs on-demand hooks"). Documents that `enforce_rules_as_hooks: true` is itself the mechanism — scaffolded projects face the question, hand-built projects skip it. Cites both audits (the-council, field-society-demo) as the two-instance evidence: each documented env-commit / deploy-CLI / worktree failures in prose and shipped zero `.claude/hooks/`. ~12 lines.
2. **DECISIONS_ACTIVE template framing** (`AGENTS.md.template`, comment block inserted between the active-decisions paragraph and the "A decision is significant if" list). Sharpens the per-decision mirror criterion with all-three-conditions framing and adds field-society-demo's correct 3-of-9 curation as a one-paragraph positive example. Template comment, not visible in scaffolded output. ~10 lines.
3. **Session-discipline three-section gap** (`principles.md`, new subsection between hooks-as-forcing-function and "Context budget"). Names the three sections systematically missed by hand-builders (Read before you write / Checkpoint / Session management) with field-society-demo + the-council as the two confirming instances. Frames the fix at the source, not per-project; calls out the audit-skill in `context-engineering-audit` (session D) as the enforcement layer. ~10 lines.
4. **Recency-block dilution sharpening** (`AGENTS.md.template`, comment guard added immediately before the "Before you respond" heading, plus a tightened explanatory sentence beneath the heading). Names the three items by name (direct-on-main, no deploy CLI, reproduce-before-fixing) and cites both audits as the dilution pattern. Names the safety valve (document an override as a decision in `docs/DECISIONS.md`) so the rule isn't absolute. ~15 lines of comment + a 1-sentence body tweak.

## The two-options decision on item 4

The iteration-2 retro framed item 4 as a choice between (a) sharpen framing in the existing template, or (b) concede that catastrophic-failure-mode items earn dual placement and update the principle. Chose **(a) sharpen framing**.

Reasons:

- iteration-2 explicitly recommended sharpen-first with "if a third project drifts the same way, change the principle" as the third-instance trigger. Two instances is enough to act, not enough to reverse the principle.
- The principle's reasoning still holds independent of how often it's violated. The U-shaped attention curve doesn't care whether the duplicated items prevent catastrophic failures — duplication still dilutes signal at the position the agent reads last.
- The override path is available: if a specific project's failure history justifies the cost, document it as a decision in `docs/DECISIONS.md`. That preserves the rule for the common case while leaving room for justified exceptions.
- Conceding dual placement would invert the rule (now seven items is canonical), which would cascade through `output-small/CLAUDE.md`, `output-medium-abbreviated.md`, `output-large-abbreviated.md`, and likely AGENTS.md itself in this repo. That's a larger blast radius than the evidence supports.

If a third project drifts the same way, revisit. The principle stays put for now.

## What's still queued

Session D — `context-engineering-audit` skill (light vs heavy scope decision first). Prompt in [iteration-2 retro Appendix D](2026-05-10-continuous-mode-iteration-2.md). Independent of session C; either order was fine. Now the only queued session.

## Where the watch items sit after session C

All six iteration-1 items are now closed-or-acted:

| # | Item | Resolved by |
|---|---|---|
| 1 | DECISIONS_ACTIVE per-decision criterion | Session C item 2 (template framing sharpened) |
| 2 | Hooks-defaults-as-forcing-function | Session C item 1 (principle added) |
| 3 | Workflows-with-PRD-pointer middle path | Session B ([retro](2026-05-10-workflows-prd-third-shape.md)) |
| 4 | Session-discipline three-section gap | Session C item 3 (principle added; enforcement queued for session D's audit-skill) |
| 5 | Recency-block dilution | Session C item 4 (framing sharpened) |
| 6 | Audit-skill template | Session D (queued) |

Continuous-mode discipline held. Watch → promote → act → close, with one item kicking forward to the audit skill rather than being directly enforced — the right shape, since enforcement at template-time is unavailable (the template already has all three sections) and audit-time is where the actual gap lands.

## Sources

- iteration-2 retro: [`2026-05-10-continuous-mode-iteration-2.md`](2026-05-10-continuous-mode-iteration-2.md).
- iteration-1 retro: [`2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md).
- the-council audit: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` (external repo).
- field-society-demo audit: `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md` (external repo).
- Files edited: [`skills/context-engineering/principles.md`](../../skills/context-engineering/principles.md), [`skills/context-engineering/templates/AGENTS.md.template`](../../skills/context-engineering/templates/AGENTS.md.template).
