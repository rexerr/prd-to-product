# BACKLOG lifecycle audit — 2026-06-20

**Purpose:** the read-only "before" baseline for the Context-lifecycle rock ([brief](../briefs/context-lifecycle-brief.md)). For every BACKLOG item: what's the *actionable* line, where does the "why" already live, what's orphaned by extracting it, and — Rex's question — **is the prose informative or accreted bloat?**

**Method:** read-only. Nothing changed. `BACKLOG.md` = 75 lines, ~39 items, and the first 35 lines alone exceed the 25K-token read cap.

---

## Headline findings

1. **The premise is confirmed, and the cause is specific.** The dominant token cost is **inline session-changelogs**. Most items accrete a running "DONE 2026-06-08 / shipped 2026-06-12 / landed / superseded" history *inside the hot file* — and that history is already recorded in `DECISIONS.md` and the retros. The agent re-reads it every session and never needs it to *act*.

2. **Are items overly verbose? Yes — but unevenly, and the bar already exists in-file.** The *actionable* content of nearly every item is 1–3 sentences. Everything past that is provenance/history. Proof the right size is achievable: the build-defaults pilot one-liners (lines 26–29), the `stack_summary` row (30), and skill-ecosystem-gaps (31) are already perfectly sized. The offenders are ~8 mega-items running 600–1,200 words each.

3. **~9 items are effectively DONE/DECLINED but still carried at full weight.** This is the clearest waste: shipped or decided work kept as full inline changelogs because **there is no retirement step**. These alone are a large share of the hot-set cost.

4. **The fix is structural *and* editorial.** A `tickets/` folder relocates bloat (good) but a 1,000-word ticket is still 1,000 words when you open it. The real discipline is a **format rule** (index = one line per active item; ticket carries "context to act," not a changelog; point to the retro/decision, never restate) **plus the retirement ritual**. Folders without that rule just move the bloat.

5. **Extraction is cheap, not blocked.** Almost every "why" already lives in a `D-NNN` or a retro. Migration is *extracting one-line entries + pointers*, not rehoming reasoning. One genuine orphan risk noted below.

---

## Disposition table

Buckets: **RETIRE** (decided/shipped — demote to a pointer now) · **EXTRACT** (active but bloated — thin to index line + ticket) · **KEEP-THIN** (already roughly right).

