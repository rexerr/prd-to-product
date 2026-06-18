<!-- Last mined: 2026-06-17 (Design lane — owl-designer-skills; DG-01–DG-02 + DG-i1–DG-i7 deferred) · Update this header on every re-mine -->

# Cribs from the owl-designer-skills ecosystem (design lane)

Design-lane companion to `cribs-from-steinberger-ecosystem.md`. Process and craft patterns mined from MC Dean's `owl-designer-skills` — a nine-plugin Claude Code design suite (MIT). Same goal as the parent doc: **import scar tissue, not reinvent it** — but the yield here is far thinner, because this corpus is design *content* (what good UX/DS is) authored for a multi-person human design org, while every Rex surface is a *meta-tool that scaffolds shape, not content*. Most of it lands `ignore` on fit, not quality.

This is a **living adoption-tracker**, not a one-shot summary. Each kept crib has a stable `DG-NN` ID, the failure it prevents, its landing surface, and a status. IDs are namespaced `DG-` (design) to avoid colliding with the parent doc's `C-NN`.

> **Adoption sequencing** for this sheet is unified with the other crib trackers in [`cribs-adoption-roadmap.md`](cribs-adoption-roadmap.md) — that's where waves and verification live.

## Sources mined

| Repo | What was read | Nature |
|---|---|---|
| `owl-designer-skills` (MC Dean, MIT) | All 9 plugins: `design-ops`, `design-research`, `design-systems`, `designer-toolkit`, `interaction-design`, `prototyping-testing`, `ui-design`, `ux-strategy`, `visual-critique` — every `SKILL.md`, command body, and `plugin.json`/README | A human-design-team operations + craft suite. ~80 skills + ~25 orchestrator commands across the nine plugins |

## The meta-theme

> **A design-content library is not a scaffold.** Owl teaches an agent *design opinions* (color, type, sprint agendas, WCAG audits, stakeholder decks); Rex's surfaces emit *structure* (CLAUDE.md/rules, PRDs, token contracts, plan discipline). The two genuinely-transferable cribs are the rare cases where a *named, mechanically-checkable rule citing its failure* surfaced through the content — exactly the parent doc's spine, found in a foreign domain.

---

## Adoption table

Grouped by landing surface. Only `integrate`/`implement`-tier cribs appear here. Status legend: **Proposed** · **Adopted** (→ `D-NNN`) · **Declined**. Tier column carries the most-skeptical verdict.

### context-engineering (the generator)

| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
|---|---|---|---|---|---|
| DG-01 | **Even-coverage synthesis rule** — when synthesizing N sources, tag every observation with its source ID *before* clustering, then post-cluster verify each source appears in the output (go back if absent), and flag single-source patterns rather than discard them | Multi-source synthesis silently over-representing the first/last inputs and fabricating a "pattern" only the early sources support — LLM primacy/recency bias under load. Generalizes to any fan-out the generator scaffolds (mining N docs, summarizing N retros) and to Rex's own subagent fan-out that produced these crib files | integrate | context-engineering — adapt as a generic `.claude/rules/` scaffold (generalize the UX-research wording; *not* a verbatim copy). Drop the proposed secondary `solutions/` landing — that library is for failures earned by a real run here, not imported principles | Proposed |

### design-system-bootstrap (DSB)

| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
|---|---|---|---|---|---|
| DG-02 | **Semantic-not-directional token naming** — design-token names must use logical/semantic axes (`*-inline-start`, `text-align: start`), never directional ones (`*-left`); pair with the CSS-logical-property mandate at emit time | A token set with directional names (`color-border-left`) that breaks or needs costly retrofit under RTL — a failure DSB's current naming guidance (C-37–C-39) does not guard against. Adopt as a *one-line constraint* on DSB's emit/naming guidance, not the whole `localization-design` skill | integrate | design-system-bootstrap — sharpens C-37/C-39 naming; conditional on RTL/logical-property naming being in DSB scope (vs out-of-scope like feature components) | Proposed |

---

### Investigate (deferred — verdict needs a live read before promoting)

