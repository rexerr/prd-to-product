# Plan-Review Mining: Synthesis Report

83 sessions, 178 classified plan-review rounds, post-adversarial-verification.

---

## 1. Headline numbers

**First-pass acceptance is a minority outcome.** Of 178 rounds, 73 (41%) were approved on first review. 102 (57%) drew a revision or interrupt (93 revise + 9 interrupt); 2 abandoned, 1 unclear. Roughly **3 of every 5 plans presented did not survive Rex's first read intact.**

**Per-session distribution** (83 sessions):

| Revisions in session | Sessions | Share |
|---|---|---|
| 0 | 32 | 39% |
| 1 | 20 | 24% |
| 2 | 17 | 20% |
| 3+ | 14 | 17% |

So 61% of sessions contain at least one plan revision, and a fat tail (17%) needed three or more rounds — multi-round grinding is concentrated in a minority of sessions (notably the-council storage/abort work, seance rebuild, epost-intelligence-feed restructure), which are also the highest-stakes ones.

---

## 2. Ranked recurring revision themes (furnace draft)

Counts are approximate; some rounds carry two themes and a few near-duplicate rounds exist (see §6).

**T1. Verification that can't prove what it claims (~20 rounds)** — seance, the-council, qventus-prototyper, prd-to-product, epost-assessment. The plan's verify step is vacuous (green with zero tests run), structurally cannot reach the code path it claims to exercise, tests only the happy/changed path, or asserts an outcome instead of measuring it.
> "The live 'abort path' test doesn't test the abort path — same sin as last time. ... A bad key is an auth failure that rejects instantly; it never arms [the timeout]" (the-council)
> "The test script may run zero tests and report green — the exact false-pass this whole plan exists to kill." (the-council)

**T2. Plan asserts codebase/doc facts it never read (~14 rounds)** — epost-intelligence-feed (+wt2), the-council, prd-to-product, qventus-prototyper. Wrong counts, claimed-missing things that exist, claimed-pointer files with real content, "no files modified" framings contradicted by the token system, missed root-cause and mirror files.
> "Step 7 — replacing AGENTS.md with @CLAUDE.md loses content. AGENTS.md isn't a pure pointer today." (epost-intelligence-feed)
> "the plan asserts they mirror each other but I never saw you confirm the ortho wording, so just pin it." (qventus-prototyper)

**T3. Unsurfaced judgment calls and safety-model shifts (~10 rounds)** — epost-assessment, prd-to-product, seance, qventus-prototyper. The plan quietly embeds a policy decision, tradeoff, or risk posture change instead of presenting it as a sign-off item: scoring direction, sacrificing swipe-back, a merge path that now edits hand-authored files, a consent mechanism the agent can write itself.
> "Confirm the scoring direction for pure-marketplace sellers. This is the one substantive judgment call" (epost-assessment)
> "The consent ledger is agent-writable — so this enforces deliberateness, not consent" (prd-to-product)

**T4. Plan contradicts recorded decisions or earlier-session agreements (~10 rounds)** — seance, the-council, qventus-prototyper. Lost-context proper: D-022 actor isolation ignored, D-020/D-017 conflicts missed, a phantom file left in a path rule after D-024, the agreed housekeeping section silently dropped, an exporter resurrected from stale memory notes.
> "that is not the full plan. where is the bit about housekeeping? are you documenting all of this?" (qventus-prototyper)
> "i dont want to work on an exporter. i want an app the opens html files. thats it." (seance)

**T5. Intent and priorities not elicited before planning (~7 rounds)** — qventus-prototyper, seance, the-council. The plan optimizes the stated task, not Rex's actual goal: wrong fidelity bar (clinical vs demo-believable), wrong ordering vs billing reality, designing eight directions before asking for his references, bolting on a reference design he wanted adopted structurally, hardening tokens before the design was validated.
> "2. i dont agree. recipe first. im almost at hours and i could sell the additional work" (qventus-prototyper)
> "before we do that. show me a mockup html file. i want to nail the design before we move into writing the design system" (the-council)

**T6. Unverified platform/tool mechanics on the critical path (~6 rounds)** — prd-to-product, epost-intelligence-feed, the-council, epost-assessment. The design rests on a mechanism never probed: `permissionDecision: ask` deadlocks headless, `paths:` frontmatter checked only at step 8, the SDK's abort error never sets `.name = "AbortError"`, an HTML-to-Doc import never piloted, an available MCP never checked.
> "Headline: ask hangs in headless mode — so it deadlocks the very orchestrator it's meant to unblock" (prd-to-product)
> "verify paths: empirically before step 1, not at step 8. The entire plan rests on [it]" (epost-intelligence-feed)

