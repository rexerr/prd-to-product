# Retro — 2026-06-12 08:46 CDT — Harness-batch external-source review (9 sources)   (1st session of the day)

## What was completed

- **Reviewed 9 external sources** for relevance to the system: 7 URLs + 2 Reddit posts (the second assessed via its linked artifact, celesteanders/harness). Method: parallel subagent fan-out — 8 general-purpose agents, each grounded in BACKLOG.md + CLAUDE.md, each returning a structured verdict. First live exercise at scale of the F heuristic ("delegate to a subagent when you need the conclusion, not the artifact"): the fetch/summarize noise of 9 sources stayed entirely out of the main context. The openai.com fetch 403'd and was recovered via a Wayback snapshot; all other fetches verified live.
- **Verdicts**, per the established pattern (review → map against BACKLOG/decisions → park with promotion triggers, adopt nothing in-session):

| Source | Verdict |
|---|---|
| arXiv 2603.25723 "Natural-Language Agent Harnesses" | converges-only + 2 refinements (items: pressure-testing, scaffold-level candidates) |
| sidbharath "The Anatomy of Claude Code" | 2 parkable (250-char description cap; `@include` for E) |
| Chachamaru127/claude-code-harness | 3 parkable (exclusion-keyword precedence; unknowns/stop-conditions; verdict schema for red-team) |
| Anthropic "harness design for long-running apps" | 2 parkable, scaffold-level (feature ledger; never-weaken-tests) |
| Anthropic "effective harnesses for long-running agents" | converges on landed A/B/F/G + 2 parkable (stale-assumption tagging; evaluator-tuning seed) |
| OpenAI "Harness engineering" | strongest of the batch — 3 parkable (hook remediation text; `llms.txt` slot; doc-gardening) + the E evidence |
| ghuntley "Ralph" | converges-only + 2 fold-ins (cold-start sufficiency; bounded agent-notes — see Open items) |
| Reddit #1 (5 agents, rules/ vs skills/) | converges-only (rules-vs-skills cut = `rule_shape` + D-011; feeds E) |
| Reddit #2 (celesteanders synthesis + repo) | derivative-only + 1 parkable (acceptance-criteria→evaluator wiring) |

- **All 16 findings landed in BACKLOG** as appends: enrichments to 9 existing entries (chain-orchestration fix-candidate D, hook defect, red-team, session-start rewrite, invariant checks 29b, pressure-testing, superpowers liftables b/c, scaffold-level candidates, harness-proposals E + kill-watch) plus one new entry, "Harness-batch liftables (2026-06-12)," carrying the four orphans (stale-assumption tagging, `llms.txt` slot, doc-gardening, feature ledger + never-weaken-tests). No existing promotion trigger was altered.

## Headline finding

**Item E (slim CLAUDE.md via progressive disclosure) met the promotion-evidence bar:** four *independent* sources converged on it — OpenAI (monolithic AGENTS.md's four named failure modes; ~100-line TOC fix that matches this skill's existing scaffold shape), Reddit #1 (context dilution observed firsthand), Anatomy (`@include` mechanism), Ralph (~147k degradation). E moves from "deliberate pass" to "promotion evidence met, awaiting Rex decision." Secondary: arXiv benchmark data now backs the kill-watch's own premise (process metrics move, outcomes don't — "locally convincing while still drifting from the acceptance object"), and claude-code-harness is a third independent source for the claim→evidence verification gate.

## Methodology notes

- **Derivative-source independence rule:** Reddit #2 synthesized the exact four primaries reviewed directly, so it was excluded from convergence counts — downstream syntheses don't count; only primaries do. Logged because the convergence-as-promotion-evidence pattern depends on it.
- **Calibration on self-reported harnesses:** celesteanders/harness advertised "strict append-only rules" (prompt-only in the artifact) and a lint hook (absent from the artifact entirely). Reddit self-reports overstate mechanical enforcement; check the repo, not the post.

## Failure this session

- **lost context (near-miss, caught by Rex's review, not by me).** My interim consolidated summary silently dropped 4 of 16 findings (exclusion-keyword precedence, feature ledger, never-weaken-tests, bounded agent-notes) and 2 more never made either consolidated list (arXiv six-component checklist, doc-gardening). Rex's "did you include all of this?" forced the coverage audit that restored them before anything landed. Mechanism: two partial consolidations across turns, each treated as authoritative. Lesson: when findings accumulate across turns, reconcile against the union before presenting a "complete" list — a checklist diff, not memory.

## Files changed

- `BACKLOG.md` — 9 entry enrichments + 1 new entry (all additive; no triggers rewritten).
- `docs/retros/2026-06-12-harness-batch-review.md` — this retro.

## Key decisions made

- **Nothing adopted in-session** — every finding parked with a promotion trigger, per the harvest-don't-install constraint. No D-NNN: no binding decision was made; E's promotion remains Rex's call (and possibly a council's, per the memo's Part 5).

## Open items

- **E decision is now squarely Rex-gated** with the evidence bar met — the one item this batch materially moved.
- Ralph's *bounded agent-notes* fold-in (a scaffolded agent-appendable notes file under the where-facts-live cut) was judged thin enough to live inside the cold-start/D enrichment context rather than its own line; resurrect if a scaffolded project's retro shows the same build quirk re-discovered in ≥2 sessions.
- Standing gated items unchanged: plan-review mining run (Workflow opt-in), the two `.claude/` self-edits, `block-deploy-cli.sh`/`block-worktree.sh` stdin fixes (now with the remediation-text enrichment attached).

## Next session

- The convergence-as-promotion pattern has now cleared three items across three batches (motion layer, council bundle, and E's evidence bar). If Rex picks up E, start from the OpenAI failure-mode list as the "failure it prevents" citations and the word-count budgets in the liftables item as the measurable bar; decide council-vs-devils-advocate per the D-009 calibration (reversible prose → DA first).
