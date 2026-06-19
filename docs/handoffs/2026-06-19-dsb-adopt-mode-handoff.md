# Handoff — DSB adopt-mode (scope via /furnace-plan)

**Date:** 2026-06-19 · **For:** a fresh session that will `/furnace-plan` this work. Self-contained — you do not need the originating chat.

## The decision (already reached, not yet built)

`design-system-bootstrap` (DSB) gains an **`adopt` mode** — alongside `bootstrap` (greenfield) and the planned `audit` mode — that ingests a finished **Claude Design bundle** and wires it so a project's later page-builds stay faithful to it. This closes the failure recorded in the [D-008 composition-fidelity extension](../DECISIONS.md) (the-council: 0% of the bundle's component library adopted, every page rebuilt inline, composition drifted ~100%).

**Why DSB and not `context-engineering`:** architecture rule 3 bars `context-engineering` from writing design content ("scaffolds shape, not content; never design tokens"). The adopt wiring *is* design content (`cp` of the rendered design, the design rule), so context-engineering literally cannot own it. DSB is the design layer, already owns bundle-awareness (D-008), already emits a design rule (`design-system.md`), and adopt composes with bootstrap/audit into one design-system-lifecycle skill.

## What adopt-mode does (three pieces, all automatic — no manual step)

1. **`cp` the rendered design into `design/reference/`** (pages + component source). This is the *presence* fix — the drift happened because the design was absent at build time. A copy, not a transform.
2. **`cp` the token values** into the product's own CSS (automates D-008's previously-manual step).
3. **Emit the import rule** into the product's `.claude/rules/` — the ready-to-drop text already drafted in [`design-handoff-adoption.md`](../design-handoff-adoption.md) ("import the components; never rebuild a covered surface; diff each surface against its dated reference; re-snapshot on re-export"). Optional 4th piece: scaffold the mechanical intra-app-consistency hook (greps for inline re-implementations of imported components).

It auto-fires because DSB is already in the chain (prd-creator → context-engineering → DSB) and its intake already scans the working dir for source material — so it detects the bundle when it runs.

## Constraints the plan must honor

- **This amends D-008**, which literally says "no DSB adopt-mode." D-008 banned a *token-transform* mode (the schema-mismatch reasoning); presence + `cp` + a static rule transforms nothing, so it honors D-008's reasoning while reversing its blanket wording. **The plan must include a D-008 amendment** (supersede the "cp by hand / no DSB adopt-mode" clause; keep the Rule-of-Two/Tailwind notes). Log it properly.
- **Not re-litigating the [2026-06-19 council](../council/council-report-2026-06-19-adopt.html).** The council killed a *heavy generator that ports components and enforces fidelity in code*. Adopt-mode does none of that — `cp` + static rule is exactly the lightweight fix the council endorsed, with the delivery gap (Rex won't hand-drop) now filled.
- **Structural change to the hardest skill** → verification class (T): dry-run substitution diffed against `skills/design-system-bootstrap/examples/output-small/`. Route through `/furnace-plan` + Cowork review (the D-014/D-016/D-017 pattern).

## Open questions to resolve during planning

- How does intake distinguish "bootstrap from brand assets" vs "adopt from a Claude Design bundle" — a new cluster-0 branch, or detection of a bundle README?
- Does the `cp`-tokens step fully replace D-008's manual cp, or stay opt-in?
- Is the mechanical intra-app-consistency hook in scope for v1, or deferred (the human fidelity gate ships first)?
- Where does `design/reference/` staleness/re-snapshot live — rule prose only, or a scaffolded check?

## Pointers (all committed)

- Decision: [D-008 + 2026-06-19 extension](../DECISIONS.md) · mirror in [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md).
- Playbook + ready-to-drop rule: [`design-handoff-adoption.md`](../design-handoff-adoption.md).
- Council: [report](../council/council-report-2026-06-19-adopt.html) · [transcript](../council/council-transcript-2026-06-19-adopt.md).
- This session: [retro](../retros/2026-06-19-design-adopt-council.md).

## Next action

Open a fresh session, then: **`/furnace-plan` the DSB adopt-mode per this brief.** The plan should cover the three pieces, the D-008 amendment, and the open questions above.
