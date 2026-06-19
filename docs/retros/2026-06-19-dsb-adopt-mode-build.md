# Retro — 2026-06-19 08:48 CDT — DSB adopt-mode build (D-044)   (5th session of the day)

## What was completed

- Built `design-system-bootstrap` **adopt mode** per the approved plan ([`~/.claude/plans/wobbly-frolicking-turing.md`](../handoffs/2026-06-19-dsb-adopt-mode-handoff.md) was the source brief; plan went through `/furnace-plan` + two Cowork `/plan-review` rounds). Three automatic product-repo pieces: `cp` rendered design → `design/reference/`, `cp` bundle tokens verbatim (bypassing the scale-first template), emit the import rule. Mechanical hook + staleness check deferred to v2 (Rex's call).
- Logged [D-044](../DECISIONS.md) (narrows D-008; copy-never-transform invariant; the deliberate invariant-crossing) + mirror in [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md); added the partial-supersession marker to D-008.
- All 5 verification checks (class T) pass — see "Key decisions."

## Failure this session

- **Tag:** bad substitution (near-miss, caught pre-commit)
- **Name the artifact.** `skills/design-system-bootstrap/generator/intake.md:21` shipped a cross-file link as `../../docs/design-handoff-adoption.md` — wrong depth. A file in `generator/` needs `../../../docs/`; `../../docs/` resolves to the non-existent `skills/docs/`. Verification check 5 (link resolution from each file's own directory) caught it before any commit; fixed to `../../../docs/`.
- **Tool or agent?** Agent judgment — I reasoned the depth correctly for `decisions.md` (also in `generator/`, used `../../../`) but slipped on `intake.md` in the same subdir. The verification *check* (tooling I wrote into the plan) is what saved it.
- **Does it generalize?** Yes — relative-link depth from a nested skill subdir is a recurring trap (the plan's own line-number convention flagged a sibling instance). It will recur whenever a `generator/` file links up to `docs/`.
- **→ The change it demands:** None new. The plan's verification check 5 (resolve every relative link from its file's dir) already catches this class and did. The lesson is to keep that check mandatory for any multi-file skill edit, which CLAUDE.md "Verification before claiming done" already requires ("confirm cross-references resolve"). Adding a rule would be guardrail-accretion against a failure the existing guardrail caught.

## Files changed

See `git diff` — the 11 planned files. Highlights: `SKILL.md` (modes framing + adopt procedure + copy-not-author carve-out), `generator/intake.md` (cluster-0 bundle detection), `generator/decisions.md` (adopt branch + amended the closed write-allowlist — the Cowork Must-fix), `generator/output-summary.md` (adopt report), `principles.md`/`NOTES.md` (rationale + deferred-v2), new `templates/design-adoption.md.template` + `examples/transcript-adopt.md`, `docs/design-handoff-adoption.md` (superseding banner), `DECISIONS.md` + `DECISIONS_ACTIVE.md`.

## Key decisions made

- **Tokens copied verbatim, never through `tokens.css.template`** — the load-bearing invariant; documented inline in `decisions.md` with the "do not optimize this away" warning so a maintainer can't re-introduce the D-008 fidelity trap. Verification check 2 is the RED gate for it.
- **Closed-allowlist amendment (Cowork Must-fix):** both `decisions.md` "What the generator never writes" *and* the parallel list in `principles.md` are positive path-allowlists — both amended to add the two adopt paths + carve the "never elsewhere" line. (I found the principles.md instance myself; Cowork had only flagged decisions.md.)
- Verification: 5/5 checks pass (bootstrap unaffected — no bootstrap template/cluster touched; tokens-copied-not-templated; presence step emitted; emitted rule byte-matches the fence; all cross-refs resolve + D-009 needs no touch). Self-verified the checks — independent sub-task not used for the final pass; the write-guard live-fire on the 3 adopt write paths is honestly **UNVERIFIED** and routed to Cowork `/verify`.

## Open items

- **Write-guard live-fire** on the 3 adopt write paths (fresh `design/reference/` cp; re-snapshot overwrite; rule re-emission on re-run) — reasoned from D-005/D-006, not fired. Route to Cowork `/verify` in a fresh session before relying on it.
- **v2:** mechanical intra-app-consistency hook + scaffolded staleness check (deferred; parked in `NOTES.md`).
- **Not mine, found in the tree:** uncommitted `BACKLOG.md` edit + new `docs/briefs/docs-structure-and-artifact-routing-brief.md` (outside-agent product writes — flag to Rex, do not absorb); `skills/furnace-plan/trial-ledger.md` (Cowork's measurement carve-out from the two plan-review rounds — sweep into its own commit per CLAUDE.md when committing).

## Next session

- Cowork `/verify` the write-guard live-fire, then commit (DSB adopt-mode + D-044 as one commit; sweep the Cowork ledger append separately). Nothing to open with a skill.
