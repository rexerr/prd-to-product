<!-- Last mined: 2026-06-18 (Claude first-party engineering/design/data skill bundles, before connector disconnect; AB-01–AB-03 + AB-i1–AB-i3) · Update this header on every re-mine. NOTE: source is a disconnected connector, NOT re-fetchable — the frozen full harvest lives in `harness-domain-notes.md`. -->

# Cribs from the Claude first-party skill bundles (engineering / design / data lanes)

Bundle-lane companion to `cribs-from-steinberger-ecosystem.md`, `cribs-from-pocock-craft.md`, and `cribs-from-designer-skills.md`. Methodology mined from the Claude first-party `engineering:*`, `design:*`, and `data:*` connector skill bundles (~25 skills) during a token audit, **captured before disconnecting the connectors**. Same goal: **import scar tissue, not reinvent it** — and the same thin yield as the designer lane, for the same reason.

This is a **living adoption-tracker**, not a one-shot summary. Each kept crib has a stable `AB-NN` ID, the failure it prevents, its landing surface, and a status. IDs are namespaced `AB-` (Anthropic bundles) to avoid colliding with `C-`/`CF-`/`DG-`.

> **Adoption sequencing** for this sheet is unified with the other trackers in [`cribs-adoption-roadmap.md`](cribs-adoption-roadmap.md) — that's where waves and verification live.

## Sources mined

| Bundle | What was read | Nature |
|---|---|---|
| `engineering:*` | 10 skills: code-review, debug, architecture, system-design, testing-strategy, tech-debt, deploy-checklist, incident-response, standup, documentation | Software-engineering playbooks for a team running a deployed, on-call, multi-service codebase |
| `design:*` | 7 skills: design-critique, design-system, accessibility-review, design-handoff, research-synthesis, ux-copy, user-research | UI/UX craft + research methodology for a human design org |
| `data:*` | 8 skills: analyze, write-query/sql-queries, build-dashboard, create-viz, explore-data, statistical-analysis, validate-data, data-context-extractor | Analytics/data-warehouse practice for a working analyst |

