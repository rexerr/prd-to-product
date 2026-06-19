# Retro — 2026-06-19 08:16 CDT — context lifecycle: council → research → brief   (4th session of the day)

**Failure tag:** none (research/design session; self-corrected mid-stream via Rex's pushback). One process insight worth keeping — see "What I'd change."

## What was done

Started as "review the productivity/PM skill group — does it build a visual roadmap better than before?" and unfolded into a foundation question: is the dense single-file `BACKLOG.md` the right project-management substrate for a solo-dev + agent workflow?

- Ran `/llm-council` on "ticket+queue vs. dense single-file BACKLOG." Verdict: don't adopt tickets/external trackers/HTML app; split the live queue from the reasoning archive. Artifacts: [`docs/council/council-report-2026-06-19-pm-system.html`](../council/council-report-2026-06-19-pm-system.html) + transcript + data + mapping.
- **Rex correctly rejected the council's concrete fix** ("thin index on top, archive below in the same file") — with the archive below in the always-read file, the agent still reads it whole, so token cost is unchanged. He then named the deeper defect: nothing ever leaves the hot set, and the decision log has no retirement mechanism either.
- Ran `deep-research` on bounding agent session-start context + backlog/decision lifecycle. 24 sources, 25 claims verified 3-0, 0 killed. It corrected the council and validated the folder-of-tickets direction. Report staged at [`research/context-lifecycle-research-2026-06-19.md`](../../research/context-lifecycle-research-2026-06-19.md).
- Wrote the proposal: [`docs/briefs/context-lifecycle-brief.md`](../briefs/context-lifecycle-brief.md) (new `docs/briefs/` folder per the routing convention) — thin always-loaded index + `tickets/` folder read on demand + `tickets/archive/`; ADR-status decisions that demote out of `DECISIONS_ACTIVE.md`; an explicit retirement ritual; archive-don't-delete hard rule; four open design questions with recommended answers.
- Added a sequenced row to [`BACKLOG.md`](../../BACKLOG.md): "Context lifecycle redesign," promote after crib-adoption waves.

## What was verified (and what was NOT)

- **Verified:** every cross-reference in the new docs resolves (bash check of all relative links from each file's actual location — brief, research, backlog row; all OK). Files exist. The research findings were adversarially verified by the harness (25/25 confirmed, 3 votes each).
- **NOT verified (honest):** the proposed structure is untested — it's a *proposal*, nothing migrated. The central premise (how many tokens BACKLOG.md actually costs at session start, and whether its reasoning is already duplicated in DECISIONS/retros) is **unmeasured** — the research itself flagged this as open, and it's the first move when the item is promoted. No `D-NNN` logged because nothing was decided; the brief explicitly defers to a future council-grade decision.

## What I'd change

**For empirical/technical forks, reach for evidence before (or alongside) a reasoning council.** The council confidently produced a plausible-but-wrong fix ("archive below") because it reasoned from priors without knowing how agents actually read files or how practitioners bound context. The deep-research overturned it on facts (Claude Code itself loads only the first 200 lines/25KB at startup; partial reads via offset/limit are real). The council was still useful — it killed the external-tracker and HTML-app options cleanly — but on the *mechanism* question it was the wrong instrument. Lesson: a council answers "which option, given trade-offs"; it does not answer "what is technically true." I also let the council's flawed fix pass into my synthesis; **Rex caught it, not me.** I should have flagged "archive below is still read whole" myself.

## Handoff — gated on Rex / next pickup

- **Gated on Rex:** whether/when to promote the context-lifecycle item; the redesign itself is a `D-NNN` decision (likely council-grade), so it returns as a plan, not a done deal.
- **Single next thing when promoted:** the read-only per-item audit of `BACKLOG.md` against `DECISIONS.md`/retros (actionable line + where the "why" already lives + what'd be orphaned by extraction) — decides whether it's cheap extraction or needs reasoning rehomed first, and gives the before/after token baseline.
- **Left untouched on purpose:** `docs/council/mapping-2026-06-19-adopt.json` (pre-existing orphan from an earlier session's council — not this session's work, not swept in).

---

## Continuation — 08:51 CDT — llm-council hardening + relocation

Same session continued past the first close-out. Directly applied arc 1's lesson ("the council weighs judgment, not fact") by hardening the `llm-council` skill, then fixed its install.

- **Added a fact-gate to `llm-council`** (Rex's own skill): a front-door "Ground the facts before you convene" triage (judgment → convene; fact-dependent → research and fold verified facts into the framing first), pointers in both workflows' Step 1, a chairman/reviewer back-door that flags unverified load-bearing premises, and a note reconciling it with the existing anti-stage-creep guardrail (the gate conditions input, it is not an added stage).
- **Relocated the skill** from the Mac app's managed bundle dir to `~/Sites/skill-llm-council` (git repo, private remote **github.com/rexerr/skill-llm-council**), reinstalled via a `~/.claude/skills/llm-council` symlink like every other ~/Sites skill, and removed the managed copy. **Why it was the odd one out:** it had been uploaded to Cowork, which synced it into the managed bundle (hence the `anthropic-skills:` namespace); Rex deleted that upload.
- **Verified:** the skills reminder now lists it as plain `llm-council` (not `anthropic-skills:`) — install took; fact-gate text loads through the symlink; both repos in sync with their remotes.

**Process notes (tag: none, but two worth logging):**
1. The auto-mode classifier **correctly denied** wiring a global `SessionStart` hook into `~/.claude/settings.json` — that's gated self-modification, and "fix the sync caveat" didn't specifically authorize it. The better fix (install like the other skills) needed no hook anyway. Guardrail worked.
2. **Concurrent-session discovery:** while closing out, found another session actively committing+pushing in this repo — `5b237bd` DSB adopt mode (D-044) + `9ae3bb6` Cowork-ledger sweep landed after my `bd719e1`, and an uncommitted docs-structure brief + BACKLOG row are its live WIP. Left entirely untouched per "never commit working-tree changes you didn't make." Only this retro file was staged in my close-out commit.
