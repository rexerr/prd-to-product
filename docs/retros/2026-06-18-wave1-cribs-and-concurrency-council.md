# Retro — 2026-06-18 09:21 CDT — Wave-1 cribs (C-14/C-10/CF-04) + global identity block + concurrency council (pinned)   (4th session of the day)

## Context

Started on Wave-1 crib adoption to grow the decisions ledger; mid-session Rex raised a global preferences question and then a real workflow constraint (concurrency on UI projects) that consumed the back half via a full LLM Council + devils-advocate pass. Ran concurrently with the 3rd session (MCP audit / AB-tracker) — the shared `cribs-adoption-roadmap.md` was the live collision risk.

## Done

- **Global `~/.claude/CLAUDE.md` identity block** — designer-not-engineer (explain implementation in plain language), always-recommend-a-path, frame-decisions-in-outcome-terms. Rex-authorized self-modification of agent config.
- **Three Wave-1 cribs adopted** via the [D-022](../DECISIONS.md) lifecycle: `C-14`→[D-025](../DECISIONS.md) (failure-mode doctrine now names the dated/quoted run + delete-signal), `C-10`→[D-026](../DECISIONS.md) (freshness/sync marker on `DECISIONS_ACTIVE.md`), `CF-04`→[D-027](../DECISIONS.md) (concept-keyed declined/parked discipline, stated once + referenced per CF-06).
- **Concurrency for UI projects — analysed, pinned, not built.** Full council ([`council-report-2026-06-18-concurrency-mode.html`](council/council-report-2026-06-18-concurrency-mode.html)) → premise correction by Rex → rev-2 brief → devils-advocate (verdict *reconsider*). Outcome + revisit trigger in [`docs/concurrency-mode-brief.md`](../concurrency-mode-brief.md) and the BACKLOG pin.

## Verified

- **C-14/C-10/CF-04 (all class D):** re-read each edit; grepped that doctrine/marker/section landed; confirmed status cells flipped (`Adopted (→ D-0NN)`) and cross-references resolve; no golden-tree diff needed (none of the three is emitted into `examples/output-small/`).
- **C-10 dogfooded:** logging D-027 bumped the `DECISIONS_ACTIVE.md` marker D-026 → D-027 — the marker's first live exercise, confirmed in-file.
- **Concurrent-session reconciliation (the load-bearing check):** `git status`/`git log` showed **HEAD == origin/main (0/0)** — the 3rd session had already pushed, dissolving the earlier push-coupling concern. Verified my roadmap markers (C-14/C-10/CF-04) **and** both tracker counts survived the other session's commits of the shared roadmap — no clobber, no drift. Transient inconsistency (committed roadmap cites D-025/26/27 before my DECISIONS.md commit lands them) resolves on this session's commit.
- **Council/DA artifacts:** `build_report.py` ran clean → HTML written and opened; transcript + mapping saved.
- **NOT verified:** the concurrency design itself — it is deliberately unbuilt, so there is no code to test; the DA is reasoning, not a red test.

## Failure this session

- **Tag: not a clean fit for the four — a premise-framing miss (closest: bad substitution, i.e. substituting an *assumed* bottleneck for the real one).**

**Name the artifact (per C-14, adopted this session):** the rev-1 concurrency brief asserted the bottleneck as a vague "throughput desire" and led with the file-collision near-miss. That framing steered a full five-advisor council to optimize against the **wrong** objective — "you're bottlenecked on serial review attention, so parallelism won't help." Rex corrected the premise *after* the council ran: *"my bottleneck is speed. i have to wait for each task to be done. i cant do concurrent work or explore options safely."* The council's own peer round had even flagged the gap ("nobody costed the throughput claim — there's no blocked-work queue").

- **Tool or agent?** Agent — my framing of the brief.
- **Does it generalize?** Yes — any costly decision artifact (council/DA) built on an unverified load-bearing premise.
- **→ The change it demands:** before spending a council or DA on a decision brief, verify the *single load-bearing premise* with one cheap question to the operator rather than asserting it. **No new guardrail** — this is operator discipline, and the tag-log ethos says don't accrete a rule on one occurrence; logged here so a second instance is visible. (Mitigating note: the multi-perspective process *did* surface the flaw — the council's peer round and then Rex's correction caught it before any build, which is the system working.)

## Files changed

Reference, don't restate (per CF-06) — see the commit diff. Spans: global CLAUDE.md (outside repo); `DECISIONS.md` (D-025/26/27), `DECISIONS_ACTIVE.md` marker, `principles.md`, `docs/retros/README.md`, the two crib trackers, `BACKLOG.md` pin, new `docs/concurrency-mode-brief.md` + `docs/council/*` (report/transcript/data/mapping).

## Open items / handoff

- **Gated on Rex:** the push (not explicitly requested this session — committed locally, awaiting go).
- **Concurrency:** pinned, not building. Revisit trigger = clone-or-branch exploration tried on a real project and found wanting **twice**. Latency practices (background agents / second project / disjoint-file same-tree) are free to adopt anytime.
- **Next Wave-1:** `C-15` and `CF-02` remain — both class **(T)** (edit emitted templates → require dry-run substitution + golden-tree diff against `examples/output-small/`), so each is its own focused pass. `DG-02` still blocked on the "is RTL in DSB scope?" question.

## Next session

- Pick up either the latency practices (free, if the wait pain bites) or the next Wave-1 **(T)** crib `C-15` with the dry-run-diff discipline. Open with `/session-start`.