| Item (line) | Words | Actionable line (the index entry) | Why lives in | Orphaned by extraction? | Verbosity | Disposition |
|---|---|---|---|---|---|---|
| plan-review rehost (9) | ~900 | "First live `cc-subagent` run on a real furnace plan; confirm Cowork transcribes its rows." | D-042, D-043, retros 06-18/06-19 | No | Extreme — inline changelog of Plans 1&2 | **EXTRACT** |
| furnace-plan trial (10) | ~1200 | "Grade Cowork catches by bucket; promote to hook only if catches collapse to bucket-3." | trial-ledger.md legend (self-admittedly self-contained), D-018/D-020, retros, council | No — rubric is duplicated *from* the ledger | Extreme — full bucket rubric restated | **EXTRACT** |
| build-defaults item 1 (10) | ~120 | "Promote to Done when a project with a live-URL deliverable exercises the deploy-shell." | retro 06-08, brief | No | OK | KEEP-THIN |
| crib adoption (14) | ~350 | "Wave 2 Sprint 3: `G-14` next, then S4 (DSB `G-19`) + solo `CF-07`." | cribs-adoption-roadmap.md (the real home), D-022–D-045 | No | High — roadmap already holds this | **EXTRACT** |
| Context-lifecycle (15) | ~330 | (this rock — see brief) | brief, council, research | No | High but *active design* | KEEP-THIN |
| OPTIONAL-marker gating (16) | ~230 | "If block-gating confirmed, move universal sentence + logic bullet outside the gate." | inline + generator/decisions.md | Partial — the analysis is the value | Med | KEEP-THIN |
| /repo-miner (17–20) | ~700 | "Build the mining engine as a lightweight playbook the roadmap points to; wire lens A now." | retro 06-17, devils-advocate | No | High — A/B fork resolution restated | **EXTRACT** |
| README symlink bug (21) | ~150 | "Exclude `context-engineering-audit` from the install loop, or add a D-019 caveat." | D-019 | No | OK | KEEP-THIN |
| Brownfield drift audit (22) | ~600 | **DECLINED (D-013).** Resort = fix by hand from the 3 audit docs. | D-013, 3 audit docs | No | Extreme — a *closed* item at full weight | **RETIRE** |
| Chain auto-compose (23) | ~700 | "Escalate to `/idea-to-product` orchestrator (cand. A) only if soft handoffs get dropped." | D-014, retro 06-14 | No — A is the only live residual | Extreme — shipped C/D history inline | **RETIRE** (keep A as thin ticket) |
| Auto-detect input (24) | ~300 | **SHIPPED (D-015).** | D-015, retro 06-14 | No | High — fully-shipped item still here | **RETIRE** |
| Verify DSB triggers (25) | ~120 | "Validate DSB from-scratch path on a real bootstrap-from-nothing project." | retro 06-08 | No | OK | KEEP-THIN |
| build-defaults 5/6/2/3 (26–29) | ~15 ea | (already one-liners) | brief | No | **Ideal — the target size** | KEEP-THIN |
| stack_summary row (30) | ~40 | "Add `other + none` row on 2nd instance." | inline | No | Ideal | KEEP-THIN |
| skill ecosystem gaps (31) | ~50 | "Promote a category only on a real failure." | inline | No | OK | KEEP-THIN |
| red-team sibling (32) | ~450 | "Build `/red-team` (Rung 2) when the prd-creator soft-handoff is observed dropped." | D-016, retro 06-15 | No | High — Rung 1 shipped history inline | **EXTRACT** |
| agent-process upgrades (33) | ~700 | **Groups 1–5 SHIPPED.** Residual: group-5 in-repo dogfood loose end. | retros 06-08, briefs | Low | Extreme — five shipped groups inline | **RETIRE** (keep loose end) |
| skill injection by type (34) | ~350 | "Blocked: design the source-dependent (plugin vs vendored) promotion mechanic first." | inline + seance ref | Med — the blocking analysis | Med-High | KEEP-THIN |
| broader session-start rewrite (35) | ~280 | "Do only if `/session-start` weight becomes a real problem." | brief Appendix A | No | Med | KEEP-THIN |
| no modular example tree (36) | ~280 | "Build `examples/output-modular/` as structural assertions (not byte-diff) when modular work picks up." | council 06-08 | Low | Med | KEEP-THIN |
| invariant/semantic checks (37) | ~320 | "Open: no-jargon-leak + provenance-grounded checks." (write-guard DONE) | D-005, D-006, retro 06-08 | No | High — DONE write-guard restated | **RETIRE** (keep open check) |
| token-adopt for bundles (38) | ~200 | ⚠️ **Partly superseded by D-044** (DSB now *has* adopt mode). Needs reconciliation. | D-008, D-044, retro 06-09 | No | Med — but stale vs D-044 | **RETIRE/reconcile** |
| pressure-test prose (39) | ~450 | "Counter 0/2; run one baseline scenario next time a discipline rule is materially edited (≥3 trials)." | retros 06-11/06-12 | Med — preconditions are load-bearing | High | KEEP-THIN |
| superpowers liftables (40) | ~350 | "Fold (a)-(d) into the next incidental edit of the named file." | handoff brief, retro 06-11 | Low | High — 4 trigger-gated watches | **EXTRACT** (collapse) |
| animations.dev patterns (41) | ~180 | "Fold into next incidental skill-template edit." | animation-taste-reference.md | No | Med | **EXTRACT** (collapse) |
| scaffold-level superpowers (42) | ~400 | "Three artifact upgrades; promote on next substantive c-e template session." | handoff brief | Low | High | **EXTRACT** (collapse) |
| harness-batch liftables (43) | ~350 | "Four trigger-gated candidates (a)-(d)." | retro 06-12 | Low | High | **EXTRACT** (collapse) |
| DSB HTML supplement (44) | ~150 | "Deferred indefinitely (D-012); reopen only on a hand-built one-off preview." | D-012 | No | OK | KEEP-THIN |
| candidate future products (45) | ~80 | "3 product briefs parked; revisit after Taste Builder." | product-briefs/ | No | OK | KEEP-THIN |
| agent-teams guidance (46) | ~150 | "Promote when a scaffolded project needs multi-agent structure." | inline | No | OK | KEEP-THIN |
| harness-proposals review (47) | ~900 | **Mostly DONE/killed.** Residual: kill-watch (a passive watch condition, not a ticket). | retros 06-11/06-12, D-005/D-006, council | Low | Extreme — A/B/E/F/G shipped inline | **RETIRE** |
| plan-review history mining (48) | ~150 | **DONE, superseded** by furnace trial. | retro 06-13, PATTERNS.md | No | Med — closed item | **RETIRE** |
| open decisions prior roadmap (49–52) | ~180 | 2 of 3 **resolved**; live one = on-demand hook scaffolds (Rule-of-Two not met). | D-012, retros | No | Med — resolved sub-bullets carried | **RETIRE** (keep hook line) |
| /decision command (54) | ~350 | "Build when by-hand decision-logging misfires twice (Rule of Two)." | D-021, inline | No | High | KEEP-THIN |
| concurrency/exploration (56) | ~300 | "Not building; reconsider clone-or-branch mode if found wanting twice." | concurrency-mode-brief.md, council 06-18 | No | Med-High | KEEP-THIN |
| docs-structure routing (57) | ~600 | (sibling rock — research done, Rex decision pending) | docs-structure brief, research | No | High but *active design* | KEEP-THIN |

---

## Tally

- **RETIRE now (decided/shipped/declined):** ~9 items — brownfield-drift (22), chain-compose (23), auto-detect (24), agent-process (33), invariant-checks write-guard half (37), token-adopt vs D-044 (38), harness-proposals (47), history-mining (48), resolved prior-roadmap sub-bullets (49–52). These carry ~3,800+ words of shipped history in the always-read file.
- **EXTRACT (active, bloated → index line + ticket):** ~8 items, incl. the two mega-items (plan-review 9, furnace 10) and the four trigger-gated "liftables" watches (40–43) which collapse into **one** "fold into next incidental edit" ticket.
- **KEEP-THIN (already roughly right):** ~16 items — and the build-defaults one-liners are the format template to copy.

**Bottom line on Rex's question:** the items are not *uninformative* — every one has a real actionable core — but a large subset is **wrapped in session-history an AI doesn't need to act**, and ~9 are finished work that should have been demoted. The verbosity is a *missing-retirement-step* symptom more than a writing-style problem. Fix the lifecycle (retirement ritual + one-line-index format rule) and the bloat stops regenerating.

## One genuine orphan risk

Most extractions are safe because the "why" sits in a `D-NNN`/retro. The exception class: items whose reasoning lives **only inline** (e.g. OPTIONAL-marker gating analysis at line 16, the skill-injection blocking-design analysis at 34). Those need their reasoning rehomed *into the ticket file* before the index line is cut — don't reduce them to a pointer that points nowhere.
