# Retro — 2026-06-16 10:21 CDT — furnace trial ledger built + Cowork wired to write it   (1st session of the day)

Session-start oriented on the 2026-06-15 red-team Rung 1 retro; Rex asked to explore the red-teaming and understand how it works. That walkthrough surfaced a real gap — the furnace trial's bucket data was scattered across retros and never tallied — and the session turned into building a centralized scorecard. All mechanism changes landed *outside* this repo (the ledger in `~/.claude/`, the Cowork skill in app-support); the in-repo deliverable is this retro + the BACKLOG update, which per "where facts live" is the only durable cross-tool record of a mechanism that isn't under version control.

## What was completed

- **Furnace trial ledger created** at `~/.claude/skills/furnace-plan/trial-ledger.md` — legend (bucket definitions + promotion/kill/tighten triggers, self-contained as an audit rubric) + a 7-column table, with 8 rows backfilled from the 06-14 and 06-15 retros. Schema: `Date(timestamp) | Project | Plan | Round | Bucket | Severity | What Cowork caught`.
- **Cowork's `/plan-review` skill edited** to append to the ledger — one row per finding per round, mapping its own Must-fix→`must-fix` / Should-consider→`refinement` severity groups, classifying each into bucket 1/2/3, gated on the plan having arrived with a `## Verification ledger`. A second edit silenced the "nothing to log" footer on non-furnace plans so reviews stay clean.
- **Design resolved through discussion, not assumed:** writer = Cowork (not Claude Code), because (a) Claude Code is in plan mode at authoring time and (b) — the sharper reason — bucketing-at-retro was the *creator grading its own misses*, the exact self-grading the furnace exists to avoid; Cowork is the distinct verifier and has the ledger + its own catches, so it's better-placed. Ledger is **global** (captures every project Cowork reviews; this repo's plans aren't representative). **Outcome column dropped** (bucket distribution is the signal; outcome would've created a cross-project retro gap). **Severity is its own column** — the 06-15 over-broad-trigger was a bucket-3 *must-fix*, proving bucket≠severity and refining the promotion read ("mostly bucket-3 *must-fixes*" argues against the hook).
- **Two "don't build" calls held:** no audit skill (the ledger legend is self-describing — point any Claude at the file; Rule of Two); no Cowork project-instruction update (the carve-out belongs at the skill layer, which is global and scales; the project rule is correctly scoped to project files and doesn't conflict — punching a hole in "never edit files" per-project would erode it and not scale).

## What was verified — and what was not

- **Skip path: live-verified.** Rex ran a real `/plan-review` pass on the seance project; Cowork emitted "No furnace `## Verification ledger` was attached … nothing to log." This concretely confirms three things at once: the edited skill is *loaded* (so the app-support path is canonical and my edit persisted — the "regenerated from a bundle" worry is dead), the `## Verification ledger` gate works, and Cowork did **not** over-refuse on its own "never edit files" rule.
- **Footer-silence edit: not yet observed.** Made after the live run; next non-furnace review will confirm the footer is gone.
- **Positive path: NOT verified.** No furnace plan with a verification ledger has gone through Cowork yet, so no row has actually been *written* by the skill (the 8 rows were hand-backfilled by me, not produced by the mechanism). This is the real end-to-end test and it fires on the next `/furnace-plan` → Cowork run.

## Failure this session

- **Tag: none.** No bad substitution, scope creep, lost context, or goal drift. One honest process note: I initially drafted the Cowork change as copy-paste-for-Rex prose before Rex pointed out I could edit the skill directly — I'd assumed the skill was un-editable app config without checking. Verifying the on-disk location first (single stable copy, Rex's 06-13 edit persisted in it) is what made the direct edit safe. Caught and corrected within the session; no artifact cost.

## Files changed

- `BACKLOG.md` — furnace In-progress entry records the centralized ledger, writer, schema, dropped-outcome / severity rationale, and verification state (modified)
- `docs/retros/2026-06-16-furnace-trial-ledger.md` — this retro (new)
- *(outside the repo, not committed:)* `~/.claude/skills/furnace-plan/trial-ledger.md` (new); Cowork `/plan-review` `SKILL.md` (modified, ×2)

## Key decisions made

- No `D-NNN` written. The furnace trial is a BACKLOG In-progress experiment, not a binding decision (precedent: the 06-13 trial resolution was recorded in retro + PATTERNS.md, not DECISIONS). The ledger is an implementation of that trial; its mechanics live in BACKLOG + this retro. Promote to a `D-NNN` only if the trial concludes (hook promotion or kill) — that conclusion *would* be a binding decision.

## Open items / handoff

- **Gated on Rex:** nothing new. Carried-over gates unchanged — Fix-candidate C (repo rename), and the furnace hook-promotion question (still gated on the content proving out).
- **Next thing to pick up:** the conversation Rex queued but we didn't open — **(3) extending the create → distinct-check → record loop to actual code** (the Addy Osmani creator-vs-checker pattern, beyond planning). Start there next session.
- **Watch:** first real `/furnace-plan` → Cowork run, to confirm the positive write path produces a correct row.

## Next session

- Open topic (3). And if a furnace plan runs through Cowork, eyeball the new ledger row before trusting the mechanism end-to-end.
