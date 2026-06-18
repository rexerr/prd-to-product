---
name: prd-creator
description: Turn a rough idea, working brief, or research dump into a structured PRD.md. Use when the user says "draft a PRD", "build a PRD", "run the PRD interview", "use the prd-creator skill", or hands you a project idea and asks for a product requirements document. Do not use for editing an existing PRD section, writing implementation specs, or scaffolding context files (that is the context-engineering skill).
---

# PRD-creator skill

Turns a rough idea or working brief into a structured `PRD.md` via an interview the user answers cluster by cluster. The output PRD is shaped to feed the context-engineering skill's cluster 0 with no edits beyond domain content.

## Binding contracts (read before acting)

- **Never silently absorb context** — draft-and-present from any brief; ask cold only where it's thin.
- **No internal scaffolding in user-facing copy** — "Cluster 0" / `D-NNN` are machinery, not the user's words.
- **Never speculate about source-material age** — describe what the material contains, not provenance you can't cite.

Full failure modes in Gotchas (bottom).

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

**Self-skip check first.** If the request is a *trivial single-feature* PRD — one capability, no real product decisions to elicit, nothing that needs a multi-cluster interview — say so and offer a lighter path (a short direct PRD, or jumping to only the sections that carry content) rather than running the full clustered interview. Proceed with the full flow only if the scope warrants it or the user asks. *Failure it prevents:* forcing a heavyweight interview onto work too small to need one.

1. Run the generator flow at `generator/intake.md`. Ask the questions cluster by cluster, in order. Do not dump every question at once.
2. Cluster 0 always asks for source material first, even if material appears to be in conversation context already. Do not silently absorb context. When material is present, draft each covered cluster's answer from it and present the draft for the user to confirm or edit, rather than asking cold or absorbing silently (see `generator/intake.md` cluster 0).
3. After every cluster, summarize what was captured in two or three sentences before moving on. The user can correct before the next cluster.
4. After all clusters are complete, run the logic at `generator/decisions.md` to determine which optional sections (brand and voice appendix, sibling `BRAND.md` file, etc.) emit.
5. State the proposed PRD outline and confirm before writing. The outline names every section in natural language, not cluster numbers. Wait for explicit confirmation.
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

## Gotchas

- **Asking cold for what the brief already answers reads as not having read it.** The anti-silent-absorption rule (cluster 0) correctly bans absorbing a brief without confirmation, but the fix is draft-and-present, not re-interrogating the user from scratch. A thorough brief that gets asked cold makes the user push back ("doesn't my brief tell you this?") and is the overcorrection a Squirreled validation run surfaced. Draft from the brief, present for edit; ask cold only where the brief is thin.
- **Internal scaffolding leaks into the conversation.** "Cluster 0," draft "D-001 candidate" narration, and "(from cluster 3)" provenance tags are the skill's machinery, not the user's vocabulary. Naming them mid-interview reads as form-processing instead of understanding. Keep user-facing copy in natural language; confirmed `D-NNN` IDs surface only at the cluster 5 read-back and in the written PRD, where they are part of the deliverable.
- **Speculating about source-material age invents provenance.** Claiming a brief was "written days ago" or that "your framing may have sharpened since" when nothing states a date is an ungrounded factual claim that undermines trust in everything else the skill asserts. Describe what the material contains, not how old it is, unless the material itself carries a date you can cite.
