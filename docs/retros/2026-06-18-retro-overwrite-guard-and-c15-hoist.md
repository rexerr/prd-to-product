# Retro — 2026-06-18 09:37 CDT — retro overwrite-guard + C-15 hoist + CF-02 durable-PRD rules   (5th session of the day)

## What was completed

- **Retro-convention overwrite guard.** Closed the one unhandled retro-collision path (two same-day sessions choosing the same topic slug → silent overwrite). One sentence added to [`docs/retros/README.md`](README.md) + the `context-engineering` template + its `output-small` example. Recommendation deliberately *declined* the heavier "add `HH:MM` to filenames" path — ordering was already solved (H1 timestamp + session-of-day + git-history selection); only the overwrite gap was live. Committed `cc42e7d` (pushed).
- **Wave-1 crib `C-15` adopted → [D-028](../DECISIONS.md).** Hoisted a terse `## Binding contracts (read before acting)` block to the top of the three generator skills' SKILL.md, above the Procedure the agent executes; `furnace-plan` already complied (the model). Tracker flipped, D-028 logged, `DECISIONS_ACTIVE.md` marker bumped D-027→D-028 (evaluated-not-mirrored), roadmap marker + count bumped.
- **Wave-1 crib `CF-02` adopted → [D-029](../DECISIONS.md)** — the heaviest Wave-1 item (tagged *integrate*). Two durable-PRD rules into prd-creator: (1) no volatile code locations in a PRD (paths/line-numbers/snippets rot on rename), carve-out for decision-encoding snippets; (2) a new always-emitted `## Testing decisions` section, sourced by one added cluster-7 question. Eight files: template + intake + `decisions.md` emission-row + principles (bullet + canonical-list renumber) + the small/medium/large example trio. Tracker flipped, D-029 logged, marker bumped D-028→D-029, pocock count 3→4.

## Failure this session

- **Tag:** none.
- **Near-miss (named), fired twice:** attempted `Edit` after only previewing a file via Bash (`tail` on `docs/DECISIONS.md`; `sed` on the medium/large transcripts) — the harness rejected both ("File has not been read yet") because a Bash preview doesn't register as a Read. Cost: ~3 wasted Edit calls, each recovered immediately with a real `Read`.
  - **Tool or agent?** Agent habit — reached for `tail`/`sed` to preview cheaply, forgetting Edit requires the Read tool specifically.
  - **Does it generalize?** Yes, recurring-class (hit twice this session): any "peek-then-edit" on a large doc. → **The change it demands:** behavioral, not rule-worthy — when the intent is to edit, Read the target region with the Read tool, never a Bash preview. Cheap and self-correcting, so it stays a habit note, not a CLAUDE.md rule (logging it so a third recurrence would cross the Rule-of-Two bar).

## Files changed

- See `git status` / the D-028 entry — 3 SKILL.md (C-15) + `DECISIONS.md` (D-028) + `DECISIONS_ACTIVE.md` (marker) + `cribs-adoption-roadmap.md` (marker + count) + `cribs-from-steinberger-ecosystem.md` (status). Retro-guard files in `cc42e7d`. (Reference, not restate — per the CF-06 convention.)

## Key decisions made

- [D-028](../DECISIONS.md) — C-15 adopted (binding contracts hoisted; pointer not copy, CF-06-compliant; class (D) not the roadmap's (T)).
- Retro filename convention: keep date-only + slug, fence the overwrite gap with one sentence rather than restructure filenames (rationale in the session, not a D-NNN — reversible prose).

## Open items

- **Wave 1 remaining: just `DG-02`** (semantic-not-directional token naming, class T, lands on design-system-bootstrap) — **blocked on a scope question: is RTL in DSB's V1 scope?** Resolve that first; if RTL is out of scope the crib may be a near-no-op. After DG-02, Wave 1 is complete and C-15/CF-02's deferred scaffold-template backports + Wave 2 are next. In [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md).
- **Deferred (carried):** scaffold-template backport of C-09/CF-06/C-14 to `context-engineering`'s emitted retro template — a class-(T) batch, still pending per D-024/D-025.

## Next session

- Resolve the **DG-02 RTL-scope question first** (is right-to-left in design-system-bootstrap's V1 scope?), then adopt or decline DG-02 accordingly — it's the last open Wave-1 item. No skill to open with (Wave-1 edits run inside the normal scope gate).
</content>
</invoke>
