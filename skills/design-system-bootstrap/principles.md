# Design-system-bootstrap principles

The conventions this skill follows and the rationale behind them. Read this when you want to understand why a template is shaped the way it is, or when you hit an edge case the templates do not cover. Do not read it on every skill invocation.

## What this skill is for

Two failure modes motivated it.

First, every project either ships without a token system — hardcoded colors, magic spacing values, inconsistent type — or grows one accidentally over months of feature work. Neither produces a design system anyone can rely on. By the time the system is needed, the codebase has dozens of inline hex values to hunt down.

Second, when an agent is handed a brand book mid-build, it improvises. It generates a `tokens.css` from a PDF excerpt, picks values that do not match the brand, and produces seed components nobody asked for. Context-engineering explicitly prohibits this behavior because it produces unreliable output. The capability is useful; it needs its own skill with deliberate input and explicit confirmation.

This skill closes both gaps. It runs once per project, typically right after context-engineering. It takes deliberate input through a clustered interview, and writes a token file and seed components grounded in the user's actual brand.

## The two-tier token architecture

Every token file this skill generates has two layers.

**Primitives layer.** Raw named values with no semantic meaning: brand colors with their full scales, neutral scales, any palette the user supplies. These live at the top of `tokens.css`. They are never referenced in components directly. They exist only so the semantic layer has something to point at.

```css
/* Primitives */
--brand-blue: #2563eb;
--brand-blue-50: #eff6ff;
--brand-blue-900: #1e3a5f;
--neutral-100: #f5f5f5;
--neutral-900: #171717;
```

**Semantic aliases layer.** Role-named tokens that map a purpose to a primitive. Components reference only semantic tokens. This is what enables dark mode, theming, and brand variants without touching component code.

```css
/* Semantic aliases */
--color-bg-default: var(--neutral-100);
--color-bg-elevated: #ffffff;
--color-text-primary: var(--neutral-900);
--color-brand-primary: var(--brand-blue);
--color-brand-primary-hover: var(--brand-blue-900);
```

The interview asks for primitives (cluster 2: brand colors as raw values) and then immediately asks for role mappings (which primitive is the primary background, the primary CTA, the primary text). Both layers land in `tokens.css` in order: primitives first, semantic aliases second, then type scale, spacing, radius, shadow, motion, z-index.

### Why two tiers

Retrofitting a semantic layer onto a primitive-only token file after components exist is painful. Every component has to be touched. Starting two-tier costs one extra question per color in the interview. The payoff is dark mode, rebranding, and brand-variant support for free, because the component code does not change — only the semantic aliases do.

Single-tier (semantic-only) is simpler to generate but collapses the two concerns. When the user asks for dark mode later and every component references `--brand-blue` directly, there is no clean way to invert it without touching all the components.

## Token naming convention

Every token uses kebab-case with a domain prefix. The prefix names the domain; the suffix names the role within that domain.

Domains and their prefixes:

- `--color-*` — color and semantic color aliases (background, text, border, brand, feedback)
- `--type-*` — typography (family, size, weight, line-height)
- `--space-*` — spacing scale
- `--radius-*` — border radius
- `--shadow-*` — elevation shadows
- `--motion-*` — durations and easing curves
- `--z-*` — z-index scale

Good: `--color-bg-default`, `--type-size-md`, `--space-4`, `--radius-lg`
Bad: `--primary`, `--lg`, `--blue`, `--md`

The bare forms are collision-prone and carry no domain information. When a component reads `--primary` it is ambiguous whether this is a color, a spacing value, or a brand rule. When it reads `--color-brand-primary` the domain is unambiguous.

Primitive names are the exception: they carry the palette name, not a domain prefix, because they are not meant for components to reference directly. `--brand-blue-500` is fine as a primitive. `--brand-blue-500` would be wrong as a semantic alias.

## Why three seed components

Three is the minimum that proves tokens work end to end across different interaction patterns.

`Button` proves interactive token use (hover states, active states, focus rings, variant switching, size scaling). `Card` proves container and elevation token use (background, border, shadow). `Input` proves form control token use (label, placeholder, focus, error state, disabled state).

More than three components before the user has a real product to design against is speculative. The seed set is not a UI library. It is a proof-of-concept that the token system is coherent and a reference point for components the user builds next. The user adds components as features land.

## Component architecture

Seed components follow three rules.

**Variant-prop pattern.** Each component accepts a `variant` prop with three to five options. No prop bloat, no boolean flags per visual variant. A button takes `variant="primary"` not `isPrimary={true} isOutline={false}`. The variant prop drives `className` composition via a lookup.

**CSS Modules for style co-location.** Each component has a paired `.module.css` file. The CSS file uses only CSS custom properties from `tokens.css` — no hardcoded values. The component imports the CSS module and maps variant and size props to class names. This keeps component styles co-located, prevents global class name collisions, and demonstrates the token system working through the full chain (token file → CSS module → component).

**Accessible by default.** Semantic HTML. Focus rings via `:focus-visible` using a token (`--color-focus-ring` maps to the brand primary by default). ARIA attributes where relevant. `forwardRef` on Input so it works with form libraries. No accessibility decision deferred to "add it later."

