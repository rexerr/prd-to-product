# Generator intake

The question flow Claude runs when the design-system-bootstrap skill is invoked. Nine clusters, asked sequentially. Cluster boundaries matter. Do not interleave.

## Question contract

- One cluster at a time. Do not dump every question at once.
- Per call: 2 to 4 options for branching questions; up to 3 questions per call.
- Free-text questions ask one at a time and accept open answers.
- Branching questions return a label the generator can match against `decisions.md`.
- After every cluster, summarize what was captured before moving on. The user can correct before the next cluster begins.
- **Source material first.** Cluster 0 captures any brand book, palette, or design assets before the question flow begins. When source material is provided, downstream clusters run as confirm-or-correct against extracted answers, not fill-from-scratch.
- **Default to asking, not detecting.** Even when context-engineering output is in the working directory, ask the cluster 1 styling question explicitly. Use detection signals as confirmation only when unambiguous.

## Cluster 0: Source material (always — runs before anything else)

The user often arrives with a brand book, a palette image, a Figma export, or a screenshot of an existing product they want to mirror. This cluster captures it before the question flow begins.

**Always ask Q0a explicitly, even if material appears to be in conversation context.** Silent absorption is the failure mode that makes the user wonder later "did the agent actually use my brand book or guess?" Asking out loud forces the user to confirm intent.

Ask in one call:

0a. **Brand assets.** Do you have a brand book, palette image, Figma file, screenshot, or notes for this design system? Paste, link, upload, or say "no."
0b. **Other source material.** Anything else relevant? (Existing site you want to match, competitor reference, prior token file, design spec doc.) Optional.

If material is provided:

- Read or extract from it before proceeding. When you reference or summarize it to the user, describe what it contains; do not speculate about when it was made or how dated it looks (no "this brand book looks a bit old") unless the material itself states a date you can cite.
- Extract proposed answers for cluster 2 (color), cluster 3 (typography), cluster 4 (spacing if specified), cluster 5 (radius/shadow/motion if specified). Most brand books cover color and type; few cover the rest.
- For each downstream cluster where extraction yielded proposed answers, present them as "I extracted X from your brand book — confirm or correct" rather than asking the question cold.
- For clusters where the source material has no relevant content, ask the user normally.

If no material is provided, run all downstream clusters as cold-start fill flows.

State map keys set by cluster 0:

- `source_assets_present` — bool
- `source_assets_summary` — string (one paragraph naming what was provided)
- `source_other_material` — string (optional)

## Cluster 1: Project context

Captures basics and the load-bearing styling-approach branch.

If context-engineering output is detected (an `AGENTS.md` or `.claude/rules/design-system.md` exists in the working directory), the generator may propose answers for Q1a–Q1c from that material. Q1d (styling approach) is always asked explicitly.

Ask in one call:

1a. **Project name.** Free text. → `project_name`.
1b. **Token file path.** Where should `tokens.css` live? Default `app/styles/tokens.css`. → `token_file_path`.
1c. **Component path.** Where should the seed components live? Default `app/components/ui/`. → `component_dir_path`.

Then a separate call for the branch question:

1d. **Styling approach.** How does this project style components?
   - **Vanilla CSS** — CSS Modules per component. Tokens via CSS custom properties. No Tailwind.
   - **Tailwind + shadcn/ui** — Tailwind utilities, `cva()` variants. Tokens wired into `tailwind.config.ts`.

→ `styling_path` (`vanilla_css_modules` or `tailwind_shadcn`)

**Detection-as-confirmation, not silent default.** If a `.claude/rules/design-system.md` file exists with the literal string "No Tailwind. No shadcn." present (and not commented out via OPTIONAL marker), the generator may propose vanilla as the default but must still ask: "Your design-system rule file forbids Tailwind. Confirm vanilla CSS path? Y/N." If the rule does not contain that line, or no rule file exists, ask Q1d cold without a proposed default.

## Cluster 2: Color system

Two phases: primitives, then semantic mapping.

If source assets specified palette colors, propose them and ask for confirmation. Otherwise ask cold.

### 2a. Primary brand color

