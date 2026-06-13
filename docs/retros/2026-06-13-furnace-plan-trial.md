# Retro — 2026-06-13 07:37 CDT — plan-review audit → furnace-plan trial   (1st session of the day)

Work spanned late 2026-06-12 into 2026-06-13; council/evidence artifacts are dated 2026-06-12, this retro 06-13.

## What was completed

- Ran the parked plan-review mining audit ([`HANDOFF.md`](../../research/feedback-extracts/HANDOFF.md)) as a multi-agent `Workflow`: 83 sessions, one extractor + one adversarial verifier each + synthesis (139 agents). Produced [`PATTERNS.md`](../../research/feedback-extracts/PATTERNS.md) + evidence JSON.
- Headline: ≥57% of plan-review rounds drew a revision; dominant preventable class is "plans assert what they never verified" (T1/T2/T6, ~40–50 of 102 rounds).
- Ran the build-now-vs-validate-first fork through `llm-council` (5 advisors + 5 reviewers + chairman). Verdict: build the narrow verification core, Cowork-graded. Report + transcript in [`docs/council/`](../council/).
- Stress-tested the build via `devils-advocate` (verdict: reconsider → don't make it self-review). Rex's correction (he keeps Cowork, just wants fewer bugs sent) resolved it into a pre-filter + ledger design.
- Built the trial: global skill `~/.claude/skills/furnace-plan/` (explicit-invoke, task optional). Drafted the paired Cowork `plan-review` adjustment (attack-the-ledger) for Rex to apply.
- Committed audit + council + design record (`ec477f5`); BACKLOG "In progress" entry tracks the trial.

## Failure this session

- **None of the four classic tags squarely** — but one honest miss worth logging: I twice asserted an **unverified causal claim** (that the pasted external reviews in the audit were the output of Rex's Cowork `plan-review` skill — a "closed loop"), and Rex corrected it (the skill had never run on his projects; he also catches *none* of these errors himself). That is precisely the **T2 failure the audit indicts** — asserting what I never verified — committed by me while building the tool meant to prevent it. Useful data for the experiment: the target failure is real and reaches even the agent that mined it. Minor secondary: the Workflow crashed on first launch (`args` undefined); fixed with a defensive parse + resume.

## Files changed

- `research/feedback-extracts/PATTERNS.md` — the audit deliverable (new)
- `research/feedback-extracts/{revise-rounds,per-session,stats-and-audit}.json`, `synthesis-raw.md` — evidence (new)
- `research/feedback-extracts/furnace-draft.md` — design record, marked SHIPPED-as-trial (new)
- `docs/council/council-report-2026-06-12-furnace.html`, `council-transcript-2026-06-12-furnace.md`, `mapping.json`, `council-data.json` — council (new/regenerated)
- `BACKLOG.md` — furnace trial "In progress" entry (modified)
- `~/.claude/skills/furnace-plan/SKILL.md` — the trial skill (global, **outside this repo**, not committed here)

## Key decisions made

- **Furnace is a pre-filter, never a replacement.** Premise correction from Rex: he catches none of these errors; Cowork catches all of them. So Cowork stays authoritative and is the only valid grading oracle — Rex cannot grade the furnace himself.
- **Self-review, not a separate reviewer subagent.** A subagent would cost ~as much as a Cowork round-trip (cold re-reads), defeating "cut the process down." The cheap self-review's blind spot is backstopped by Cowork attacking the emitted ledger.
- **Skill now, hook only if it earns it.** Explicit-invoke skill is the reversible trial vehicle; promote to an `ExitPlanMode` hook only after the content proves out (council + audit evidence that standing CLAUDE.md rules get skipped).
- **Method correction recorded in PATTERNS.md §0:** the HANDOFF's "collapse back-to-back plans" rule was backwards — those are rejections whose feedback lives in the `ExitPlanMode` rejection `tool_result`, invisible to the digest. Revision counts are a floor.

## Open items

- ~~Rex applies the Cowork `plan-review` adjustment~~ **DONE 2026-06-13** — applied in Cowork. Full loop (furnace ledger → Cowork attacks it) is wired.
- **Trial grading** rides the existing Cowork round-trip over the next several real sessions: watch mechanical Must-fix count + hollow-ledger catches. Promote/kill triggers in the BACKLOG entry.
- `research/feedback-extracts/` is staging per HANDOFF; deletable once the trial concludes and any furnace lesson is folded in. `furnace-draft.md` + `HANDOFF.md` are the records to keep.

## Next session

- **Active next-session work: the brownfield context-drift audit pilot** (BACKLOG top of Backlog). Run a one-off, read-only audit of the most-outdated real project (qventus / seance / epost — scan and pick the most drifted) against a current-standard checklist derived from context-engineering; produce a drift report; then decide what to fix + whether `/audit-context` earns building. Do NOT build the skill first — same furnace lesson (pilot by hand, earn the build).
- Background, passive: the furnace trial keeps running — use `/furnace-plan that` on real work and watch the Cowork-graded signal accumulate. Do not promote to a hook until the catch-rate drop is real.
