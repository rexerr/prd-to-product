# Context-drift audit — `epost-intelligence-feed`

**Date:** 2026-06-13 · **Type:** one-off, read-only, by-hand (brownfield audit pilot, BACKLOG top-of-Backlog)
**Target:** `/Users/rexc/Sites/epost-intelligence-feed` — Next.js app, modular `.claude/rules/` shape, last context activity **2026-05-08** (~5 weeks stale).
**Method:** derived the current `context-engineering` modular-shape standard, inventoried epost's actual context structure, diffed, then **classified each gap by kind** (the diff alone over-reports).

> Pilot's second purpose: decide whether `/audit-context` earns building. The headline finding below (a mechanical diff over-reports ~2×; the value is in the human classification) is the evidence for that call.

---

## Headline

epost is a **well-built earlier-generation** context structure, not a neglected one. It already has the load-bearing pieces: modular `paths:`-scoped rules, AGENTS.md-canonical / `CLAUDE.md`=`@AGENTS.md`, a vocabulary lock, design non-negotiables, multi-agent (Codex) awareness, session-start/end commands, a seeded `permissions.allow`, and a real retro discipline.

What it's missing is the **agent-process / failure-taxonomy layer** that landed in the skill across 06-08 → 06-12 — *and even there, only about a third of the raw "gaps" are genuine, safe, project-agnostic improvements.* The rest are intentional divergences, cosmetic naming, or things that don't apply to a product repo.

**Raw diff: ~11 gaps. After classification: 4 worth backporting, 3 judgment calls, 4 not-drift / N/A.**

---

## Classification (the actual finding)

| # | Gap vs. current standard | Status in epost | Kind | Recommend |
|---|---|---|---|---|
| 1 | Retro convention: timestamped H1 + session-of-day ordinal | older `# Retro — DATE — topic`, no time/ordinal | **A — improvement, evidenced** | **Backport.** epost already has same-day collisions (2× `2026-05-06`, 2× `2026-05-07`) — the exact failure the ordinal fixes. Cheap: edit `retros/README.md` template + going-forward only. |
| 2 | "Where facts live — memory vs. repo" (survives-a-tool-switch) | ABSENT | **A — improvement, high fit** | **Backport.** epost is genuinely multi-agent (Codex reads rules directly) — the survives-a-tool-switch cut applies directly. One section in AGENTS.md. |
| 3 | Autonomy "run to done" charter (scope = outer gate; named gated surfaces) | ABSENT | **A — improvement** | **Backport.** One section in `session-discipline.md`. Reduces unnecessary permission-asking inside an already-scoped task. |
| 4 | `/compact` vs `/clear` + `/rewind` session-management guidance | ABSENT | **A — improvement, cheap** | **Backport.** A few lines in `session-discipline.md`. |
| 5 | Enforcement hooks: `block-env-commit`, `block-deploy-cli`, `block-worktree` | ABSENT (zero hooks; rules are prose-only) | **B — real gap, needs judgment** | **`block-env-commit` worth it** (epost has `.env.local` on disk; secrets are the failure). Others optional — the project's git/deploy rules have held in prose. Medium effort. |
| 6 | "Every rule cites its failure mode" | PARTIAL (strong in design-heuristics; thin in AI/product invariant lists) | **B — quality, not urgent** | **Backfill opportunistically**, not a session. The weak files work; tighten when next editing one. |
| 7 | Council-recommend-at-genuine-forks note | ABSENT | **B — minor for solo product** | Optional. Low value on a single-dev product vs. the meta-skill repo where it originated. |
| 8 | Agent-failure taxonomy as a retro tag (laziness / self-pref / goal-drift) | ABSENT (free-form retros) | **B — adopt only if wanted** | Optional. It's the kill-watch instrument; only worth it if epost wants the same evidence-logging discipline. |
| 9 | Non–Claude-Code-agents-are-read-only rule | ABSENT — and epost does the **opposite** on purpose (Codex writes under `workspace-write`, `on-request` approval) | **C — NOT drift** | **Do not backport.** This is an intentional, opposite policy for this project. A naive diff flags it as a defect; it is a deliberate choice. *This is the headline false-positive.* |
| 10 | Command named `session-end.md` vs current `end-session.md` | divergent name; `session-start.md` reads it fine | **C — cosmetic** | Leave, or trivially rename for cross-project muscle memory. Rex's call; zero functional impact. |
| 11 | Decisions log `decisions-history.md` (no `DECISIONS_ACTIVE.md`) vs `DECISIONS.md` + active mirror | divergent name; no active mirror | **C — naming / conditional** | Low priority. `DECISIONS_ACTIVE` is conditional in the standard anyway; the project works. Rename only if it bothers you. |
| — | Write-guard hook (`write-guard.sh`) | ABSENT | **N/A** | Generator-specific (stops `context-engineering` clobbering hand-authored files). epost isn't a generator. Irrelevant. |

---

## What this says about building `/audit-context`

- The **mechanical half is cheap and already automatable** (derive checklist, diff present/absent) — two subagents produced it in ~100s.
- The **valuable half is the classification** — improvement vs. intentional-divergence vs. cosmetic vs. N/A — and it is irreducibly judgment-heavy and *project-aware*. Item 9 (Codex-writes-on-purpose) would be a confident false-positive for any skill that only diffs a checklist.
- So a bare diff skill would **over-report ~2× and train you to ignore it** — the same trust-erosion the 2026-06-08 council warned about for golden-tree byte-diffs, and the same furnace lesson (the cheap mechanical layer isn't the bottleneck; the judgment is).
- **Implication:** `/audit-context` only earns building if it encodes the *classification* (kinds + project-intent awareness), not just the diff. One pilot isn't enough to design that — Rule of Two says run this again on a 2nd project (qventus / seance) before deciding.

---

## Open decisions (for Rex)

**(a) What to fix in epost.** Recommended minimum: items **1–4** (all Tier A — cheap, safe, going-forward) + **`block-env-commit` hook** from item 5. All are incremental, human-gated, no blind regen (D-005/D-006 class). Everything else: skip or defer.

**(b) Does `/audit-context` earn building?** Recommendation: **not yet** — run the same by-hand pass on one more project first, because the load-bearing classification layer needs ≥2 data points to design well.