**T7. Revision not propagated through the whole plan (~5 rounds)** — epost-assessment, epost-intelligence-feed, qventus-prototyper. After a fix lands in one section, stale lines and un-recomputed derived numbers contradict it elsewhere — a second review round spent purely on internal consistency.
> "Verification gate #2 still reads: 'expect P-05; confirm others hold' That contradicts §4" (epost-assessment)
> "The token target math doesn't reflect step 0's contribution." (epost-intelligence-feed)

**T8. Scope bundling that defeats the gate (~5 rounds)** — seance, the-council, qventus-prototyper. Over-scoped sessions that invalidate the characterization-test gate's "only the container changed" promise, missing line estimates against the 300-line cap, bundled risky refactors without checkpoints.
> "Session B is over-scoped in a way that quietly defeats the D-021 gate" (seance)

**T9. Over-engineering vs a simpler alternative (~5 rounds)** — qventus-prototyper, epost-assessment, the-council. JS content model where a CSS gate suffices, token-auth where a plain route suffices, a speculative single-use provider abstraction.
> "do NOT build the SPECIALTIES JS model / renderSpecialty / QVSpecialty bridge from your earlier plan. Use a much lighter mechanism" (qventus-prototyper)

**Long tail (~10 rounds, not force-fit):** prompt-copy persona/tone calibration (epost-assessment, 3 near-duplicate rounds), doc phrasing ambiguity, padded heuristic list, unspecified flip-reset behavior, missing source SVG, mockup-vs-token-tier fidelity calls.

---

## 3. Where the fix lives

The distribution is decisive: **planning-prompt 64/102 (63%)**, context-file 11, claude-md 11, decisions 5, skill 4, code 2, none/unclear 5. Almost two-thirds of revisions would have been prevented by a better standing instruction applied *at plan time* — a plan-review furnace prompt — not by new repo rules. This makes sense: CLAUDE.md already carries the scope caps and read-before-write rules; what's failing is the plan's epistemics (unverified claims, unprovable verification, unsurfaced tradeoffs), which is checklist territory. The 11 context-file and 5 decisions fixes are project-specific facts (persona constraints, D-numbered rules) that belong in each repo's docs, not in any cross-project prompt. CLAUDE.md's 11 are mostly sharpenings of existing rules (read-before-write, scope estimates) rather than new ones. Skills get only 4 — the skill content itself is rarely the failure point. Conclusion: **build the furnace prompt first; promote only the survivors into CLAUDE.md.**

## 4. Promotable rules (from the 32 promotable=yes rounds)

**R1. No load-bearing factual claim about the codebase without a citation you actually ran.** Every count, "X is missing," "no files modified," or "these mirror each other" must be backed by a read/grep performed this session. Prevents: plans built on imagined repo state. Justified by: epost-intelligence-feed ("AGENTS.md isn't a pure pointer today. Lines 36–58 contain Codex-specific material"), epost-intelligence-feed-wt2 ("The '51 hex literals' number is misleading"), prd-to-product ("You're missing generator/output-summary.md — it's the actual source of the biggest vocab leak"), the-council ("breaks the plan's '3 files, none modified' framing"), qventus-prototyper ("I never saw you confirm the ortho wording").

**R2. Every verification step must be able to fail, and must reach the path it claims to test.** For each verify item, state the failure that would make it red; include the default/unchanged path and the failure path, not just the happy path; measure claimed wins instead of asserting them. Prevents: vacuous green checkmarks. Justified by: the-council ("A bad key... never arms [the timeout]"; "may run zero tests and report green"), qventus-prototyper ("export once with the font left at default"; "Wrap the assembly in try/catch and surface a visible error"), seance ("Measure the perf win, don't assert it"), prd-to-product ("the verification grep inherits its blind spots").

**R3. Probe unverified platform mechanics before step 1, not at the end.** If the design rests on a tool/SDK/platform behavior you have not empirically confirmed, the probe is the first step and its result can fork the plan. Prevents: whole architectures built on a mechanism that doesn't behave as documented. Justified by: prd-to-product ("ask hangs in headless mode — so it deadlocks the very orchestrator it's meant to unblock"), epost-intelligence-feed ("verify paths: empirically before step 1, not at step 8").

