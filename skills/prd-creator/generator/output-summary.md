# Output summary

The post-generation report. Print this to the user after the PRD (and optional `BRAND.md`) is written. Mirror the shape below; fill the bracketed pieces.

## Format

```
PRD generated at <PRD_PATH>.

Write-guard outcome: <"all targets were new" | existing files marked (skipped — already exists; not overwritten) or (overwritten with consent)>.

Sections that emitted:
- <section name>
- <section name>
...

Sections that were skipped:
- <section name>. Reason: <one-line reason>.
...

Decisions captured: <count>. Highest-impact:
- D-001 <one-line statement>
- D-002 <one-line statement>
...

Open questions: <count>. Top blockers for V1:
- <question>
- <question>
...

Brand and voice placement: <inline appendix | sibling file at BRAND_PATH | not run>.

Files written:
- <PRD_PATH>
- <BRAND_PATH if emitted>

Next step:
Run the context-engineering skill against this PRD to scaffold AGENTS.md, CLAUDE.md, .claude/rules/, and docs/. The PRD's decisions and architecture sections feed that skill directly; you will not be asked to restate them.
```

## Rules for filling each section

- **Sections that emitted.** List in PRD order, not capture order. The user reads top-down so this matches. Name the sections only, never which cluster filled them (per "What never goes in the summary" below, internal scaffolding stays internal).
- **Sections that were skipped.** Include only optional sections that were not emitted. Do not list always-on sections. Reasons should be terse and traceable, and named by section not cluster number: "brand and voice not run, no user-facing copy" or "no V2 items captured, deferred capabilities omitted."
- **Decisions captured.** Show all if five or fewer. Show top three plus a "+N more" line if six or more. Top is by criticality, same heuristic as in `decisions.md`.
- **Open questions.** Show all if three or fewer. Show top three plus a "+N more" line if four or more. Top means V1-blocking.
- **Brand and voice placement.** Use the literal phrase from the table: "inline appendix," "sibling file at <path>," or "not run."
- **Next step.** Always points to the context-engineering skill. Do not invent other next steps. If the user is not planning to run context-engineering next, they will say so.

## When to write a longer summary

Default to terse. Three cases warrant more detail. The first is mandatory whenever it applies; the other two are case-by-case.

1. **Routed-elsewhere material was mentioned during intake.** Mandatory flag. Per `decisions.md` "Routed-elsewhere content," any visual-aesthetic, design-token, rule-file, or rich tech-spec content the user mentioned during cluster 0 or any cluster gets named in the summary so the user knows it was not silently dropped. Phrase as: "<Type of content> you mentioned (<one-line paraphrase>) was not captured in the PRD or BRAND.md. It belongs in <target skill>." Do not skip this even when the rest of the summary is terse. Silent dropping is a regression.
2. **The user overrode the brand placement rule.** Note the override and the user's stated reason. Useful when re-reading the PRD later and wondering why a one-item BRAND.md exists.
3. **The user delegated content authoring to the skill mid-cluster.** When the user says "come up with some and I'll approve" (or equivalent) in clusters 6 or 7, the skill correctly proposes options for the user to accept, edit, or reject. The summary should note this with one line: "Success criteria were proposed by the skill at your request and pruned to <N> items based on your edits." This is not invention because the user delegated and reviewed; the note exists so the provenance is traceable.

## What never goes in the summary

- Internal scaffolding details. The user does not need to know which cluster captured which decision; they need to know what shipped and what is next.
- Self-praise. "The PRD is comprehensive" or "good interview" is noise. Cut.
- Restated PRD content. The PRD is the artifact. The summary is metadata.
