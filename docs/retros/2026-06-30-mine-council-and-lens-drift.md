# Retro — 2026-06-30 17:47 CDT — TanStack/intent mine, foundation-gap council, and the recurring lens drift   (4th session of the day)

**Dominant failure tag: goal drift** (3× in one session — the headline of this retro).

## What happened

- **`/mine` on TanStack/intent** (cloned `f9269e5`, MIT, gitignored at `docs/mined/repos/intent/`). Dived in passes; landed [`docs/mined/2026-06-30-tanstack-intent.md`](../mined/2026-06-30-tanstack-intent.md) + 3 consolidated board rows (intake upgrades CE-1/CE-2, path-portability decision F-05, skill-authoring upgrades F-01/F-02/F-03). Findings verified against actual repo files.
- **Rex flagged the frame was wrong:** the mine — and my framing throughout — kept collapsing the work to "improve the skill `.md`" instead of "improve what the skills *produce for his downstream projects* (his apps)." Reframed: the trio (`prd-creator`/`context-engineering`/`design-system-bootstrap`) is **necessary but not sufficient**; surfaced the project-setup / foundation gap.
- **Council** (Rex chose "pressure-test"): full `/llm-council` — 5 advisors → 5 anonymous reviewers → chairman ([report](../council/council-report-2026-06-30-foundation.html), [transcript](../council/council-transcript-2026-06-30-foundation.md)). Verdict: don't author/freeze a foundation skill; capture the *question* not the *answer*; instrument with a `FOUNDATION.md`; gate on repeated-need evidence. Peer round caught the load-bearing unverified premise (is the gap a one-app hunch or a structural step every project hits?).
- **Rex pushed back on the council's scope:** it answered a narrower question than his real need, and "are the 100s of build skills out there unnecessary?" exposed that **all four framed options assumed *Rex authors and solo-maintains* the skill** — "compose existing, externally-maintained build skills" was never on the table. Wrote [`docs/handoffs/project-setup-system-handoff.md`](../handoffs/project-setup-system-handoff.md): real question at full size, 3 next-session review tracks (real projects · TanStack template/workflow/devtools · deep online research), the premise to verify.
- **Rex named the recurring pattern (≈3×): collapsing the work to `.md`-tidying.** Diagnosed the root cause as structural — the always-loaded context states the *artifact* + *rules* but never the *telos* (skills serve downstream projects); the loud markdown-only invariant reinforces the misread. Remediation agreed: a "What this is FOR" north-star block at the top of `CLAUDE.md`/`AGENTS.md` (drafted in handoff §0, **PROPOSED, gated on Rex**), sequenced as next-session **task 0** (board Seq 1), ahead of the repo eval.

## The dominant failure — goal drift, honestly

Three times in one session I optimized the **artifact** (skill markdown: frontmatter validation, intake craft, mine findings about the skills' own prose) instead of the **outcome** Rex cares about (his future projects shipping well). I took the repo's self-description ("markdown-only skill workspace") as the mining lens instead of asking *"in service of what?"* Each time Rex had to re-widen the frame.

The honest diagnosis is that this is **structural, not just carelessness** — the repo's own context points every session at the wrong altitude — which is *why* it recurs and why the fix is a top-of-`CLAUDE.md` telos statement, not a resolution to "be more careful." But I own my half: I should run an altitude check at lens-setting. This is now task 0 next session.

**Adjacent honesty miss:** the first `/mine` "deep dive" was a skim — the strongest findings (CE-1/CE-2) only surfaced on a *second* "go deeper" prompt, and the highest-IP files (`domain-discovery`/`tree-generator`) were initially triaged away by title. "Resembles a rule we already have" stood in for reading the implementation. Caught and corrected mid-session, but it's the same goal-drift family: optimizing the appearance of coverage over the real thing.

## Verification — what it did and didn't cover

- **Did:** mine findings checked against real files (validate.ts six-key spec vs. our 7 skills, all passing; F-05 absolute-path leak confirmed at `output-small/AGENTS.md:79`; CE-1/CE-2 gaps confirmed against `generator/intake.md`). Board render clean (0 tag warnings, exit 0). Link checker clean (116 live docs, no broken links). Council artifacts built and opened.
- **Did NOT (by design, deferred to next session):** review TanStack `template`/`workflow`/`devtools` — documented as *priors, not findings*. The foundation "repeated need" premise is **unverified** (track 1 next session). The `CLAUDE.md` telos fix is **drafted but not applied** — gated on Rex.

## Deviations / calls

- **No `D-NNN` logged.** The foundation question is open (not settled); the lens-fix is agreed-in-principle but implementation is deferred — a premature decision entry would contradict the session's own "ground in evidence first" lesson. The handoff + board carry the state; log the telos rule as a `D-NNN` when the `CLAUDE.md` edit actually lands next session.
- **No product/skill/template files changed** this session — it was a mine (proposals), a council (advisory), and a planning/handoff/diagnosis. Lower-risk surface; verification was doc-level accordingly.
