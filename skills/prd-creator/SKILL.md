---
name: prd-creator
description: Run an interview-driven question flow that turns a rough idea, working brief, or research dump into a structured PRD.md. Use when the user says "draft a PRD", "build a PRD", "run the PRD interview", "use the prd-creator skill", or hands you a project idea and asks for a product requirements document. Do not use for editing an existing PRD section, writing implementation specs, or scaffolding context files (that is the context-engineering skill).
---

# PRD-creator skill

Turns a rough idea or working brief into a structured `PRD.md` via an interview the user answers cluster by cluster. The output PRD is shaped to feed the context-engineering skill's cluster 0 with no edits beyond domain content.

## When to trigger

Activate on any of these phrasings:

- "draft a PRD"
- "build a PRD"
- "write a PRD for this"
- "run the PRD interview"
- "use the prd-creator skill"
- "turn this brief into a PRD"

Do not activate on:

- "edit the PRD" or "fix the open questions section" — too narrow. Use direct file edits.
- "scaffold context for this project" — that is the context-engineering skill. PRD-creator runs first; context-engineering consumes its output.
- "design the system" or "write the architecture doc" — separate scope. The PRD captures decisions already made, not new architecture.

## Procedure

When triggered:

1. Run the generator flow at `generator/intake.md`. Ask the questions cluster by cluster, in order. Do not dump every question at once.
2. Cluster 0 always asks for source material first, even if material appears to be in conversation context already. Do not silently absorb context.
3. After every cluster, summarize what was captured in two or three sentences before moving on. The user can correct before the next cluster.
4. After all clusters are complete, run the logic at `generator/decisions.md` to determine which optional sections (brand and voice appendix, sibling `BRAND.md` file, etc.) emit.
5. State the proposed PRD outline and confirm before writing. The summary should name every section and its source cluster. Wait for explicit confirmation.
6. Write `PRD.md` at the user-named path (default `docs/PRD.md`). Use the template at `templates/PRD.md.template` and fill the parameterized fields from the captured answers.
7. If the brand-and-voice cluster produced sibling-file material, also write `templates/BRAND.md.template` to the user-named path (default `docs/BRAND.md`).
8. Output the post-generation summary at `generator/output-summary.md`. Name every section that emitted, every section that was skipped and why, and the next step (typically "run the context-engineering skill against this PRD").

Read `principles.md` only when the user asks why a pattern exists, or when you hit an edge case the templates do not cover. Do not load it on every invocation.

## Files in this skill

- `principles.md` — rationale, cluster contract, hand-off contract with context-engineering. Reference, not boot.
- `templates/PRD.md.template` — annotated PRD skeleton. Sentence-case headers, H1/H2/H3 only.
- `templates/BRAND.md.template` — optional sibling file. Emits when the brand-and-voice cluster produces enough material.
- `generator/` — `intake.md` (clustered question flow), `decisions.md` (which optional sections emit), `output-summary.md` (post-generation report).
- `examples/` — three transcripts (small, medium, large) plus the full output PRD for the small case.
- `NOTES.md` — internal notes, regression test definition, parked ideas.

## Annotation conventions in templates

- `<!-- PARAMETERIZE: <field> -->` — fill from the captured answer to the named cluster question.
- `<!-- KEEP AS-IS: <reason> -->` — do not change without good reason.
- `<!-- OPTIONAL: <condition> -->` — include or omit based on the captured answers.

## What this skill does not do

- Does not invent decisions the user has not made. The interview elicits, structures, and writes back. It does not propose product strategy.
- Does not run research or synthesize interview transcripts the user has not provided. It ingests material the user supplies.
- Does not generate code, design tokens, or implementation specs.
- Does not scaffold the rules or docs structure around the PRD. That is the context-engineering skill.
- Does not review or critique an existing PRD.
