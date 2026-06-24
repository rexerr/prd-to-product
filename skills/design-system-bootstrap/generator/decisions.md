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

## Adopt-mode branch (when `mode == adopt`)

When cluster 0 set `mode = adopt`, the bootstrap interview and template substitution **do not run** — everything below this section (styling-path branch, per-template inclusion table, derived values) is bootstrap-mode logic and is skipped. Adopt **copies** a finished Claude Design bundle into the product and wires one rule. Authorized by [D-044](../../../docs/DECISIONS.md), which narrows [D-008](../../../docs/DECISIONS.md).

Three writes, all in the **product repo**, each governed by the non-destructive write guard (below):

1. **Copy the rendered design → `design/reference/`.** `cp` the bundle's pages + component source verbatim (a directory copy, not a transform). This is the *presence* fix — composition drifted ~100% in `the-council` because the finished design was absent at compose time.
2. **Copy the bundle's token values → the product's own CSS, verbatim.** Keep the bundle's structure. **Do NOT route bundle tokens through `tokens.css.template`.** *Why (do not "optimize" this away):* the scale-first template is **structurally non-isomorphic** to a real bundle — it fabricates a numeric shade scale, holds only 3 type slots, and has no tier for categorical accents or a theme scalar; forcing a bundle into it is the exact fidelity trap [D-008](../../../docs/DECISIONS.md) documented and [D-044](../../../docs/DECISIONS.md) preserves the ban on. A literal copy is value-lossless; the template is not. A future maintainer who reaches for `tokens.css.template` here is re-introducing the bug.
3. **Emit the import rule → `.claude/rules/design-adoption.md`** from `templates/design-adoption.md.template` (substitute `reference_dir`, default `design/reference/`; the default emission matches the source-of-record fence in `../../../docs/design-handoff-adoption.md`). This is the only substituted artifact adopt produces.

**Write-guard interplay.** Steps 1–2 are Bash `cp` operations: on a first run they create fresh files (auto-tracked as run-owned, ungated, like the arm/disarm Bash). On a **re-run / re-snapshot**, `design/reference/` and the copied tokens already exist — the guard gates the overwrite (interactive `ask`, headless skip), so a second adopt never silently clobbers a hand-edited reference. Step 3's rule emission is a `Write|Edit`: gated the same way if `.claude/rules/design-adoption.md` already exists. (These three guard interactions are flagged for a `/verify` live-fire — they are reasoned from D-005/D-006, not yet fired.)

After the three writes, hand off to `output-summary.md` (adopt variant).

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

The "Triggered when" column below says *whether* a template is emitted; this guard says *whether an existing file is overwritten* — the two are orthogonal. `tokens.css`, the seed components, and `DESIGN_SYSTEM.md` are always in scope but are still overwrite-or-skip when the file already exists (this is the qventus-class failure: a hand-authored `tokens.css` must never be silently clobbered). The rule file's `rule_overwrite_strategy` (below) is the richest instance of this one guard — it alone adds the marker fast-path and a merge branch.

**Enforced (D-005).** This guard is now backed by the global `write-guard.sh` PreToolUse hook ([`hooks/README.md`](../../../hooks/README.md)) when it is installed and this run is armed: a write to a file that **existed before this run** is gated — interactive runs get a non-forgeable permission dialog (`ask`), headless runs are auto-skipped (`deny`, so an unattended run never clobbers and never hangs). Files this run *creates* are auto-tracked as run-owned and stay freely editable. Still honor the prose above: the hook may be absent (not installed on this machine / not yet distributed) or bypassed (`--dangerously-skip-permissions`), and it does nothing unless this run armed it.

**Arm at run start (before writing any file), disarm at run end** — via Bash, so it bypasses the guard's own `Write|Edit` matcher:

```bash
# run start
mkdir -p ~/.claude/state/write-guard
: > ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel
# run end
rm -f ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel \
      ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".owned
```

Where the hook isn't installed this is a harmless no-op (a sentinel nobody reads). A forgotten arm = no enforcement for that run (the prose is the backstop); a forgotten disarm is harmless.

## Per-template inclusion table

