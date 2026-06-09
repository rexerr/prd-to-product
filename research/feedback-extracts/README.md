# feedback-extracts — plan-review history mining (staging)

One-time investigation: mine Rex's Claude Code history for how often his proposed **plans** get sent back for revision, and **why**. Produces the evidence the LLM council demanded before any "self-healing plan-review loop" gets built (see `docs/council/council-report-2026-06-09-self-healing-loop.html`). NOT the rejected `docs/plan-reviews/` subsystem; this folder can be deleted once a pattern read is taken.

## Start here

**[`HANDOFF.md`](HANDOFF.md)** — the standalone pickup doc. A cold session should be able to run the extraction from it alone: method, findings, per-round schema, scripts, scope decision, and step-by-step run instructions.

## State (2026-06-09)

- **Method pivoted** from correction-based (broad keyword grep — rejected as too broad) to **round-based**: anchor on each *plan presented* and classify Rex's response as approve / revise / interrupt. The signal is the plan → revise → plan loop, not scattered corrections.
- The six `feedback-extract-*.md` files here are **correction-based samples** from the rejected format — kept as method-validation only. The real next-session run re-does these sessions **round-based** per HANDOFF.md §6.
- `scripts/` — preserved read-only utilities (`planscan.py`, `rounds.py`, plus legacy `prefilter.py` / `corrview.py`).

## Naming

`feedback-extract-<project-slug>-<YYYY-MM-DD|undated>-<topic-slug>.md`