2a-i. **Primary brand color.** What is the base color (typically the 500 stop on a 50–900 scale)? Hex value. → `brand_primary_500`.
2a-ii. **Token prefix.** Short word for this color (used as `--<prefix>-50` through `--<prefix>-900`). Example: "indigo", "twilight", "primary". → `brand_primary_token_prefix`.
2a-iii. **Display name for the color** (used in comments). → `brand_primary_name`.

Then ask whether to derive the scale or fill it manually:

2a-iv. **Color scale.** How should the 50–900 stops be derived?
   - **Provide all 9 stops.** Free text, paste hex values for 50/100/.../900.
   - **Derive from base.** Generator computes a balanced scale from the 500 stop using a perceptual lightness curve.

If "Provide all 9 stops": ask one fill for the full set. → `brand_primary_50` through `brand_primary_900`.
If "Derive from base": compute and confirm before locking. → same nine state keys.

### 2b. Secondary brand color (optional)

2b-i. **Do you have a secondary brand color?**
   - **Yes** — repeat the 2a flow for `brand_secondary_*`. Sets `has_secondary_brand_color = true`.
   - **No** — skip. Sets `has_secondary_brand_color = false`.

### 2c. Neutral scale

2c-i. **Neutral scale.** How should the neutral (grays) be derived?
   - **Provide all 9 stops.** Paste hex values.
   - **Use a balanced default.** Generator emits a neutral-50 through neutral-900 scale from `#fafafa` to `#0a0a0a`.

→ `neutral_50` through `neutral_900`.

### 2d. Feedback colors

2d-i. **Feedback colors.** Pick base colors for success, warning, error, info. Default set provided; user can override per color.

Defaults: success `#16a34a` / `#dcfce7`, warning `#d97706` / `#fef3c7`, error `#dc2626` / `#fee2e2`, info `#2563eb` / `#dbeafe`.

→ `feedback_success`, `feedback_success_light`, `feedback_warning`, `feedback_warning_light`, `feedback_error`, `feedback_error_light`, `feedback_info`, `feedback_info_light`.

### 2e. Semantic role mapping

For each semantic alias, the generator proposes a sensible default mapped to a primitive. The user confirms or overrides.

2e-i. **Semantic background mapping.** Confirm the proposed mapping or override:
   - `--color-bg-default` → `--neutral-0` (white)
   - `--color-bg-elevated` → `--neutral-0`
   - `--color-bg-subtle` → `--neutral-50`
   - `--color-bg-inverse` → `--neutral-900`

2e-ii. **Semantic text mapping.**
   - `--color-text-primary` → `--neutral-900`
   - `--color-text-secondary` → `--neutral-700`
   - `--color-text-tertiary` → `--neutral-500`
   - `--color-text-inverse` → `--neutral-0`
   - `--color-text-link` → `--<brand_primary_token_prefix>-600`

2e-iii. **Semantic border mapping.**
   - `--color-border-default` → `--neutral-200`
   - `--color-border-strong` → `--neutral-400`
   - `--color-border-subtle` → `--neutral-100`

→ `color_bg_default`, `color_bg_elevated`, `color_bg_subtle`, `color_bg_inverse`, `color_text_primary`, `color_text_secondary`, `color_text_tertiary`, `color_text_inverse`, `color_text_link`, `color_border_default`, `color_border_strong`, `color_border_subtle`.

## Cluster 3: Typography

3a. **Display family.** Font family for headings. Free text. Default: same as body. → `font_family_display`.
3b. **Body family.** Font family for body text and UI. Free text. → `font_family_body`.
3c. **Monospace family?**
   - **Yes** — fill `font_family_mono`. Sets `has_mono_font = true`.
   - **No** — skip. Sets `has_mono_font = false`.

3d. **Type scale.** Pick a scale shape:
   - **Compact.** 11 / 12 / 14 / 16 / 18 / 21 / 28 / 36 (px). For dense UIs.
   - **Comfortable.** 12 / 14 / 16 / 18 / 21 / 24 / 30 / 40 (px). For balanced UIs.
   - **Generous.** 14 / 16 / 18 / 20 / 24 / 32 / 48 / 64 (px). For marketing-leaning UIs.
   - **Custom.** Provide your own scale.