Read 2026-06-18 by a 3-agent read-only fan-out (each agent loaded the bundle's `SKILL.md` from disk and **returned drafts, did not write product** — the gate that failed 2026-06-17). The full per-project-type harvest is frozen in [`harness-domain-notes.md`](harness-domain-notes.md), which here plays the role the GitHub source repo plays for the other trackers — **except the source is disconnected and not re-fetchable**, so that capture is the only source-of-record.

## The meta-theme

> **An app-building/operating playbook is not a scaffold.** These bundles teach an agent *how to build, ship, and operate a real product* (SEV ladders, touch-target sizes, SQL joins, postmortems); Rex's surfaces emit *structure* (CLAUDE.md/rules, PRDs, token contracts, plan discipline). The two genuinely-transferable kinds are (a) **net-new *generator-shape* gaps the bundles exposed** — project *types* the generator can't yet scaffold (mobile, data) — and (b) the rare rule already shaped as a *named, mechanically-checkable failure-citing scaffold* the generator could emit. Everything that is *content an agent applies while building the downstream app* lands `ignore` on fit, not quality — the exact rule-#3 call the designer lane already settled (its declined "ui-design content skills").

---

## Adoption table

Grouped by landing surface. Only `integrate`/`implement`-tier survivors appear here. Status legend: **Proposed** · **Adopted** (→ `D-NNN`) · **Declined**. Tier column carries the most-skeptical verdict.

### context-engineering (the generator) — net-new project types

| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
|---|---|---|---|---|---|
| AB-01 | **Mobile (React Native / Expo) project type** — add a mobile branch to the stack enum (intake Q5b) with its derived flags, and a scaffolded `mobile-ui.md` rule that *cites* the mobile failure classes (touch targets ≥44px, safe-area insets, OS-gesture collision, platform-HIG conformance, offline/poor-network as a required state, binary-rollback-is-remote-config) | The generator can't scaffold a harness for a named target type at all — mobile work gets a web-shaped or generic harness that never names the failures unique to a shipped binary on a real device | implement | `intake.md` (Q5b enum + derivations) + `decisions.md` + a `mobile-ui.md` rule template (scaffolds the *shape*; the specific values stay reference in `harness-domain-notes.md`) | Proposed · real-run evidence 2026-06-21 (cat-tracker dogfood: 0/8 mobile rules emitted; gap is context-engineering-specific — DSB on the same project was mobile-aware and is a reference impl). See `harness-domain-notes.md` + [retro](retros/2026-06-21-dsb-cattracker-chain-close.md) |
| AB-02 | **Data / analytics project type** — branch the existing Python stack into a data sub-type that captures the SQL dialect as a first-class fact and scaffolds: rules (metric/entity-definition lock, red-capable query-validation, pre-share bias/methodology pass, reproducibility-metadata disclosure) + docs (`metrics.md`, `data-context.md`, per-table schema) | A data project gets a code-shaped harness with no metric-lock or query-validation discipline — so the agent silently redefines KPIs, ships join-inflated numbers, and produces unreproducible headline figures | implement | `intake.md` + `decisions.md` + data-project rule/doc templates | Proposed |

### CLAUDE.md / the generated harness's repro discipline

| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
|---|---|---|---|---|---|
| AB-03 | **Per-project-type red-capable-repro definitions** — extend the "reproduce before fixing" gate with a small table defining what a red-capable repro *is* per type (web: failing component/visual-diff; mobile: real OS/network/permission state; backend: HTTP-layer integration/contract test or deploy-window metric query; CLI: shell invocation asserting exact exit code + stdout/stderr; data: re-derive the number a second way and watch the cross-check reconcile) | "Reproduce before fixing" stays abstract per type, so a "repro" that doesn't actually assert the symptom (a unit test of logic, a simulator happy path) passes for the gate | integrate | extends **CF-03** (red-capable-repro gate) on CLAUDE.md "Reproduce before fixing" + the generated harness's repro rule | Adopted (→ D-045) |

---

## Investigate (deferred — verdict needs a call before promoting)

| ID | Candidate | Open question | Lands on |
|---|---|---|---|
| AB-i1 | **CLI-discipline rule scaffold** — exit-code contract, stdout-vs-stderr (machine-readable to stdout, diagnostics to stderr), install/upgrade/uninstall + version-skew behavior as part of "done" | Node CLI is already a stack option — does a scaffolded CLI-discipline rule earn its keep as *shape* (a mechanically-checkable rule the harness emits), or is it downstream content an agent applies while building the CLI (decline per rule #3)? | context-engineering (CLI stack branch) |
| AB-i2 | **ADR enhancement to the generated DECISIONS scaffold** — a `Superseded` status + an options-considered comparison table (scored on complexity/cost/scalability/familiarity) on top of the current terse decision log | Does this add over the existing `DECISIONS.md` log format, or is it the multi-person RFC ceremony the repo already declined as correct-to-not-adopt (**D-002**)? The Superseded status may be the only non-ceremony primitive | context-engineering (DECISIONS scaffold) / this repo's `DECISIONS.md` |
| AB-i3 | **"Specify states & edge cases, don't assume them"** as a generic scaffolded UI-states rule (every interactive element/list declares default/hover/active/focus/disabled/loading/error/empty before "done") | Is this a mechanically-checkable scaffold-rule (DG-01-shaped, generator emits it for UI types), or design *content* an agent applies while building UI (decline per rule #3)? It's the strongest of the web-UI items — the rest are clearly content | context-engineering `.claude/rules/` (UI project types) / DSB |

---

## Declined / ignored (notable)

One line each — near-misses recorded so a future re-mine doesn't re-litigate. (Trivial off-domain content — standup formatting, doc "write for the reader" principles, requirements-gathering framing, testing-pyramid basics — omitted wholesale.)

- **Web-UI content rules** (truncation/i18n expansion, responsive-breakpoint specifics, CTA-label/error-copy wording) — design opinions an agent applies *while building UI*; off the generator domain (rule #3), the same call as the designer lane's declined ui-design skills. The one meta-rule worth lifting is hoisted to **AB-i3**; the specifics stay reference in `harness-domain-notes.md`.
- **Mobile-UI specifics** (the 44px / safe-area / gesture / thumb-zone values) — not individual cribs; they are the *referenced content* **AB-01**'s scaffolded `mobile-ui.md` rule would cite. Captured in `harness-domain-notes.md`.
- **Backend SEV ladder · blameless postmortem · 5-whys · on-call escalation** — team-ops ceremony for a multi-person on-call org; no backend project type in the generator and no on-call here. The PR/process-ceremony divergence the repo already settled (**D-002**).
- **N+1 / unbounded-query gate · idempotency+retry semantics · dependency-debt cadence** — real, but downstream *code* concerns an agent applies while building a service; backend isn't a generator branch. Reference only.
- **Tech-debt register template** (`docs/DEBT.md` + Severity×Frequency/Effort formula) — **DEDUP: this is DG-i5**, already an open investigate gating on "does a generic register survive rule #3?" Don't re-mint; resolve under DG-i5.
- **Design-handoff spec format · component-documentation template** — **DEDUP against the repo's existing design-handoff work** (`docs/design-handoff-adoption.md`, `-adopt-brief.md`, `-fidelity-test.md`). Already in flight; don't re-mint.
- **Research-synthesis doc · observation-vs-interpretation discipline** — overlaps **DG-i6** (Observation/Problem/Fix triad) and is UX-research content; cite DG-i6, no extension.
- **Runbook · deploy-checklist · rollback-triggers block** — ops content; the harness already ships the `engineering:deploy-checklist` skill, and there's no deployed service here to run a book against.
- **Visual-regression / a11y as a frontend test layer** — a downstream project's CI concern, not generator shape; the a11y *audit* capability the harness already holds (`web-design-guidelines`, `ui-design-review`).

---

## Divergence / fit notes

Same axis as the designer lane: **audience and direction.** These bundles are built for people *building and operating real products* (engineers shipping services, designers producing UI, analysts querying warehouses); Rex's workspace is a single-developer, markdown-only, *generate-side* shop whose product is scaffolding for AI-coding projects. That divergence explains nearly every `ignore` — adopting the build/operate content would invert the generator's "shape, not content" thesis (architecture rule #3) and pay skill-budget rent (C-21) for capability the harness already ships. Where the bundles *converge* with us it's because a project-*type* gap surfaced (AB-01, AB-02 — net-new generator shape, like DG-01 was) or a rule happened to take the shape of our doctrine (AB-03 extends CF-03). One source-specific caveat: unlike the GitHub-sourced lanes, **this source is a disconnected connector and cannot be re-mined** — so `harness-domain-notes.md` is the permanent source-of-record, not a convenience copy.

---

## Recommended sequencing

Thin yield; small batches.

**Real-build cribs (genuine generator additions — `/furnace-plan` each):**
- **AB-01** (mobile type) and **AB-02** (data type) each *expand what project types the generator scaffolds.* That is the **shape-vs-content fork** flagged in `harness-domain-notes.md` — how much domain content a "scaffolds shape, not content" generator should bake in. Per **D-009**, take that scope-expansion to a **council before building** — it's costly to reverse if the generator bloats with content. Candidates for **Big Rock** status, not a cheap Wave slot.

**Extension crib (cheap, rides an adopted gate):**
- **AB-03** per-type repro definitions → fold into **CF-03** when CF-03 is adopted (Wave 1), or just after. One small table on the repro rule.

**Resolve-then-decide (gated investigates):**
- **AB-i3** (specify-states rule) and **AB-i1** (CLI rule) both reduce to one rule-#3 read: *is this scaffold-shape or downstream content?* Answer once, both resolve.
- **AB-i2** (ADR enhancement) → a short check against `DECISIONS.md` + the D-002 ceremony line.

Everything in Declined needs no further action.

---

## Provenance

Generated 2026-06-18 by a 3-agent read-only `Agent` fan-out (engineering / design / data readers → returned distilled drafts → triaged + deduped here). Source: the Claude first-party `engineering:*` / `design:*` / `data:*` connector skill bundles, **disconnected the same session** during a token audit. Full harvest frozen in [`harness-domain-notes.md`](harness-domain-notes.md). Not re-fetchable — treat that capture as the source.
