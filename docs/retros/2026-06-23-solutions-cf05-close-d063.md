# Retro — 2026-06-23 18:05 CDT — solutions/ + CF-05 closed don't-build (D-063), via council + empirical retro-scan   (6th session of the day)

Rex asked to review the `solutions/` scar-tissue library concept — the biggest unbuilt thing in the repo — and whether it's of value. Ran it through `/devils-advocate`, discovered we'd already councilled the structurally identical system, ran the council's untaken "name-the-patterns" test empirically as a one-time scan of all 56 retro failure-sections, and closed both `solutions/` and CF-05 don't-build ([D-063](../DECISIONS.md#d-063)). The scan surfaced one genuine hidden shipped-product fix (Pattern A), now the top board row.

## What was completed

- **Reviewed the `solutions/` concept** against its real record (steinberger decision #3, roadmap Big Rocks, CF-05 gating) and the existing retro mechanism (87 retros, 56 with failure sections, 5-tag vocabulary).
- **Ran `/devils-advocate`** on my own "don't build, decouple CF-05" recommendation. It landed — flagged that I'd misapplied the evidence-gate to *observed* failures (39 logged) and that a one-time consolidation of the existing 56 retros isn't speculative. Verdict was Reconsider.
- **Caught the bigger miss myself only after Rex prompted ("didn't we council this?"):** the 2026-06-09 [self-healing-loop council](../council/council-transcript-2026-06-09-self-healing-loop.md) had already ruled **5/5 build-nothing** on the same capture/tag/count/fold-back system, on a *volume* kill-shot.
- **Ran the council's untaken test empirically** — delegated a sub-agent to scan all 56 failure-sections, grouping by root cause (not symptom tag), cross-referencing each against existing rules to find recurrence-after-a-rule. Result: log is mostly healthy (~35/56 none/caught-by-the-loop); one genuinely hidden, not-already-solved pattern (**Pattern A** — furnace Check 1 verifies *that* a read happened, not that it grounds the claim; n=9+, hidden by per-session micro-splitting).
- **Logged [D-063](../DECISIONS.md#d-063)** — `solutions/` + CF-05 closed don't-build; lever is periodic aggregation not a library; recurring scan ritual deliberately NOT minted (Rule-of-Two-gated); scaffold answer recorded (solutions/ rides AB-01's D-009 gate for high-error project types).
- **Paperwork:** flipped CF-05 ([pocock tracker](../cribs-from-pocock-craft.md) status + scope note + sequencing), decision #3 + divergence-audit row ([steinberger tracker](../cribs-from-steinberger-ecosystem.md)), [roadmap](../cribs-adoption-roadmap.md) Big Rocks + sync marker, [BACKLOG](../../BACKLOG.md) (solutions row → watching/closed; added Pattern-A `next` Seq-1 row; renumbered next lane 1-2-3), `DECISIONS_ACTIVE.md` marker → D-063.

## Failure this session

- **Tag: lost context.** The real miss: I spent the entire `solutions/` discussion re-deriving the build-vs-don't question from scratch — read the trackers, reasoned about value, even ran a full devils-advocate pass — without checking whether the repo had already decided it. It had: the 2026-06-09 self-healing-loop council ruled 5/5 build-nothing on the structurally identical system, and the [Harness-proposals kill-watch](../../BACKLOG.md) row ("read retro failure-tags after ~10 sessions") had been pointing at the exact scan I eventually ran. I only surfaced the council when Rex asked "didn't we council this?".
  - **Tool or agent?** Agent. The council transcript and the kill-watch row were both in the repo and both readable at session start; I didn't grep `docs/council/` before reasoning at length on a costly-to-reverse fork.
  - **Does it generalize?** Yes — "before re-opening a build/architecture question, check `docs/council/` and the relevant `watching` triggers for a prior ruling" is a real recurring risk in a council-dense repo. But note: this is a **non-execution of an existing instinct**, not a missing rule (D-009 already says recommend a council at forks; the implied complement is "check whether one already ran"). Per the scan's own Pattern D finding, a stronger rule can't fix non-execution — so I'm **not** minting one. The fix is the periodic-scan habit + reading the kill-watch row, both now live.
- **Secondary (meta, worth noting): Pattern F ate its own dogfood.** My devils-advocate "build the thin consolidation" recommendation was itself a recommend-before-grounding miss — I made the call before running the scan that would test it, and the scan then qualified it (the repo is disciplined; accretion isn't biting). That's Pattern F (recommend before the grounding read) recurring in real time, n+1 evidence for the find.

## Verification — what it did and didn't cover

- **The scan WAS the independent sub-task.** Delegated to a fresh general-purpose agent with the artifact + acceptance criteria (extract recurring root-cause patterns, cross-ref already-ruled-on, judge scaffold-vs-this-repo), withholding my own conclusion so it wasn't anchored. It returned a per-pattern table with verbatim artifacts and rule cross-references. This is the D-063 evidence base.
- **Cross-references checked:** grepped D-063 after editing — anchor `#d-063` resolves (header at DECISIONS.md:593); references land in all six files; the self-healing-loop council link target exists on disk; BACKLOG next-lane Seq verified contiguous (1, 2, 3); `git status` shows six docs + this retro, no code.
- **What it did NOT cover:** the scan is a one-time read, not a re-runnable check; its pattern-clustering is the sub-agent's judgment (I read its artifacts but did not independently re-cluster all 56). The Pattern A *fix* is not built or verified this session — it is a `next` row for a future `/furnace-plan` pass.

## Key decisions made

- **[D-063](../DECISIONS.md#d-063)** — `solutions/` library + CF-05 closed don't-build. Lever = detection by periodic aggregation, not a card library or compression. Recurring scan ritual NOT minted (Rule-of-Two-gated). Scaffold-emit for high-error project types rides AB-01's D-009 gate. Not council-gated (the structural question was already councilled; a don't-build is low-reversal-cost), not mirrored (no new binding rule).

## Pattern worth noting

This session is a clean case *for* periodic aggregation and *against* a standing library at once: a single scan, run on demand when the question arose, found the one real hidden insight (Pattern A) that 56 sessions of per-session review structurally couldn't see — and it did so without any permanent subsystem. That's the whole D-063 thesis demonstrated in the act of making the decision. The honest counterweight: the scan only happened because Rex pushed; left to the standing kill-watch row alone, it sat overdue. So the open question D-063 leaves is whether on-demand-when-asked is reliable enough, or whether the Rule-of-Two-gated ritual will be needed after all.

## Next session

- **Pick up: `/furnace-plan` the Pattern-A furnace grounding fix** — top board row ([BACKLOG.md](../../BACKLOG.md) `next` Seq 1). Add a Check-1 sub-case ("ground a claim at the breadth/granularity/forward-reach the claim asserts") to [`skills/furnace-plan/SKILL.md`](../../skills/furnace-plan/SKILL.md) AND the scaffolded verification rule (both shapes + `output-small`). Genuine `/furnace-plan` candidate — shipped product, both scaffold shapes, fixture diff to verify. Full context in [D-063](../DECISIONS.md#d-063).
</content>