→ `type_size_2xs`, `type_size_xs`, `type_size_sm`, `type_size_md`, `type_size_lg`, `type_size_xl`, `type_size_2xl`. Plus a derived `type_scale_table` for the docs template.

3e. **Display sizes.** Need sizes above 2xl (display, hero, marketing)?
   - **Yes** — fill `type_size_3xl`, `type_size_4xl`. Sets `has_display_sizes = true`.
   - **No** — skip.

3f. **Line heights.** Pick a set:
   - **Default.** tight 1.2 / normal 1.5 / relaxed 1.7.
   - **Custom.** Free text per token.

→ `line_height_tight`, `line_height_normal`, `line_height_relaxed`.

## Cluster 4: Spacing

4a. **Base unit.** What is the base spacing unit?
   - **4px (recommended).** Tailwind's default. Multiples scale evenly.
   - **8px.** Coarser scale; works for spacious layouts.

→ `spacing_base_unit`.

The generator derives `space_1` through `space_16` from the base unit via the rule: `space_n = base × n` for `n` in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16). Skipping 9, 11, 13–15 keeps the scale focused. The user can override individual stops.

→ `space_1` through `space_16`.

## Cluster 5: Radius, shadow, motion

5a. **Radius scale.** Pick the project's tightness:
   - **Sharp.** 2 / 4 / 6 / 8 (px). Square-feeling UI.
   - **Default.** 4 / 6 / 8 / 12 (px). Modern UI baseline.
   - **Rounded.** 6 / 10 / 14 / 20 (px). Friendlier UI.
   - **Custom.** Provide values for sm/md/lg/xl.

→ `radius_sm`, `radius_md`, `radius_lg`, `radius_xl`.

5b. **Shadow weight.** Pick a recipe:
   - **Soft (default).** Subtle, restrained — five-stop scale from hairline to full overlay.
   - **Crisp.** Tighter shadows with sharper edges; better for compact data UIs.
   - **None.** Use borders instead of shadows. Generator emits `--shadow-*: none` placeholders for compatibility.

→ `shadow_xs`, `shadow_sm`, `shadow_md`, `shadow_lg`, `shadow_xl`.

5c. **Inset shadow needed?** (For input focus rings or pressed states.)
   - **Yes** — fill `shadow_inset`. Sets `has_inset_shadow = true`.
   - **No** — skip.

5d. **Motion durations.** Pick a tempo:
   - **Snappy (default).** fast 120ms / normal 200ms / slow 320ms.
   - **Mellow.** fast 180ms / normal 280ms / slow 440ms.
   - **Custom.** Free text per token.

→ `motion_duration_fast`, `motion_duration_normal`, `motion_duration_slow`.

5e. **Easing curves.** Pick a set:
   - **Standard (default).** default `cubic-bezier(0.4, 0, 0.2, 1)`, enter `cubic-bezier(0, 0, 0.2, 1)`, exit `cubic-bezier(0.4, 0, 1, 1)`, spring `cubic-bezier(0.34, 1.56, 0.64, 1)`.
   - **Custom.** Free text per token.

→ `motion_easing_default`, `motion_easing_enter`, `motion_easing_exit`, `motion_easing_spring`.

## Cluster 6: Component personality (light parameterization)

These shape default values inside the seed components. Most users accept defaults.

6a. **Density.** Default component vertical rhythm:
   - **Compact.** Buttons 28 / 36 / 44 px tall. Inputs 36 px.
   - **Default.** Buttons 32 / 40 / 48 px tall. Inputs 40 px.
   - **Spacious.** Buttons 36 / 44 / 52 px tall. Inputs 44 px.

→ `component_density` (state map; affects derived sizing in component CSS modules and Tailwind classes).

6b. **Border emphasis.**
   - **Hairline (default).** 1px borders, used sparingly.
   - **Prominent.** 2px borders on inputs and outlined cards.
   - **Borderless.** Shadows and backgrounds carry separation.

→ `border_emphasis`.

## Cluster 7: Accessibility floor

7a. **WCAG target.**
   - **AA (default).** 4.5:1 for body text, 3:1 for large text and UI.
   - **AAA.** 7:1 for body text, 4.5:1 for large text. Stricter; constrains color choices.

