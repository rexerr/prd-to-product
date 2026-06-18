# Retro — 2026-06-18 10:31 CDT — gstack crib mine: capture, adversarial verify, Wave-2 sequencing   (6th session of the day)

## What was completed

- Mined `garrytan/gstack` (60 skills + framing docs, MIT) with the hand-run crib engine: 7-agent surgical fan-out (D-022 depth discipline), deduped against the four existing trackers.
- Captured the full inventory as a new tracker — [`docs/cribs/cribs-from-gstack.md`](../cribs/cribs-from-gstack.md) (`G-01`–`G-21`): 21 candidates + fold-ins + parked + divergences. RETURN-not-Write gate held (synthesis returned as a draft; file written only on explicit "capture" approval).
- Ran adversarial verification (4 surface-grouped skeptics, default-refuted, real-file evidence): **7 survive / 8 revise / 3 park / 2 refuted.** Verdicts recorded in the tracker's "Adversarial verification" section.
- Sequenced the 7 survivors into Wave 2 of [`docs/cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md) as a labeled, plan-ready cohort (6 actionable + G-18 blocked on the unbuilt C-24 prompt), registered the tracker, updated the sync marker.
- Committed in two atomic commits (`9e04c5a` capture, `8f6e39e` roadmap). Handled a live parallel-session collision (the Wave-2 session, paused in plan mode) without entangling working trees.

## Failure this session

- **Tag:** bad substitution (near-miss, caught) + lost context (near-miss, caught) — neither landed.
- **Artifact 1 — the G-10 misread.** The mining synthesis claimed gstack's autoplan "upgrades a concern raised by ≥2 blinded reviewers; lone flags are not." The adversarial skeptic read the actual source: autoplan uses a *binary 2-voice* consensus + "single critical finding from one voice = flagged **regardless**" — the opposite of the crib. No "≥2→upgrade" rule exists in gstack. The bogus claim was synthesized into the tracker as `G-01`-adjacent `G-10`, and I had recommended the survivors *before* verification, so absent the gate this would have reached a CLAUDE.md/council edit.
  - **Tool or agent?** Agent — a synthesis subagent over-read the source; my pre-verification recommendation amplified it.
  - **Does it generalize?** Yes — fan-out synthesis over a large source reliably over-claims; it's the exact failure the engine's adversarial-verify-every-pick gate exists for.
  - **→ The change it demands:** None new. The gate worked as designed and earned its cost this session (it also killed `G-02` as a no-op). The standing lesson, already in the engine: never promote a crib pre-verification — which I violated in framing and the gate corrected. Tracker now carries the struck/corrected G-10 row so it can't be re-litigated.
- **Artifact 2 — tracker written to `docs/` root.** I created `cribs-from-gstack.md` at root, unaware the parallel session had committed a docs-routing convention (`1a7c242`) minutes earlier requiring `cribs-* → docs/cribs/`. Caught only because Rex flagged the parallel session and I checked `git log`/`status`.
  - **Tool or agent?** Agent — didn't re-check repo state when a concurrent session was known-active.
  - **Does it generalize?** Yes, whenever two sessions share `main`. Already named by CF-07 (reload-before-write) and the concurrency-mode wave.
  - **→ The change it demands:** None new (covered conceptually). Practical habit reinforced: when a parallel session may be live, read `git log -n` + `git status` before creating/editing shared files.

## Files changed

- [`docs/cribs/cribs-from-gstack.md`](../cribs/cribs-from-gstack.md) — new tracker (committed `9e04c5a`).
- [`BACKLOG.md`](../../BACKLOG.md) — crib bullet: five trackers incl. gstack, survivors→Wave 2 (committed `9e04c5a`).
- [`docs/cribs-adoption-roadmap.md`](../cribs-adoption-roadmap.md) — gstack registered + Wave-2 survivor cohort + sync marker (committed `8f6e39e`).
- This retro (this commit).

## Key decisions made

- **No `D-NNN` minted** — consistent with prior mining sessions: trackers record cribs, `DECISIONS.md` records *adoptions*. Nothing was adopted (all `Proposed`/queued), so no binding constraint to log or mirror.
- **This session does not promote.** With the Wave-2 session active on the same `main`, the gstack survivors are sequenced as roadmap input; the owning (paused) session does the actual skill edits. Collision-avoidance, not a durable rule.
- **Verification scope (honest):** the adversarial pass verified each crib's *net-new / fit / faithful-read* claims against the current repo files, and I re-checked that all relocated/added cross-references resolve (`../DECISIONS.md`, the BACKLOG and roadmap links — confirmed via `test -f`). It did **not** verify any *implementation* — no skill template changed, so no dry-run/diff-against `examples/output-small/` was run (none was due). The survivors' real fit when edited in is unverified by construction — that's the next session's job.

## Open items

- **Gated on Rex:** push (local is ahead of `origin/main`; I held it — only "commit" was asked, not "push"). Promotion of the survivors (the actual skill edits) — owned by the paused Wave-2 session.
- Queued in Wave 2: `G-16, G-08, G-06, G-11, G-19, G-14` (actionable) + `G-18` (blocked on the unbuilt C-24 oracle prompt). The 8 REVISE-tier gstack cribs are folds recorded in the tracker (into C-18/CF-13, C-22, etc.), no wave slot. `G-04/G-05/G-21` parked.

## Next session

- In the **other (paused) session**: pull the Wave-2 gstack cohort into a `/furnace-plan`, cleanest single-file first — `G-16` (furnace-plan ledger) then `G-11` (CLAUDE.md). Carry G-14's wording-inversion caveat; don't plan G-18 standalone. This session's thread (mine → capture → verify → sequence) is complete.
