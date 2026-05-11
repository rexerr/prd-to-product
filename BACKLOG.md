# Backlog — prd-to-product

Single surface for work that isn't done. Mid-session deferrals, V2 candidates, watch items, and open investigations all land here.

Read this at session start alongside the most recent retro in `docs/retros/`.

## In progress

- **Build-defaults pilot item 1 — awaiting real-project validation.** Shipped in commit `0afaa17` (2026-05-11). Phase 1 of scaffolded ROADMAPs now derives a deploy-shell from `deploy_target`. Promote to Done when the next real project runs on it and produces a retro confirming the deploy-shell pattern works. Brief: [`docs/build-defaults-brief.md`](docs/build-defaults-brief.md).
- **HTML-over-markdown investigation — not started.** Active per D-001 in [`docs/DECISIONS_ACTIVE.md`](docs/DECISIONS_ACTIVE.md). Parallel-eligible. Brief: [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md).

## Backlog

- **Verify `design-system-bootstrap` actually triggers and produces usable output.** Skill is built and symlinked but no retro covers its validation in this repo's discipline. Promote to In progress with a real test project.
- **Build-defaults item 5 (check/test pre-commit, prose-only).** Pilot pending item 1's real-project evidence. Brief: [`docs/build-defaults-brief.md`](docs/build-defaults-brief.md).
- **Build-defaults item 6 (defer abstraction).** Pilot pending items 1, 5.
- **Build-defaults item 2 (vertical slice).** Pilot pending items 1, 5, 6.
- **Build-defaults item 3 (test-first for logic).** Pilot pending earlier items.
- **`stack_summary_one_line` row missing for `stack=other + deploy_target=none`.** Decisions table in [`skills/context-engineering/generator/decisions.md`](skills/context-engineering/generator/decisions.md) covers Next/React/Node/Python permutations but not `other + none`. One observed instance (Phase 2 dog-food). Fix on second instance per continuous-mode discipline.
- **Skill ecosystem gaps (Thariq 9-category framework).** Eight uncovered categories: Library/API Reference, Product Verification, Data Fetching, Business Process Automation, Code Quality/Review, CI/CD, Runbooks, Infrastructure Ops. Promote to In progress only when a real failure surfaces. Existing three skills all fall in Code Scaffolding.
- **Open decisions from prior roadmap.**
  - Should `prd-creator` and `design-system-bootstrap` switch to HTML output? Gated on HTML investigation above.
  - Verification skill: build, defer, or skip? Decide when continuous-mode failures pile up.
  - When `agent teams` moves from experimental to standard, what changes for the skill? Watch upstream Claude Code releases.
  - Should there be on-demand hook scaffolds in the skill? Pending a real failure mode (e.g., user repeatedly hits a moment where a scoped `/careful` would have helped).

## Done

See [`docs/retros/`](docs/retros/) for the session-by-session record. Skill-build Phases 1–4 (2026-05-10) and continuous-mode sessions (2026-05-10 → 2026-05-11) are recorded there.

## Format

Mid-session deferrals: log here immediately with one line on what + one line on what would promote it to In progress. Resolved items move to a retro, not back to this file.

In-progress entries name a promotion criterion ("when X happens, this is done"). Backlog entries name a promotion trigger ("when X observed, move to In progress").

## Cross-references

- Project rules: [`CLAUDE.md`](CLAUDE.md).
- Active decisions: [`docs/DECISIONS_ACTIVE.md`](docs/DECISIONS_ACTIVE.md).
- Decisions log: [`docs/DECISIONS.md`](docs/DECISIONS.md).
- Session retros: [`docs/retros/`](docs/retros/).
