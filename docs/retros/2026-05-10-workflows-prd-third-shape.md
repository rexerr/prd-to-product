# Retro — 2026-05-10 — Workflows-PRD third shape (continuous-mode session B)

Design pass on the open design question from [iteration-1 retro item 3](2026-05-10-continuous-mode-iteration-1.md). Lands the third shape for AGENTS.md's "What this project is" section in `decisions.md`. This is session B from that retro's appendix.

## What was done

Three files edited:

- [`skills/context-engineering/generator/decisions.md`](../../skills/context-engineering/generator/decisions.md) — PRD redundancy guard rewritten from binary (pointer vs paragraph) to three-way on `len(workflows)`:
  - 0–1 workflows → pointer-only (tagline + `See docs/PRD.md`).
  - 2–5 workflows → pointer + workflow bullet list. The orientation shape `the-council` arrived at by hand.
  - 6+ workflows → pointer-only, list lives in PRD only (compact-pointer goal defeated past five bullets).
- [`skills/context-engineering/principles.md`](../../skills/context-engineering/principles.md) — one-sentence addendum on prose-vs-list distinction (the paper's 2.7% finding targets duplicated *prose*; a bulleted workflow list is an orientation index, not a narrative duplicate), pointing back to decisions.md.
- [`skills/context-engineering/templates/AGENTS.md.template`](../../skills/context-engineering/templates/AGENTS.md.template) — gating comment on `workflows_list` updated from `> 1` to `2..5` with a cross-ref to the guard.

Under hard scope: 3 files, well under 100 lines of edits.

## Design decisions

- **Threshold is 2–5.** Below 2, no list earns its tokens. Above 5, the list defeats the compact-pointer goal and the data belongs in PRD only. Empirical anchor: `the-council` has 4 workflows and the shape works well there.
- **No new intake question.** The shape is derivable from `source_prd_present` × `len(workflows)`. Q2a (`project_tagline_one_line`) already fires whenever the pointer fires. Adding `include_workflow_list_in_agents` would have been intake-load with no information gain.
- **Flat-shape unchanged in practice.** Flat projects have 0–1 workflows by construction (see `rule_shape` triggers in `decisions.md` — `len(workflows) > 1` is itself a modular trigger). They land in the pointer-only row when PRD exists; `workflows_list` doesn't fire. The new shape is modular-only in effect.
- **Definition of "workflow" unchanged.** Still the named flows from intake Q30. Not user stories, not edge cases. The intake answer is the gate; don't broaden what counts.
- **Paper-redundancy framing.** The 2.7% finding from the AGENTS.md paper is about duplicated *prose*. A bulleted workflow list is structurally distinct — closer to a tools-and-commands index than a narrative description. So the failure mode is reduced, not eliminated. Worth saying in principles.md so future edits don't re-collapse to the binary.

## Verification gap (accepted)

CLAUDE.md's verification contract for skill/template/decision changes says: dry-run substitution against `examples/output-small/`. Output-small is flat shape (0–1 workflows) — the new behavior doesn't fire there. The abbreviated medium and large examples (`output-medium-abbreviated.md`, `output-large-abbreviated.md`) are sketches, not full file dumps, and don't render the section verbatim.

So this design pass has no worked example demonstrating the 2–5-workflow pointer-plus-workflows shape. Accepted as a gap rather than fixed because:

- The design is small and the template comment now aligns with `decisions.md`.
- Designing a synthetic example would just round-trip the rule — it would emit what the rule says, which doesn't prove anything.
- Wait for a real 2–5-workflow project (next continuous-mode audit, or a real scaffolded project) to exercise the rule, then verify against that.

If a continuous-mode audit on a 2–5-workflow project surfaces a problem with the rule, escalate then.

## What unblocks

- Iteration-1 retro item 3 (open design question) → resolved.
- Session B from iteration-1 appendix → done.
- Session C (act on promoted items: DECISIONS_ACTIVE per-decision criterion + hooks-defaults-as-forcing-function principle) still queued; independent of this session.
- Session A (second-project audit) still queued; will provide the real-project evidence that exercises the new rule.

## References

- [Iteration-1 retro](2026-05-10-continuous-mode-iteration-1.md) — item 3 is the design question this session answers.
- `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` lines 99–105 — the audit observation that surfaced the third shape (external repo).
- [`decisions.md`](../../skills/context-engineering/generator/decisions.md) — landing site for the rule.