| Template | Triggered when | Output path |
|---|---|---|
| `tokens.css.template` | always (overwrite-or-skip per write guard) | `<token_file_path>` |
| `globals.css.template` | always (write fresh if absent; if it exists, the agent merges the missing pieces — see below) | sibling of `<token_file_path>`, named `globals.css` |
| `Button.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Button.tsx` |
| `Button.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Button.module.css` |
| `Button.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Button.tsx` |
| `Card.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Card.tsx` |
| `Card.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Card.module.css` |
| `Card.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Card.tsx` |
| `Input.tsx.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Input.tsx` |
| `Input.module.css.template` | `styling_path == "vanilla_css_modules"` | `<component_dir_path>/Input.module.css` |
| `Input.tailwind.tsx.template` | `styling_path == "tailwind_shadcn"` | `<component_dir_path>/Input.tsx` |
| `tailwind.config.tokens.ts.template` | `styling_path == "tailwind_shadcn"` | `tailwind.config.tokens.ts` (agent merges into `theme.extend` additively + diff confirm, not full overwrite) |
| `DESIGN_SYSTEM.md.template` | always (overwrite-or-skip per write guard) | `docs/DESIGN_SYSTEM.md` |
| Design-system rule | per `rule_overwrite_strategy` (see below) | `.claude/rules/design-system.md` |

> All component-file rows above (`Button`/`Card`/`Input`, both styling paths) are governed by the write guard: overwrite-or-skip if the target already exists. The `styling_path` condition selects *which* component template emits; the guard still gates overwriting an existing file. No merge for components.

### globals.css merge (when the file already exists)

If `globals.css` is absent, write it fresh. **If it already exists, the agent merges in the missing pieces itself — it never emits a merge note for the user to apply.** Three additive pieces, each written only if not already present, **all inserted at the top of the file, above existing rules** (CSS silently drops any `@import` that follows another rule, so position is not optional — prepend, never insert mid-file):

1. `@import "./tokens.css";`
2. The font `@import url(...)` lines — only when `has_font_imports` (the `font_import_urls` block).
3. `@tailwind base; @tailwind components; @tailwind utilities;` — Tailwind path only.

**Interactive:** show the diff and ask for confirm before writing (the Edit rides the write-guard hook — `ask` on this pre-run file, D-006). **Headless:** skip — the hook `deny`s edits to pre-run files unattended (D-006 ceiling); report as skipped. Same merge mechanics apply to `tailwind.config.tokens.ts`: add only to `theme.extend.*`, never replace existing `extend` keys, surface any key collision in the diff.

## Rule integration: three-state logic

When `rule_overwrite_strategy` resolves, behavior:

- `write_fresh` — `.claude/rules/design-system.md` does not exist. Generator writes a new fully-parameterized rule. Source: this skill carries a small inline rule template in `decisions.md` "Inline rule template" below (no separate file in `templates/` because the existing context-engineering template covers it).
- `overwrite_safe` — file exists with PARAMETERIZE markers. User confirmed overwrite. Generator overwrites with the fully-parameterized rule.
- `merge` — file exists, no markers (filled or hand-written). User chose merge. **The agent performs the merge itself; it never hands the user a snippet to apply.** Insert the generated rule as a single HTML-comment-fenced block — `<!-- design-system-bootstrap:start -->` … `<!-- design-system-bootstrap:end -->`. **Position is deterministic:** if no prior fence exists, append the block at end-of-file; if a fence already exists, replace only the content *within* it, never touching lines outside the fence. This is *positionally additive*, not a semantic reconcile — if the user already has inline design-system rules the fenced block lands alongside them, and the diff surfaces the overlap for the user to resolve. **Interactive:** show the diff and ask for confirm before writing (the Edit also rides the global write-guard hook, which `ask`s on this pre-run file — D-006). **Headless:** skip — the hook `deny`s edits to pre-run files unattended (D-006 ceiling); report as skipped, never silently apply.
- `skip` — user chose to leave the rule alone. No file written. Output summary flags this as "rule update skipped — your design-system.md may reference the wrong token paths."

### PARAMETERIZE marker detection

The check: read the file content, grep for the literal string `<!-- PARAMETERIZE:`. If found, the file is in scaffolded-but-not-filled state — `overwrite_safe`. If not found, the file is filled or hand-written — `merge` or `skip` (user decides).

### Inline rule template (used by `write_fresh` and `overwrite_safe`)

The skill writes a parameterized version of context-engineering's `design-system.md.template` with the specific values filled in. The pattern: load the context-engineering template from `~/.claude/skills/context-engineering/templates/claude-rules-modular/design-system.md.template` (or its symlinked location), substitute every PARAMETERIZE marker with values from the state map below, and write to `.claude/rules/design-system.md`.

