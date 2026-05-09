# Working brief: design-system-bootstrap skill

Working brief for Claude Code. The third skill in the sequence after context-engineering and prd-creator.

## Goal

A Claude skill that takes brand book material or design assets and produces a small, opinionated design system: a token CSS file, a handful of seed components, and a `DESIGN_SYSTEM.md` doc that captures token semantics. The output integrates with the design-system rule that context-engineering already scaffolds.

## What this skill is for

Two real failure modes from prior projects motivate this skill.

First, every project either ships without a token system (hardcoded colors, magic spacing values, inconsistent type) or grows one accidentally over months of feature work. Neither produces a design system anyone can rely on.

Second, when an agent is handed a brand book mid-build, it improvises. The agent generates a `tokens.css` from a PDF excerpt, picks values that don't match the brand, and produces seed components nobody asked for. Context-engineering explicitly prohibits this. The capability is useful; it just needs its own skill.

This skill closes both gaps. It runs once on a project (typically right after context-engineering), takes deliberate input, and writes a token file and seed components grounded in the user's brand.

## Inputs

The skill should accept any of:

- A brand book PDF (palette, typography, spacing, illustration style).
- A Figma file or Figma export image.
- A loose folder of brand assets (palette image, type specimen, logo lockups).
- A screenshot of an existing site or product the user wants to mirror.
- A combination of the above.
- Direct text input ("primary is #2C5F2D, type is Inter for body, Söhne for display").

The skill does not require structured input. It runs interview-style questions to fill in what is missing or to verify what the user provided.

## Outputs

A small set of files under a project-named root directory. Default paths:

- `app/styles/tokens.css` — CSS custom properties for color, type, spacing, radius, shadow, motion. Organized by domain.
- `app/styles/globals.css` — base resets and the import for tokens.css. Only created if not already present.
- `app/components/ui/Button.tsx` — seed component using only tokens.
- `app/components/ui/Card.tsx` — seed component using only tokens.
- `app/components/ui/Input.tsx` — seed component using only tokens.
- `docs/DESIGN_SYSTEM.md` — token semantics, component usage, the rules that govern the system.

The seed components are deliberate. Three is the minimum that proves "tokens work end to end." Adding more before the user has a real product to design against is bloat.

If context-engineering has already scaffolded a design-system rule under `.claude/rules/`, this skill updates it to reflect the actual generated paths. If no rule exists, this skill creates one.

## What this skill is NOT

- Not a context-engineering skill. The output of this skill assumes context-engineering already ran (or will run shortly).
- Not a prd-creator skill. PRD content does not belong here. Voice and tone live in `BRAND.md`, which this skill never touches.
- Not a UI library. Three components is the seed set. The user builds the rest as features land.
- Not a design tool. The skill does not generate Figma files, art, or illustrations. It writes CSS and component code from values the user provides or confirms.
- Not a brand designer. The skill does not invent palettes or typographic hierarchies. The user supplies the brand; the skill structures it.

## Architecture (mirror context-engineering and prd-creator)

Same five-piece shape that worked twice already.

- `SKILL.md` — trigger phrases, procedure, file map. Under 500 words.
- `principles.md` — rationale and conventions. Deferred-loaded per the SKILL.md procedure.
- `generator/` — `intake.md` (clustered question flow), `decisions.md` (output structure rules and conditional emission), `output-summary.md` (post-generation report).
- `templates/` — `tokens.css.template`, `globals.css.template`, `Button.tsx.template`, `Card.tsx.template`, `Input.tsx.template`, `DESIGN_SYSTEM.md.template`.
- `examples/` — three runs (small, medium, large) plus full output for the small case.
- `NOTES.md` — internal notes, regression test definitions, parked ideas.

Read `context-engineering/SKILL.md`, `prd-creator/SKILL.md`, and both `principles.md` files to absorb the pattern. Do not copy content; copy shape.

## Question flow design

The interview captures what the templates need. Cluster shape proposal (refine in build).

- **Cluster 0: source material.** "Do you have a brand book, Figma file, palette image, or notes? Paste, link, or upload. Tell me there's none."
- **Cluster 1: project context.** Project name, framework (default Next.js), file path conventions. Confirm or correct from context-engineering output if present.
- **Cluster 2: color system.** Primary, secondary, neutrals. Semantic colors (success, warning, error, info). Background and foreground tokens. Accessibility floor (default WCAG AA contrast).
- **Cluster 3: typography.** Font families (display, body, mono). Type scale (six to nine sizes). Line height defaults. Weight set.
- **Cluster 4: spacing and layout.** Base unit (4px or 8px). Spacing scale. Container max widths. Grid columns if relevant.
- **Cluster 5: radius, shadow, motion.** Radius scale. Elevation set (zero to four shadows is typical). Motion durations and easings.
- **Cluster 6: component personality.** Density (compact, regular, spacious). Border emphasis (none, hairline, prominent). Interactive feedback (subtle, expressive). One question per attribute.
- **Cluster 7: accessibility floor.** WCAG level (AA default), focus ring style, reduced-motion behavior, dark-mode strategy (auto-pair tokens, opt-in, no).
- **Cluster 8: integration and confirmation.** Confirm the token namespacing convention, file paths, and rule-file path. Show a preview of what will be generated.

