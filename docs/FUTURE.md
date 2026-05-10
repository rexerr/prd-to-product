# Future — prd-to-product

V2-and-beyond capabilities. Deferred from MVP, not from a session. Do not propose any of these as MVP work.

When an item moves from V2 candidate to actual roadmap, delete it here and add it to [`ROADMAP.md`](../ROADMAP.md).

## Format

- **[Short title]** — what it is, why it's deferred (cost, dependency, sequencing), what would unlock it.

---

## A. Skill ecosystem gaps (Thariq 9-category framework)

The current three skills (`context-engineering`, `prd-creator`, `design-system-bootstrap`) all fall in the **Code Scaffolding** category. The other eight categories from Thariq Shihipar's *Lessons from Building Claude Code: How We Use Skills* (Anthropic 2025) are uncovered. Each is logged as a pre-allocated bucket; **promotion to a roadmap phase requires a real failure observed in session work, not speculation**.

This section is intentionally sparse — eight one-line entries, not designs. Future sessions should not expect density here. The audit signal is the framework itself; content arrives only when evidence does.

- **Library/API Reference** — gap exists / no real failure yet (likely candidate: a per-stack reference skill the agent loads on first touch of an unfamiliar library).
- **Product Verification** — gap exists / no real failure yet (likely candidate: a `verify-ui` skill if the visual-confirmation gate ever fails repeatedly enough to need automation).
- **Data Fetching** — gap exists / no real failure yet (no clear candidate; this repo has no data layer).
- **Business Process Automation** — gap exists / no real failure yet (likely candidate: a session-retro authoring skill if retro quality drifts across sessions).
- **Code Quality/Review** — gap exists / no real failure yet (likely candidate: a pre-commit review skill — but `/ultrareview` already covers part of this surface; would need a real gap to justify a sibling).
- **CI/CD** — gap exists / no real failure yet (no clear candidate; this repo has no CI surface).
- **Runbooks** — gap exists / no real failure yet (likely candidate: incident or recovery runbooks if recurring breakage patterns emerge in dog-food sessions).
- **Infrastructure Ops** — gap exists / no real failure yet (no clear candidate; this repo has no infrastructure).

Candidates promote to a roadmap phase only when a real failure is observed and recorded. Until then, leave un-annotated.

---

## B. Continuous-mode watch items (one instance, awaiting a pattern)

Per [`ROADMAP.md`](../ROADMAP.md) "Continuous mode" — one-off failures may not be the rule's fault; patterns are. These items have a single observed instance each. Fix when the second instance lands.

- **`stack_summary_one_line` row missing for `stack=other + deploy_target=none`.** Decisions table in [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) covers Next/React/Node/Python permutations but not `other + none`. The Phase 2 dog-food run derived "Skill-development workspace (markdown only, no runtime)" by hand. Single observation. When second `stack=other`-class project surfaces: either add a row, or write a fallback rule covering the `other` family.

(The `env_pattern` doubled-period item was resolved in Phase 4 when the second instance landed — see [`PARKING_LOT.md`](PARKING_LOT.md) "Resolved items".)

---

## Cross-references

- MVP scope: [`docs/PRD.md`](PRD.md) "Out of scope" and "Deferred capabilities".
- Mid-session deferrals (different surface, drained per phase): [`docs/PARKING_LOT.md`](PARKING_LOT.md).
- Roadmap: [`ROADMAP.md`](../ROADMAP.md).
