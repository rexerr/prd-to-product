---
name: design-system-bootstrap
description: Bootstrap a token-based design system from brand assets or direct input. Use when the user says "bootstrap design system", "generate tokens from brand assets", "set up my token file", "use the design-system-bootstrap skill", or hands you a brand book and asks you to set up the design system. Do not use for migrating an existing token system, generating Figma files or illustrations, building feature components, or voice and tone work (use prd-creator for that).
---

# Design-system-bootstrap skill

Turns brand assets or direct input into a working token CSS file, three seed React components, and a DESIGN_SYSTEM.md doc via a clustered interview. Integrates with the design-system rule that context-engineering scaffolds.

## Binding contracts (read before acting)

- **Never clobber an existing design system** — decline an unrequested collision; diff and require consent on any existing file.
- **No raw hex in the semantic layer** — semantic aliases reference `var(--<primitive>)` only.
- **Design-system files only** — three seed components max; never product code.

Full failure modes in Gotchas (bottom).

## When to trigger

Activate on any of these phrasings:

- "bootstrap design system"
- "generate tokens from brand assets"
- "set up my token file"
- "create design system from brand book"
- "use the design-system-bootstrap skill"

Do not activate on:

- "migrate my existing tokens" — out of scope for V1. This is a request to *port* an existing system.
- a complete design system is already present even though you were asked to bootstrap one — decline rather than clobber it. Distinct from the migrate line above: that is a *request* to port; this is an *unrequested collision* with a system already on disk (the qventus case). See the write-guard gotcha below.
- "add a new component" — this skill writes seed components only; feature components belong to the build.
- "set up voice and tone" — that is prd-creator's BRAND.md.
- "scaffold context for a new project" — that is the context-engineering skill, which runs before this one.

## Procedure

When triggered:

1. Run the generator flow at `generator/intake.md`. Ask the questions cluster by cluster, in order. Do not dump every question at once.
2. Cluster 0 always asks for source material first, even if material appears to be in conversation context. Do not silently absorb a pasted palette or brand doc.
3. After every cluster, summarize what was captured in two or three sentences before moving on. The user can correct before the next cluster begins.
4. After all clusters complete, run the logic at `generator/decisions.md` to determine which optional sections emit (dark mode, icon set rule, Codex config update).
5. State the proposed file list and confirm the token namespace before writing. Wait for explicit user confirmation.
6. Write all files. Use the templates in `templates/`. Substitute every PARAMETERIZE marker from the captured answers.
7. Output the post-generation report at `generator/output-summary.md`.

Read `principles.md` only when the user asks why a pattern exists or when you hit an edge case the templates do not cover.

## Files in this skill

- `principles.md` — rationale and conventions. Reference, not boot.
- `templates/` — annotated token and component templates.
- `generator/` — `intake.md` (clustered question flow), `decisions.md` (output structure and conditional emission), `output-summary.md` (post-generation report).
- `examples/` — three runs (small, medium, large) plus full output for the small case.
- `NOTES.md` — internal notes, regression test definitions, parked ideas.

## Annotation conventions in templates

- `<!-- PARAMETERIZE: <field> -->` — fill from the captured answer to the named cluster question.
- `<!-- KEEP AS-IS: <reason> -->` — do not change without good reason.
- `<!-- OPTIONAL: <condition> -->` — include or omit based on captured answers.

## What this skill does not do

- Does not invent brand palettes or typographic hierarchies. The user supplies the brand; the skill structures it.
- Does not generate Figma files, illustrations, icons, or image assets.
- Does not write feature components, page layouts, or product UI.
- Does not migrate an existing token system.
- Does not generate voice, copy, or product strategy content. Flag any such material and point at prd-creator.
- Does not scaffold the rules and docs structure around the project. That is the context-engineering skill.

## Gotchas

- **Re-running must not clobber hand-edited files.** This skill writes a token file, three seed components with paired CSS modules, and `DESIGN_SYSTEM.md` — all governed by the **non-destructive write guard** (`generator/decisions.md`): before writing any file that already exists, show a diff and ask **overwrite / skip** (default skip; merge only for the rule file, Tailwind config, and `globals.css` — and the agent performs those merges itself, never handing you a snippet to apply). It is **enforced** by the global `write-guard.sh` hook ([`hooks/README.md`](../../hooks/README.md)) when installed and the run is armed (interactive → `ask` dialog, headless → `deny`; arm at run start per `generator/decisions.md`) — but still honor the prose, since the hook may be absent or bypassed. The qventus near-miss (a hand-authored `tokens.css`/design system) is exactly the case it protects.
- **Never emit raw hex in the semantic layer.** Semantic aliases must reference primitives as `var(--<primitive>)`, never a literal hex value — a hardcoded color in the semantic layer collapses the two-tier architecture and silently kills dark mode and theming.
- **Design-system files only, never product code.** When a brand book implies a component library, utilities, or page layout, the agent drifts into writing them — flag that material in the output summary and decline, and do not expand past the three seed components even on request.
