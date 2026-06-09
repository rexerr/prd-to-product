# Retro — 2026-06-09 08:32 CDT — D-008 bookkeeping + adoption baseline doc   (3rd session of the day)

## What this session did

Closed out the handoff left by the 2nd session of the day ([Claude Design adopt council](2026-06-09-claude-design-adopt-council.md)). That session decided **build nothing** for Claude Design bundle ingestion but deliberately deferred the bookkeeping to a fresh session. This session executed all five handoff items. No skills touched; docs-only.

Rex also picked up handoff item 5 (the "tiny adopt a bundle" doc) as something worth building — so it went from open question to written.

## What landed

1. **D-008 logged** in [`DECISIONS.md`](../DECISIONS.md) + one-liner mirror in [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md): kit builds no adopt-skill / no DSB adopt-mode / no token-adopt command; Claude Design bundles stay authoritative; tokens reach a real product via a one-time product-side `cp`; revisit only on a 2nd bundle (Rule of Two). Tailwind-default note (CSS-vars, never Tailwind) folded in so item 4 isn't a separate dangling follow-up.
2. **Superseded banner** added to [`design-handoff-adopt-brief.md`](../design-handoff-adopt-brief.md) pointing at D-008 + the audit council. Brief kept intact below as the record of the rejected proposal.
3. **BACKLOG entry** for the deferred token-adopt command with promotion trigger = a 2nd real bundle.
4. **New baseline doc** [`design-handoff-adoption.md`](../design-handoff-adoption.md) — observation log + manual playbook + bundle ledger, explicitly *not a tool*. Holds: what a bundle contains, the fidelity finding (lossless values / non-isomorphic structure), the product-side adoption procedure (recreate components per the bundle README; `cp` lossless tokens into the product repo; bundle stays source of record), and a ledger whose second row is the literal Rule-of-Two tripwire.

## Why the doc is the right shape

The council killed every *automated* path at N=1 (can't separate a shipped theme from tweak-tool scratch → unvalidated schema). But killing automation doesn't mean discarding what dismantling bundle #1 taught us. A prose baseline:
- doesn't reopen the "build nothing" verdict (it's not a tool),
- makes the deferred decision cheap and grounded when bundle #2 arrives (re-derive against a record, don't rediscover),
- gives the Rule of Two an actual ledger to trip on.

## Verification

Doc-change contract (re-read + cross-refs resolve): all 8 referenced paths exist (fidelity test, superseded brief, the new doc, both council reports, the prior retro, both decisions files); D-008 present in `DECISIONS.md`, `DECISIONS_ACTIVE.md`, and `BACKLOG.md`. No skill templates touched → no dry-run/diff needed.

## Notes

- Light bookkeeping session, but Rex explicitly asked to document it — hence this retro despite the low bar.
- The only "ship now" from the whole Claude Design investigation remains **product-side** (the `cp` in a real app's repo), untouched by this kit. This session just recorded that procedure; it didn't run it.

## Commit / push

This session's artifacts (D-008 in both decisions files, brief banner, BACKLOG entry, the new adoption doc, this retro) committed and pushed together. No skill changes; no `the-council` changes.
