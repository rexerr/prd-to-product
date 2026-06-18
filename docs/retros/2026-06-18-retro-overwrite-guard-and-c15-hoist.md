# Retro — 2026-06-18 09:37 CDT — retro overwrite-guard + C-15 hoist + CF-02 durable-PRD rules   (5th session of the day)

## What was completed

- **Retro-convention overwrite guard.** Closed the one unhandled retro-collision path (two same-day sessions choosing the same topic slug → silent overwrite). One sentence added to [`docs/retros/README.md`](README.md) + the `context-engineering` template + its `output-small` example. Recommendation deliberately *declined* the heavier "add `HH:MM` to filenames" path — ordering was already solved (H1 timestamp + session-of-day + git-history selection); only the overwrite gap was live. Committed `cc42e7d` (pushed).
- **Wave-1 crib `C-15` adopted → [D-028](../DECISIONS.md).** Hoisted a terse `## Binding contracts (read before acting)` block to the top of the three generator skills' SKILL.md, above the Procedure the agent executes; `furnace-plan` already complied (the model). Tracker flipped, D-028 logged, `DECISIONS_ACTIVE.md` marker bumped D-027→D-028 (evaluated-not-mirrored), roadmap marker + count bumped.
- **Wave-1 crib `CF-02` adopted → [D-029](../DECISIONS.md)** — the heaviest Wave-1 item (tagged *integrate*). Two durable-PRD rules into prd-creator: (1) no volatile code locations in a PRD (paths/line-numbers/snippets rot on rename), carve-out for decision-encoding snippets; (2) a new always-emitted `## Testing decisions` section, sourced by one added cluster-7 question. Eight files: template + intake + `decisions.md` emission-row + principles (bullet + canonical-list renumber) + the small/medium/large example trio. Tracker flipped, D-029 logged, marker bumped D-028→D-029, pocock count 3→4.
- **Wave-1 crib `DG-02` declined-and-parked → [D-030](../DECISIONS.md).** Grep of design-system-bootstrap settled the crib's own RTL-in-scope condition: DSB emits no directional tokens, its seed CSS has no physical-direction properties, and RTL appears nowhere in scope — so the failure DG-02 guards against can't occur. Declined as a guard against a non-live failure (the anti-ceremony call, D-025/Rule-of-Two), parked concept-keyed with a re-entry trigger (DSB gains directional tokens, or RTL enters scope). **First real exercise of the D-027 declined-ledger discipline.** Tracker flipped to Parked, D-030 logged, marker bumped D-029→D-030, designer-row updated. **This closes Wave 1 — all cribs resolved.**

## Failure this session

- **Tag:** none.
- **Near-miss (named), fired twice:** attempted `Edit` after only previewing a file via Bash (`tail` on `docs/DECISIONS.md`; `sed` on the medium/large transcripts) — the harness rejected both ("File has not been read yet") because a Bash preview doesn't register as a Read. Cost: ~3 wasted Edit calls, each recovered immediately with a real `Read`.
  - **Tool or agent?** Agent habit — reached for `tail`/`sed` to preview cheaply, forgetting Edit requires the Read tool specifically.
  - **Does it generalize?** Yes, recurring-class (hit twice this session): any "peek-then-edit" on a large doc. → **The change it demands:** behavioral, not rule-worthy — when the intent is to edit, Read the target region with the Read tool, never a Bash preview. Cheap and self-correcting, so it stays a habit note, not a CLAUDE.md rule (logging it so a third recurrence would cross the Rule-of-Two bar).

## Files changed

- Three commits this session. Retro-overwrite-guard in `cc42e7d`; C-15 (3 SKILL.md + D-028 + tracker/roadmap/marker) in `52a2ffc`; CF-02 (8 prd-creator surfaces + D-029 + bookkeeping) in `e6c8f39`; DG-02 decline (D-030 + designer tracker + roadmap + marker) pending this session's close. See each commit / D-028–D-030 entries. (Reference, not restate — per the CF-06 convention.)

## Key decisions made

- [D-028](../DECISIONS.md) — C-15 adopted (binding contracts hoisted; pointer not copy, CF-06-compliant; class (D) not the roadmap's (T)).
- [D-029](../DECISIONS.md) — CF-02 adopted (two durable-PRD rules; always-emit Testing decisions section sourced by one cluster-7 question, not a new cluster).
- [D-030](../DECISIONS.md) — DG-02 declined-and-parked (failure not live in DSB; first exercise of the D-027 declined-ledger).
- Retro filename convention: keep date-only + slug, fence the overwrite gap with one sentence rather than restructure filenames (rationale in the session, not a D-NNN — reversible prose).

## Open items

- **Wave 1 is complete** — all cribs resolved (adopted or declined). The standing BACKLOG crib-row still names "Wave 1" as current; next session should advance it to **Wave 2** (high-value medium) in [`cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md), or pick up a Big Rock.
- **Deferred (carried):** scaffold-template backport of C-09/CF-06/C-14 to `context-engineering`'s emitted retro template — a class-(T) batch, still pending per D-024/D-025. Now joined by nothing new (C-15/CF-02 backports are skill-internal, not emitted).

## Next session

- Advance the BACKLOG crib-row to **Wave 2** and pick its top item (e.g. `C-16` decision-ready handoff brief, or `CF-18` interview discipline), or take a Big Rock (AGENTS.md-canonical flip; the `solutions/` scar-tissue library). Optionally clear the deferred scaffold-template retro-backport batch first. No skill to open with for Wave-2 cheap items; Big Rocks get `/furnace-plan`.