**R4. Diff the plan against recorded decisions and this session's agreements before presenting.** Name every D-NNN the plan touches, flag any reversal as an explicit sign-off item, and confirm nothing agreed earlier in the session was dropped. Prevents: silently overturning binding decisions and losing in-flight agreements. Justified by: seance ("The plan never addresses concurrency, and this project runs SWIFT_DEFAULT_ACTOR_ISO[LATION]" — D-022), qventus-prototyper ("that is not the full plan. where is the bit about housekeeping?"; "The stepper change reverses D-027 — get Rex to bless it up front"), the-council ("deliberate.ts re-commits the exact import-crash the last two splits exist to avoid"; "ai-reviewer.md's paths: now lists a phantom file").

**R5. After any plan revision, sweep the whole document: stale references and derived numbers.** A revision is not done until every section that referenced the changed design is updated and every computed target is recomputed. Prevents: shipping the inconsistency the revision was meant to fix. Justified by: epost-intelligence-feed ("The token target math doesn't reflect step 0's contribution"), qventus-prototyper ("the Stage B row still says upload writes → brandState.logoDataUri. That's stale naming").

**R6. State per-stage line estimates against the session cap, and never bundle changes that defeat your own test gate.** The heaviest stage gets an explicit estimate; anything that would make the gate unable to prove "only X changed" is split out. Prevents: scope creep that invalidates the safety mechanism protecting the change. Justified by: seance ("Session B is over-scoped in a way that quietly defeats the D-021 gate"), qventus-prototyper ("No line estimate for Stage 1, and it's the heavy one"), the-council ("bundled separable work into one commit and one over-cap session").

**R7. When a reviewer flags a risk, the plan absorbs it as a check — don't make the reviewer ask twice.** Any risk acknowledged in discussion gets a corresponding verification item in the next plan version automatically. Prevents: watch-items evaporating between review and execution. Justified by: epost-assessment ("do you need to add any checks to the plan for that?" — asked twice across rounds), qventus-prototyper ("The insertion can't be a blind replace_all — anchor per screen").

## 5. Taxonomy fit

The taxonomy mostly held: only 19/102 rounds (19%) fell to "other," so 81% landed in a named tag. But the distribution is top-heavy in a telling way: two tags — unstated-assumption (31) and weak-acceptance-criteria (24) — absorb 54% of all rounds, which means they are functioning as coarse buckets rather than precise diagnoses. Each wants a split: unstated-assumption conflates "unverified codebase/platform fact" (overlapping missing-read-before-write) with "unsurfaced judgment call needing sign-off," which have different fixes (a grep vs a sign-off item). Weak-acceptance-criteria conflates "verification structurally can't fail" with "a flagged risk got no check." Meanwhile the classic build-time retro tags barely fired at plan-review time — bad-substitution (1), goal-drift (2), scope-creep (3) — confirming that plan-review failures are a different species from execution failures and the retro taxonomy was imported, not derived, for this use.

## 6. Honest caveats

- **Refutation rate ~9%.** The verifier refuted 10 of 112 initially claimed revisions. The 102 "confirmed" rounds passed one adversarial pass, but if the classifier's base over-claim rate is ~9%, a handful of residual false positives likely survive; treat counts as ±5.
- **Known false negatives.** Spot-checks found 3 missed revisions, including one hidden inside an ExitPlanMode rejection tool_result that the digest pipeline doesn't render as a human turn. That channel is *systematically* under-captured, so the 57% revise rate is a floor, not a point estimate — plan rejections delivered via the rejection UI are the most plan-review-shaped events there are.
- **Near-duplicate rounds inflate theme counts.** Several entries share identical verbatims across two rounds (the persona-fit example, "3 files, none modified," "Session B is over-scoped," "B1 doesn't verify," docs/feedback). Some are genuinely re-litigated rounds; some may be the same feedback double-counted across worktree/session boundaries (note epost-intelligence-feed vs -wt2). T1 and T3 counts are most exposed.
- **Not all reviews are Rex's.** Multiple revise rounds are Rex pasting external reviews (other Claude conversations, councils). The themes measure what *survives to be caught at review*, blending Rex's own catch profile with external reviewers'; promotable rules drafted from these are still valid (they describe plan defects) but the "Rex's review style" framing overstates a single source.
- **Unit mismatch and residue.** 177 presentations vs 178 rounds classified, plus 2 abandoned and 1 unclear — small, but the denominators in §1 shift by a point depending on which you use.
- **Promotability is mostly "maybe."** Only 32/102 rounds were confidently promotable; 60 were "maybe." The furnace draft in §2 is a hypothesis list to be burned down against the next batch of sessions, not a settled rulebook — consistent with this repo's own retro-tag philosophy of adopting guardrails on evidence, not instinct.
- **Single developer, single workflow.** N=1 human. Nothing here generalizes beyond Rex's projects without re-validation.