→ `wcag_target`.

7b. **Focus ring style.**
   - **Outline + offset (default).** 2px outline, 2px offset. Most legible across backgrounds.
   - **Glow ring.** Soft outer ring using `color-mix()`. Less visually heavy.
   - **Inset.** Border-color shift, no outline. Most subtle.

→ `focus_ring_style`.

7c. **Reduced-motion behavior.**
   - **Disable transitions (default).** All animations under 0.01ms when `prefers-reduced-motion: reduce`.
   - **Reduce, don't eliminate.** Slow durations to fast tier.
   - **Ignore the preference.** Not recommended; surface the warning.

→ `reduced_motion_strategy`.

7d. **Dark mode strategy.**
   - **None.** No dark mode tokens. Sets `has_dark_mode = false`.
   - **Opt-in via class.** `.dark` selector overrides semantic aliases. Sets `has_dark_mode = true` and `dark_mode_selector = ".dark"`.
   - **Opt-in via media.** `@media (prefers-color-scheme: dark)`. Sets `has_dark_mode = true` and `dark_mode_selector = "@media (prefers-color-scheme: dark) :root"`.

If dark mode is on, ask for the dark semantic mappings (cluster 7e).

7e. **Dark mode token mapping** (only if `has_dark_mode == true`). For each semantic alias, propose an inverted mapping and confirm:

   - `--color-bg-default` → `--neutral-900`
   - `--color-bg-elevated` → `--neutral-800`
   - `--color-bg-subtle` → `--neutral-800`
   - `--color-bg-inverse` → `--neutral-0`
   - `--color-text-primary` → `--neutral-50`
   - `--color-text-secondary` → `--neutral-200`
   - `--color-text-tertiary` → `--neutral-400`
   - `--color-text-inverse` → `--neutral-900`
   - `--color-border-default` → `--neutral-700`
   - `--color-border-strong` → `--neutral-500`
   - `--color-border-subtle` → `--neutral-800`

→ `dark_color_bg_default`, etc. (parallel to the light values from cluster 2e).

## Cluster 8: Integration and confirmation

8a. **Existing design-system rule.** The generator checks for `.claude/rules/design-system.md` in the working directory. Three states drive behavior:

- **No file exists** — generator writes the rule from scratch. No question.
- **File exists with PARAMETERIZE markers still present** — file was scaffolded by context-engineering but never filled. Generator confirms: "I see a design-system rule with unfilled markers. Safe to overwrite with the generated content? Y/N."
- **File exists with no PARAMETERIZE markers** — file was filled or hand-written. Generator shows the current content side-by-side with the proposed content and asks "Overwrite, merge into the existing file, or skip the rule update?" Three options. Default: skip if user is unsure.

**Existing token / component / doc files (the non-destructive write guard).** The generator also checks `<token_file_path>`, the seed component files, `docs/DESIGN_SYSTEM.md`, and `<globals_css_path>` before writing. For each that already exists: show a diff against the proposed content and ask **overwrite or skip** (default skip). These are whole-file artifacts — do **not** offer merge for them; merge is defined only for the rule file and `tailwind.config.tokens.ts`. This is the qventus-class guard: a hand-authored `tokens.css` is never overwritten without explicit consent. See `generator/decisions.md` "Non-destructive write guard."

8b. **Final preview.** Before writing, the generator outputs:

- The state map summary (cluster-by-cluster, captured answers).
- The file list to be written, grouped by destination.
- The styling-path branch decision (vanilla CSS Modules or Tailwind path).
- Any flagged routed-elsewhere material from cluster 0 (voice, copy, product strategy).

8c. **Confirm before writing.** Wait for explicit user confirmation. Phrases that count: "yes", "go", "proceed", "looks good." Anything that asks a clarifying question or proposes a change resets to the relevant cluster.

## Dry-run mode

If the user invokes the skill with a "dry run" flag (e.g., "use the design-system-bootstrap skill in dry-run mode"), run all clusters, run the cluster 8 preview, and stop without writing files. Output the preview as the final message.

## Notes

