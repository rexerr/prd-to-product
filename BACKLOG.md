# Backlog — prd-to-product

Single surface for work that isn't done. Mid-session deferrals, V2 candidates, watch items, and open investigations all land here.

Read this at session start alongside the most recent retro in `docs/retros/`.

## In progress

- **Build-defaults pilot item 1 — awaiting real-project validation.** Shipped in commit `0afaa17` (2026-05-11). Phase 1 of scaffolded ROADMAPs now derives a deploy-shell from `deploy_target`. Promote to Done when the next real project runs on it and produces a retro confirming the deploy-shell pattern works. Brief: [`docs/build-defaults-brief.md`](docs/build-defaults-brief.md).
- **Validation project: Squirreled** (working name; was *Taste Builder*). Will exercise the full skill chain end-to-end: brief → prd-creator → PRD → context-engineering → scaffold → build → deploy. Single test validates build-defaults pilot item 1, the BACKLOG/ROADMAP shape, and prd-creator + context-engineering composition simultaneously. Brief: [`docs/product-briefs/taste-builder.md`](docs/product-briefs/taste-builder.md) (filename preserved; product name may change during PRD interview). Promote to Done when a retro covers a working deployed Phase 1.
- **Skill consolidation: BACKLOG.md scaffolded for new projects.** Mirror the docs-audit pattern (commit `afb2964`) back into `context-engineering`: scaffold a `BACKLOG.md` at root, delete `PARKING_LOT.md.template` and `FUTURE.md.template`, patch ROADMAP terminal phase, "Where to look" tables, session-start command. Gated on Taste Builder retro — if the new shape feels right under real load, ship; if not, modify or defer. ~150–200 lines net change.
- **HTML-over-markdown investigation — not started.** Active per D-001 in [`docs/DECISIONS_ACTIVE.md`](docs/DECISIONS_ACTIVE.md). Parallel-eligible. Brief: [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md).

## Backlog

- **Verify `design-system-bootstrap` actually triggers and produces usable output.** Skill is built and symlinked but no retro covers its validation in this repo's discipline. Promote to In progress with a real test project.
- **Build-defaults item 5 (check/test pre-commit, prose-only).** Pilot pending item 1's real-project evidence. Brief: [`docs/build-defaults-brief.md`](docs/build-defaults-brief.md).
- **Build-defaults item 6 (defer abstraction).** Pilot pending items 1, 5.
- **Build-defaults item 2 (vertical slice).** Pilot pending items 1, 5, 6.
- **Build-defaults item 3 (test-first for logic).** Pilot pending earlier items.
- **`stack_summary_one_line` row missing for `stack=other + deploy_target=none`.** Decisions table in [`skills/context-engineering/generator/decisions.md`](skills/context-engineering/generator/decisions.md) covers Next/React/Node/Python permutations but not `other + none`. One observed instance (Phase 2 dog-food). Fix on second instance per continuous-mode discipline.
- **Skill ecosystem gaps (Thariq 9-category framework).** Eight uncovered categories: Library/API Reference, Product Verification, Data Fetching, Business Process Automation, Code Quality/Review, CI/CD, Runbooks, Infrastructure Ops. Promote to In progress only when a real failure surfaces. Existing three skills all fall in Code Scaffolding.
- **Sibling skill: `red-team` (adversarial review).** New skill that takes any document — PRD, scaffolded ROADMAP, design rationale, brief, brand statement — and returns critique: where the story breaks, where a client will object, where it's derivative or trend-chasing, what's missing. Sibling to prd-creator / context-engineering / design-system-bootstrap rather than a feature inside any of them, because the capability is generic across documents and each existing skill should stay single-purpose. Promote when a real failure surfaces where having red-team would have caught it. Source: 2026-05-11 ideation conversation (#15 Creative Red Team + #18 Narrative Gap Finder).
- **Candidate future products parked for exploration.** Three product briefs captured in [`docs/product-briefs/`](docs/product-briefs/) for future PRD development: AI Research Synthesizer, Anti-Generic Machine, Design Process Black Box Recorder. The Black Box Recorder is the most ambitious — multi-system passive-capture product, parked deliberately as a long-horizon idea. None are scoped as next-build; revisit after Taste Builder validation completes.
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
