# Harness domain notes — per-project-type methodology

**What this is.** A reference harvest of methodology from the `engineering`, `design`, and `data`
connector skill bundles, captured on **2026-06-18** *before disconnecting those connectors* (token
audit, this session). It answers one question: when `context-engineering` scaffolds a harness for a
**web app / mobile app / backend service / CLI / data project**, what failure-mode-citing rules,
verification disciplines, and docs should it know to emit — beyond what the generator captures today?

**Status — frozen source capture, NOT an adoption plan.** This is the raw, un-triaged harvest. The
triaged inventory (what's adoptable vs. declined-on-fit, deduped against existing cribs) lives in
[`cribs-from-claude-skill-bundles.md`](cribs-from-claude-skill-bundles.md) (`AB-` cribs); sequencing
lives in [`cribs-adoption-roadmap.md`](cribs-adoption-roadmap.md). This file plays the role the source
GitHub repo plays for the other crib lanes — **except the source is a disconnected connector and is
NOT re-fetchable**, so this capture is the permanent source-of-record. Do not adopt from here directly;
go through the `AB-` tracker's lifecycle. The shape-vs-content fork (how much domain content a
"scaffolds shape, not content" generator should bake in — architecture rule 3) gates AB-01/AB-02 and is
council-worthy per D-009; see the tracker's sequencing section.

**Provenance.** Distilled by three read-only subagents that loaded each skill's `SKILL.md` from disk
(none executed, none reconstructed; they returned drafts, did not write product). Source bundles:
`engineering:*`, `design:*`, `data:*`, mined 2026-06-18 before connector disconnect.

---

## Generator gaps this surfaced (the actionable headline)

1. **Mobile is absent.** The stack enum in [`intake.md`](../skills/context-engineering/generator/intake.md)
   (Q5b) has no React Native / Expo option, yet mobile is a named target. Both the engineering and
   design harvests flagged mobile-specific concerns the generator can't currently encode.
2. **Data-project type is hollow.** The Python stack option exists but carries no data-specific rule
   or doc content. A data/analytics harness wants its own rules (metric-lock, query-validation) and
   docs (`metrics.md`, `data-context.md`).
3. **Per-type domain methodology isn't encoded.** The generator asks *structural* questions (stack,
   commands, surfaces) but doesn't seed the *domain failure modes* a given project type should guard.

---

## Candidate rules by project type

House style: each rule names the failure it prevents. De-duplicated across the three harvests.

### Web app

- **Specify every interactive element's full state set (default/hover/active/focus/disabled/loading/error/empty) before "done."** — Failure it prevents: devs guessing unspecified states, so loading/empty/error ship as raw spinners or blank screens.
- **Every list/data view declares empty, loading, and error states as first-class.** — Failure it prevents: the "blank rectangle on first run" — unhandled zero-data and slow-connection cases that only surface in production.
- **Specify truncation/overflow per text field (min/max content, long strings, ~30% i18n expansion).** — Failure it prevents: layouts that break on real data because they were designed at ideal length.
- **Declare responsive breakpoints with *what changes* at each, not "make it responsive."** — Failure it prevents: desktop-only layouts that collapse unpredictably because reflow was never specified.
- **Require visual-regression + a11y checks in the frontend test layer, not just unit tests.** — Failure it prevents: a green unit suite while the rendered UI is broken or keyboard-inaccessible.
- **Set numeric rollback triggers before deploy (error-rate %, P50 latency ms, a named critical flow).** — Failure it prevents: arguing about whether to roll back *during* the incident instead of against pre-agreed limits.

### Mobile app (the generator's biggest gap)

