# PATTERNS.md — Plan-review history mining

**What this is:** the evidence deliverable promised by [`HANDOFF.md`](HANDOFF.md). A round-based extraction over every plan-bearing Claude Code session in Rex's history, answering the question the [self-healing-loop council](../../docs/council/council-report-2026-06-09-self-healing-loop.html) demanded before anything gets built: **how often do Rex's plans get sent back for revision, and why?**

**Run:** 2026-06-12. 83 sessions (58 with an `ExitPlanMode` plan, 25 interrupt-only). 139 agents — one extractor per session, one adversarial verifier per session with claimed revisions, one synthesis. Every claimed revision was re-checked by a skeptic prompted to *refute* it; refuted rounds were reclassified before tallying. Raw evidence staged alongside this file: [`revise-rounds.json`](revise-rounds.json), [`per-session.json`](per-session.json), [`stats-and-audit.json`](stats-and-audit.json), [`synthesis-raw.md`](synthesis-raw.md).

**Scope note:** This documents Rex's *manual* plan-review habit — pasting reviews from ad-hoc other-Claude conversations, councils, and his own reads into the revise box. It is **not** a record of the Cowork `plan-review` skill (that skill is new and has never run on these projects). Per Rex's call, the skill is out of scope here; this is its potential seed evidence, nothing more.

---

## 0. Method correction (read first — it inverts a HANDOFF rule)

[`HANDOFF.md`](HANDOFF.md) §2 finding #2 said: *collapse back-to-back plan presentations with no human turn between them into one — the model is just re-editing its own plan doc.* **That rule is backwards and would corrupt any future run.**

The extractors, reading raw `.jsonl` instead of trusting the `rounds.py` digest, found that most "back-to-back" plans are **not** self-edits. They are **rejections whose feedback lives inside the `ExitPlanMode` rejection `tool_result`** — a channel the digest's human-turn scan cannot see. When Rex rejects a plan through the plan-mode UI (often pasting an external review), the next plan presentation *looks* back-to-back with "no human turn between," but a genuine review round happened in between, invisible to the text scan.

Consequence: the old collapse heuristic would have reduced, e.g., epost-intelligence-feed's 8 reviewed presentations to 2. The deterministic `interrupts` pre-count also misses these (rejections aren't interrupts). **The rejection-`tool_result` channel is systematically under-captured by the digest, so every revision count below is a floor, not a point estimate.** Future runs must parse `tool_result` rejection bodies, not rely on `rounds.py`'s `[REX]` lines.

---

## 1. Rounds-to-acceptance (both denominators)

178 plan-review rounds across 177 plan presentations, post-verification:

| Closing | Count | Share |
|---|---|---|
| approve (first-pass) | 73 | 41% |
| revise | 93 | 52% |
| interrupt (treated as revise) | 9 | 5% |
| abandoned / unclear | 3 | 2% |

**102 of 178 rounds (57%) drew a revision.** Roughly 3 of every 5 plans did not survive first read intact — a floor, given §0.

Per-session distribution (83 sessions):

| Revisions in session | Sessions | Share |
|---|---|---|
| 0 | 32 | 39% |
| 1 | 20 | 24% |
| 2 | 17 | 20% |
| 3+ | 14 | 17% |

61% of sessions carry ≥1 revision; a 17% fat tail needed 3+ rounds, concentrated in the highest-stakes work (the-council storage/abort, seance rebuild, epost-intelligence-feed restructure).

### The denominator that actually matters (recommended target)

Headlining "57% fail" overstates the problem, because **not every revision is a defect to engineer away.** Splitting the 102 by kind:

- **Preventable epistemics (~40–50 rounds): the real furnace target.** Themes T1, T2, T6 below — the plan asserted something a grep, a probe, or a re-read would have settled. Pure round-trip waste.
- **Healthy human-in-loop friction (~17 rounds): leave alone.** Themes T3, T5 — unsurfaced judgment calls and un-elicited intent. Rex *should* be the one deciding scoring direction or "recipe first, I'm almost at billable hours." A furnace should *surface these faster*, not suppress them.
- **Hygiene / propagation (~remainder): T4, T7, T8, T9** — mixed; some preventable, some inherent to iterative planning.

**Recommendation:** report the full 102 for completeness; aim the intervention at the ~40–50 preventable-epistemics subset. That is the honest, actionable number.

---

## 2. Ranked recurring revision themes (furnace draft)

Counts approximate; some rounds carry two themes; near-duplicates exist (see §6). **[P]** = preventable-epistemics (target). **[H]** = healthy friction (leave).