Each names the open question that gates it. Default-low until resolved.

| ID | Candidate | Open question | Lands on |
|---|---|---|---|
| DG-i1 | **Motion token category** (`motion-system`): a duration scale (instant→deliberate, 50–600ms), an easing table mapped to semantic uses, and a `prefers-reduced-motion` strategy handled at `:root`, not per-component | Does DSB's current token taxonomy (C-37–C-39, color/spacing-centric) cover a motion layer, or is motion a genuine gap? If gap → the duration/easing tables + reduced-motion `:root` override are adaptable content | design-system-bootstrap |
| DG-i2 | **Brand-reference triad contract** (`critique-brand-consistency`): a stable named `mood.md` / `voice.md` / `tokens.md` set a consumer can mechanically locate, plus "if a file is missing, note it and skip — do *not* invent brand rules" | Does DSB's emitted file set already match this triad, or is it a third naming scheme? Is our `DESIGN.md` the same artifact as their `mood.md`, and should names align so generate-side and check-side share a contract? Meaningfully extends C-39 if so; the missing→abstain rule is C-04's spirit at the generate/consume boundary | design-system-bootstrap (+ prd-creator for `voice.md`) |
| DG-i3 | **Question-bias guardrail** (`interview-script`/`survey-design`): a paired leading→non-leading rewrite table plus an emit-time self-test ("if the question contains its own implied answer, rewrite it") | Does prd-creator (or any Rex skill) actually run a question-asking loop where leading-question bias is a live risk? If only the UX domain → downgrade to ignore. Pattern-overlaps C-18 (emit-time self-check) | prd-creator interview mode (conditional) |
| DG-i4 | **Falsifiable-principle record** (`design-principles`): author each principle with a counter-example + a named trade-off + a "would anyone disagree?" falsifiability test + rank-order for conflict resolution | Does the counter-example/trade-off structure add anything to C-14's dated-named-quoted failure tag, or collapse into it? The "would anyone disagree?" test may be the only non-overlapping primitive — could sharpen how `principles.md`/scaffolded rules author rules | context-engineering / principles.md |
| DG-i5 | **Debt-register template as a scaffoldable doc** (`design-debt-audit`): an empty `docs/DEBT.md` register (issue / category / severity / status / owner / target) + a Severity×Frequency/Effort triage formula, reviewed on a cadence | Does a generic register *template* survive architecture-rule-3 (generator scaffolds shape only), and does it earn its keep vs C-09's retro loop + the harness `engineering:tech-debt` skill? Rex must decide: optional generator doc, or scope creep? | context-engineering (optional docs scaffold) |
| DG-i6 | **Observation/Problem/Fix + enumerated verdict** (`visual-critique`, all 7 skills): force a critique step to separate neutral observation from judgment from remedy, and grade `pass`/`minor`/`major` rather than free prose | Does the triad add anything the furnace-plan ledger doesn't already get from C-04 (narrow explicit verdict) + C-22 (claim vocabulary) combined? Likely confirmatory — if so, fold in as a citation, not a new crib | furnace-plan ledger / scaffolded rule output-shape |
| DG-i7 | **Command-orchestrates-named-skills convention** (recurs across all 9 plugins): a thin command = ordered pipeline of skill invocations by *name* + a declared output contract + an explicit "consider following up with /X" chaining footer | As the family grows past 4 skills, does an explicit command→skill→next-command convention buy anything over C-12 (on-demand commands) + C-34 (reference-not-copy)? Or is it ceremony C-41 would reject? Needs a call on whether DSB/CE expose a command layer at all today | context-engineering / DSB command layer (if one is ever wanted) |

---

## Declined / ignored (notable)

One line each — the near-misses worth recording so a future re-mine doesn't re-litigate them. (Trivial off-domain content skills — personas, journey maps, case studies, sprint agendas, ux-writing, negotiation, impact decks — are omitted wholesale.)