Refine cluster boundaries during build. The shape that worked for prd-creator was 8 clusters down from 11; this skill might land at 6 or 7. Decide with a real run.

## Question contract (carry from prior skills)

- One cluster at a time. Do not dump every question at once.
- 2 to 4 options for branching questions; up to 3 questions per call.
- Free-text fills ask one at a time.
- Cluster 0 always asks for source material first, even if material is already in conversation context.
- After every cluster, summarize what was captured before moving on.
- Confirm the proposed file list and namespace before writing.

## Routed-elsewhere content

Per the lesson from prd-creator Pass 2.1, flag and decline material that belongs to another skill.

- **Voice, tone, vocabulary, copy.** Belongs to prd-creator's BRAND.md. If the user pastes brand voice content, capture it as "use the prd-creator skill for this," do not absorb into design-system output.
- **Product strategy, decisions, scope.** Belongs to prd-creator's PRD. Same handling.
- **Always-on coding rules, retros, deploy gates.** Belongs to context-engineering. Same handling.
- **Specific feature components (a checkout flow, a settings page).** Out of scope. The skill writes seed components only.

The output summary names any routed-elsewhere material that was mentioned during intake.

## What to read before building

In priority order:

1. This brief.
2. `handoff.md` (the skill-build handoff at the same path).
3. `context-engineering/SKILL.md` and `prd-creator/SKILL.md` (architectural pattern references).
4. `context-engineering/principles.md` and `prd-creator/principles.md` (pattern references).

Optional shape exemplars (read for shape, not as a Phase 0 audit):

- `~/Sites/the-council/app/styles/` and `~/Sites/the-council/app/components/ui/` if present, as the shape of a real token file and seed components in a Rex project.
- `~/Sites/epost-assessment/docs/UI_SYSTEM.md` as a shape reference for the `DESIGN_SYSTEM.md` output.
- `~/Sites/epost-intelligence-feed/docs/STATCARD_SPEC.md` and `CONTENT_SYSTEM.md` for how visual structure docs read in Rex's workflow.

Do not audit these as a Phase 0. Read them to inform building, not to produce a findings doc.

## Definition of done for the build

The skill is complete when:

1. Folder exists at `~/.claude/skills/design-system-bootstrap/` (or symlinked from a source repo) with all five required pieces.
2. Running the skill on a real project produces a token file, three seed components, and a design-system doc the user would actually use.
3. The token file is referenced correctly by the design-system rule (whether scaffolded by context-engineering or created by this skill).
4. The seed components import from tokens only. No hardcoded values in any generated component.
5. The validation run produces a design system the user adopts as-is or with cosmetic edits.

## Out of scope for the first build

- Generating illustrations, icons, or imagery.
- Multi-brand support (several brand systems in one project).
- Per-feature component libraries beyond the three seeds.
- Theme switching beyond the optional dark-mode pair.
- Visual regression testing or Storybook scaffolding.
- Migrating an existing token system to this one.

## Style requirements for the output

The output content (tokens.css, components, DESIGN_SYSTEM.md) follows these rules in addition to Rex's standard style.

- **CSS custom properties use kebab-case with a domain prefix.** `--color-bg-default`, `--space-4`, `--type-size-md`, `--radius-lg`. No bare `--primary` or `--lg`.
- **Tokens never reference hex values inline.** Use a tokens file as the only source of color, spacing, and type values. Components reference tokens; tokens reference primitives.
- **Components use the variant-prop pattern.** No prop bloat. A button has three to five variants, not eleven booleans.
- **Components are accessible by default.** Focus rings, ARIA where relevant, semantic HTML.
- **The design system doc is checkable.** Each token has a one-line description and a usage rule. Each component lists props, variants, and the accessibility notes.
- **Never use Tailwind utility classes inside seed components when a token exists.** The seed components prove that tokens work; if Tailwind covers the gap, the user will skip the tokens.

## Execution recommendation

Pass 1: SKILL.md + principles.md + templates/ (tokens, three components, DESIGN_SYSTEM.md, globals) + NOTES.md. Stop for review.
Pass 2: generator/ (intake, decisions, output-summary) + examples/.
Pass 1.5 if needed for any patches before Pass 2.

Same two-pass shape that worked for context-engineering and prd-creator. Pass 2.1 patches happen after the validation run, not preemptively.

## When to ask vs when to proceed

Default to proceeding. Only stop and ask when:

- The brand assets the user provided contradict each other (palette PDF says one primary, screenshot shows another). Surface the contradiction; do not pick silently.
- A token decision would force a downstream cascade you want to confirm (base unit 4 vs 8 affects every spacing token).
- The brief is wrong about something material.

Do not ask permission to begin. Read the brief, read the references, plan the work, execute.
