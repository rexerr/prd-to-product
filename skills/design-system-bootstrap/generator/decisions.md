# Generator decisions

The mapping logic from intake answers to template choices, file outputs, and substitutions. Read this after `intake.md` has produced a complete answer set, before writing files.

## State map (from intake)

Held as a flat map keyed by the names in `intake.md` "Marker map". The keys most load-bearing for template selection:

| Key | Source question | Type | Notes |
|---|---|---|---|
| `project_name` | Q1a | string | |
| `token_file_path` | Q1b | string path | Default `app/styles/tokens.css`. |
| `component_dir_path` | Q1c | string path | Default `app/components/ui/`. |
| `styling_path` | Q1d | enum | `vanilla_css_modules` or `tailwind_shadcn`. **Gates component template selection.** |
| `has_secondary_brand_color` | Q2b-i | bool | |
| `has_mono_font` | Q3c | bool | |
| `has_display_sizes` | Q3e | bool | |
| `has_inset_shadow` | Q5c | bool | |
| `has_dark_mode` | Q7d | bool | |
| `dark_mode_selector` | Q7d | string | `.dark` or `@media (prefers-color-scheme: dark) :root`. |
| `rule_overwrite_strategy` | Q8a | enum | `write_fresh`, `overwrite_safe`, `merge`, `skip`. |

## The styling-path branch

`styling_path` is the most consequential decision. Three things change with it.

1. **Component templates.** Vanilla path emits `.tsx` plus `.module.css` per component. Tailwind path emits a single `.tsx` per component using `cva()`.
2. **Tailwind config snippet.** Emits only on the Tailwind path.
3. **Globals.css.** Emits on both paths but the Tailwind path's `globals.css` adds `@tailwind base; @tailwind components; @tailwind utilities;` directives if not already present.

The `tokens.css` file is identical on both paths — it carries the source of truth either way.

## Non-destructive write guard

Before writing any file, check whether the target path already exists on disk. This governs every file in the table below.

- **Does not exist** → write normally.
- **Exists and is a recognizable unfilled scaffold** (contains `<!-- PARAMETERIZE:` markers) → safe to overwrite after a one-line confirm; don't make the user diff a never-customized file.
- **Exists and differs** → **do not overwrite.** Show a diff against the existing file, state it already exists, and ask: **overwrite / skip** — and **merge only where this skill defines a merge operation** (the `.claude/rules/design-system.md` snippet and `tailwind.config.tokens.ts`; **never offered for `tokens.css`, the seed components, or `DESIGN_SYSTEM.md`**, which are whole-file artifacts with no merge semantics). **Default to skip.** Never overwrite hand-authored work without explicit consent.

Report skipped/overwritten files in the post-generation summary with the standard markers `(skipped — already exists; not overwritten)` and `(overwritten with consent)`. Because generation is non-deterministic, a re-run sees most prior files as "differs" and prompts (default skip) on each — expected; the guard prioritizes never-clobber over silent re-runs.

The "Triggered when" column below says *whether* a template is emitted; this guard says *whether an existing file is overwritten* — the two are orthogonal. `tokens.css`, the seed components, and `DESIGN_SYSTEM.md` are always in scope but are still overwrite-or-skip when the file already exists (this is the qventus-class failure: a hand-authored `tokens.css` must never be silently clobbered). The rule file's `rule_overwrite_strategy` (below) is the richest instance of this one guard — it alone adds the marker fast-path and a merge branch. **This is a prose guard the agent must honor; it is not yet hook-enforced.**

## Per-template inclusion table

