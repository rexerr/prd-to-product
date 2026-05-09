# Example: small project, vanilla CSS path

A worked example of the design-system-bootstrap skill applied to a small hypothetical project. Direct text input, no source assets, vanilla CSS Modules path, no dark mode. Demonstrates the always-on path through the generator.

Project: **Linkpad** — a personal link-saver app. Single user, Next.js + Vercel, no design system yet.

## Cluster 0 — source material

> **Q0a.** Do you have a brand book, palette image, Figma file, screenshot, or notes for this design system? Paste, link, upload, or say "no."

> No, just direct values. Primary is indigo (#4f46e5).

> **Q0b.** Anything else relevant? (Existing site you want to match, competitor reference, prior token file.) Optional.

> No.

**Captured:** no source assets. Direct fills throughout.

## Cluster 1 — project context

> **Q1a–c.** Project name? Token file path? Component path?

> Linkpad. Defaults are fine — `app/styles/tokens.css` and `app/components/ui/`.

> **Q1d.** Styling approach. How does this project style components?
> — Vanilla CSS (CSS Modules, no Tailwind)
> — Tailwind + shadcn/ui

> Vanilla.

**Captured:** project=Linkpad, paths=defaults, styling_path=`vanilla_css_modules`.

## Cluster 2 — color system

> **Q2a-i, ii, iii.** Primary brand color (hex). Token prefix. Display name.

> #4f46e5. Prefix: indigo. Name: Indigo.

> **Q2a-iv.** How should the 50–900 stops be derived?
> — Provide all 9 stops
> — Derive from base

> Derive.

> Generator: derived `--indigo-50: #eef2ff` through `--indigo-900: #312e81`. Confirm or override?

> Confirm.

> **Q2b-i.** Secondary brand color?

> No.

> **Q2c-i.** Neutral scale?

> Use the balanced default.

> **Q2d-i.** Feedback colors? Defaults: success #16a34a / warning #d97706 / error #dc2626 / info #2563eb. Override?

> Defaults are fine.

> **Q2e-i, ii, iii.** Semantic mapping? (Generator proposes, user confirms.)

> Confirm all defaults.

**Captured:** indigo as primary, balanced neutrals, default feedback, default semantic mappings.

## Cluster 3 — typography

> **Q3a–c.** Display family? Body family? Mono?

> Display: Inter. Body: Inter. No mono.

> **Q3d.** Type scale?
> — Compact / Comfortable / Generous / Custom

> Comfortable.

> **Q3e.** Display sizes (3xl, 4xl)?

> No.

> **Q3f.** Line heights?

> Default.

**Captured:** Inter for both, comfortable scale, no display sizes, default line heights.

## Cluster 4 — spacing

> **Q4a.** Base unit?
> — 4px (recommended)
> — 8px

> 4px.

**Captured:** 4px base. Generator derived `--space-1: 4px` through `--space-16: 64px`.

## Cluster 5 — radius, shadow, motion

> **Q5a.** Radius scale?
> — Sharp / Default / Rounded / Custom

> Default.

> **Q5b.** Shadow weight?
> — Soft / Crisp / None

> Soft.

> **Q5c.** Inset shadow?

> No.

> **Q5d.** Motion durations?
> — Snappy / Mellow / Custom

> Snappy.

> **Q5e.** Easing curves?
> — Standard / Custom

> Standard.

**Captured:** default radius, soft shadows, no inset, snappy motion, standard easing.

## Cluster 6 — component personality

> **Q6a.** Density?
> — Compact / Default / Spacious

> Default.

> **Q6b.** Border emphasis?
> — Hairline / Prominent / Borderless

> Hairline.

**Captured:** default density, hairline borders.

## Cluster 7 — accessibility floor

> **Q7a.** WCAG target?

> AA.

> **Q7b.** Focus ring style?

> Outline + offset.

> **Q7c.** Reduced-motion behavior?

> Disable transitions.

> **Q7d.** Dark mode strategy?
> — None / Opt-in via class / Opt-in via media

> None.

**Captured:** WCAG AA, default focus, default reduced-motion, no dark mode.

## Cluster 8 — integration and confirmation

> **Q8a.** Existing design-system rule? (Generator checks `.claude/rules/design-system.md`.)

> Generator: file does not exist. Will write fresh.

> **Q8b.** Final preview.

> Files to write:
> ```
> app/styles/tokens.css
> app/styles/globals.css
> app/components/ui/Button.tsx
> app/components/ui/Button.module.css
> app/components/ui/Card.tsx
> app/components/ui/Card.module.css
> app/components/ui/Input.tsx
> app/components/ui/Input.module.css
> docs/DESIGN_SYSTEM.md
> .claude/rules/design-system.md
> ```
>
> Path: vanilla CSS Modules. No dark mode. No mono font. No display sizes. No secondary brand color.

> **Q8c.** Confirm before writing.

> Go.

## Generator writes files. Output summary follows.

See `examples/output-small/` for the full file tree the generator produced.
