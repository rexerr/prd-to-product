## Retro — 2026-05-10 — Continuous-mode session D: audit-skill design

Designed and implemented the light tier of `context-engineering-audit` per [iteration-2 retro Appendix D](2026-05-10-continuous-mode-iteration-2.md). Closes the last queued item from continuous-mode iteration 2.

## Scope decision: light

Chose the light path. Reasons:

- Two real audits (`the-council`, `field-society-demo`) produced consistent six-section output structure without coordination, run human-read-driven. The pattern is portable enough to encode as a skill but doesn't yet need automation to be repeatable.
- No drift class has appeared yet that a programmatic validator would catch but a careful human reader would miss. The trigger for heavy-tier work is third-instance evidence; we're at zero.
- Light scope (~200 lines) lets us ship the skill and learn from its third invocation before deciding what automation would actually pay for itself.

Heavy-validator option is logged in `NOTES.md` with three concrete implementation paths (Bash + jq, Python, MCP server) and explicit build triggers (`paths:` globs that match nothing, malformed hook matchers, broken cross-references in rule files). Gated on a class of drift the light tier consistently misses.

## What landed

New directory `skills/context-engineering-audit/` with four files:

- **`SKILL.md`** (58 lines) — trigger-shaped description matching the audit context; don't-trigger cases distinguishing from `context-engineering` (scaffold) and generic code review; explicit read-only contract.
- **`procedure.md`** (72 lines) — operational procedure: reading order (skill → standard → examples → project → prior audits), output structure pointer to the skeleton, three explicit watch-item checks (session-discipline three-section coverage; recency-block dilution; hooks-presence-vs-prose-only), source-of-truth precedence, read-only contract, output location.
- **`templates/output-skeleton.md`** (152 lines) — the report skeleton to copy and fill. Six mandatory sections plus the conditional seventh comparison-to-prior. Headings verbatim; sub-buckets and table columns fixed.
- **`NOTES.md`** (41 lines) — internal notes: heavy-validator option as future work, design observations from the two reference audits, naming rationale, what lives here vs `procedure.md`.

Total: 323 lines across 4 files. Operational pair (`SKILL.md` + `procedure.md`) is 130 lines — under Appendix D's 200-line cap. Skeleton loads only when writing the report; NOTES.md is author-only.

## The scope-cap moment

First draft put everything in `procedure.md` and hit 263 lines on the operational pair — over Appendix D's 200-line ceiling. The skeletons were the bloat: the user explicitly approved filled-skeleton output in the planning round, and the skeletons earn their lines, but they don't belong in the procedure file.

Surfaced the overshoot before committing. Three options offered: commit as-is and document the overshoot; trim skeletons to prose; or split skeletons into a separate `templates/output-skeleton.md`. User chose split.

The split is structurally better than either alternative — `procedure.md` becomes a tight "what to do" file (loaded at audit time, every audit) and the skeleton becomes a "what the output looks like" reference (loaded only when filling the report, which is a smaller fraction of the audit's compute). Mirrors `context-engineering`'s own split between `SKILL.md` (light), `principles.md` (reference, on-demand), and `templates/` (filled at generation time).

The lesson worth keeping: **the 200-line cap surfaced the right structural split**. Without the cap, the skill would have shipped with everything in one file and a worse separation of concerns. The cap did its job — not as a hard ceiling on what to ship, but as a forcing function that made the structural question visible.

## Files-in-this-skill convention

The four-file shape (`SKILL.md` + `procedure.md` + `templates/` + `NOTES.md`) is now an in-house pattern across two skills (`context-engineering` and `context-engineering-audit`). Worth naming explicitly:

| File | Loaded when | Purpose |
|---|---|---|
| `SKILL.md` | Always (when skill triggers) | Trigger discrimination, procedure pointer, contracts. Light. |
| `procedure.md` (or `generator/`) | On execution | What to do. Operational. |
| `templates/` | When emitting output | Filled at generation/report time. |
| `principles.md` | On-demand | Why the patterns are shaped this way. Reference. |
| `NOTES.md` | Never at invocation | Author's reference; internal observations and deferred decisions. |

`context-engineering-audit` doesn't have a `principles.md` (its principles are inherited from `context-engineering`) but otherwise matches the shape. Worth surfacing this convention in `context-engineering`'s `principles.md` if a third skill in this repo lands and confirms the pattern.

## What's still queued

Nothing. All six iteration-1 items closed-or-acted; sessions B, C, D complete; continuous-mode is now in true maintenance mode. Next edits trigger only on:

- A real failure mode landing during dog-fooded session work (capture in `PARKING_LOT.md`; fix at second instance unless single-instance evidence is high-conviction).
- A Claude Code feature shipping that obsoletes a current pattern.
- New peer-reviewed or insider-source evidence with traceable failure-mode connection.

The `context-engineering-audit` skill's first invocation will be its own evidence-gathering moment. Run it on a third hand-built project to validate that the procedure-and-skeleton split holds; if the third audit produces a meaningfully different shape, the skill needs an update before it's stable.

## Sources

- iteration-2 retro (the source of the queued work): [`2026-05-10-continuous-mode-iteration-2.md`](2026-05-10-continuous-mode-iteration-2.md).
- iteration-1 retro Appendix A (the original audit prompt that became `procedure.md`): [`2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md).
- Reference audits encoded in the procedure: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`, `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md` (external repos).
- Files created: [`skills/context-engineering-audit/SKILL.md`](../../skills/context-engineering-audit/SKILL.md), [`skills/context-engineering-audit/procedure.md`](../../skills/context-engineering-audit/procedure.md), [`skills/context-engineering-audit/templates/output-skeleton.md`](../../skills/context-engineering-audit/templates/output-skeleton.md), [`skills/context-engineering-audit/NOTES.md`](../../skills/context-engineering-audit/NOTES.md).
