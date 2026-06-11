---
paths:
  - "components/**"
  - "features/**/*.jsx"
  - "app/**/*.{jsx,tsx}"
  - "styles/**/*.css"
---

# Design system

Path-scoped rule. Loads when working in any UI file.

This rule has two layers. **Tokens are normative.** `app/styles/tokens.css` is the source of truth for every color, spacing, radius, shadow, and motion value. Product UI must resolve through a CSS custom property, never a literal. **This rule is non-normative rationale.** It carries the design judgment that lives outside the codebase and does not duplicate token values. If the two ever conflict, the CSS file wins.

**Hard rule:** no hardcoded hex values anywhere in product UI.

## Foundations

- **Typography:** Inter for body, Inter for display.
- **Motion:** --motion-easing-hover for hover/color transitions, --motion-duration-fast + --motion-easing-default for other micro-interactions, longer durations for panels and modals. Keyboard-initiated and high-frequency (100+/day) actions use --motion-duration-instant. Spring is an accent for drag/playful moments only.
- **No Tailwind. No shadcn.** Style everything via the design system CSS.
- **Icons:** _TODO: define when icon component ships._

## Layout

Use --space-* tokens for all spacing. Maximum content width 1200px (override per-route).

## Indicator vocabulary

_TODO: Define indicator vocabulary when chip/badge/alert components ship._

### Naming taboo

_TODO: Add forbidden indicator terms when chip/badge/alert components ship._

## Button hierarchy

primary, secondary, ghost, destructive.

Rules:

- Buttons always use sentence case with a focus ring.
- Icon sizes inside buttons are controlled by CSS descendant rules. Never set icon `font-size` inline inside a button.

## Forms and inputs

Inputs use the Input seed component. Required fields show a label asterisk. Errors use --color-error and announce via role='alert'.

## Empty and error states

Every data surface needs a defined empty state. Never render a blank region. Empty states are inline, centered, and calm. No error color unless something actually failed.

## Things to avoid

Hardcoded hex values.

## Cross-references

- Design laws and ARIA: `.claude/rules/design-heuristics.md`.
