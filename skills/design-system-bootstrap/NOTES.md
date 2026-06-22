# Design-system-bootstrap skill — internal notes

Notes for whoever maintains this skill. Not part of the user-facing flow.

## Regression test definition

The skill must produce usable output for three project shapes. "Usable" means the token file, seed components, and DESIGN_SYSTEM.md require no structural edits before the user starts building — only cosmetic value tweaks if needed.

The `DESIGN_SYSTEM.md` shape these three cases assert is defined once in [`DESIGN_SYSTEM-FORMAT.md`](DESIGN_SYSTEM-FORMAT.md) (the shape source of truth); on any conflict, that file wins. The per-shape "Expected output" notes below name what each shape adds to the core skeleton — the medium dark-mode conventions and large full-listing + accessibility-notes additions are recorded there as shape-gated sections.

### Small shape

**Input:** direct text only. No brand book, no assets.
- Primary: `#2563eb`
- Text: Inter (body), system-ui fallback
- Spacing base unit: 8px
- Radius: rounded (8px default)
- Dark mode: no
- Design heuristics: no

**Expected output:** `tokens.css` (two-tier, six domains), `globals.css`, three seed components each with a paired `.module.css`, `DESIGN_SYSTEM.md`. No dark mode section. No icon set rule.

### Medium shape

**Input:** palette image (or pasted hex values from a brand guideline doc) plus a few direct fills.
- Two brand colors with full scales provided
- Typography: Geist + Geist Mono (Google Fonts)
- Spacing base unit: 4px
- Radius: tight (4px default)
- Dark mode: opt-in (separate dark-mode section in tokens.css)
- Accessible focus ring: yes (AAA)

**Expected output:** same file set as small, plus dark mode token block. DESIGN_SYSTEM.md documents dark mode token conventions.

### Large shape

**Input:** brand book PDF or Figma export with full palette, typography specimen, spacing spec.
- Full palette (three brand colors, each with scales)
- Two typefaces
- Component personality specified (compact density, hairline borders, subtle interaction)
- Dark mode: auto-pair from semantic aliases
- Accessibility: WCAG AA floor, custom focus ring color, reduced-motion behavior

**Expected output:** full token file including motion tokens and dark mode block. Three seed components show all variant states including disabled and error. DESIGN_SYSTEM.md includes a complete token listing, full component catalog, and accessibility notes section.

### Adopt shape (D-044)

**Input:** a Claude Design handoff bundle present in the working directory (a `claude-design*`/`design-*` dir whose README self-declares a bundle). No interview.

**Expected output:** three artifacts in the product repo — `design/reference/**` (bundle pages + component source, copied verbatim), the product's token CSS (bundle `:root` values copied verbatim, NOT routed through `tokens.css.template`), and `.claude/rules/design-adoption.md` (the emitted import rule). The emitted rule's default paths + three failure-mode bullets match the `# Design adoption — import, don't rebuild` fence in `docs/design-handoff-adoption.md` byte-for-byte. Regression fixture: `examples/transcript-adopt.md` (interview branch + emitted rule only — the `cp` steps have no substitution to dry-run). **RED conditions:** tokens routed through the template; no `design/reference/` copy step; emitted rule drifts from the fence default.

## Styling approach decision (2026-05-09)

Context-engineering scaffolds projects with "No Tailwind. No shadcn." (see `context-engineering/templates/claude-rules-modular/design-system.md.template`). The real ePost projects (feed, assessment) use CSS custom properties via inline `style` props and global CSS classes — no Tailwind, no CSS Modules. CSS Modules is the better pattern for the seed components in App Router because it co-locates styles and prevents global class name collisions. The seed components prove the token system works; CSS Modules is the right demonstration vehicle for that proof.

If a future project uses Tailwind + shadcn, the generator should detect this in cluster 1 (project context) and branch to a Tailwind-flavored output path. V1 assumes No Tailwind.

## Token namespace collision detection

A common generator error: the user provides two brand colors with similar names and the semantic aliases resolve to identical primitives. Example: `--brand-primary: #2563eb` and `--color-brand-primary: #2563eb` both in the file. The second is the semantic alias, the first is the primitive — but the domain prefix (`--color-*` vs `--brand-*`) is the only distinguisher. The generator must not emit raw hex values in the semantic layer, only `var(--<primitive>)` references.

## Component template expansion