**T1 [P] — Verification that can't prove what it claims (~20).** seance, the-council, qventus, prd-to-product, epost-assessment. Verify steps that pass green with zero tests run, can't reach the path they name, test only the happy path, or assert an outcome instead of measuring it.
> *"The live 'abort path' test doesn't test the abort path — same sin as last time. A bad key is an auth failure that rejects instantly; it never arms [the timeout]."* (the-council)

**T2 [P] — Plan asserts codebase/doc facts it never read (~14).** epost-intelligence-feed (+wt2), the-council, prd-to-product, qventus. Wrong counts, "missing" things that exist, "pure pointer" files with real content, "no files modified" framings contradicted by the code.
> *"Step 7 — replacing AGENTS.md with @CLAUDE.md loses content. AGENTS.md isn't a pure pointer today."* (epost-intelligence-feed)

**T3 [H] — Unsurfaced judgment calls and safety-model shifts (~10).** epost-assessment, prd-to-product, seance, qventus. The plan quietly embeds a policy/tradeoff/risk decision instead of presenting it for sign-off.
> *"Confirm the scoring direction for pure-marketplace sellers. This is the one substantive judgment call."* (epost-assessment)

**T4 — Plan contradicts recorded decisions or earlier-session agreements (~10).** seance, the-council, qventus. D-022 actor isolation ignored, D-020/D-017 conflicts missed, a phantom file in a path rule after D-024, an agreed housekeeping section silently dropped.
> *"that is not the full plan. where is the bit about housekeeping? are you documenting all of this?"* (qventus)

**T5 [H] — Intent and priorities not elicited before planning (~7).** qventus, seance, the-council. The plan optimizes the stated task, not Rex's actual goal.
> *"2. i dont agree. recipe first. im almost at hours and i could sell the additional work."* (qventus)

**T6 [P] — Unverified platform/tool mechanics on the critical path (~6).** prd-to-product, epost-intelligence-feed, the-council, epost-assessment. The design rests on a mechanism never probed.
> *"Headline: ask hangs in headless mode — so it deadlocks the very orchestrator it's meant to unblock."* (prd-to-product)

**T7 — Revision not propagated through the whole plan (~5).** A fix lands in one section; stale lines and un-recomputed numbers contradict it elsewhere.
> *"Verification gate #2 still reads: 'expect P-05; confirm others hold'. That contradicts §4."* (epost-assessment)

**T8 — Scope bundling that defeats the gate (~5).** Over-scoped sessions that invalidate the characterization-test gate's "only the container changed" promise; missing line estimates against the 300-line cap.
> *"Session B is over-scoped in a way that quietly defeats the D-021 gate."* (seance)

**T9 — Over-engineering vs a simpler alternative (~5).** JS content model where a CSS gate suffices; token-auth where a plain route suffices; speculative single-use abstractions.
> *"do NOT build the SPECIALTIES JS model / renderSpecialty / QVSpecialty bridge. Use a much lighter mechanism."* (qventus)

**Long tail (~10, not force-fit):** prompt-copy persona/tone calibration, doc-phrasing ambiguity, padded heuristic lists, unspecified flip-reset behavior, fidelity-tier calls.

---

## 3. Where the fix lives

`planning-prompt 64 · context-file 11 · claude-md 11 · decisions 5 · skill 4 · code 2 · none/unclear 5` (of 102).

**63% of revisions would have been prevented by a better standing instruction applied at plan time** — not by new repo rules. CLAUDE.md already carries the scope caps and read-before-write rules; what fails is the plan's *epistemics* (unverified claims, unprovable verification, unsurfaced tradeoffs), which is checklist territory. The 11 context-file + 5 decisions fixes are project-specific facts (persona constraints, D-numbers) that belong in each repo's docs. The 4 skill hits confirm the skill *content* is rarely the failure point. **Conclusion: a plan-time furnace prompt is the highest-leverage single intervention; promote only survivors into CLAUDE.md.**

---

## 4. Promotable rules (from the 32 promotable=yes rounds)

Each cites the rounds that justify it. The first four map directly onto the preventable-epistemics target.

**R1 — No load-bearing factual claim about the codebase without a citation you actually ran.** Every count, "X is missing," "no files modified," "these mirror each other" must be backed by a read/grep performed this session. *Prevents:* plans built on imagined repo state. *(epost-intelligence-feed: "AGENTS.md isn't a pure pointer today"; prd-to-product: "you're missing generator/output-summary.md"; the-council: "breaks the plan's '3 files, none modified' framing".)*

**R2 — Every verification step must be able to fail, and must reach the path it claims to test.** State the failure that would make each check red; include the unchanged/default path and the failure path, not just the happy path; measure claimed wins, don't assert them. *Prevents:* vacuous green checkmarks. *(the-council: "may run zero tests and report green"; seance: "Measure the perf win, don't assert it".)*