| Template | Triggered when | Output path |
|---|---|---|
| `tokens.css.template` | always (overwrite-or-skip per write guard) | `<token_file_path>` |
| `globals.css.template` | always (write only if file does not exist; otherwise emit a merge note) | sibling of `<token_file_path>`, named `globals.css` |
| `Button.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Button.tsx` |
| `Button.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Button.module.css` |
| `Button.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Button.tsx` |
| `Card.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Card.tsx` |
| `Card.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Card.module.css` |
| `Card.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Card.tsx` |
| `Input.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Input.tsx` |
| `Input.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Input.module.css` |
| `Input.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Input.tsx` |
| `tailwind.config.tokens.ts.template` | `styling_path == "tailwind_shadcn"` | `tailwind.config.tokens.ts` (snippet for merge, not full overwrite) |
| `DESIGN_SYSTEM.md.template` | always (overwrite-or-skip per write guard) | `docs/DESIGN_SYSTEM.md` |
| Design-system rule | per `rule_overwrite_strategy` (see below) | `.claude/rules/design-system.md` |

> All component-file rows above (`Button`/`Card`/`Input`, both styling paths) are governed by the write guard: overwrite-or-skip if the target already exists. The `styling_path` condition selects *which* component template emits; the guard still gates overwriting an existing file. No merge for components.

## Rule integration: three-state logic

When `rule_overwrite_strategy` resolves, behavior:

- `write_fresh` — `.claude/rules/design-system.md` does not exist. Generator writes a new fully-parameterized rule. Source: this skill carries a small inline rule template in `decisions.md` "Inline rule template" below (no separate file in `templates/` because the existing context-engineering template covers it).
- `overwrite_safe` — file exists with PARAMETERIZE markers. User confirmed overwrite. Generator overwrites with the fully-parameterized rule.
- `merge` — file exists, no markers. User chose merge. Generator emits a `design-system.md.merge-snippet` to standard out and asks the user to apply it manually. Does NOT overwrite the file.
- `skip` — user chose to leave the rule alone. No file written. Output summary flags this as "rule update skipped — your design-system.md may reference the wrong token paths."

### PARAMETERIZE marker detection

The check: read the file content, grep for the literal string `<!-- PARAMETERIZE:`. If found, the file is in scaffolded-but-not-filled state — `overwrite_safe`. If not found, the file is filled or hand-written — `merge` or `skip` (user decides).

### Inline rule template (used by `write_fresh` and `overwrite_safe`)

The skill writes a parameterized version of context-engineering's `design-system.md.template` with the specific values filled in. The pattern: load the context-engineering template from `~/.claude/skills/context-engineering/templates/claude-rules-modular/design-system.md.template` (or its symlinked location), substitute every PARAMETERIZE marker with values from the state map below, and write to `.claude/rules/design-system.md`.

Marker → state-map mapping for context-engineering's design-system.md.template:

- `token_file_path` — Q1b
- `token_linter_command` — empty (no linter scaffolded by V1 of this skill); OPTIONAL `linter_line` block omits
- `typography_rules` — derived: `<font_family_body> for body, <font_family_display> for display`
- `motion_tokens` — derived: `--motion-duration-fast / --motion-easing-default for micro-interactions, longer durations for panels`
- `icon_set` — empty (not scaffolded by this skill); the line is omitted
- `layout_rules` — derived: `Use --space-* tokens for all spacing. Maximum content width 1200px (override per-route).`
- `indicator_vocabulary_table`, `forbidden_indicator_terms` — empty (not scaffolded by this skill); these PARAMETERIZE markers are replaced with a TODO line: "Define indicator vocabulary when chip/badge/alert components ship."
- `button_tier_list` — derived from the Button component variants: "primary, secondary, ghost, destructive."
- `form_rules` — derived: "Inputs use the Input seed component. Required fields show a label asterisk. Errors use --color-error and announce via role='alert'."
- `design_things_to_avoid_list` — derived: "Hardcoded hex values. Tailwind utilities outside this project's config (Tailwind path only)." Vanilla path drops the second item.
- `voice_cross_ref` — true if `docs/BRAND.md` exists, else OPTIONAL block drops
- `no_tailwind_ban` — `styling_path == "vanilla_css_modules"` (the OPTIONAL block stays). On Tailwind path, the line is dropped.

## Substitution rules

### General

For every `<!-- PARAMETERIZE: <key> -->` marker, substitute the corresponding value from the state map. Trim leading/trailing whitespace. Preserve indentation.

### OPTIONAL block handling

`<!-- OPTIONAL: <key> -->` markers gate the line or block immediately following.

