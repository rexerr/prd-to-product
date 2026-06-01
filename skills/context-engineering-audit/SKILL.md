---
name: context-engineering-audit
description: Audit an existing project's AI-context structure (CLAUDE.md, AGENTS.md, .claude/, docs/) against the context-engineering skill's standard. Produces a drift report. Use when the user says "audit this project's context", "compare this project to context-engineering", "drift report against the standard", or "use the context-engineering-audit skill". Do not use to scaffold context from scratch (use context-engineering instead), to fix drift (the audit is read-only — fixes happen in a follow-up session), or to review code for bugs.
---

# Context-engineering audit skill

Audits an existing project's AI-context structure against the standard scaffolded by the `context-engineering` skill. Produces a drift report; does not write fixes. Designed for projects that were hand-built or pre-date the skill — the audit catalogs where the project diverges, names what's load-bearing vs cosmetic, and surfaces open questions. Decisions on what to act on are deferred to follow-up sessions.

Modeled on two real audits run option-2 style (read principles directly, no skill invocation) on `the-council` and `field-society-demo`. The audits produced consistent structure across two independent projects; this skill encodes that structure so it's triggerable and repeatable.

## When to trigger

Activate on any of these phrasings:

- "audit this project's AI-context structure"
- "audit context against the context-engineering standard"
- "compare this project to context-engineering"
- "drift report against context-engineering"
- "use the context-engineering-audit skill"

Do not activate on:

- "scaffold context for a new project" — that is the `context-engineering` skill, not this one.
- "fix the drift in this project's context" — the audit is read-only. Run the audit first, then a follow-up session acts on findings.
- "review this code" / "audit my code" — too broad. This skill audits context files only, not product code.

## Procedure

When triggered, follow `procedure.md` step by step. The procedure carries the reading order, output structure (six canonical sections), explicit watch-item checks, and the source-of-truth precedence rule.

Do not read `procedure.md` up-front on every invocation discussion — read it when running the audit, not when explaining what the skill does.

## Files in this skill

- `SKILL.md` — this file. Trigger description and procedure pointer.
- `procedure.md` — operational audit procedure: reading order, watch checks, contracts. Read at audit time.
- `templates/output-skeleton.md` — the report skeleton to copy and fill. Loaded when about to write the report, not at invocation.
- `NOTES.md` — internal notes including the heavy-validator option as future work. Not read at invocation.

## Output location

Save the drift report to the audited project's `docs/context-audit-YYYY-MM-DD.md`, using today's ISO date. Branch on what the project already has:

- No `docs/` directory → save to the project root with the same filename and flag that the audited project may need a `docs/` set first.
- An existing `context-audit-*.md` from an earlier date → write a new one with today's date. Do not overwrite. The comparison-to-prior-audit section of the new audit replaces the function of overwriting.
- An audit already dated today → suffix `-rerun-N` to the filename per `procedure.md`. Do not overwrite.

## Read-only contract

This skill writes the drift report and nothing else. It does not edit `.claude/rules/`, `AGENTS.md`, `CLAUDE.md`, hooks, or any other project file. Fixes are a follow-up session's job, sized and decided after the audit lands.

If during the audit the user asks to "just fix it while you're in there," decline and capture the fix as an open question in the report's section 5. The read-only boundary is what keeps audit-and-act phases separable.

## What this skill does not do

- Does not audit code quality, test coverage, or product correctness. Context-files-only.
- Does not run programmatic checks (file-existence asserts, frontmatter parsers, drift diffs against templates). The light tier is human-read-driven. The heavy-validator option is logged in `NOTES.md` as future work, gated on third-instance evidence.
- Does not promote findings to skill changes. That promotion happens in `prd-to-product`'s continuous-mode retros, not in the audited project.
- Does not write fixes. Read-only contract.

## Gotchas

- **"Just fix it while you're in there" breaks the read-only contract.** The audit writes one file, the drift report, and edits nothing else — if the user asks for an in-line fix, decline and capture it as an open question in section 5, because that separation is what keeps the audit-and-act phases independent.
- **Running without the standard on disk grades against nothing.** If `prd-to-product`'s `context-engineering` skill is not available to read (files 1–4 in `procedure.md`), halt and ask rather than auditing against an assumed standard — a report measured against a standard you cannot see is worse than no report.
- **Do not reshape the six canonical sections.** The output structure converged across two independent real audits, so the sub-buckets and table columns are the load-bearing part — reshaping them loses the portability that made the structure worth templating.
