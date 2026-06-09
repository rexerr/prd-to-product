---
name: context-engineering
description: Scaffold the context structure (AGENTS.md, CLAUDE.md, .claude/rules/, docs/) for a new AI-assisted coding project. Use when the user says "scaffold context for a new project", "set up rules and docs for this codebase", "build the context structure for a new project", or "use the context-engineering skill". Do not use for framework setup (Next.js, etc.), single-file edits to an existing CLAUDE.md, or generic project setup.
---

# Context engineering skill

Scaffolds the rules and docs that orient an AI agent in a new coding project. Modeled on conventions developed across two production projects. Stack and deploy target are intake parameters: the generator supports Next.js, React + Vite, Node CLI, Python, or other; deploy targets include Vercel, Netlify, Cloudflare, Fly, Railway, manual, or none. Single developer, single human visual confirmer.

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

- Does not manage multi-developer workflows, branch policies, or PR review templates. Future scope.
- Does not handle build-system-specific rules (Turbo, Nx, monorepo layouts). Future scope.
- Does not write product content (PRD body, domain vocabulary, voice rules). It scaffolds the shape; the user fills the content.

## Gotchas

- **The generator writes shape, not content.** When source material includes a brand book or design spec, the agent drifts into improvising a `tokens.css` file or filling PRD body prose — that is product content the generator never writes (see `generator/decisions.md` "What the generator never writes"), and it belongs to `design-system-bootstrap` or to the user.
- **Re-running must not overwrite existing files.** The emitters are not idempotent, so a second run would clobber hand-edited files. The **non-destructive write guard** (`generator/decisions.md`) governs this: any target that already exists is diffed and requires explicit overwrite/skip consent (default skip) — the way the field-society-demo run caught a `PRD.md` collision. This is a *prose* guard, **not yet hook-enforced** (cf. the `enforce_rules_as_hooks` gotcha below), so the agent must honor it deliberately, not rely on a mechanism to stop it.
- **Flipping `enforce_rules_as_hooks` to false removes the only thing that enforces the rules.** Prose rules do not enforce themselves — two audited projects documented their failure modes in prose and still shipped zero hooks, so treat the hook default as load-bearing and require a named replacement before disabling it.
