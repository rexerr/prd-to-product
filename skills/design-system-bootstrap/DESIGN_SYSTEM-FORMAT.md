<!-- Authority: this file is the single source of truth for the DESIGN_SYSTEM.md body-shape — the section skeleton (names + order, including the H4 token-domain breakdown) and the failure-cited rules for the doc's opening and placement. On any conflict between a thin restatement elsewhere (the template's loaded cues, SKILL.md's file-list mention, principles.md's rationale) and this file, THIS FILE WINS. Diff it against examples/output-small/docs/DESIGN_SYSTEM.md to verify shape. Adopted via CF-29 / D-057. -->

# DESIGN_SYSTEM-FORMAT — shape contract for `DESIGN_SYSTEM.md`

What lives where: `SKILL.md` routes; `templates/DESIGN_SYSTEM.md.template` is the **loaded** artifact at generation (step 6), carrying the `PARAMETERIZE` markers plus the operative cues that must fire while the doc is written (`**Hard rule:**`, the `## Positioning anchor` section, `**Rationale rule.**`); **this file** is the reference authority — the canonical skeleton + the failure-cited shape rules, diffable against the example. `principles.md` holds the *why* (the two-tier architecture, naming, why three components); this file holds the *what* of the doc's shape. This file governs the `DESIGN_SYSTEM.md` doc only — not `tokens.css` or the components (see "What this file does not govern").

## Canonical section skeleton

The doc has one **core skeleton** (always emitted), plus OPTIONAL pieces that appear by captured answer or project shape. This is the **ordering authority** — do not re-list section order anywhere else.

**Core skeleton — required, in order** (verified against `examples/output-small/docs/DESIGN_SYSTEM.md`):

```
# Design system                       H1: doc title only
## Positioning anchor                 the one line the system is remembered for
## Token system
### Color
#### Backgrounds                      semantic background roles
#### Text                             semantic text roles
#### Borders                          semantic border roles
#### Brand interactive                CTA / brand action roles
#### Feedback                         success / warning / error / info roles
#### Focus                            focus-ring role
### Typography
#### Families                         family roles (may collapse to prose for a single display+body family — see below)
#### Type scale                       the type scale table (heading may carry a density descriptor, e.g. "Type scale (comfortable)")
#### Weights                          weight tokens
### Spacing
### Radius
### Shadows
### Motion
## Seed components
### Button
### Card
### Input
## What is not in this file
## Cross-references
```

**Heading-level OPTIONAL section** (allowed-absent; the only OPTIONAL that adds a heading): `### A note on the Tailwind path` (gated `OPTIONAL: tailwind_path`), placed at the end of `## Token system`.

**Row-level OPTIONAL content** (a conditional *row inside* a core section, never its own heading — so not a skeleton entry): `--color-brand-secondary` / `--color-brand-secondary-hover` rows under `#### Brand interactive` (gated `has_secondary_brand_color`); the `--type-family-mono` row under `#### Families` (gated `has_mono_font`). When a project supplies a single display+body family, `#### Families` may collapse to one prose line instead of a table — the small shape does this.

**Shape-gated additions** (larger shapes only; sourced from `NOTES.md` regression definitions, **not currently emitted by the template** — a known gap this contract surfaces but does not close):

- *Medium shape* documents dark-mode token conventions in the doc (`NOTES.md` "Medium shape"). Dark mode itself is a `tokens.css` block gated by `has_dark_mode`; this is the doc's prose about it, not a doc section of its own.
- *Large shape* adds a complete token listing and an **accessibility-notes** section (`NOTES.md` "Large shape").

## Per-section shape rules

One line each — what each section must contain.

- **Positioning anchor** — one blockquoted line (`> …`) naming what the system should be remembered for, captured at intake (Q1e), followed by the falsifiable-rationale rule (below). No token values here.
- **Token system → Color** — six H4 domains in the order above; each a `Token | Role` table of semantic aliases (not primitives, not raw hex). Focus ring states its 3:1 contrast requirement.
- **Token system → Typography** — Families (display + body, optional mono), Type scale (table), Weights. Never px font sizes in prose — token names only.
- **Token system → Spacing / Radius / Shadows / Motion** — one table or short list each, naming tokens and their role; the base unit is stated for Spacing; Motion names duration/easing pairs.
- **Seed components** — exactly three (Button, Card, Input), each an H3 naming its variants and the token-driven states it proves. Never more than three (the seed set is a proof, not a library).
- **What is not in this file** — points at context-engineering's `.claude/rules/design-system.md` for behavior constraints and prd-creator's `BRAND.md` for voice. Names what the doc deliberately omits, so a reader does not look here for it.
- **Cross-references** — the canonical token file path, the globals path, and (conditionally) the design-heuristics rule and brand doc.

## The positioning anchor and falsifiable-rationale rules

Relocated from `principles.md` (the failure-cited bodies; `principles.md` keeps the rationale + a pointer). The operative echo that fires at generation lives in the loaded template (`## Positioning anchor` + `**Rationale rule.**`) — these are the diffable reference statement of the same rules.

- **Positioning anchor.** `DESIGN_SYSTEM.md` opens with a positioning anchor: one line naming what the system should be remembered for, captured at intake (Q1e) and checked against every token choice thereafter. When source material is present, propose a candidate anchor extracted from it; the user always owns the final line. *Failure it prevents: a coherent-but-generic palette — a system that tries to be memorable for everything is memorable for nothing, so a value chosen to serve no particular intent defaults to the generic AI aesthetic.*
- **Falsifiable rationale.** Wherever the doc (or the interview) explains *why* a token holds a value, the reason must cite a concrete observation — a brand asset, a stated brand attribute, a measured contrast ratio — never a vibe. "Feels clean," "looks professional," and "modern" are banned: they are unfalsifiable and justify any value equally. This is invariant #2 ("every rule cites its failure mode") turned on design judgments — cite an observable. *Adopted from gstack `G-19` ([D-050](../../docs/DECISIONS.md)).*

## Progressive-disclosure placement

Relocated from `principles.md`. `DESIGN_SYSTEM.md` follows the same position-aware placement principle as the PRD and `AGENTS.md`. The load-bearing facts go at the top: the positioning anchor, then which token file is canonical, the no-hardcoded-values hard rule, where the linter command lives. Details (full token listing, component props tables) go in the middle. "What is not in this file" goes at the bottom. *Failure it prevents: the U-shaped attention curve penalizes the middle, so a load-bearing fact buried there is read as optional.*

## What this file does not govern

This file is the shape contract for the `DESIGN_SYSTEM.md` doc **only**. The shape of the other artifacts this skill emits is governed elsewhere and is authoritative there:

- **Token-file structure** (two-tier primitives + semantic aliases, six color domains, RGBA shadows, motion pairs) — `principles.md` "The two-tier token architecture" and "Conventions for writing token values"; the operative invariant ("no raw hex in the semantic layer") is a `SKILL.md` binding contract.
- **Token naming** — `principles.md` "Token naming convention".
- **Component structure** (variant-prop, CSS Modules, accessible-by-default, three-components-max) — `principles.md` "Why three seed components" and "Component architecture"; the three-components-max invariant is a `SKILL.md` binding contract.
- **The output file list and the non-destructive write guard** — `generator/decisions.md`.

These are operative invariants that fire at generation and stay in their loaded homes; a FORMAT file per output type would be sprawl, not consolidation.
