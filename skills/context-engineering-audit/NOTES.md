# Internal notes — context-engineering-audit

Notes for the skill author. Not read at invocation. Captures future-work options and design observations that don't belong in `SKILL.md` or `procedure.md`.

## Heavy-validator option as future work

The light tier of this skill (current state) is human-read-driven: a Claude session follows `procedure.md`, reads the project, and writes the report. No automation.

The heavy tier would be a programmatic validator: read the project's `.claude/` and `docs/`, parse frontmatter, diff against templates, report missing canonical sections and structural drift. Tool, not pure skill. Three implementation options if it ever lands:

1. **Bash + jq + yq.** Cheap, no dependencies, works anywhere. Limited to file-presence checks and frontmatter parsing. Hard to extend to richer drift (e.g., "the recency block has 7 items but should have 4").
2. **Python script.** Mid-weight. PyYAML for frontmatter, regex for section detection. Easier to extend than Bash but introduces a dependency the audited project may not have.
3. **MCP server wrapping context-engineering.** Heaviest. Exposes `audit_project(path)` as a tool. Reusable across sessions but the audit-write loop is already lightweight enough that an MCP layer may not pull its weight.

**Build trigger:** third real failure mode that the light tier missed. The first two audits found drift the light tier was perfectly capable of finding; the heavy tier earns its existence only when a class of drift exists that human reading consistently misses but a programmatic check would catch. Examples that would qualify:

- A `paths:` frontmatter glob that doesn't match any actual file path in the project (silent miss — the rule never loads). A grep-against-tree check catches it; a human reader might not.
- A `.claude/settings.json` with a malformed hook matcher (silent miss — the hook never fires). A schema check catches it.
- A cross-reference in one rule file to another rule file that doesn't exist (broken link). A link-checker catches it.

None of these have appeared in the two audits so far. Wait for the third instance, per the same continuous-mode discipline `prd-to-product`'s ROADMAP uses.

## Design observations from the two reference audits

A few patterns that emerged from `the-council` and `field-society-demo` audits worth preserving here, in case future iteration on the skill needs the evidence:

- **Both audits converged on the same six-section structure without coordination.** Different projects, different shapes (one modular+UI, one modular+UI but smaller AI scope), different stages — same output structure. The structure is portable enough to template; that's why `procedure.md` carries filled skeletons rather than prose descriptions.
- **The judgment column in §3 (intentional vs accidental) is where the audit earns its keep.** A pure presence/absence diff would miss the "the project did this on purpose because their failure history justifies it" cases. Human judgment is the load-bearing part; that's why this skill stays light-tier.
- **The "Comparison to prior audit" section emerged from running the second audit, not from designing for it.** When `field-society-demo` was audited with `the-council`'s audit already in the user's context, the comparison-to-prior shape produced itself. Worth preserving the section structure so future audits don't re-invent it.

## Naming

Sibling-suffix pattern (`context-engineering-audit`) matches `prd-creator` / `design-system-bootstrap`'s trigger-shaped naming. Considered alternatives: `audit-context` (too generic — "audit" alone could mean code review, security audit, accessibility audit) and `context-drift-report` (action-shaped, but "drift report" describes the output, not the trigger). Stuck with the suffix form.

## Symlinking

Like the other skills in this repo, this one will need a symlink at `~/.claude/skills/context-engineering-audit/` for Claude Code to load it. That's a deploy step, not a session-D concern. If a user clones this repo and wants the skill available, they need to symlink it the same way they symlink `context-engineering`.

## What lives in this file vs `procedure.md`

`procedure.md` is the executable procedure — read at audit time, end-to-end, every time. This file is the author's reference — read when iterating on the skill, never at audit time. The split keeps `procedure.md` short and prevents internal context (like "we considered three implementation options for the heavy tier") from leaking into the operational instructions.