- Every PARAMETERIZE marker across templates must trace to a question or to a derivation in `decisions.md`. The marker map below is the audit trail.
- Branching questions write the answer into the generator-state map. `decisions.md` reads from that map to drive template inclusion and substitution.

## Marker map

Every PARAMETERIZE marker, its source question (or "derived"), and its cluster.

### Cluster 0

State-map keys only (no PARAMETERIZE markers):

- `source_assets_present`, `source_assets_summary`, `source_other_material`

### Cluster 1

- `project_name` — Q1a
- `token_file_path` — Q1b
- `component_dir_path` — Q1c
- `styling_path` — Q1d (state map only; gates template selection in decisions.md)

### Cluster 2

- `brand_primary_token_prefix`, `brand_primary_name` — Q2a-ii, Q2a-iii
- `brand_primary_50`–`brand_primary_900` — Q2a-iv (provided or derived)
- `has_secondary_brand_color` — Q2b-i (state map)
- `brand_secondary_token_prefix`, `brand_secondary_name`, `brand_secondary_50`–`brand_secondary_900` — Q2b (per-color, only if `has_secondary_brand_color`)
- `neutral_50`–`neutral_900` — Q2c-i
- `feedback_success`, `feedback_success_light`, `feedback_warning`, `feedback_warning_light`, `feedback_error`, `feedback_error_light`, `feedback_info`, `feedback_info_light` — Q2d-i
- `color_bg_default`, `color_bg_elevated`, `color_bg_subtle`, `color_bg_inverse` — Q2e-i
- `color_text_primary`, `color_text_secondary`, `color_text_tertiary`, `color_text_inverse`, `color_text_link` — Q2e-ii
- `color_border_default`, `color_border_strong`, `color_border_subtle` — Q2e-iii

### Cluster 3

- `font_family_display` — Q3a
- `font_family_body` — Q3b
- `has_mono_font`, `font_family_mono` — Q3c
- `type_size_2xs`–`type_size_2xl` — Q3d (and per-size usage comments derived from the picked scale)
- `has_display_sizes`, `type_size_3xl`, `type_size_4xl` — Q3e
- `line_height_tight`, `line_height_normal`, `line_height_relaxed` — Q3f
- `type_size_2xs_usage`–`type_size_2xl_usage` — derived per-scale defaults; user can edit
- `type_scale_comment_summary` — derived
- `type_scale_table` — derived

### Cluster 4

- `spacing_base_unit` — Q4a
- `space_1` through `space_16` — derived from `spacing_base_unit`, with user override

### Cluster 5

- `radius_sm`, `radius_md`, `radius_lg`, `radius_xl` — Q5a
- `shadow_xs`–`shadow_xl` — Q5b
- `has_inset_shadow`, `shadow_inset` — Q5c
- `motion_duration_fast`, `motion_duration_normal`, `motion_duration_slow` — Q5d
- `motion_easing_default`, `motion_easing_enter`, `motion_easing_exit`, `motion_easing_spring` — Q5e

### Cluster 6

- `component_density`, `border_emphasis` — Q6a, Q6b (state map; affect derived component values)

### Cluster 7

- `wcag_target`, `focus_ring_style`, `reduced_motion_strategy` — Q7a, Q7b, Q7c (state map)
- `has_dark_mode`, `dark_mode_selector`, `dark_mode_strategy` — Q7d
- `dark_color_bg_default`, etc. — Q7e (only if `has_dark_mode`)

### Cluster 8

- No new markers. Q8a sets `rule_overwrite_strategy` (state map): `write_fresh`, `overwrite_safe`, `merge`, `skip`.

### Derived markers (computed in decisions.md)

- `font_import_urls` — computed from `font_family_*` if any are Google Fonts; else empty
- `globals_css_path` — defaults to sibling of `token_file_path` (e.g., `app/styles/globals.css`)
- `linter_present`, `token_linter_command`, `check_command` — derived if context-engineering output is detected and a linter is wired
- `has_brand_doc` — true if `docs/BRAND.md` exists in the working directory
- `has_design_heuristics_rule` — true if `.claude/rules/design-heuristics.md` exists
- `tailwind_path` — derived: `styling_path == "tailwind_shadcn"`
