# Retro — 2026-06-18 12:24 CDT — Wave-2 Sprint 3, Pass 1: retro-template backport (8th session of the day)

## What was completed

Backported three already-ratified retro conventions into the template `context-engineering` **emits** (they had landed only on this repo's own `docs/retros/README.md` via [D-024](../DECISIONS.md)/[D-025](../DECISIONS.md)). Authored through `/furnace-plan`, Cowork-reviewed across two rounds before any edit. See [D-039](../DECISIONS.md) for the per-crib detail and the generalized-tag rationale — not restated here.

- **CF-06** → 4th Discipline bullet ("Reference, don't restate"). **C-14** → "Name the artifact" in a new `## Failure this session` section. **C-09** → the tool-or-agent / generalize / →change sub-bullets in that section. CF-06's suggested-skills atom → the Next-session line.
- Landed identically on the emitted template and the `output-small` fixture; **failure-tag set generalized** to drop this repo's CE-internal `bad substitution` (Rex's sign-off pick A; Cowork-endorsed).
- C-09/CF-06/C-14 status cells gained `; scaffold-emit backport → D-039`; roadmap marker + BACKLOG row updated; the "small carried debt" note dropped.

## Failure this session

- **Tag:** none (product) — the session shipped clean; the dominant event was a furnace/Cowork **bucket-1 must-fix caught pre-edit**, which is the trial working, not a product failure.
- **Name the artifact.** The plan's verification ledger asserted the check was `diff <(tail -n +7 …template) …fixture`, "empty = GREEN." Cowork re-ran it: `tail -n +7` prints `1d0 <` (a spurious blank) **even on the clean tree**, because template line 7 is blank between `-->` (line 6) and `# Session retros` (line 8). The correct command is `tail -n +8`. I had written the command without running it.
- Lesson→change jump:
  - **Tool or agent?** Agent — the furnace preflight Check 2 ("make every verification step able to fail *and* reach what it tests") technically passed because a diff *is* red-capable, but I never executed it to confirm the offset.
  - **Does it generalize?** This is the **third** adjacent "read-happened ≠ inference-correct" data point (Sprint-1 granularity, Sprint-2 load-site/fixture inference, now this off-by-one). The prior two retros set the trigger: *watch for a third before sharpening Check 1.* It has now landed. But note the sub-type differs — this one is "didn't run the command I wrote," nearer CF-03's string/equality miss than the earlier inference misses. Not a clean single sub-type at n=3.
  - **→ The change it demands:** Candidate — add to furnace Check 2 an explicit "run the verify command against the current tree once while authoring; paste its real output (not its intended output) into the ledger." Hold at **propose**, not adopt: it's one occurrence of this exact sub-type. Logged for the next furnace-trial review to weigh against the scorecard.

- **Commit-hygiene lesson from last session APPLIED.** Cowork appended 3 rows to `skills/furnace-plan/trial-ledger.md` this session. Last session that append got swept into a product commit; this session it gets its **own dedicated** "Sweep Cowork ledger append" commit *first*, before any product `git add` — the D-018 carve-out honored.

## Files changed

Two product files (emitted retro template + `output-small` fixture) + five bookkeeping files (DECISIONS, two crib trackers, roadmap marker, BACKLOG) + this retro. Exact paths in `git status` / the [plan](../../.claude/plans/lucky-exploring-seal.md); not enumerated here (CF-06).

## Key decisions made

- [D-039](../DECISIONS.md) — the backport + the generic failure-tag set + the deliberate single-source choice (session-discipline templates untouched). Not mirrored to `DECISIONS_ACTIVE.md` (template content, visible by reading; Sprint-2 skip precedent).

## Open items

- **Wave 2 continues.** S3 remaining: DG-01 + CF-13 + G-14\* + AB-03; then S4 DSB (G-19), solo CF-07. Sequencing in [BACKLOG](../../BACKLOG.md) + the [roadmap](../cribs-adoption-roadmap.md).
- **Furnace Check-2 candidate** (run-the-command-while-authoring) logged above at *propose* — for the next trial review, not adopted now.
- **No push this session** — commits staged locally per the plan; push when asked.

## Next session

- Continue S3 — next tightest is **G-14\*** (provenance banner on emitted files + `output-small`) or **DG-01** (even-coverage `.claude/rules` scaffold); both single-surface class-T. Open with `/furnace-plan` (multi-artifact surface warrants it).
