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

None of these have appeared in the two audits so far. Wait for the third instance, per the same continuous-mode discipline `prd-to-product`'s BACKLOG uses.

## Design observations from the two reference audits

A few patterns that emerged from `the-council` and `field-society-demo` audits worth preserving here, in case future iteration on the skill needs the evidence:

- **Both audits converged on the same six-section structure without coordination.** Different projects, different shapes (one modular+UI, one modular+UI but smaller AI scope), different stages — same output structure. The structure is portable enough to template; that's why `procedure.md` carries filled skeletons rather than prose descriptions.
- **The judgment column in §3 (intentional vs accidental) is where the audit earns its keep.** A pure presence/absence diff would miss the "the project did this on purpose because their failure history justifies it" cases. Human judgment is the load-bearing part; that's why this skill stays light-tier.
- **The "Comparison to prior audit" section emerged from running the second audit, not from designing for it.** When `field-society-demo` was audited with `the-council`'s audit already in the user's context, the comparison-to-prior shape produced itself. Worth preserving the section structure so future audits don't re-invent it.

## Naming

Sibling-suffix pattern (`context-engineering-audit`) matches `prd-creator` / `design-system-bootstrap`'s trigger-shaped naming. Considered alternatives: `audit-context` (too generic — "audit" alone could mean code review, security audit, accessibility audit) and `context-drift-report` (action-shaped, but "drift report" describes the output, not the trigger). Stuck with the suffix form.

## Symlinking / promotion status — intentionally NOT global (decided 2026-06-17)

Unlike the other skills in this repo, this one is **deliberately not symlinked** into `~/.claude/skills/`. Two reasons:

1. **[D-013](../../docs/DECISIONS.md) declined an audit *tool*.** The 2026-06-13 brownfield pilots specced a richer `/audit-context` and Rex declined building it — brownfield drift is low-stakes and one-time, handled **by hand** from the audit docs. On 2026-06-17 the question of promoting *this* pre-D-013 light-tier skill to global was raised and declined for the same reason: keep it a design record, don't make it an always-available skill.
2. **It lacks the field-0 gate the pilots proved was non-optional.** The pilots found that an audit must first gate on *"was this project ever scaffolded by / opted into the standard?"* — without it, a run against a never-scaffolded project produces a false-positive cascade the BACKLOG calls *"actively harmful, not just noisy."* This skill has no such gate; it starts auditing immediately.

The skill stays in-repo as the **design record** of the light-tier audit method. **Do not symlink / promote it without first porting the field-0 opted-in gate** (see [`docs/audits/2026-06-13-*-context-drift.md`](../../docs/audits/) and [D-013](../../docs/DECISIONS.md)).

## What lives in this file vs `procedure.md`

`procedure.md` is the executable procedure — read at audit time, end-to-end, every time. This file is the author's reference — read when iterating on the skill, never at audit time. The split keeps `procedure.md` short and prevents internal context (like "we considered three implementation options for the heavy tier") from leaking into the operational instructions.