- **`design-token` / `theming-system` / `naming-convention` skills** — strictly weaker 3-tier token model than C-37's 4-layer contract-with-promotion-path; no self-resolving `:root`, no failure citation. Subset of what we already hold.
- **`design-token-audit` / `design-debt-audit` (audit halves)** — generic drift checklists with no *gate*; C-37/C-39 already encode the tiers. Ignore unless an actual audit gate (not prose) emerges.
- **`design-review-process` / `design-system-governance`** — multi-person org approval ceremony (RFCs, sign-offs, semver release policy); the exact PR-discipline divergence the repo already settled as correct-to-not-adopt (D-002). One overlap (scale gate to risk) already held by C-06 + D-009.
- **`research-repository` / `summarize-interview` confidence tagging** — restates C-01 (stable IDs), C-10/C-20/C-29 (freshness/sync), C-22 (confidence vocab) in a UX-repository idiom; no extension.
- **`design-impact-reporting` / `presentation-deck` / `case-study`** — stakeholder/portfolio communication for an in-house org; no workspace stakeholder to report to.
- **Hand-maintained README/`plugin.json` skill index** — the drift-prone anti-pattern C-32 (generated index) and C-29 (in-sync assertion) exist to *prevent*; confirms the call, adds nothing.
- **Cognitive-law / "Common Mistakes" / "Best Practices" trailers** — generic misapplication bullets, not a dated run that earned the rule; a *weaker* instance of C-14, below its bar.
- **`interaction-design` / `ui-design` / `ux-strategy` / `prototyping-testing` content skills** — design opinions an agent applies when *building UI*; Rex's skills generate scaffolds and PRDs, they don't build UI. Off the generator domain (architecture rule #3).

---

## Divergence / fit notes

The author's practice diverges from ours on one axis that explains nearly every `ignore`: **audience and direction.** Owl is built *for a human design organization* (sprints, critiques, stakeholder decks, file-versioning rituals, adoption campaigns) and its skills mostly *review or produce finished design content*. Rex's workspace is a *single-developer, markdown-only, generate-side* shop whose product is scaffolding for AI-coding projects. That divergence is fully justified by product shape — adopting the team-ops or content layers would invert the generator's "shape, not content" thesis (architecture rule #3) and pay skill-budget rent (C-21) for review capability the harness already ships (`ui-design-review`, `web-design-guidelines`, `design:*`). Where Owl *does* converge with us — the rare named-rule-citing-a-failure (DG-01) and the RTL naming constraint (DG-02) — it's because a craft detail happened to take the shape of our doctrine, not because the domains overlap. The one structural pattern that keeps recurring (command-orchestrates-skills, DG-i7) is real but unproven against C-12/C-34 for a 3-skill family; holding it until the family grows is the C-41-disciplined call.

---

## Recommended sequencing

Thin yield, so the batches are small.

**Cheap win (a sub-50-line edit, closes a latent failure):**
- DG-02 semantic-not-directional token-naming constraint → one line in DSB's emit/naming guidance, *if* RTL is in DSB scope (resolve that scope call first — it's a one-question decision, not a council fork).

**Real-build crib (a genuine generator addition):**
- DG-01 even-coverage synthesis rule → a new generic `.claude/rules/` scaffold the generator can emit. Adapt the wording off UX-research into source-agnostic synthesis language; this is the one crib worth lifting because it also hardens Rex's *own* subagent fan-out (the very mechanism that produced these crib docs).

**Resolve-then-decide (gated investigates, cheapest question first):**
- DG-i2 brand-triad contract and DG-i1 motion tokens both reduce to one DSB-scope read — do that read once and both resolve together.
- DG-i4 falsifiable-principle test vs C-14 — a short overlap check against `principles.md`.
- DG-i7 command-orchestration — defer until the skill family grows past 4; revisit then, not now.

Everything else is `ignore` on fit and needs no further action.

---

## Provenance

Generated 2026-06-17 by a `Workflow` fan-out (9 plugin readers → adversarial verify on every integrate/implement pick → synthesis; `wf_304bfa35-eeb`, 24 agents). Source: `Owl-Listener/designer-skills` (MC Dean, MIT), shallow-cloned to scratch. Not a substitute for reading the source skill when adopting a specific crib.