## Integration with context-engineering

If context-engineering ran before this skill, it may have scaffolded `.claude/rules/design-system.md` with unfilled PARAMETERIZE markers for `token_file_path`, `token_linter_command`, and related fields. This skill fills those gaps.

Three-state rule integration logic:

1. **No rule file exists.** Write `.claude/rules/design-system.md` from this skill's template, fully parameterized with the generated paths.
2. **Rule file exists with PARAMETERIZE markers still present** (context-engineering scaffolded but the user skipped the design system cluster). Safe to overwrite — the file was never customized. Do it.
3. **Rule file exists with no PARAMETERIZE markers** (filled and possibly customized). Show the current content alongside what this skill would write, state the diff, ask before overwriting. Do not silently replace a customized file.

Same detection logic used when the prd-creator and context-engineering hand-off collided on `docs/PRD.md` during the field-society-demo validation run. Detect, surface, ask. Do not decide silently.

**This non-destructive principle now governs every file the skill writes, not only the rule.** `tokens.css`, the seed components, and `DESIGN_SYSTEM.md` are overwrite-or-skip when they already exist (merge is defined for the rule file, the Tailwind config, and `globals.css` — where the agent performs the merge itself and shows the diff, never handing the user a snippet) — see `generator/decisions.md` "Non-destructive write guard." The three-state rule logic above is the richest instance of that one guard. It is a *prose* guard the agent must honor **and is now enforced by the global `write-guard.sh` hook** ([`hooks/README.md`](../../hooks/README.md), D-006) when installed and the run is armed.

## Routed-elsewhere content

During the interview, the user may provide material that belongs to another skill. Flag it and decline to absorb it.

- **Voice, tone, vocabulary, copy.** Belongs to prd-creator's BRAND.md. If the user pastes brand voice content, capture it as "this belongs in prd-creator — use that skill to generate your BRAND.md."
- **Product strategy, decisions, scope.** Belongs to prd-creator's PRD. Same handling.
- **Always-on coding rules, deploy gates, session discipline.** Belongs to context-engineering. Same handling.
- **Feature components beyond the seed set.** Out of scope. The skill writes Button, Card, and Input only. Flag any request for additional components and decline.

The output summary names any routed-elsewhere material that was mentioned during intake, so the user knows what to do with it.

## What the generator never writes

This skill's scope is design-system files only. Never product or application code beyond the seed components and token files.

Never write files at these paths:

- `app/**/*.{ts,tsx,js,jsx}` except the three seed components at their declared paths
- `lib/**/*` — library code
- `features/**/*` — feature modules
- `pages/**/*` — page components
- Any path outside `app/styles/`, `app/components/ui/`, `docs/DESIGN_SYSTEM.md`, and `.claude/rules/design-system.md`

If source material (a brand book, a Figma export) implies product-code-shaped content (component library beyond the seed set, utility functions, page layout), surface it in the output summary as "your [component/utility/etc.] is not in scope for this skill — build it as a feature once the token system is established."

## Progressive disclosure in the output

The output `DESIGN_SYSTEM.md` follows the same position-aware placement principle as the PRD and AGENTS.md. The load-bearing facts go at the top: which token file is canonical, what the no-hardcoded-values rule is, where the linter command lives. Details (full token listing, component props tables) go in the middle. "What is not in this file" goes at the bottom, pointing at context-engineering's rule for behavior constraints and prd-creator's BRAND.md for voice.

## Conventions for writing token values

- **No magic numbers.** Every value in `tokens.css` has a comment explaining its role. Short is fine: `/* primary CTA, AA contrast on white */`.
- **Scales are complete.** A color scale has at least five stops (50, 100–900 in 100-step increments is conventional). A partial scale signals a future extension that never happens.
- **Spacing follows a base unit.** 4px or 8px. Ask in cluster 4. Never mix base units.
- **Motion tokens come in pairs.** Every duration token has a companion easing token (`--motion-duration-fast: 120ms` plus `--motion-easing-default: cubic-bezier(0.4, 0, 0.2, 1)`). Components reference both.
- **Shadows use RGBA.** Never named colors in shadow values. `rgba(0, 0, 0, 0.08)` ages better than `rgba(var(--neutral-900-raw), 0.08)` — the latter requires CSS variable tricks that break in some contexts.

## Interview conduct: stay in natural language, stay grounded

Two conduct rules for the cluster interview, shared across all three skills in this family (mirrors `prd-creator` principles; the failures were observed there first — 2026-06-09, D-010).

- **Internal scaffolding stays internal.** Cluster numbers, the `0a`/`0b` sub-question labels, and state-map variable names are the generator's machinery. User-facing copy never names them — speak in natural language about the brand assets, not "cluster 0 source." **Failure it prevents:** naming the machinery reads as form-processing instead of understanding, and erodes trust in the interview.
- **No temporal or provenance claims about source material.** When you reference a brand book, palette, or other asset, describe what it contains, never speculate about when it was made or how dated it looks. Cite a date only if the asset states one. **Failure it prevents:** a confident but ungrounded claim about provenance is usually wrong and undermines trust in everything else the skill asserts.
