# Generator output summary

The post-generation report. Run after every file in the inclusion table has been written.

## Format

Output a single message to the user with four sections.

### 1. Files generated

A tree of every file written, grouped by location:

```
<repo_root>/
├── app/
│   ├── styles/
│   │   ├── tokens.css
│   │   └── globals.css
│   └── components/
│       └── ui/
│           ├── Button.tsx
│           ├── Button.module.css      (vanilla path only)
│           ├── Card.tsx
│           ├── Card.module.css        (vanilla path only)
│           ├── Input.tsx
│           └── Input.module.css       (vanilla path only)
├── tailwind.config.tokens.ts          (Tailwind path only — snippet to merge)
├── docs/
│   └── DESIGN_SYSTEM.md
└── .claude/
    └── rules/
        └── design-system.md           (per rule_overwrite_strategy)
```

Mark files skipped because they already existed (per the non-destructive write guard) with `(skipped — already exists; not overwritten)`, and files overwritten after explicit consent with `(overwritten with consent)`. Mark files emitted as merge snippets (`tailwind.config.tokens.ts`, optional rule merge case) with `(snippet — apply by hand)`.

### 2. The path you took

State the styling path branch decision and why it matters:

- **Vanilla CSS path.** Your seed components use CSS Modules. Each `.tsx` imports a paired `.module.css`. All values resolve through CSS custom properties in `tokens.css`.
- **Tailwind path.** Your seed components use `cva()` with Tailwind utilities. Color and border tokens are wired through `tailwind.config.tokens.ts` (merge snippet). Spacing and radius use Tailwind's default scale, not `tokens.css`.

If Tailwind path: include the explicit caveat from `DESIGN_SYSTEM.md`:
> Spacing and radius use Tailwind's default scale (`p-4`, `rounded-md`), not the `--space-*` and `--radius-*` tokens. To change spacing or radius, edit `tailwind.config.ts`, not `tokens.css`.

### 3. What you should review before starting work

A checklist of high-leverage things to verify. The user should be able to scan and confirm in under five minutes.

- **Token values.** Read `tokens.css` end to end. Confirm every brand color, semantic mapping, and scale stop is the value you want. Especially the semantic aliases — `--color-bg-default`, `--color-text-primary`, `--color-brand-primary` — these drive every component.
- **Focus ring contrast.** Verify `--color-focus-ring` meets 3:1 contrast against `--color-bg-default`. The default uses the brand primary 500 stop; override if the contrast fails.
- **Seed components render.** Spin up the dev server. Render each seed component on a page. Confirm the variants look right and the focus rings are visible.
- **Tailwind config merged** (Tailwind path only). The `tailwind.config.tokens.ts` is a snippet, not a full config. Open your existing `tailwind.config.ts` and merge the `theme.extend` block in. Restart the dev server after the merge.
- **Rule file** (if `rule_overwrite_strategy` was `merge` or `skip`). Open `.claude/rules/design-system.md` and confirm the `token_file_path` and other markers point at the actual generated paths.
- **DESIGN_SYSTEM.md cross-references.** Read the cross-reference block at the bottom. Confirm every linked file exists or will exist soon.

### 4. What's next

A suggested next-step sequence:

1. Run the dev server and view each seed component. Confirm they render correctly. If the brand colors look wrong, edit `tokens.css` (specifically the primitives, not the semantic aliases).
2. Build one real feature component using only the seed components and the tokens. The first real use is when the design system either confirms its shape or surfaces gaps.
3. Update `docs/DESIGN_SYSTEM.md` as the system grows. Add new components to the catalog. Document any new tokens you add.
4. If `.claude/rules/design-system.md` was merged or skipped, finish the integration before starting feature work. The agent will reference this rule on every UI task.

## Routed-elsewhere material

If during cluster 0 the user provided material that belongs to other skills, surface it here:

- **Voice and copy content.** "I noticed your brand book has a tone-of-voice section. This skill does not write voice content. Use `prd-creator` to generate `docs/BRAND.md`."
- **Product strategy or PRD content.** "Your brand book includes feature concepts and roadmap notes. Use `prd-creator` for PRD work."
- **Coding rules or session discipline.** "I noticed deploy and commit rules in your source material. Those belong in `.claude/rules/` via the `context-engineering` skill."
- **Feature components beyond the seed set.** "You mentioned a checkout flow / settings page / data table. This skill writes seed components only. Build feature components as features land, using the seeds and tokens as the base."

## Flags to surface

If any of these are true, add a "things to address before starting work" sub-section:

- Any `<!-- PARAMETERIZE: ... -->` marker remained unfilled in any output file. Surface the marker name and the file. This is a generator bug.
- Any `<!-- OPTIONAL: ... -->` marker was left visible (the marker line was not stripped). This is a generator bug.
- A token value contains an obvious placeholder like `#000000` or `TODO`. Surface the token name and ask the user to replace.
- The vanilla path emitted a `.module.css` that references a CSS variable not defined in `tokens.css`. Surface the variable name.
- The Tailwind path emitted a `tailwind.config.tokens.ts` that references a Tailwind utility name not present in any seed component (unused token wiring is fine; the inverse — utility used but not configured — is a bug).
- The dark mode block was emitted but the dark-token mappings are still primitives without semantic role names. Surface the line numbers.

## Tone

Direct. No celebration. The generator wrote files; the user has work to do. Match the project's house style: sentence-case headers, no em dashes, no Oxford commas.
