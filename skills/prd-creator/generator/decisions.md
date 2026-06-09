# Decision logic

After the intake completes, run this logic to determine which optional sections emit and where the brand-and-voice content lands. Read this file when transitioning from intake summary to file writing.

## Emission table

Each row names a section, the cluster that fills it, the condition for inclusion, and the file the section emits to.

| Section | Source cluster | Inclusion condition | File |
|---|---|---|---|
| Product summary | 1 | Always | `PRD.md` |
| Target users | 1 | Always | `PRD.md` |
| Core problem | 1 | Always | `PRD.md` |
| Main workflow | 2 | Always | `PRD.md` |
| Version 1 scope | 3 | Always | `PRD.md` |
| Out of scope | 3 | Always | `PRD.md` |
| Deferred capabilities | 3 | Emit only if at least one item captured. If empty, omit the section. | `PRD.md` |
| Architecture and stack | 4 | Always | `PRD.md` |
| Decisions already made | 5 | Always (even if zero captured, emit the section with a one-line "no decisions locked yet" placeholder) | `PRD.md` |
| Open questions | sweep across clusters | Emit only if at least one captured. If empty, omit the section. | `PRD.md` |
| Success criteria | 7 | Always | `PRD.md` |
| Brand and voice (inline) | 6 | Cluster 6 ran AND total items captured ≤ 3 | `PRD.md` (appendix section) |
| Brand and voice (sibling file) | 6 | Cluster 6 ran AND total items captured > 3 | `BRAND.md` |
| Supporting documents | 0, 6 | Sibling `BRAND.md` was emitted, OR cluster 0 named external source documents the reader should reference, OR the user named other sibling docs (e.g. existing research) | `PRD.md` |

## Brand placement decision

The threshold for sibling vs inline is item count, not paragraph count. Count one item per:

- One audience segment named with a tone note.
- One tone attribute (name plus definition plus example counts as one item, not three).
- One vocabulary canonical name plus its forbidden alternatives.
- One do-not pattern.

Three or fewer total → inline appendix in `PRD.md` under `## Brand and voice`. More than three → sibling `docs/BRAND.md` rendered from `templates/BRAND.md.template`, plus a link from the PRD's `## Supporting documents` section.

If the user explicitly says "put it in a sibling file even though it's small" or "keep it inline even though it's substantive," honor the user's choice and note the override in the post-generation summary.

## Decision IDs

The final D-NNN list is the one confirmed in cluster 5. No gaps. Format each entry as:

```
- **D-NNN** <statement>. Rationale: <rationale>.
```

If cluster 5 produced zero decisions, emit the section with a single line: "No decisions locked at PRD time. The first decisions land when scaffolding context (see DECISIONS.md after running the context-engineering skill)."

## Open questions

Open questions accumulate across every cluster's closing sweep. Deduplicate before writing. If two captured questions ask the same thing, merge into the more specific phrasing. If a captured question turned out to be answered by a later cluster, drop it.

Sort the final list by criticality: questions that block V1 first, questions that affect V2 last. Criticality is judged from cluster topic. Stack and architecture questions usually block V1. Deferred-capability questions usually do not.

## File paths

Default paths, used unless the user named a different path during intake or in the pre-write confirmation:

- PRD: `docs/PRD.md`
- Brand sibling file: `docs/BRAND.md`

The skill writes files only at user-confirmed paths. If the project does not have a `docs/` folder yet, ask before creating one.

## Non-destructive write guard

Before writing `PRD.md` or `BRAND.md`, check whether the target path already exists on disk.

- **Does not exist** → write normally.
- **Exists** → **do not overwrite.** Show a diff against the existing file, state it already exists, and ask **overwrite / skip**. **Default to skip.** These are whole-file artifacts with no merge operation — do not offer merge. Never overwrite a hand-authored or previously generated PRD without explicit consent.

Report skipped/overwritten files in the output summary with the standard markers `(skipped — already exists; not overwritten)` and `(overwritten with consent)`. Because generation is non-deterministic, a re-run on an existing PRD shows as "differs" and prompts (default skip) — expected; the guard prioritizes never-clobber over silent re-runs.

**Enforced (D-005).** This guard is now backed by the global `write-guard.sh` PreToolUse hook ([`hooks/README.md`](../../../hooks/README.md)) when installed and this run is armed: a write to a file that **existed before this run** (`PRD.md`/`BRAND.md`) is gated — interactive → a non-forgeable permission dialog (`ask`), headless → auto-skip (`deny`, never clobbers/hangs). A `PRD.md` this run *creates* is auto-tracked as run-owned and stays editable. Still honor the prose: the hook may be absent or bypassed, and does nothing unless this run armed it. The field-society-demo run hit exactly this — a `PRD.md` collision between this skill and context-engineering — which is why the guard exists.

**Arm at run start (before writing `PRD.md`/`BRAND.md`), disarm at run end** — via Bash, so it bypasses the guard's own `Write|Edit` matcher:

```bash
# run start
mkdir -p ~/.claude/state/write-guard
: > ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel
# run end
rm -f ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".sentinel \
      ~/.claude/state/write-guard/"$CLAUDE_CODE_SESSION_ID".owned
```

Where the hook isn't installed this is a harmless no-op. A forgotten arm = no enforcement for that run (the prose is the backstop); a forgotten disarm is harmless.

## What never emits

These never appear in the output, even if mentioned during intake:

- Implementation code or pseudocode.
- Design tokens, color values, typography specs. (Design-system-bootstrap territory.)
- Rule files for `.claude/rules/`. (Context-engineering territory.)
- ROADMAP entries with dates or sprint assignments. (Context-engineering scaffolds the roadmap shape; PRD captures what to build, not when.)
- New decisions the user did not state. The skill does not invent.

## Routed-elsewhere content

Some material the user provides during intake belongs to a different skill or tool. The PRD does not absorb it, but the post-generation summary must flag it explicitly so the user knows it was not silently dropped.

Detect and flag any of the following if mentioned during cluster 0 source material or any cluster:

- **Visual aesthetic, color palettes, typography, illustration styles, design tokens.** Belongs to the design-system-bootstrap skill (parked). Flag in the summary as: "Visual aesthetic content you mentioned (e.g. <one-line paraphrase>) was not captured in the PRD or BRAND.md. It belongs in the design-system-bootstrap skill, which has not been built yet."
- **Specific rule files or `.claude/rules/` content.** Belongs to context-engineering. Flag in the summary as: "Rule-file content you described will be scaffolded by the context-engineering skill in the next run."
- **Implementation specifics that read like a tech spec.** Belongs to architecture documentation, which context-engineering scaffolds. Flag if the content is rich enough that dropping it silently would be a loss.

The flag is not optional. If routed-elsewhere material was mentioned, the summary names it. Silent dropping is a regression.
