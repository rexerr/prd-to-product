# Retro — 2026-06-18 ~11:00 CDT — Wave-2 Sprint 1: furnace ledger cribs (6th session of the day)

## What was completed

Wave 2 opened. Sprint 1 (furnace-plan surface cluster, gstack-integrated) adopted **six cribs across four passes**, authored through `/furnace-plan` and Cowork-reviewed across two rounds before any edit:

- **Pass A — C-16 + G-16 + G-01** (→ [D-031](../DECISIONS.md), [D-032](../DECISIONS.md)). furnace-plan SKILL.md gains a `## Sign-off items` section (decision-ready handoff, never a bare question), a **mandatory unbolded `NO UNRESOLVED DECISIONS` terminal sentinel** on the ledger spec, and a verbatim-quote `Checked:` clause (G-01 adopted-as-revised — cap machinery + framework-meta nudge dropped).
- **Pass B — CF-20** (→ [D-033](../DECISIONS.md)). Self-skip gate: an in-plan-mode bow-out offer in furnace-plan (preserving the mandatory `EnterPlanMode`-first contract, [D-020](../DECISIONS.md)) + a parallel self-skip in prd-creator (Procedure + principle).
- **Pass C — CF-23** (→ [D-034](../DECISIONS.md), **mirrored to `DECISIONS_ACTIVE.md`**). The two-load model (context-load vs cognitive-load) as the binding rule for `disable-model-invocation`; `skill-md-template.md` carries pointer/example only.
- **Pass D — G-11** (→ [D-035](../DECISIONS.md), isolated gated commit). CLAUDE.md delegate-to-subagent line tightened: withhold the author's reasoning from the verifier; named self-verify fallback.

**CF-15 deferred** out of Sprint 1 — a near-no-op on furnace-plan (no scored verdict for "no-cross-rerank" to govern; the G-02-REFUTED pattern). Stays `Proposed`; re-enters only if a scored multi-axis review surface appears.

## Failure this session

- **Tag:** none reached product — but the furnace/Cowork loop caught two real plan-stage errors before any edit, which is the trial's whole point. Recorded for the bucket scorecard:
  - **Bucket-1** (R1 must-fix): the plan asserted "G-16/C-16/CF-15 all land on the verification-ledger region." A section-by-section re-read showed three distinct surfaces (ledger / sign-off prose / preflight). Check 1 *technically passed* (SKILL.md was read this session) but I summarized the read at the wrong granularity — the forcing function underperformed on a **claim-vs-read granularity** sub-case, not a string/equality one. Held at n=1 (Rule of Two); a second granularity miss would argue for sharpening Check 1 to "re-read at the granularity of the specific claim." Not a CLAUDE.md change.
  - **Bucket-2/3** (R1 must-fix): CF-15 flagged as a near-no-op — a blind spot a fresh context caught (no verdict structure exists to merge), correctly deferred rather than adopted as ceremony.
- This is the **first multi-round live furnace result with a real must-fix bucket-1** (prior live result, CF-03, was 1×bucket-1 string-claim + 1×bucket-3). Two data points now; the granularity sub-case is distinct from the CF-03 string-equality one, so neither has hit Rule-of-Two yet.

## Files changed

Five commits (reference, not restate — per CF-06): Pass A `1b0f0de`; Cowork ledger sweep `98a4ebd` (D-018 — 9 rows, this file only); Pass B `21e0f63`; Pass C `7053ef2`; Pass D `8df8731` (isolated gated CLAUDE.md edit). Decisions D-031–D-035 carry the per-crib detail.

## Key decisions made

- [D-031](../DECISIONS.md)–[D-035](../DECISIONS.md) — the six adoptions (D-032 covers G-16 + G-01-as-revised). D-034 mirrored to `DECISIONS_ACTIVE.md` (the one Sprint-1 crib that binds future authoring with a live `/repo-miner` consumer).
- **CF-15 deferred** (not declined) — stays Proposed with a concrete re-entry trigger; recorded here, no D-NNN, no tracker status change.
- **D-NNN granularity:** two IDs for the C-16/G-16 pair (distinct trackers each cite their own) — a co-designed pass ≠ a batch-adopt under [D-022](../DECISIONS.md).

## Open items

- **Wave 2 continues.** Sprint 1 complete. Per the surface-clustered re-sequence: **S2** prd-creator = CF-18 + G-06 + G-08; **S3** context-engineering = DG-01 + CF-13 + G-14\* + AB-03 + the deferred C-09/CF-06/C-14 retro-template backport; **S4** DSB = G-19 (+ G-09 REVISE); **solo /furnace-plan** = CF-07; **parked** = G-18 (rides unbuilt C-24).
- **CF-15** sits deferred in Wave 2 (Proposed) — revisit only if a scored multi-axis review surface emerges.
- **Furnace trial:** the bucket-1 granularity sub-case is logged at n=1; watch for a second before touching Check 1.

## Next session

Start **Sprint 2** (prd-creator: CF-18 + G-06 + G-08) — a `/furnace-plan` is warranted (real interview-discipline edits across SKILL.md + intake + principles), and it's the same surface so it clusters cleanly. Or take a Big Rock (AGENTS.md-canonical flip; the `solutions/` library).
