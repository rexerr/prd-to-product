## Retro — 2026-05-11 — Build-defaults pilot: item 1 (smallest deployable first)

First implementation session after the build-defaults brief landed at [`docs/build-defaults-brief.md`](../build-defaults-brief.md). Shipped the pilot opinion only — items 2, 3, 5, 6 deferred per the brief's pilot-one-first sequencing.

## What landed

| File | Change |
|---|---|
| [`skills/context-engineering/templates/docs/ROADMAP.md.template`](../../skills/context-engineering/templates/docs/ROADMAP.md.template) | Phase 1 task slot widened to multi-line `phase_1_tasks` substitution. Added gated Phase 2 section (`<!-- OPTIONAL: phase_2_section -->`). |
| [`skills/context-engineering/generator/intake.md`](../../skills/context-engineering/generator/intake.md) | Q31 reframed: state-map keys renamed to `phase_user_*`; question framing depends on `deploy_target`. No new question added. |
| [`skills/context-engineering/generator/decisions.md`](../../skills/context-engineering/generator/decisions.md) | New "Phase 1 derivation (deploy-shell scaffold)" section with per-`deploy_target` task table and `phase_user_*` → `phase_1_*` / `phase_2_*` routing rules. Documented an OPTIONAL-gate convention extension for heading-anchored blocks. |
| [`skills/context-engineering/examples/output-small/ROADMAP.md`](../../skills/context-engineering/examples/output-small/ROADMAP.md) | Regenerated as dry-run check. Vercel + Next.js project: Phase 1 is the deploy shell; the previous "MVP launch" content moved to Phase 2 unchanged. |
| [`docs/DECISIONS.md`](../DECISIONS.md) | New D-004. Not mirrored to `DECISIONS_ACTIVE.md` — the constraint is visible in `decisions.md` and the template, so it fails the "not visible in code" criterion for active-set promotion. |

## What was rejected vs. what shipped

The session opened with a written position pass on all six brief opinions. Conclusions:

- **Item 1: ship as proposed** — pilot subject.
- **Item 2 (vertical slice): ship with modification** — the session-discipline one-liner is fine; the ROADMAP Phase 2 scaffolding the brief proposed is **not**, because Phase 2 has no existing template entry and the slice is project-specific in a way Phase 1 (deploy hello-world) isn't.
- **Item 3 (test-first): defer** — most contested opinion, biggest implementation cost, lowest-conviction. Trigger: after items 1+5 produce a real-project retro identifying a verification gap.
- **Item 5 (check/test pre-commit): ship as proposed** — pilot #2.
- **Item 6 (defer abstraction): ship with modification** — paragraph in session-discipline only; skip the principles.md cross-link the brief proposed (`principles.md` is skill-author-facing, not scaffolded output).
- **Item 4: already shipped.**

Pilot order changed from the brief's `1 → 5 → 2 → 3, 6` to **`1 → 5 → 6 → 2 → 3`**. Reasoning: item 6 is universal prose with no template-shape change, lower cost than the now-modified item 2.

## Open questions resolved

| # | Position |
|---|---|
| 1 (ROADMAP vs new `BUILD_GUIDE.md`) | ROADMAP. New file is rule proliferation; "intrusive" is overstated. |
| 3 (rule-of-three for rule files/docs?) | Product code only. Rule files have continuous-mode discipline that already governs them. |
| 4 (Phase 1 prescriptiveness) | Fully filled-in. The meta-problem ("user can't evaluate at the code level") kills the trust-the-agent-to-fill-in option. |
| 5 (override path) | In-project for stack-shape opinions; intake-time for universal-ish. For item 1, the existing `deploy_target == "none"` IS the intake-time override. No new question. |

Flagged: open questions 2 (test-discipline as its own file or section) and 6 (ship the brief as `docs/build-philosophy.md` in scaffolded projects). Both are bundle-shaped and meaningless until ≥2 opinions ship.

## What surfaced during implementation

Three things I didn't predict before writing code:

1. **The OPTIONAL marker convention needed an extension.** The existing spec at `decisions.md` "OPTIONAL block handling" says markers gate "the next line, or the next contiguous block ending at a blank line, depending on context." The `phase_2_section` gate spans a heading with internal blank lines and ends at a `---` divider. I documented the context-specific extension in the new derivation section ("OPTIONAL gate convention extension") rather than amend the general spec — keeping the change local until a second case forces a generalization.
2. **`phase_1_task_placeholder` (singular) was the wrong shape for the new Phase 1.** Stack-derived Phase 1 is six tasks, not one. I widened the slot to `phase_1_tasks` (multi-line) and put the wrapping logic in `decisions.md` so the user-supplied case (`deploy_target == "none"`) still works from a single `phase_user_task_placeholder` fill — the generator wraps it as `- [ ] {placeholder}`.
3. **Non-UI stacks need a different done-when.** The brief's example wording ("page with project name in `<h1>`") assumes UI. Python/Node-CLI projects deployed to Fly/Railway need a response-body check instead. Handled via `stack_has_ui` branching on `phase_1_done_when` and on the project-name marker task. This wasn't called out explicitly in the brief — likely because the brief used Vercel as its mental model. Worth a callout for whoever pilots items 2, 3, 6 next: brief examples lean UI-heavy.

## Scope

Net diff: ~110 lines added across the three template/spec files, plus the example regen (~20 lines net) and the DECISIONS + retro entries. Inside the 300-line feature-work cap.

## Verification

- Dry-run substitution: regenerated [`examples/output-small/ROADMAP.md`](../../skills/context-engineering/examples/output-small/ROADMAP.md) by hand against the new template and `decisions.md` derivation. The output is consistent with the per-`deploy_target == vercel` table row and the `stack_has_ui == true` branch.
- No hooks emitted by this change. No live-fire test needed.
- Cross-references in `decisions.md` and `DECISIONS.md` resolve to the correct files.

## What to watch for on next real project

The pilot's success criterion (per the brief): "did the project deploy in week 1 or didn't it." Specifically:

- The agent should read Phase 1 of the scaffolded ROADMAP and treat it as the immediate work, not as boilerplate to skip.
- The deploy tasks should complete without the agent improvising around them (e.g., not jumping straight to feature code, not declaring Phase 1 done before the production URL responds).
- The project-name marker step should produce a visible change in production that confirms the deploy pipeline works end-to-end.

If any of those go sideways, the pilot has produced its own next-iteration signal.

## Next session

Pilot item 5 (check/test pre-commit, prose-only) once a real project has run on the new Phase 1 scaffold and produced a retro. Not before — the brief's pilot-one-first discipline applies.