Behavior:

- If the condition is true: keep the marker line itself removed from output, keep the gated block as-is.
- If the condition is false: drop the marker line **and** the gated block (the next line, or the next contiguous block ending at a blank line, depending on context).

OPTIONAL keys used in this skill's templates:

- `has_secondary_brand_color` — gates the secondary scale block in `tokens.css.template` and the secondary entries in `tailwind.config.tokens.ts.template`
- `has_mono_font` — gates the `--type-family-mono` line in `tokens.css.template`, the `mono` family in `tailwind.config.tokens.ts.template`, and the mono row in `DESIGN_SYSTEM.md.template`
- `has_display_sizes` — gates the `--type-size-3xl` and `--type-size-4xl` lines
- `has_inset_shadow` — gates the `--shadow-inset` line
- `has_dark_mode` — gates the entire dark-mode block at the bottom of `tokens.css.template`
- `has_font_imports` — gates `font_import_urls` in `globals.css.template`
- `tailwind_path` — gates the "A note on the Tailwind path" section in `DESIGN_SYSTEM.md.template`. Derived: `styling_path == "tailwind_shadcn"`.
- `has_design_heuristics_rule`, `has_brand_doc`, `linter_present` — gate cross-reference lines in `DESIGN_SYSTEM.md.template`. Derived from working-directory inspection.

### KEEP AS-IS

`<!-- KEEP AS-IS: <reason> -->` markers do not require substitution and should not be removed. They are documentation for the user that the line they precede is intentionally fixed.

## Derived value computations

Some markers require a small derivation, not a direct lookup.

### `font_import_urls`

If any of `font_family_display`, `font_family_body`, `font_family_mono` look like a Google Fonts family (single name without quotes that matches Google's catalog — e.g., "Inter", "Geist", "Chivo Mono"), emit the appropriate `@import url(...)` line at the top of `globals.css`. If all three are system fonts (`system-ui`, `-apple-system`, etc.), set `has_font_imports = false` and the OPTIONAL block drops.

The detection check is simple substring: if the family value contains a recognizable Google Fonts name without quotes, emit the import. Edge cases (custom hosted fonts, locally-imported fonts via `next/font`) get a TODO comment in `globals.css` instead of an import.

### `space_*` derivation

The base unit determines the spacing scale: `space_n = n × spacing_base_unit`px for n in (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16). Default values:

| n | 4px base | 8px base |
|---|---|---|
| 1 | 4px | 8px |
| 2 | 8px | 16px |
| 3 | 12px | 24px |
| 4 | 16px | 32px |
| 5 | 20px | 40px |
| 6 | 24px | 48px |
| 7 | 28px | 56px |
| 8 | 32px | 64px |
| 10 | 40px | 80px |
| 12 | 48px | 96px |
| 16 | 64px | 128px |

User can override individual stops in cluster 4.

### `type_scale_table` (for DESIGN_SYSTEM.md.template)

Build a markdown table from the picked type scale plus per-size usage comments:

```
| Token | Value | Common uses |
|---|---|---|
| `--type-size-2xs` | <type_size_2xs> | <type_size_2xs_usage> |
| ...
```

Per-size usage strings come from the picked scale shape's defaults (compact / comfortable / generous), or from user overrides if the user customized.

## What the generator never writes

This skill writes only files at these paths:

- `<token_file_path>` (default `app/styles/tokens.css`)
- `<globals_css_path>` (default `app/styles/globals.css`) — and only if the file does not exist
- `<component_dir_path>/Button.tsx`, `Card.tsx`, `Input.tsx` (and the paired `.module.css` files on vanilla path)
- `tailwind.config.tokens.ts` (Tailwind path only, as a snippet for manual merge)
- `docs/DESIGN_SYSTEM.md`
- `.claude/rules/design-system.md` (per `rule_overwrite_strategy`)

**Never** write files anywhere else. If source material implies content elsewhere (a brand book describing voice, a Figma export with feature components), surface in the output summary.

## After writing

After all files are written, hand off to `output-summary.md` for the post-generation report.
