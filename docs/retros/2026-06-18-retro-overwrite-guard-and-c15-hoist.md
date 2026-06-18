# Retro — 2026-06-18 09:37 CDT — retro overwrite-guard + C-15 binding-contracts hoist   (5th session of the day)

## What was completed

- **Retro-convention overwrite guard.** Closed the one unhandled retro-collision path (two same-day sessions choosing the same topic slug → silent overwrite). One sentence added to [`docs/retros/README.md`](README.md) + the `context-engineering` template + its `output-small` example. Recommendation deliberately *declined* the heavier "add `HH:MM` to filenames" path — ordering was already solved (H1 timestamp + session-of-day + git-history selection); only the overwrite gap was live. Committed `cc42e7d` (pushed).
- **Wave-1 crib `C-15` adopted → [D-028](../DECISIONS.md).** Hoisted a terse `## Binding contracts (read before acting)` block to the top of the three generator skills' SKILL.md, above the Procedure the agent executes; `furnace-plan` already complied (the model). Tracker flipped, D-028 logged, `DECISIONS_ACTIVE.md` marker bumped D-027→D-028 (evaluated-not-mirrored), roadmap marker + count bumped.

## Failure this session

- **Tag:** none.
- **Near-miss (named):** attempted an `Edit` on `docs/DECISIONS.md` after only `tail`-ing it via Bash; the harness rejected it ("File has not been read yet") because a Bash `tail` doesn't register as a Read. Cost: one wasted Edit call, recovered immediately with a real `Read`.
  - **Tool or agent?** Agent habit — reached for `tail` to preview a long file's end cheaply, forgetting Edit requires the Read tool specifically.
  - **Does it generalize?** Minor, recurring-class: any "peek then edit" on a large doc. → **The change it demands:** none structural — when the intent is to edit, Read the target region with the Read tool, not Bash. Not rule-worthy (one wasted call, self-correcting).

## Files changed

- See `git status` / the D-028 entry — 3 SKILL.md (C-15) + `DECISIONS.md` (D-028) + `DECISIONS_ACTIVE.md` (marker) + `cribs-adoption-roadmap.md` (marker + count) + `cribs-from-steinberger-ecosystem.md` (status). Retro-guard files in `cc42e7d`. (Reference, not restate — per the CF-06 convention.)

## Key decisions made

- [D-028](../DECISIONS.md) — C-15 adopted (binding contracts hoisted; pointer not copy, CF-06-compliant; class (D) not the roadmap's (T)).
- Retro filename convention: keep date-only + slug, fence the overwrite gap with one sentence rather than restructure filenames (rationale in the session, not a D-NNN — reversible prose).

## Open items

- **Wave 1 remaining:** `CF-02` (durable-PRD rules, class T — prd-creator output discipline) and `DG-02` (semantic-not-directional token naming, class T — *first resolve: is RTL in DSB scope?*). Both in [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md).
- **Deferred (carried):** scaffold-template backport of C-09/CF-06/C-14 to `context-engineering`'s emitted retro template — a class-(T) batch, still pending per D-024/D-025.

## Next session

- Pick `CF-02` (top open Wave-1 item; class T → dry-run + diff against `output-small`). `DG-02` is blocked on the RTL-scope question — resolve that first or skip it. No skill to open with (Wave-1 cheap edits run inside the normal scope gate).
</content>
</invoke>