**R3 — Probe unverified platform mechanics before step 1, not at the end.** If the design rests on a tool/SDK/platform behavior you haven't empirically confirmed, the probe is the first step and its result can fork the plan. *Prevents:* whole architectures built on a mechanism that doesn't behave as documented. *(prd-to-product: "ask hangs in headless mode"; epost-intelligence-feed: "verify paths: empirically before step 1, not at step 8".)*

**R4 — Diff the plan against recorded decisions and this session's agreements before presenting.** Name every D-NNN the plan touches, flag any reversal as an explicit sign-off item, confirm nothing agreed earlier was dropped. *Prevents:* silently overturning binding decisions and losing in-flight agreements. *(seance: D-022 concurrency; qventus: "where is the bit about housekeeping?"; the-council: "re-commits the exact import-crash the last two splits exist to avoid".)*

**R5 — After any plan revision, sweep the whole document for stale references and derived numbers.** A revision isn't done until every dependent section is updated and every computed target recomputed. *Prevents:* shipping the inconsistency the revision was meant to fix. *(epost-intelligence-feed: "token target math doesn't reflect step 0"; qventus: "Stage B row still says … That's stale naming".)*

**R6 — State per-stage line estimates against the session cap; never bundle changes that defeat your own test gate.** *Prevents:* scope creep that invalidates the safety mechanism protecting the change. *(seance: "defeats the D-021 gate"; the-council: "bundled separable work into one over-cap session".)*

**R7 — When a reviewer flags a risk, the plan absorbs it as a check — don't make the reviewer ask twice.** *Prevents:* watch-items evaporating between review and execution. *(epost-assessment: "do you need to add any checks for that?" — asked twice.)*

---

## 5. Taxonomy fit

The 8-tag taxonomy held better than the 6-sample suggested: only 19/102 (19%) fell to `other`. But it's top-heavy in a telling way — `unstated-assumption` (31) and `weak-acceptance-criteria` (24) absorb 54% of rounds, functioning as coarse buckets, not precise diagnoses. Each wants a split: `unstated-assumption` conflates "unverified codebase/platform fact" (a grep) with "unsurfaced judgment call needing sign-off" (a sign-off item) — different fixes. `weak-acceptance-criteria` conflates "verification structurally can't fail" with "a flagged risk got no check." Meanwhile the execution-era retro tags barely fired at plan time — `bad-substitution` (1), `goal-drift` (2), `scope-creep` (3) — confirming **plan-review failures are a different species from build failures; the retro taxonomy was imported, not derived, for this use.**

---

## 6. Honest caveats

- **Revision counts are a floor, not a point estimate.** The rejection-`tool_result` channel (§0) is systematically under-captured; 3 missed revisions were already spot-found. The true revise rate is ≥57%.
- **Refutation rate ~9%.** The verifier refuted 10 of 112 initially-claimed revisions. If the classifier's base over-claim rate is ~9%, a few residual false positives likely survive the 102 confirmed. Treat counts as ±5.
- **Near-duplicate rounds inflate theme counts.** Several entries share identical verbatims across two rounds; some are genuine re-litigations, some may be the same feedback double-counted across worktree/session boundaries (note epost-intelligence-feed vs -wt2). T1 and T3 are most exposed.
- **Not all reviews are Rex's own read.** Many revise rounds are Rex pasting external reviews (other Claude conversations, councils). The themes measure *what survives to be caught at review* — a blend of Rex's catch profile and external reviewers'. The promotable rules remain valid as descriptions of plan defects, but "Rex's review style" would overstate a single source.
- **Promotability is mostly "maybe."** 32/102 confidently promotable; 60 "maybe." §2 is a hypothesis list to burn down against the next batch, not a settled rulebook — consistent with this repo's "earn a guardrail with evidence, not instinct" philosophy.
- **N=1 human, single workflow.** Nothing here generalizes beyond Rex's projects without re-validation.

---

## 7. The decision this unlocks (for the council)

The evidence the [self-healing-loop council](../../docs/council/council-report-2026-06-09-self-healing-loop.html) required now exists: the count is real (≥57%), and the dominant failure is a single preventable class — **plans asserting what they never verified** (~40–50 of 102 rounds, T1+T2+T6). The fix overwhelmingly lives at plan-authoring time (63% planning-prompt). The open fork — costly to get wrong, hard to reverse, i.e. [D-009](../../docs/DECISIONS.md) council territory:

**Build the plan-time furnace prompt now (seeded with R1–R4), or run one more validation batch to confirm the patterns hold before building?**

The data supports either. That's exactly the kind of plausible-but-wrong-first-instinct fork a council exists to stress-test.
