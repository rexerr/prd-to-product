# Example: large project, Tailwind path with full brand book

Abbreviated transcript of the design-system-bootstrap skill applied to a large-shape project. Source material is a brand book PDF, Tailwind + shadcn path, full dark mode auto-pair, custom motion. Demonstrates the Tailwind branch end-to-end.

Project: **Atlas Field Notes** — a field research data-collection platform. Multi-user pre-launch, Next.js + Vercel, full brand identity already developed.

## Cluster 0 — source material

> **Q0a.** Brand assets?

> Yes. Uploading brand-book.pdf (52 pages, full identity guide).

> Generator reads the PDF. Extracts:
> - Three brand colors with full scales: Field Green, Cobalt, Sunrise.
> - Typography: Söhne (body), Söhne Breit (display), JetBrains Mono (mono).
> - 4px spacing base, full scale specified.
> - Custom shadow recipes (specific RGBA values).
> - Custom motion: enter 240ms, exit 180ms, custom spring curve.
> - Dark mode is required.
> - Brand book also has a voice-and-tone section ("plainspoken, never folksy") and a list of five product principles.

> **Q0b.** Other source material?

> No.

**Captured:** rich source assets. Generator confirms each cluster as confirm-or-correct. Voice-and-tone section flagged as routed-elsewhere (belongs to prd-creator).

## Cluster 1 — project context

> Q1a — Atlas Field Notes.
> Q1b — `app/styles/tokens.css`.
> Q1c — `app/components/ui/`.
> Q1d — Tailwind + shadcn/ui. **(Tailwind branch)**

> Generator: detection check on `.claude/rules/design-system.md`. File exists. Reading...
> File contains the literal string "No Tailwind. No shadcn." but the OPTIONAL marker for `no_tailwind_ban` is present, suggesting context-engineering left the line conditional.
> Will overwrite the rule file (Q8a will confirm the strategy) and emit the Tailwind-path version of the rule, dropping the no-Tailwind line.

## Cluster 2 — color system

> 2a — Field Green. Token prefix: `field`. Stops 50–900 from PDF.
> 2b — Two secondaries.
>   - Cobalt. Token prefix: `cobalt`. Stops from PDF.
>   - Sunrise. Token prefix: `sunrise`. Stops from PDF.
>   (Generator: Q2b only handles one secondary in V1. Captures Cobalt as the secondary; Sunrise gets recorded in `additional_brand_palettes` and added to `tokens.css` as a primitive, but no semantic alias is mapped to it. Flagged in output summary as "Sunrise primitives present but unmapped — assign a semantic role if you need to use it directly.")
> 2c — Custom neutral scale provided (warm-leaning grays).
> 2d — Custom feedback colors from brand book.
> 2e — Generator proposed semantic mapping; user accepted with two overrides (text-link and brand-primary-hover).

## Cluster 3 — typography

> 3a — Söhne Breit.
> 3b — Söhne.
> 3c — JetBrains Mono. `has_mono_font = true`.
> 3d — Custom scale from brand book (8 sizes with bespoke usage notes).
> 3e — Display sizes yes (3xl, 4xl). `has_display_sizes = true`.
> 3f — Custom line heights.

## Cluster 4 — spacing

> 4a — 4px base. Brand book specifies the full scale. Generator confirms each stop matches the spec.

## Cluster 5 — radius, shadow, motion

> 5a — Custom radius from brand book.
> 5b — Custom shadow recipes — specific RGBA values from spec.
> 5c — Inset shadow yes (used on input pressed state in brand book examples).
> 5d — Custom durations.
> 5e — Custom easing including a brand-specific spring curve.

## Cluster 6 — component personality

> 6a — Compact density. Field research context favors data-dense UIs.
> 6b — Prominent borders. Inputs use 2px borders; cards use 1px.

## Cluster 7 — accessibility floor

> 7a — AA.
> 7b — Glow ring (uses `color-mix`).
> 7c — Reduce, don't eliminate. Long-form interactions stay smooth on reduced-motion.
> 7d — Opt-in via class (`.dark`).
> 7e — Generator proposed dark mappings. User overrode bg-default (`--neutral-800`) and text-primary (`--neutral-50`) for warmer dark surfaces.

## Cluster 8 — integration and confirmation

> Q8a — `.claude/rules/design-system.md` exists, no PARAMETERIZE markers. Generator shows the file content and the proposed Tailwind-path version side by side. User chooses **overwrite** (file was a stale scaffolded version with hand-edits to two lines; user inspected and confirmed the diff is acceptable).

> Q8b — Final preview:
>
> ```
> app/styles/tokens.css
> app/styles/globals.css                  (already present — append @import only)
> app/components/ui/Button.tsx            (Tailwind path: cva-based, no module.css)
> app/components/ui/Card.tsx              (Tailwind path)
> app/components/ui/Input.tsx             (Tailwind path)
> tailwind.config.tokens.ts               (snippet — merge into existing tailwind.config.ts)
> docs/DESIGN_SYSTEM.md
> .claude/rules/design-system.md          (overwriting existing — confirmed)
> ```
>
> Path: Tailwind + shadcn. Three brand colors (one secondary mapped, one primitive only). Mono font present. Display sizes present. Custom shadow recipes. Custom motion. Compact density. Prominent borders. Glow focus ring. Reduce-don't-eliminate motion. Dark mode opt-in via `.dark`.
>
> Routed-elsewhere material:
> - **Voice-and-tone section.** Belongs in prd-creator's `docs/BRAND.md`. Not absorbed here.
> - **Five product principles.** Belongs in prd-creator's PRD `## Product principles` section. Not absorbed here.

> Q8c — Go.

## Notes on what's different from the small and medium cases

- **Tailwind path.** No `.module.css` files emit. Each component is a single `.tsx` file using `cva()`. Token references resolve through `tailwind.config.tokens.ts` extend.colors (e.g., `bg-brand-primary` → `var(--color-brand-primary)`).
- **Tailwind config snippet.** The generator emits `tailwind.config.tokens.ts` as a file-shaped snippet with a comment block at the top explaining "merge into existing tailwind.config.ts." Does not overwrite the existing config.
- **Spacing and radius use Tailwind defaults** even though brand book specified them. The token file still defines `--space-*` and `--radius-*` for raw CSS contexts, but Tailwind components reference Tailwind's scale (`p-4`, `rounded-md`). DESIGN_SYSTEM.md emits the "A note on the Tailwind path" caveat section explaining this.
- **Three brand colors, one mapped.** Sunrise is in the primitives but no semantic alias references it. Surfaced in output summary so the user can decide whether to add `--color-accent: var(--sunrise-500)` or leave it for direct primitive reference.
- **Rule file overwrite confirmed, not silent.** Detection found the existing rule had been hand-edited; generator showed the diff and asked. User confirmed overwrite. The "No Tailwind. No shadcn." line is dropped on Tailwind path via the OPTIONAL `no_tailwind_ban` marker.
- **Glow focus ring** uses `color-mix(in srgb, var(--color-focus-ring) 30%, transparent)` instead of the default outline.
- **Routed-elsewhere material is named explicitly.** Voice-and-tone section and product principles from the brand book are flagged in the output summary as belonging to prd-creator. Not absorbed into this skill's output.
