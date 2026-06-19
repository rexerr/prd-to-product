# Retro — 2026-06-19 ~12:50 CDT — Plan 2: blind in-session reviewer loop   (2nd session of the day)

Built Plan 2 (the cc-subagent reviewer loop in `furnace-plan`) via `/furnace-plan` itself, as a deliberate two-for-one: the plan authored here was the first real plan run through the freshly-deployed Cowork `/plan-review` — so we smoke-tested the deployed skill *and* reviewed Plan 2 in the same loop. Shipped as [D-043](../DECISIONS.md).

## What was completed

- **Front-end mechanics explained first** (Rex's blindspot question): the reviewer runs *inline* in the furnace session — no popup, no `spawn_task` chip, no copy-paste. Settled that the right shape is exactly what Rex sketched: agent + blind subagent produce a twice-baked plan, which then goes to Cowork. Drew the two loops (courier vs. inline) to make it concrete.
- **Authored Plan 2 with `/furnace-plan`**, ran the preflight + ledger, and presented through Cowork **twice**. Cowork passed it on round 2 with no Must-fixes.
- **Implemented across 6 files:** `furnace-plan/SKILL.md` (new `## The blind review` section, +26 lines), `trial-ledger.md` (last-column `Reviewer`, per-reviewer promotion rubric, miss-rate tally, dated divider, prose rename), `plan-review/SKILL.md` (Reviewer column + transcribe-`## Subagent review log` rule), `DECISIONS.md` (D-043), `DECISIONS_ACTIVE.md` (mirror + line-1 marker bump to D-043), `BACKLOG.md` (Plan 2 → BUILT).
- **Writer-model decision (the binding governance call): option (a) — Cowork stays the sole ledger writer.** cc-subagent is read-only; Cowork transcribes its findings. This **declines** the D-042-flagged D-018 evolution. Rex approved the plan written on this default.
- **Mechanics probed green this session** (not assumed): read-only subagents run in plan mode; they inherit no parent context (blindness); they Read files outside their cwd by absolute path; the symlink-sibling rubric path resolves; the main agent can write the plan-mode plan file (the read-from-disk handoff's foundation).

## Failure this session

- **Tag:** none (for the session) — the furnace+Cowork loop worked exactly as designed: it caught real issues and we fixed them before shipping. But two rev-1 plan misses are worth naming.
- **The artifact:** rev 1 of the plan had two defects Cowork caught — (1) the read-from-disk handoff referenced a plan file that no step wrote (I'd resolved the *subagent's* read-only status but missed that the *main agent* must write the plan file first); (2) inserting a second reviewer silently broke the promotion/kill rubric (Cowork no longer sees raw furnace output, so its post-fix bucket distribution can't be read as the furnace's report card).
- **Tool or agent?** Agent judgment. My furnace preflight Check 3 (probe unverified mechanics) should have flagged "does any step write the plan to disk?" as load-bearing and it didn't — I probed the subagent side and stopped.
- **Does it generalize?** Partially. The lesson: when a design hinges on an artifact existing on disk, trace *who writes it*, not just *who reads it*. Watch for a second instance before landing any guardrail.
- **The good half:** Cowork bucketed both Must-fixes as **bucket-3** (design/judgment), and confirmed the *entire* verification ledger held against the live repo — zero bucket-1/2 fact errors. That's the intended division of labor working: the furnace got every fact right; Cowork caught the design-level confounds. First real Plan-2-era data point, and it's a clean one for the furnace's fact-checking.

## What verification did and did NOT cover

- **Did:** format parity (ledger header vs `plan-review` row format — byte-identical match test green); marker bumped to D-043; D-043 present in all three decision surfaces; blind-review section present; table header+separator both 8 columns; `What this is not` intact after the insert; the four mechanics above probed live.
- **Did NOT:** the **live end-to-end** — a real furnace run that actually spawns the reviewer, emits a `## Subagent review log`, and has Cowork transcribe it into `cc-subagent` rows — **has not run.** This session's furnace pass predates the SKILL change, so it produced no review log. The first true exercise is the next `/furnace-plan` run *after* Rex redeploys the edited `plan-review` ZIP.

## Files changed

- `skills/furnace-plan/SKILL.md`, `skills/furnace-plan/trial-ledger.md`, `skills/plan-review/SKILL.md`, `docs/DECISIONS.md`, `docs/DECISIONS_ACTIVE.md`, `BACKLOG.md` — all uncommitted at retro-write (commit with this retro when Rex says).
- `trial-ledger.md` also carries Cowork's live rows 95–99 (its review of this plan) — swept into the same commit; intertwined with the structural edits, so not separable into the usual dedicated ledger-sweep commit.

## Open items / follow-ups

- **Rex re-uploads the edited `plan-review` ZIP to Cowork** — its row format changed (added `Reviewer` + the transcribe rule). Required before any paired data is captured.
- **First live cc-subagent run** on a real furnace plan — the real end-to-end proof; not yet done.
- **Calibration-pass** use (toggle off → raw output to Cowork) is documented but never exercised.
- **Watch the writer-model decision (a):** if first paired data shows a real need for the cc-subagent to write its own row, reopen the D-018 evolution under option (b) — probe the plan-mode-write mechanic first.

## Next session

- To validate Plan 2: redeploy the `plan-review` ZIP, then run `/furnace-plan` on any real task and watch the loop fire end-to-end.
