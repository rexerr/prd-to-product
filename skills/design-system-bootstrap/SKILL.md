---
name: design-system-bootstrap
description: Bootstrap a token-based design system from brand assets or direct input, or adopt a finished Claude Design handoff bundle. Use when the user says "bootstrap design system", "generate tokens from brand assets", "set up my token file", "use the design-system-bootstrap skill", or hands you a brand book and asks you to set up the design system; also use to adopt a Claude Design bundle — "adopt this Claude Design bundle", "wire up this design handoff", or pointing the skill at an exported bundle in the repo. Do not use for migrating an existing token system, generating Figma files or illustrations, building feature components, or voice and tone work (use prd-creator for that).
---

# Design-system-bootstrap skill

Turns brand assets or direct input into a working token CSS file, three seed React components, and a DESIGN_SYSTEM.md doc via a clustered interview. Integrates with the design-system rule that context-engineering scaffolds.

## Modes

- **bootstrap** (default) — generate a token system from brand assets or direct input via the clustered interview. The rest of this file is the bootstrap procedure unless a section says otherwise.
- **adopt** — a Claude Design handoff bundle is present; wire it into the product so later page-builds stay faithful to it. Copies the rendered design + tokens into the repo and emits an import rule. Does **not** interview for token values and does **not** route the bundle through the scale-first `tokens.css` template — it copies. See "Adopt mode" below. Authorized by [D-044](../../docs/DECISIONS.md), which narrows [D-008](../../docs/DECISIONS.md).
- **audit** — *planned, not built.* Do not improvise it.

Detection lives in cluster 0 (`generator/intake.md`): a self-declaring Claude Design bundle in the working directory proposes adopt; everything else is bootstrap. The fork is always proposed and confirmed, never silent.

## Binding contracts (read before acting)

- **Never clobber an existing design system** — decline an unrequested collision; diff and require consent on any existing file.
- **No raw hex in the semantic layer** — semantic aliases reference `var(--<primitive>)` only.
- **Design-system files only** — three seed components max; never product code. **Adopt-mode carve-out:** adopt *copies* a bundle's existing components into `design/reference/` and emits one import rule — it never *authors* product code. Copying the design of record is the presence fix D-044 turns on; authoring feature components stays banned.

Full failure modes in Gotchas (bottom).

## When to trigger

Activate on any of these phrasings:

- "bootstrap design system"
- "generate tokens from brand assets"
- "set up my token file"
- "create design system from brand book"
- "use the design-system-bootstrap skill"
- "adopt this Claude Design bundle" / "wire up this design handoff" (→ adopt mode)

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

## Adopt mode

When cluster 0 detects a Claude Design bundle and the user confirms adopt (not bootstrap), run this instead of the interview. All three steps run in the **product repo** and ride the non-destructive write guard. Full logic: `generator/decisions.md` "Adopt-mode branch."

1. **Copy the rendered design into `design/reference/`.** The bundle's pages + component source, copied verbatim — `cp`, not a transform. This is the *presence* fix: composition drifted ~100% in `the-council` because the design was absent at compose time.
2. **Copy the bundle's token values into the product's CSS — verbatim, keeping the bundle's structure.** Do **not** route them through `tokens.css.template`. The scale-first template is structurally non-isomorphic to a real bundle (6 fonts won't fit 3 slots; no tier for categorical accents or a theme scalar) — forcing the fit is the exact fidelity trap [D-008](../../docs/DECISIONS.md) documented. A literal copy is lossless; the template is not.
3. **Emit the import rule** to `.claude/rules/design-adoption.md` from `templates/design-adoption.md.template` (the default emission matches the source-of-record fence in [`design-handoff-adoption.md`](../../docs/design-handoff-adoption.md)).

The bundle stays the design source of record. In v1 the import rule enforces intra-app consistency and reference-staleness as **prose** — the mechanical hook is deferred to v2 (see `NOTES.md`).

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
- **Design-system files only, never product code.** When a brand book implies a component library, utilities, or page layout, the agent drifts into writing them — flag that material in the output summary and decline, and do not expand past the three seed components even on request. *Adopt mode is the one sanctioned exception, and only by copy:* it brings a bundle's existing components into `design/reference/` verbatim, never authoring them (see Modes / Adopt mode).