Marker → state-map mapping for context-engineering's design-system.md.template:

- `token_file_path` — Q1b
- `token_linter_command` — empty (no linter scaffolded by V1 of this skill); OPTIONAL `linter_line` block omits
- `typography_rules` — derived: `<font_family_body> for body, <font_family_display> for display`
- `motion_tokens` — derived: `--motion-easing-hover for hover/color transitions, --motion-duration-fast + --motion-easing-default for other micro-interactions, longer durations for panels and modals. Keyboard-initiated and high-frequency (100+/day) actions use --motion-duration-instant. Spring is an accent for drag/playful moments only.`
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
- `reduced_motion_disable`, `reduced_motion_reduce` — gate the two mutually exclusive `@media (prefers-reduced-motion: reduce)` blocks in `globals.css.template`. Derived from Q7c `reduced_motion_strategy`: `disable` → first key true; `reduce_dont_eliminate` → second key true; `ignore` → both false, no block emits, and the output summary repeats the intake warning ("reduced-motion preference ignored — accessibility risk"). Exactly one key may be true; never both.
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

**Bootstrap mode:**

- `<token_file_path>` (default `app/styles/tokens.css`)
- `<globals_css_path>` (default `app/styles/globals.css`) — written fresh if absent, else agent-merged additively (top-of-file `@import`/`@tailwind` pieces) with diff confirm
- `<component_dir_path>/Button.tsx`, `Card.tsx`, `Input.tsx` (and the paired `.module.css` files on vanilla path)
- `tailwind.config.tokens.ts` (Tailwind path only, agent-merged additively into `theme.extend` with diff confirm)
- `docs/DESIGN_SYSTEM.md`
- `.claude/rules/design-system.md` (per `rule_overwrite_strategy`)

**Adopt mode** ([D-044](../../../docs/DECISIONS.md)) — these are **copies of the design of record**, not authored product code:

- `design/reference/**` — the bundle's rendered pages + component source, copied verbatim
- the product's token CSS — bundle `:root` values copied verbatim (path is the product's own; not a new template output)
- `.claude/rules/design-adoption.md` — the emitted import rule

**Never** write files anywhere else — **except the adopt-mode paths above, which are the one sanctioned exception and only by copy** (adopt copies a bundle's existing design into `design/reference/`; it still never *authors* feature components, utilities, or page layout). If source material implies content elsewhere (a brand book describing voice, a Figma export with feature components to build), surface in the output summary.

## Scaffolding-leak scan before finalizing

Before writing the files, run a **mechanical category grep** over the about-to-be-written content (`DESIGN_SYSTEM.md`, the emitted rule block, and any CSS/TS comments) for internal interview/generator machinery that must never reach a user's repo. Deterministic — run the grep and read its output, do not eyeball. It is the independent backstop to the "Internal scaffolding stays internal" prose rule in `principles.md`, and mirrors the same scan in `prd-creator` ([generator/decisions.md](../../prd-creator/generator/decisions.md)).

**Use category patterns, never a literal word-list:**

- `grep -niE '[Cc]luster [0-9]'` → expect **zero** (interview-stage machinery).
- `grep -niE 'Q[0-9][a-z]'` → expect **zero** (state-map question labels). This was a real leak: a `(Q7c)` label shipped in a `globals.css` comment until 2026-06-24 (template fixed).
- `grep -niE 'state.?map'` → expect **zero**.
- `grep -niE '<!-- *(PARAMETERIZE|OPTIONAL)|PARAMETERIZE:'` → expect **zero** unsubstituted template markers. Match the **comment-marker form**, never the bare word — "optional" is ordinary English ("optional layout slots" in `DESIGN_SYSTEM.md` is legitimate) and must not flag.

Any hit → fix before writing; do not ship the file with the leak in it.

**Failure it prevents:** internal machinery (`cluster N`, `Q7c`-style labels, `state map`, unsubstituted markers) reaching a user's design files — the [D-010](../../../docs/DECISIONS.md) leak class, mechanically backstopped. (DSB emits no decisions-log file, so unlike `context-engineering` there is no `D-0[0-9]` sanctioned-content case here.)

## After writing

After all files are written, hand off to `output-summary.md` for the post-generation report.
