# Example: medium project, vanilla path with dark mode

Abbreviated transcript of the design-system-bootstrap skill applied to a medium-shape project. Source material is a palette image (paste of hex values from a brand guideline doc), vanilla CSS Modules path, opt-in dark mode via class.

Project: **Threadcount** — a writing-focused journaling app. Single user, Next.js + Vercel, design-first.

## Cluster 0 — source material

> **Q0a.** Brand assets?

> Yes. Pasting from the Threadcount brand doc:
> - Primary: warm orange "Ember" — base #d97706, full scale below.
> - Secondary: deep teal "Verdigris" — base #0f766e, full scale below.
> - Body: Söhne. Display: Söhne Breit.
> - 8px base spacing.
> - Wants dark mode.
>
> [Pasted scales for both colors]

> **Q0b.** Other source material?

> No.

**Captured:** source assets present. Will use brand-doc primitives for both colors. Will propose the rest from Threadcount's defaults; user confirms or corrects.

## Cluster 1 — project context

> Q1a–c — defaults, project=Threadcount.
> Q1d — vanilla CSS path.

## Cluster 2 — color system

> 2a — Ember. Token prefix: `ember`. Display name: Ember. Stops 50–900: provided from brand doc.
> 2b — Verdigris. Token prefix: `verdigris`. Stops 50–900: provided.
> 2c — Use balanced default neutrals. Confirmed.
> 2d — Default feedback colors. Confirmed.
> 2e — Generator proposed semantic mapping. User overrode `--color-text-link` to `--verdigris-700` (matches brand convention; primary brand color is reserved for CTAs).

## Cluster 3 — typography

> 3a — Söhne Breit (display).
> 3b — Söhne (body).
> 3c — No mono.
> 3d — Comfortable scale.
> 3e — No display sizes.
> 3f — Default line heights.

## Cluster 4 — spacing

> 4a — 8px base. Generator derives `--space-1: 8px` through `--space-16: 128px`.

## Cluster 5 — radius, shadow, motion

> 5a — Default radius.
> 5b — Soft shadows.
> 5c — No inset.
> 5d — Mellow motion (150ms / 250ms / 300ms). User wants the journaling app to feel less snappy, more deliberate.
> 5e — Standard easing.

## Cluster 6 — component personality

> 6a — Spacious density. Larger touch targets for the long-form writing context.
> 6b — Hairline borders.

## Cluster 7 — accessibility floor

> 7a — AA.
> 7b — Outline + offset.
> 7c — Disable transitions on reduced-motion.
> 7d — Opt-in dark mode via class (`.dark`).
> 7e — Generator proposed dark token mapping. User confirmed all proposed values except `--color-bg-default` (overrode to `--neutral-800` for a softer dark — `--neutral-900` felt too pure black for a journaling context).

## Cluster 8 — integration and confirmation

> Q8a — `.claude/rules/design-system.md` does not exist. Will write fresh.
>
> Q8b — Final preview:
>
> ```
> app/styles/tokens.css
> app/styles/globals.css
> app/components/ui/Button.tsx + Button.module.css
> app/components/ui/Card.tsx + Card.module.css
> app/components/ui/Input.tsx + Input.module.css
> docs/DESIGN_SYSTEM.md
> .claude/rules/design-system.md
> ```
>
> Path: vanilla CSS Modules. Dark mode opt-in via `.dark` class. Two brand colors. 8px base spacing. Mellow motion. Spacious density.

> Q8c — Go.

## Notes on what's different from the small case

- **Two brand color scales emit** instead of one. `tokens.css` gets the `ember-*` and `verdigris-*` blocks. `--color-brand-primary` resolves to `--ember-500`. `--color-text-link` overrides to `--verdigris-700`.
- **Dark mode block emits.** A `.dark` selector at the bottom of `tokens.css` overrides every semantic alias. Components do not change — they reference the same semantic tokens, which resolve differently under `.dark`.
- **Component vertical rhythm differs.** Spacious density makes Button heights 36 / 44 / 52 instead of 32 / 40 / 48. Input height is 44 instead of 40.
- **Motion durations differ.** All component transition references resolve to mellow values via the token layer; component code unchanged.
- **DESIGN_SYSTEM.md gains a dark mode section** documenting the dark token overrides and the `.dark` class convention.
