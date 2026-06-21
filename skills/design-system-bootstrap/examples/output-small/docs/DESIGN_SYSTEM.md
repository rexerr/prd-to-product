# Design system

This file is the semantic reference for Linkpad's design system. The token file at `app/styles/tokens.css` is the normative source for all values. This file explains what those tokens mean and when to use them.

**Hard rule:** no hardcoded hex values, px font sizes, or magic spacing numbers anywhere in product UI. Every visual value resolves through a token.

## Positioning anchor

> Linkpad is remembered for *making a shared link feel instant* — one saturated brand hue (indigo) on a calm neutral field, so the primary action is never in doubt.

Every token choice serves this line; a value that serves nothing in particular is generic by default. **Rationale rule:** every "why" in this file cites a concrete observation (brand asset, stated attribute, measured contrast), never a vibe — "feels clean" / "looks professional" are banned.

## Token system

### Color

Tokens follow a two-tier structure: primitives (raw values, defined but not used in components) and semantic aliases (role-named tokens that components reference).

#### Backgrounds

| Token | Role |
|---|---|
| `--color-bg-default` | Primary page and app background |
| `--color-bg-elevated` | Cards, popovers, modals — surfaces that float above default |
| `--color-bg-subtle` | Sidebars, secondary panels, muted regions |
| `--color-bg-inverse` | Dark surfaces on a light theme; inverts fg/bg |

#### Text

| Token | Role |
|---|---|
| `--color-text-primary` | Body text, headings — highest contrast |
| `--color-text-secondary` | Metadata, labels, supporting copy |
| `--color-text-tertiary` | Placeholders, disabled text, hints |
| `--color-text-inverse` | Text on dark or brand-colored surfaces |
| `--color-text-link` | Inline links |

#### Borders

| Token | Role |
|---|---|
| `--color-border-default` | Standard dividers, input borders at rest |
| `--color-border-strong` | Focused inputs, selected states, emphasis borders |
| `--color-border-subtle` | Very light separators — hairlines between sections |

#### Brand interactive

| Token | Role |
|---|---|
| `--color-brand-primary` | Primary CTA background (buttons, key actions) |
| `--color-brand-primary-hover` | CTA hover state |
| `--color-brand-primary-text` | Text on primary CTA surfaces |

#### Feedback

| Token | Role |
|---|---|
| `--color-success` / `--color-success-bg` | Success states |
| `--color-warning` / `--color-warning-bg` | Warning states |
| `--color-error` / `--color-error-bg` | Error states and destructive actions |
| `--color-info` / `--color-info-bg` | Informational states |

#### Focus

`--color-focus-ring` — focus ring color on all interactive elements. Currently `var(--indigo-500)`. Must meet 3:1 contrast against `--color-bg-default` (white). Confirmed at AA.

---

### Typography

`--type-family-display` and `--type-family-body` both resolve to Inter. No mono family in this project.

#### Type scale (comfortable)

| Token | Value | Common uses |
|---|---|---|
| `--type-size-2xs` | 12px | Metadata, captions |
| `--type-size-xs` | 14px | Body small, helper text |
| `--type-size-sm` | 16px | Body, buttons, labels |
| `--type-size-md` | 18px | Card titles, prominent labels |
| `--type-size-lg` | 21px | h3 |
| `--type-size-xl` | 24px | h2 |
| `--type-size-2xl` | 30px | h1 |

Rules:
- Use `--type-size-sm` for most UI.
- Use `--type-size-xs` or smaller for metadata and helper text.
- Use `--type-size-lg` and above for headings.
- Never set `font-size` in px. Use only tokens from this scale.

#### Weights

`--type-weight-normal` (400), `--type-weight-medium` (500), `--type-weight-semibold` (600), `--type-weight-bold` (700).

---

### Spacing

Base unit: 4px. Every spacing token is a multiple.

| Token | Value | Common uses |
|---|---|---|
| `--space-1` | 4px | Gap between icon and label |
| `--space-2` | 8px | Tight component padding |
| `--space-3` | 12px | Compact list items |
| `--space-4` | 16px | Standard padding |
| `--space-5` | 20px | Section padding |
| `--space-6` | 24px | Component gaps |
| `--space-7` | 28px | Section gaps |
| `--space-8` | 32px | Large layout spacing |
| `--space-10` | 40px | Page-level margins |

---

### Radius

| Token | Value | Use |
|---|---|---|
| `--radius-none` | 0 | No rounding |
| `--radius-sm` | 4px | Chips, badges, small tags |
| `--radius-md` | 6px | Buttons, inputs, small cards (default) |
| `--radius-lg` | 8px | Cards, modals |
| `--radius-xl` | 12px | Feature hero cards |
| `--radius-full` | 9999px | Pills, avatar circles |

---

### Shadows

Soft scale. `--shadow-xs` for hairline lift through `--shadow-xl` for full overlays. See `tokens.css` for exact RGBA values.

---

### Motion

Snappy tempo. fast 120ms, normal 200ms, slow 280ms; instant (0ms) for keyboard-initiated and high-frequency actions. Standard easing: the semantic `--motion-easing-*` tokens (default / enter / exit / spring / hover / linear) pick from the fixed `--ease-*` bank in `tokens.css`. Exits run ~20% faster than entrances; paired elements share one easing and one duration. All transitions respect `prefers-reduced-motion` via the global rule in `globals.css`.

---

## Seed components

### Button

**File:** `app/components/ui/Button.tsx`

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `"primary" \| "secondary" \| "ghost" \| "destructive"` | `"primary"` | |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | |
| `disabled` | `boolean` | `false` | |
| `children` | `ReactNode` | required | |

**Accessibility:** `<button>` element; `aria-disabled` on disabled; focus ring via `:focus-visible` using `--color-focus-ring`.

---

### Card

**File:** `app/components/ui/Card.tsx`

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `"default" \| "elevated" \| "outlined" \| "ghost"` | `"default"` | |
| `as` | `"div" \| "article" \| "section" \| "li"` | `"div"` | |
| `onClick` | `() => void` | — | Makes the card clickable. Adds `role="button"` and keyboard support. |

**Sub-components:** `Card.Header`, `Card.Body`, `Card.Footer` — optional layout slots.

---

### Input

**File:** `app/components/ui/Input.tsx`

| Prop | Type | Default | Notes |
|---|---|---|---|
| `label` | `string` | required | Always required for accessibility. |
| `hideLabel` | `boolean` | `false` | Hides visually; keeps in accessibility tree. |
| `error` | `string` | — | Triggers error state. |
| `hint` | `string` | — | Helper text when no error. |

**Accessibility:** `aria-invalid` on error; `aria-describedby` wired to error or hint; `forwardRef` for form library compatibility.

---

## What is not in this file

This file covers token semantics and the seed component catalog. Behavior constraints (scope limits, verification before claiming done) live in `.claude/rules/session-discipline.md` and the always-on sections of `AGENTS.md`. Voice and copy rules live in `docs/BRAND.md` if that file exists.

## Cross-references

- Token source of truth: `app/styles/tokens.css`
- Global resets and import: `app/styles/globals.css`
- Design-system rule (agent-facing constraints): `.claude/rules/design-system.md`
