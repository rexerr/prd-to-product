# Retro — 2026-06-18 ~16:50 CDT — Wave-2 Sprint 2: prd-creator interview/output cribs (7th session of the day)

## What was completed

Wave 2 Sprint 2 (prd-creator surface cluster) adopted **three cribs across three passes**, authored through `/furnace-plan` and Cowork-reviewed across two rounds before any edit:

- **Pass A — CF-18** (→ [D-036](../DECISIONS.md), commit `7a388e5`). Three interview-*form* rules into [`intake.md`](../../skills/prd-creator/generator/intake.md) "How to run a cluster" (the runtime file), rationale into [`principles.md`](../../skills/prd-creator/principles.md): explainer-before-choice; recommended-answer **scoped** (candidate only on material-covered + branching/decision questions; genuinely open free-text stays a *bare* question — "ask cold" ≠ "pose a bare question"; never originate a user decision); explore-before-you-ask (user-answer-vs-brief contradiction → one forced choice, placed in the general per-cluster shape). furnace-plan landing of CF-18 deferred (prd-creator surface only).
- **Pass B — G-06** (→ [D-037](../DECISIONS.md), commit `61b726e`). Anti-sycophancy posture — banned-hedge list + take-a-position-and-name-what-would-change-it + steelman-then-challenge — as an **actionable block in `intake.md`** (not principles.md, which the interview does not load), rationale mirrored to principles. Bound to premise-challenge, never to inventing product direction.
- **Pass C — G-08** (→ [D-038](../DECISIONS.md), commit `45ce75f`). Five-category semantic-leak scan: checklist body in [`decisions.md`](../../skills/prd-creator/generator/decisions.md) (beside the write guard / "What never emits"), trigger at `intake.md`'s pre-write step, resolution-provenance line in [`output-summary.md`](../../skills/prd-creator/generator/output-summary.md) (case 4). Flag-not-redact; gstack's regex/audit-sink infra dropped.

CF-18/G-06/G-08 flipped `Adopted` in their source trackers; roadmap sync marker bumped (Sprint 2 complete).

## Failure this session

- **Tag: lost context (process)** — *not* in product, but in commit hygiene. My Pass A `git add -A` swept Cowork's trial-ledger append (5 rows) into the CF-18 product commit `7a388e5`, where the [D-018](../DECISIONS.md) carve-out requires the Cowork ledger append to be its **own dedicated** "Sweep Cowork ledger append" commit, scoped strictly to that one file. Root cause: reflexive `git add -A` without checking whether the working tree held a Cowork-owned change that needed isolating. **Not corrected by history rewrite** — the three passes share files (intake.md, DECISIONS.md each carry all three passes), so a reset can't reconstruct the A/B/C granularity the D-036/037/038 entries cite; the rows are committed, correct, and traceable, so the bundling is a cosmetic slip not worth a risky rewrite of unpushed main. **Guard for next time:** before the first `git add` of a crib pass, `git status` for an unstaged `trial-ledger.md` and commit it dedicated *first*. (Candidate cheap edit: stage crib files explicitly by path, never `-A`, when a Cowork review just ran.)

- **Furnace/Cowork loop caught four real plan-stage findings before any edit** (the trial's whole point). Recorded for the bucket scorecard — Cowork's `/plan-review` wrote the rows live (timestamps 16:20 / 16:45 UTC):
  - **R1 must-fix (bucket-1):** G-06's actionable list was planned into `principles.md`, which SKILL.md line 50 + principles.md line 3 both say is *not* loaded per-invocation — so the rule would be inert at runtime. A no-read-behind-it-class miss on the *consequence* of a fact I had read but didn't reason forward from. Fixed: actionable content moved to `intake.md`.
  - **R1 must-fix (bucket-1):** the bounded CF-18 rule 1 collided with the flagship small transcript + regression #11 (bare cold opening) from Q1 — I had under-weighted it as "log a follow-up." Fixed: rule 1 scoped so open free-text stays bare; the fixture stays valid by design.
  - **R1 refinements (bucket-3 ×2):** rule 3 contradiction-check belonged in the general per-cluster shape not cluster 0; G-08 output-summary line should be resolution-provenance not a live warning. Both adopted.
  - **R2 refinement (bucket-2, latent):** rule 1(b)'s recommended-option on a genuine undecided *product* branching question edges toward the rejected literal form; bind it by the same anti-invention guard as 1(a). Folded into the wording though it rarely bites today (no scripted cluster poses a branching product question).
- **Two bucket-1 must-fixes in one session.** Both were *forcing-function-underperformed* cases: Check 1 (cite codebase claims to a read) technically passed — I had read the files — but I drew a wrong *forward inference* from a correct read (where-does-it-load; does-it-break-the-fixture). This is the same shape as Sprint 1's granularity miss: Check 1 verifies the read happened, not that the plan reasoned correctly *from* it. **Now two adjacent data points** (Sprint-1 granularity + this session's load-site/fixture inference) suggesting Check 1's blind spot is "read-happened ≠ inference-correct," not the string/equality sub-case CF-03 flagged. Still below a clean Rule-of-Two for any single sub-type; watch whether a third lands before touching Check 1.

## Files changed

Three product commits + the (mis-bundled) ledger rows: Pass A `7a388e5`; Pass B `61b726e`; Pass C `45ce75f`. Decisions D-036–D-038 carry the per-crib detail. No push this session.

## Key decisions made

- [D-036](../DECISIONS.md)–[D-038](../DECISIONS.md) — the three adoptions. None mirrored to `DECISIONS_ACTIVE.md` (all visible by reading the prd-creator files; the skip-precedent holds — D-034 was the one Sprint-1 mirror, no Sprint-2 crib clears that bar).
- **CF-18 rule 1 resolved to bounded-and-scoped** (sign-off item 1) — Rex + Cowork finding 2; literal form rejected (breaks the fixture), minimal form (rules 2&3 only) held as the fallback.

## Open items

- **Wave 2 continues.** Per the surface-clustered re-sequence: **S3** context-engineering = DG-01 + CF-13 + G-14\* + AB-03 + the deferred C-09/CF-06/C-14 retro-template backport; **S4** DSB = G-19 (+ G-09 REVISE); **solo /furnace-plan** = CF-07; **parked** = G-18 (rides unbuilt C-24). Or take a Big Rock.
- **CF-18 furnace-plan landing** — deferred this sprint (prd-creator surface only). A future sequencing item, not a gap; furnace-plan already had its Sprint-1 pass.
- **Furnace trial:** the "read-happened ≠ inference-correct" Check-1 blind spot now has two adjacent data points (Sprint-1 granularity + this session). Watch for a third before sharpening Check 1.
- **Commit-hygiene guard:** consider an explicit-path staging habit (or a pre-commit reminder) after a Cowork review, so a trial-ledger append never co-mingles with product again.

## Next session

Start **Sprint 3** (context-engineering surface — the largest cluster: DG-01 + CF-13 + G-14\* + AB-03 + the C-09/CF-06/C-14 backport). It's a bigger, multi-artifact surface (templates + emitted files + the example tree), so `/furnace-plan` is warranted and the verification genuinely *is* class (T) here (dry-run + diff against `output-small/`), unlike the prd-creator self-instruction edits this sprint. Or take a Big Rock (AGENTS.md-canonical flip; the `solutions/` library).