- **Touch targets ≥ 44×44 px (WCAG 2.5.5) with spacing between adjacent targets.** — Failure it prevents: mis-taps from controls sized for a mouse cursor.
- **Respect safe areas / notches / home-indicator insets, not the raw viewport.** — Failure it prevents: content and controls hidden under the notch, status bar, or gesture zone.
- **Custom gestures must not collide with OS-reserved ones (edge-swipe back, pull-to-refresh).** — Failure it prevents: an app gesture fighting the platform's, making back-swipe or refresh unreliable.
- **Conform to the target platform HIG (iOS vs Android nav, system controls, back behavior).** — Failure it prevents: an Android-looking iOS app (or vice versa) that feels broken to native users.
- **Design for one-handed reach — primary actions in the thumb zone, not top corners.** — Failure it prevents: key actions stranded out of reach on large phones.
- **Offline / poor-connectivity behavior is a required state (optimistic UI, retry, cached views).** — Failure it prevents: a frozen or blank app the moment the network degrades.
- **Treat store-review + forced-upgrade as a release gate; old client versions never disappear.** — Failure it prevents: a breaking API change bricking un-updated users, with no server-side rollback once the binary ships.
- **Rollback means feature-flag / remote-config, not redeploy.** — Failure it prevents: assuming you can roll back a shipped binary like a server.

### Backend service

- **Name the SEV ladder and per-level response time (SEV1 all-users-down → immediate; SEV4 cosmetic → next day).** — Failure it prevents: ad-hoc severity calls so a real outage gets a casual response or a cosmetic bug pages everyone.
- **N+1 / unbounded-query / missing-index review is a standing gate on data-access changes.** — Failure it prevents: a query that passes review and tests but melts the DB under production row counts.
- **Declare idempotency + retry semantics for every queue consumer and external-call path.** — Failure it prevents: duplicate side effects (double charge, double email) on the retry distributed systems guarantee will happen.
- **Require a blameless postmortem with a 5-whys chain and owned action items for any SEV1/2.** — Failure it prevents: the same root cause recurring because the fix stopped at the symptom and no one owned the follow-up.
- **Track outdated/unmaintained deps as security risk, on a cadence — not "cleanup."** — Failure it prevents: a known-CVE transitive dep sitting unpatched because "update deps" never outranks features.

### CLI

- **Specify the exit-code contract and stdout-vs-stderr discipline (machine-readable to stdout, diagnostics to stderr).** — Failure it prevents: breaking every downstream pipe and `&&` chain that depends on exit status and clean stdout.
- **Define install / upgrade / uninstall and version-skew behavior as part of "done."** — Failure it prevents: shipping a tool that can't be cleanly updated or misbehaves against a stale config from an older version.

### Data / analytics

- **Lock metric/entity definitions in `docs/metrics.md` before querying; use the documented formula, window, and exclusions verbatim — never silently redefine a KPI mid-analysis.** — Failure it prevents: denominator shift — "conversion improved" because "eligible" was recounted differently than last run, making periods incomparable.
- **Disambiguate entity grain before SQL: state "one row per ___", the business key, and which ID joins to what.** — Failure it prevents: join explosion — a silent many-to-many inflates every COUNT/SUM (and `user` vs `account` vs `org` conflation).
- **A query result isn't done until a red-capable check passes: row-count before/after each join, null rate on key columns, subtotals reconcile, magnitude smell-test, and the number derived a second way.** — Failure it prevents: shipping a plausible-but-wrong number from a bad join, NULL-skewed average, or a silently dropped filter.
- **Compare complete, equal-length periods in one timezone (UTC); exclude or flag partial periods.** — Failure it prevents: "January is down vs December" when January isn't over.
- **Run an explicit bias/methodology pass before sharing: who's missing (survivorship), is the segment defined by its outcome (selection), does the trend survive segmentation (Simpson's), correlation stated as correlation.** — Failure it prevents: a confident wrong conclusion from a self-selected population or a reversed aggregate.
- **Disclose reproducibility metadata with every result: data "as of" date/snapshot, exact filters, sampling, and a fixed seed for stochastic steps.** — Failure it prevents: an unreproducible headline number no one can re-derive.
- **Report mean and median together; give ranges, not false-precision points, for forecasts.** — Failure it prevents: a skewed mean misread as "typical," and "churn will be 4.73%" implying false certainty.
- **Label synthetic/sample/template data as such in the output artifact.** — Failure it prevents: a stakeholder treating a demo dashboard as real numbers.

