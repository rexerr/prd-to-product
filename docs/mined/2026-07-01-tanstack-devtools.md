# Mine — TanStack/devtools — 2026-07-01

- **Source:** [github.com/TanStack/devtools](https://github.com/TanStack/devtools) — "a framework-agnostic devtool for managing and debugging your devtools" — a dev-only debugging shell + plugin platform.
- **Pinned:** `92f69d014a981518915064593adc7bb4ffb71f3a` (shallow clone, `docs/mined/repos/devtools/`, gitignored)
- **License:** MIT (TanStack)
- **Lens:** Track 2 project-setup. Prior was *"likely tangential (observability panel)."* Two blind readers (what-it-is/QA relevance · `_artifacts/skill_spec.md` skill-craft) tested it. Lens **A** = our skill-authoring; **B** = scaffold output.

## Verdict — prior CONFIRMED for the core product, REFUTED at the margins

The core devtools shell + event-bus is genuinely **app-runtime debugging** — "wire up devtools" is an app-author's runtime choice, dev-only (stripped from prod builds, `docs/production.md:7-12`), producing no test artifact or CI gate. Out of scope for a context-engineering scaffold; do **not** mine the plugin/event-system architecture as a transferable pattern. **But two things the lightweight prior would have missed:** (1) devtools is an **intent-generated repo**, so `_artifacts/skill_spec.md` exposes the TanStack/intent pipeline's skill-spec output end-to-end — with three moves we don't make; (2) two concrete items bear on the Seq-1 **test/QA hole**.

## Findings

### D-1 — Failure-mode spec enrichments (the intent pipeline does 3 things we don't) · code-grounded (Lens A/B) · ADOPTED (→ watching row, gate:rule-of-2)

**Source:** `_artifacts/skill_spec.md` — a planning spec where the **failure mode is the organizing spine**, not a per-rule appendage (strongest external validation yet of our "every rule cites its failure mode" invariant). Three net-new deltas over our discipline:

- **Priority-rank on every failure mode** — `skill_spec.md:34,36` CRITICAL/HIGH/MEDIUM column. We tag failure modes but don't rank severity; ranking is what lets an agent under attention pressure triage which rule to honor first.
- **Source-*type* on every cite** — `skill_spec.md:36,57` the Source column distinguishes `docs/…` (documented) vs `packages/…/src/…` (code-derived) vs **`maintainer interview` (tacit, un-documented)**. Our cites point at our own decisions/retros; theirs flag "written down" vs "only in a human's head" — a discovery aid we lack.
- **A "Tensions" conflict-map** — `skill_spec.md:116-122` names skill pairs that pull against each other and **predicts the agent's wrong move at each fork** (e.g. "agent optimizing for debugging coverage emits in hot paths"); the per-row **Cross-skill?** column (`:36`) links each failure to the skills it collides with. Sharper than our scattered "failure it prevents" notes — a conflict map, potentially a "known tensions" block in scaffolded rules (Lens B).

**Confirmatory (no action):** the emitted `SKILL.md` `name` matches its directory (`packages/event-bus-client/skills/devtools-event-client/SKILL.md:2`) — independent validation of one of our three frontmatter checks. (The intent-pipeline mechanics themselves are dedup — already mined from [TanStack/intent](2026-06-30-tanstack-intent.md).)

### D-2 — Test/QA-hole reference shapes · code-grounded (Lens B) · ADOPTED (→ handoff Track-2 design input)

- **e2e Playwright-harness pattern** — `e2e/helpers/src/` ships a reusable `DevtoolsPage` page-object + `SELECTORS` constants consumed identically across **8 framework apps** (`e2e/apps/{react-vite,react-start,react-cloudflare,react-nitro,solid,vue,preact,angular}/`). A concrete reference model for what "knowing a downstream app works" looks like structurally — a shared page-object + selector constants + per-target Playwright config, not just unit tests. Complements gstack's `/qa` test-framework bootstrap.
- **a11y as a CI-QA dimension** — `packages/devtools-a11y` is real axe-core/WCAG auditing (`src/core/utils/ally-audit.utils.ts:1,35` — `wcag2a`/`wcag2aa`/`wcag21aa`). The tool itself is a dev-time manual aid (not a gate), so the **scaffold takeaway is "recommend a CI-runnable axe/Playwright a11y check"** as a legitimate QA dimension — not "wire up this plugin."

### Dropped (no action)

- **Core devtools shell + event-bus / bidirectional-communication / plugin-lifecycle** — app-runtime debugging plumbing (CustomEvents, WebSocket/SSE, BroadcastChannel); does not transfer to a markdown-only scaffolding skill. Explicitly out of scope.
- **`.cursor/rules/jsdoc.mdc`** — a single-source-of-truth-with-failure-mode doc rule; the pattern is one we already use. No new mechanics.
