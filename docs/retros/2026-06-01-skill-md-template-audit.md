# Retro — 2026-06-01 — SKILL.md template audit and Gotchas backfill

Audited four SKILL.md files against `docs/skill-md-template.md`'s seven patterns (read-only first pass), then fixed the three non-gated skills. The consistent gap across all four was a missing bottom-anchored `## Gotchas` section (pattern #7); a secondary gap was no idempotency/re-run note (pattern #6).

## What was completed

- Read-only audit of all four SKILL.md files against the seven template patterns. Verdicts: all four "minor gaps," prd-creator edging toward significant because its real-failure content has no home in SKILL.md. Patterns #5 (self-cleaning process) and largely #6 are N/A — markdown-only skills, no daemons, no `scripts/`.
- Fixed `context-engineering/SKILL.md`: added `## Gotchas` (shape-not-content, re-run-clobbers, hooks-default-false). The re-run bullet closes both #7 and #6.
- Fixed `context-engineering-audit/SKILL.md`: bulletized the prose output-location branches (#3) and added the same-day `-rerun-N` case from `procedure.md`; added `## Gotchas` (read-only contract, halt-if-standard-absent, do-not-reshape-canonical-sections).
- Fixed `design-system-bootstrap/SKILL.md`: added `## Gotchas` (re-run-clobbers closing #6, no-raw-hex-in-semantic-layer, design-system-files-only).
- Added BACKLOG note: prd-creator still needs a Gotchas section, folded into its existing deferred-fixes entry.

## Files changed

- `skills/context-engineering/SKILL.md` — added bottom-anchored `## Gotchas`, 3 modes.
- `skills/context-engineering-audit/SKILL.md` — bulletized output-location branches; added `## Gotchas`, 3 modes.
- `skills/design-system-bootstrap/SKILL.md` — added `## Gotchas`, 3 modes.
- `docs/skill-md-template.md` — committed the previously-untracked reference template the audit was run against.
- `BACKLOG.md` — one-line note on prd-creator's pending Gotchas section.

## Key decisions made

- **Every gotcha cites a documented failure mode, none invented.** Grounded each in `principles.md`/`NOTES.md`/`procedure.md`: improvised `tokens.css`, the field-society `PRD.md` collision, two audited projects shipping prose-only with zero hooks, raw-hex-in-semantic-layer, the read-only contract. This holds the CLAUDE.md "every rule cites its failure mode" invariant.
- **Pattern #2 (fenced exact commands) treated as a deliberate divergence, not a gap.** These are markdown-reference generators, not bash-driven skills; "exact command" maps to "exact file to read," named inline. Not forced.
- **prd-creator deferred, not fixed.** Its substantive gotcha content (temporal hallucination, "ask anyway" overcorrection, vocab leak) overlaps the intake.md fixes already gated on Squirreled validation. Touching its Gotchas now would pre-empt that gate.
- **No DECISIONS entry.** Template-compliance backfill, not a new binding constraint. No trigger phrases or the markdown-only invariant touched.

## Open items

- **prd-creator Gotchas section** — deferred to the Squirreled-gated prd-creator fix pass. Noted in BACKLOG.
- Pattern #2 across all four remains a standing deliberate divergence; revisit only if a skill grows a bash-driven flow.

## Next session

- Unchanged priority: the Squirreled validation run (new session in `~/Sites/squirreled/`) is still the next evidence-input. The prd-creator Gotchas backfill rides along with that skill's deferred fixes once the validation retro lands.