---

## Verification disciplines worth scaffolding (red-capable repro per type)

The repo's "reproduce before fixing" rule needs a *type-specific* definition of what a red-capable repro is:

- **Web:** a failing component/interaction test or visual-diff, captured red before the fix; plus a keyboard-only + contrast a11y pass as a gate.
- **Mobile:** the failing state reproduced on a real OS version / network condition / permission state — not the simulator happy path.
- **Backend:** a failing integration/contract test at the HTTP layer, or a log/metric query around the deploy window — not a unit test of business logic alone.
- **CLI:** a shell invocation asserting exact exit code + stdout/stderr, run once and watched to fail.
- **Data:** re-derive the key number a *second way* and watch the cross-check reconcile before theorizing. Red-flag triggers that mandate investigation: >50% PoP swing with no cause, exact round numbers, rates at exactly 0%/100%, identical values across segments (query ignoring a dimension), results that perfectly confirm the hypothesis. Outliers are investigated, never auto-dropped; any exclusion is reported with count and %.

Cross-cutting: report findings as observation vs interpretation ("5 of 8 clicked the wrong button" = observation; "the placement is confusing" = interpretation) to keep verification claims grounded. A three-level confidence gate (*ready to share / share with caveats / needs revision*) forces caveats to travel with the result.

---

## Docs / structure worth scaffolding

- **ADR format** (distinct from `DECISIONS.md`'s terse log): Status (Proposed/Accepted/Deprecated/**Superseded**) · Context · options-considered table scored on complexity/cost/scalability/familiarity · explicit Trade-offs · Consequences (easier / harder / must-revisit). The Superseded status + options table are what the current log lacks.
- **Runbook template** (backend/CLI): when-to-use · prerequisites/access · steps · rollback steps · escalation path.
- **Deploy checklist** with a Rollback-Triggers block authored *before* deploy (numeric thresholds).
- **Postmortem template** (backend/mobile): timeline · root cause · 5 whys · went-well/poorly · owned action items.
- **Tech-debt register** with a prioritization formula `(Impact + Risk) × (6 − Effort)` and six categories (code/architecture/test/dependency/documentation/infrastructure).
- **Design-handoff spec** (web/mobile): per-screen overview · layout/grid · tokens-used table · components/variants/props · states-and-interactions table · responsive table · edge cases · motion table · a11y notes. Principle: reference tokens never raw values; if it's not specified, the dev guesses.
- **Component documentation template**: when-to-use · variants table · props table · full states table · a11y (role/keyboard/SR) · do's-and-don'ts.
- **Research-synthesis doc** (UI projects): themes with prevalence + quotes + implication; insight→opportunity with impact/effort; user segments.
- **`docs/data-context.md`** (data): warehouse dialect, entity disambiguation, primary IDs, standard always-on exclusions (`is_test`/`is_internal`/`status='deleted'`). Highest-leverage data artifact.
- **`docs/metrics.md`** (data): per-KPI plain-English definition, exact formula with column refs, source tables, time-window convention, caveats/exclusions. Plus per-table schema docs (grain, PK, update frequency, join keys, gotchas).

---

## Next step

Captured; connectors disconnected without losing the substance. Adoption is tracked, not done — the
survivors are `AB-01` (mobile type), `AB-02` (data type), and `AB-03` (per-type repro), filed in
[`cribs-from-claude-skill-bundles.md`](cribs-from-claude-skill-bundles.md) and sequenced in
[`cribs-adoption-roadmap.md`](cribs-adoption-roadmap.md). AB-01/AB-02 expand generator scope → council
before building (D-009). Most of the per-type UI/ops content above landed `ignore`-on-fit (rule #3) —
it stays here as reference, not as cribs.