The three seed components (Button, Card, Input) are the minimum. The generator should not expand this set even if the user requests it during the interview. Capture additional component requests in the output summary as "build these as features once the token system is in place." Do not add them to the template set without a V2 decision.

## Rule integration: PARAMETERIZE marker detection

The three-state rule integration logic requires detecting whether a file has PARAMETERIZE markers remaining. The detection check: look for the string `<!-- PARAMETERIZE:` anywhere in the file. If found, the file is safe to overwrite (never filled). If not found, the file has been filled or was written by hand — show diff, ask before overwriting.

## Parked ideas

### Tailwind + cva output path (Phase 2)

If the user's project uses Tailwind, the component templates need to change: instead of CSS Modules, emit `className` strings composed with `cva()` and expose tokens via `tailwind.config.ts` `extend.colors`. The generator question is in cluster 1: "does this project use Tailwind?" If yes, branch to the Tailwind path. Template set would be identical minus the `.module.css` files plus a `tailwind.config.ts` update snippet.

### Dark mode auto-pair generation

Cluster 7 asks for dark mode strategy (auto-pair, opt-in, no). "Auto-pair" means the generator derives dark-mode semantic aliases automatically by inverting the color scale (bg-default → neutral-900, text-primary → neutral-100). The logic is simple for a two-color palette. It breaks for brand accent colors with no obvious dark-mode complement. V1 does not attempt auto-pair inference; it prompts the user for explicit dark values. Auto-pair inference is a Phase 2 capability.

### Storybook scaffolding

Considered during Pass 1. Out of scope. If the user wants Storybook, they add it after the seed components are stable. Don't scaffold stories as part of the design-system-bootstrap output.

### Token migration

Out of scope for V1. "Migrating an existing token system" is explicitly listed as out of scope in the brief. If a user has partial tokens and wants this skill to augment them, surface the conflict and ask the user to either clear the existing file or proceed knowing this skill overwrites it.

### Adopt-mode v2: mechanical intra-app-consistency hook + staleness check (deferred)

Adopt v1 ([D-044](../../docs/DECISIONS.md)) ships presence + cp-tokens + the import rule, enforcing intra-app consistency and `design/reference/` staleness as **rule prose**. Deferred to v2, by deliberate decision (Rex, 2026-06-19):

- **A mechanical intra-app-consistency hook** — a session-start check / emitted hook that greps for inline re-implementations of components that already exist in the imported `design/reference/` set, the way the write-guard hook live-fires on blocked operations. This is the half of composition that *can* be made mechanical even in a markdown workspace; fidelity-to-source genuinely needs a human and stays a present, cheap gate.
- **A scaffolded staleness check** on `design/reference/` (flag a surface diffed against a reference older than the latest export).

Why deferred, not dropped: the council sequenced "the human fidelity gate ships first," and a hook carries its own authoring + heavy live-fire verification contract (copy emitted scripts to `/tmp`, fire each blocked op in a fresh session) that would roughly double v1's verification surface and blow the per-session scope ceiling. The v1 import rule already carries both checks as prose (`templates/design-adoption.md.template`, the `hook_deferred` OPTIONAL block) — drop that block when the hook ships.

### FUTURE.md entry

If context-engineering's `FUTURE.md` exists in the project, the output summary should offer to add a note about potential design-system evolutions (component library expansion, Storybook, theming). Do not write to FUTURE.md without asking.

## Style notes for any update to this skill

- Sentence-case headers, H1/H2/H3 only.
- No em dashes.
- No Oxford commas.
- Imperatives, not principles, in rule content.
- AP style, Strunk and White.
- No colons in titles.
- CSS custom property names in code blocks, never inline prose.

## Templates quick reference

```
templates/
├── tokens.css.template         Two-tier token file: primitives + semantic aliases + all domains
├── globals.css.template        Base resets + @import for tokens.css
├── Button.tsx.template         Variant-prop button (primary/secondary/ghost/destructive, sm/md/lg)
├── Button.module.css.template  CSS custom properties only, all variant states
├── Card.tsx.template           Container with optional shadow and clickable variants
├── Card.module.css.template    CSS custom properties only
├── Input.tsx.template          Labeled input with error state and forwardRef
└── Input.module.css.template   CSS custom properties only, focus, error, disabled states
DESIGN_SYSTEM.md.template       Token semantics, component catalog, rule cross-reference
```
