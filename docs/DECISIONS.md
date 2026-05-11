# Decisions log

Append-only log of significant technical and product decisions for prd-to-product.

> For currently binding constraints, see [`docs/DECISIONS_ACTIVE.md`](DECISIONS_ACTIVE.md). New decisions are appended here. Mirror to `DECISIONS_ACTIVE.md` only if they impose ongoing constraints not visible from reading code alone.

## What goes here

A decision belongs in this log if it is significant — meaning:

- it would surprise a future session that hadn't seen it made
- it ruled out an obvious alternative
- it affects a core workflow
- it touches a safety default

Do not log every small implementation detail. Log the calls that matter.

## Format

### [Short title]

**Date:** YYYY-MM-DD
**Context:** What situation prompted the decision.
**Decision:** What was chosen.
**Reason:** Why — what was ruled out and why.
**Revisit if:** Conditions that would make this worth reconsidering.

---

## Decisions

### D-001 — Skills stay markdown-only (pending HTML investigation)

**Date:** 2026-05-10
**Context:** [`docs/html-over-markdown-brief.md`](html-over-markdown-brief.md) raises whether `prd-creator` and `design-system-bootstrap` should output HTML for richer artifacts. The investigation is parallel to the main skill-refinement work and not yet resolved.
**Decision:** All skills in this repo continue to produce markdown output until the HTML-over-Markdown investigation concludes and explicitly authorizes a change. The default holds; do not pre-decide based on speculation.
**Reason:** A switch to HTML touches output paths in multiple skills, downstream consumer assumptions, and the renderer story. The investigation is the right place to make that call. Switching ad-hoc would fragment the skills' output formats and orphan work in flight.
**Revisit if:** The investigation in [`docs/html-over-markdown-brief.md`](html-over-markdown-brief.md) recommends HTML for one or more skills, with a specific failure mode the change prevents.

### D-002 — Direct-on-main, no branches for skill-refinement phases

**Date:** 2026-05-10
**Context:** The skill-refinement phases in [`ROADMAP.md`](../ROADMAP.md) are sequential; each phase touches the same template and decisions files. Branching would force serial merges with no parallelism benefit.
**Decision:** Skill-refinement phases run direct on `main`. Branches only for genuinely parallel work (e.g., the HTML-over-Markdown investigation if it edits skill files that overlap with main-branch refinement).
**Reason:** Single developer, sequential work, files overlap → branches add friction with no win. Phasing principles in `ROADMAP.md` codify this.
**Revisit if:** A second contributor joins the repo, or two genuinely-parallel skill changes need to ship together.

### D-003 — `context-engineering` recency-block item 2 is conditional, not always-on

**Date:** 2026-05-10
**Context:** The Phase 2 dog-food on this repo (no UI, no deploy) hit the abort criterion: the templates assumed UI exists. Item 2 ("Visual confirmation gates the commit") was hardcoded as always-on in the recency block.
**Decision:** Item 2 is gated on `uses_visual_confirmation_gate == true`. Same gate also drops the body Commit gate section, the Verification "UI changes" bullet, the Codex visual-override paragraph, and the "No worktrees" suffix in primary-constraints item 3 (worktrees are only restricted because they break visual confirmation in single-dev-server workflows).
**Reason:** The hardcoded always-on item is dead text for no-UI projects (CLI tools, skill-dev workspaces, backend services). Hardcoding it produces a false constraint that confuses the agent and weakens signal in the recency block. The same flag already exists for the worktree hook and rule, so the gate is consistent.
**Revisit if:** A clearer or more general categorization of "always-on rules" emerges that subsumes this distinction.

### D-004 — Scaffolded Phase 1 is a deploy-shell when `deploy_target != "none"`

**Date:** 2026-05-11
**Context:** [`docs/build-defaults-brief.md`](build-defaults-brief.md) item 1 ("Smallest deployable first") was selected as the pilot from the six-opinion bundle. The brief argues the user's meta-problem — inability to evaluate at the code level — breaks the continuous-mode feedback loop the rest of the skill relies on; the response is to bake externally-validated opinions into scaffolded defaults rather than wait for user-observed failures.
**Decision:** The `context-engineering` skill's `ROADMAP.md.template` now scaffolds Phase 1 as a stack-aware deploy-hello-world block when `deploy_target != "none"`. The user's first user-defined phase (Q31) becomes Phase 2 in that case. When `deploy_target == "none"`, behavior is unchanged: Q31 fills Phase 1, no Phase 2 scaffold is emitted. Implementation lives in [`skills/context-engineering/generator/decisions.md`](../skills/context-engineering/generator/decisions.md) "Phase 1 derivation (deploy-shell scaffold)" and in the updated [`skills/context-engineering/templates/docs/ROADMAP.md.template`](../skills/context-engineering/templates/docs/ROADMAP.md.template).
**Reason:** Highest-conviction, lowest-cost, easiest-to-evaluate item in the bundle. The `deploy_target` intake question (Q5c) already provides a clean gate. Failure mode is observable on the next real project ("did the project deploy in week 1 or didn't it"). Other five opinions deferred per the pilot-one-first sequencing in the brief.
**Revisit if:** The next real project run produces a retro showing the scaffolded Phase 1 was wrong-shaped (e.g., a spike that explicitly should not deploy slipped through `deploy_target == "none"` by accident), or the per-`deploy_target` task lists drift from the platforms' actual deploy paths.

## Cross-references

- Currently-binding subset (curated): [`docs/DECISIONS_ACTIVE.md`](DECISIONS_ACTIVE.md).
- Decisions-log discipline (what counts as significant): [`CLAUDE.md`](../CLAUDE.md) "Decisions log".
- Roadmap and open decisions: [`ROADMAP.md`](../ROADMAP.md).
