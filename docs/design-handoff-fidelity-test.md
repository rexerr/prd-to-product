# Fidelity test — transcribing The Council bundle into our two-tier `tokens.css`

**Date:** 2026-06-09. **Input:** `the-council/spikes/claude-design/` (3 surfaces: Session, Terminal, Extension Panel + `tweaks-panel.jsx` colorway picker). **Target schema:** [`skills/design-system-bootstrap/templates/tokens.css.template`](../skills/design-system-bootstrap/templates/tokens.css.template). **Artifact:** `/tmp/council-fidelity/tokens.adopted.css` (the honest transcription).

This is the empirical test the council's verdict turned on: *can our two-tier schema hold base + N theme-overrides + motion + `oklch` accents LOSSLESSLY?*

## Result: value-lossless, structurally non-isomorphic

**Values — 100% preserved.** All 40 global tokens across the three surfaces transcribe verbatim: 5 `oklch()` advisor accents, 2 `cubic-bezier()` easings, 3 `rgba()` alpha composites, 2 bespoke scalars. They're all valid CSS — copying them can't lose information. Coverage diff: zero global tokens dropped. (The only token the sweep flagged, `--accent: var(--ink)`, is scoped *inside* a `.card {}` block — a component-local var, not a design token; correctly out of scope, it's "recreate" territory per the bundle's README.)

**Structure — our DSB template schema does NOT fit.** Four concrete mismatches, each forcing a mutation if you bend the bundle into the template:

1. **Primitive model is wrong [the big one].** The DSB template's primitive tier is built on 10-step generated *scales* (`brand-50…900`, `neutral-0…900`). The bundle has **no scales** — it has curated flat values (`--field`, `--plate`, `--gold`) and 3-step ramps (`--chrome`/`-2`/`-3`, `--signal`/`-2`/`-3`). Filling `…-50…900` would **fabricate 7–8 shades the designer never chose — that's *generating*, the exact anti-goal.** The honest shape inverts the model: the bundle's curated values *are* the primitives.
2. **Font slots too few.** Template has exactly 3 family slots (display/body/mono). The bundle uses **6 distinct stacks** across surfaces (IM Fell SC, IM Fell italic, IBM Plex Sans, IBM Plex Mono, VT323, Newsreader). Forcing 3 slots drops three families.
3. **No slot for whole token classes.** Five *categorical* advisor accents (not brand-primary/secondary, not feedback), the `--crt: 0.45` effect-intensity scalar, and the `--placeholder-tag-display` layout toggle have **no tier** in the schema (color/type/space/radius/shadow/motion/z). Values copy fine; they're homeless structurally.
4. **One theme block vs. many.** The template emits a *single* dark-mode override block. The bundle needs base + `body.twilight` + per-surface foreground + N runtime colorways. **The pattern fits perfectly** (class-based override of semantic aliases is exactly DSB's dark-mode mechanism) — but the fixed *single-block* schema doesn't; you add `body.X {}` blocks.

## What this settles

- **The Skeptic's "fidelity trap" was real — but precisely scoped.** It is NOT "CSS-vars can't be adopted" (they map cleanly — the bundle even ships a `var()` alias, `--ok: var(--signal)`). It's specifically that the **DSB scale-first template** mutates a curated-value input. Adopt by filling that template → you fabricate scales and drop fonts. Confirmed.
- **Rex's theme-picker correction holds.** Theming is the *mechanical* part: twilight + colorways + surfaces are all `body.X {}` override blocks — repeatable, lossless, the good case for class-based tokens. It is **not** the irreducible-judgment risk the first council framing implied.
- **The right adopted artifact is a different, simpler shape than DSB generates:** flat-primitives (the bundle's values) + a thin semantic-alias layer + N class-override theme blocks. Mechanical enough to be a **small command**, not a skill and not a DSB mode (which is scale-first).

## The one residual human judgment (small, askable)

Which colorway/theme variants are **shipped product themes** vs **design-time exploration** in the tweaks panel. The PRD commits to light/dark ("oracle mode dark by default"); the 4 colorway presets (`#D97757` clay, blue, green, violet) look like tweak-tool samples, not necessarily V1 product themes. That's a one-line question to the user — not a reconciliation epic.

## Implication for the build decision

Do **not** adopt by filling the DSB template (structurally lossy → fabrication). If a token-adopt is built, it emits the flat-primitive + N-theme shape and is a small command under the write guard; component recreation stays delegated to the bundle's own README. This is the question the final council audit pressure-tests.
