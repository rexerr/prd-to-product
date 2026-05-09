---
name: context-engineering
description: Scaffold the context structure (AGENTS.md, CLAUDE.md, .claude/rules/, docs/) for a new AI-assisted coding project. Use when the user says "scaffold context for a new project", "set up rules and docs for this codebase", "build the context structure for a new project", or "use the context-engineering skill". Do not use for framework setup (Next.js, etc.), single-file edits to an existing CLAUDE.md, or generic project setup.
---

# Context engineering skill

Scaffolds the rules and docs that orient an AI agent in a new coding project. Modeled on conventions developed across two production projects. V1 assumes Vercel + Next.js App Router, single developer, single human visual confirmer. Other stacks come later.

## When to trigger

Activate on any of these phrasings:

- "scaffold context for a new project"
- "set up rules and docs for this codebase"
- "build the context structure for a new project"
- "use the context-engineering skill"

Do not activate on:

- "scaffold a Next.js app" — that is framework setup, not context engineering.
- "create a CLAUDE.md" — too narrow. Point the user at `templates/CLAUDE.md.template` directly.
- "set up a project" — too broad. Ask the user what they mean.

## Procedure

When triggered:

1. Run the generator flow at `generator/intake.md`. Ask the questions in order. Do not ask everything at once.
2. After all answers are collected, run the decision logic at `generator/decisions.md` to determine which templates apply.
3. State a "here is what I'm about to generate" summary. Wait for the user to confirm before writing files.
4. Produce files using the templates in `templates/`. Keep annotation comments inline so the user can see what came from where.
5. Output the post-generation summary at `generator/output-summary.md`.

Read `principles.md` only when the user asks why a pattern exists, or when you hit an edge case the templates do not cover. Do not read it up-front on every invocation.

## Files in this skill

- `principles.md` — structural conventions and rationale. Reference, not boot.
- `templates/` — annotated example files. The generator fills these in.
- `generator/` — question flow, decision logic, output summary.
- `examples/` — three worked examples (small as full output tree, medium and large as abbreviated transcripts) showing the generator applied to hypothetical projects.
- `NOTES.md` — internal notes including the regression test definition.

## Annotation conventions in templates

- `<!-- PARAMETERIZE: <field> -->` — the generator fills this in from a user answer.
- `<!-- KEEP AS-IS: <reason> -->` — do not change without good reason.
- `<!-- OPTIONAL: <condition> -->` — include or omit based on user answers.

## What this skill does not do

- Does not run on frameworks other than Next.js App Router or deploy targets other than Vercel. Future scope.
- Does not manage multi-developer workflows, branch policies, or PR review templates. Future scope.
- Does not write product content (PRD body, domain vocabulary, voice rules). It scaffolds the shape; the user fills the content.
