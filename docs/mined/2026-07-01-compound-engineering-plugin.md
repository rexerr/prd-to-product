# Mine — compound-engineering-plugin (authoring-discipline slice) — 2026-07-01

- **Source:** [github.com/EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) — Every's 27-skill compound-engineering plugin.
- **Pinned:** `db21ba21eff9cc216537cd75c6e44dd49e1a4200` (v3.17.1, MIT; shallow clone `docs/mined/repos/compound-engineering-plugin/`, gitignored)
- **Lens:** this workspace's own product is hand-authored markdown skills — the same domain. Lens **A** = our skill-authoring discipline; **B** = what the `context-engineering` scaffold emits.
- **Scope of THIS mine (deliberate slice):** `AGENTS.md` (the authoring rulebook) · `docs/solutions/skill-design/` (all 20 docs) · 3 large skills as built artifacts (`ce-code-review` 835 lines, `ce-plan` 806, `ce-compound` 727) + 1 small contrast (`ce-commit` 105) · the enforcement test suite. **NOT mined (remainder, queued as its own board row):** the other 24 skills, the other 19 solutions docs (best-practices/integrations/workflow/conventions), the eval harnesses, the cross-host converter machinery.

## How this mine ran

Three blind readers over disjoint slices (rulebook conventions · evidence-base quality · large-skill anatomy), each given house conventions and the parked-row dedup inventory as *facts*, not valuations; reader 3 explicitly tasked with anti-evidence and barred from recommending the cap decision. Nine load-bearing citations spot-checked against the clone afterward — **all confirmed** (one initially missed because the #714 cite is a frontmatter URL, not an inline `#714`).

## Evidence-quality verdict (the meta-finding)

Their `docs/solutions/` base is **real incident-grounded engineering, not post-hoc rationalization**: of 20 skill-design docs, ~9 are concrete-incident (issue/PR numbers, regression tests named for the incident), ~7 measured-eval (trial tables with N), ~4 design-rationale (below our failure-mode bar, and mostly self-labeled as such). The tells: **falsified hypotheses are recorded** — a 60-trial eval disproving the motivating issue's own theory (`safe-auto-rubric-calibration.md`); their own over-generalized rule corrected against the spec + independent implementations (`bundled-script-path-resolution…md:34,76`). Cite density grades *above* our current practice.

## The two forks (adjudicate in the consolidation pass — both reversible, below the D-009 council bar)

### Fork 1 — the ≤500-line cap

- **Their position (verified verbatim):** body length is *deliberately not gated* — "The line guidance is advice, not a constraint… gating guidance would tax every deliberately-large skill with exemption-list ceremony" (`tests/skill-conventions.test.ts:93-96`). The circulating "8KB Codex body cap" is **folklore** — the real limit is on the injected metadata *list*; bodies load from disk on demand (`:97-100`). Their instrument is **conditionality**: extract blocks that are conditional or late-sequence AND ≥~20% of the skill; inline unconditional content costs nothing extra (`AGENTS.md:147-149`).
- **Artifact evidence FOR:** inline SKILL.md is only **15–22% of each big skill's total mass**; the conditional bulk (13 personas, rendering modes, deepening flows) is verifiably in `references/` loaded at named stages; ~70–80% of the inline file executes on every run. A 500-line cap here would push *mainline* into mandatory every-run loads: same always-loaded cost, +1 file, plus their documented reference-never-opened failure (#714).
- **Artifact evidence AGAINST:** the rule is applied with unstated judgment (~250 late-sequence lines kept inline in ce-code-review against their own trigger — load-reliability trade the rulebook doesn't state), and the big files carry genuine bloat a cap would have pressured out: the pipeline-mode override restated **7×** in ce-plan; motivational prose failing their own deletion test (`ce-compound/SKILL.md:15,674`); "The current year is 2026" rot (`ce-plan/SKILL.md:9`); two menu options both numbered "5".
- **Synthesis candidate for the pass:** their real invariant is not "no cap" — it's *deletion test + conditionality extraction + inline-the-trigger*, imperfectly enforced. Ours could become: cap what's **always-loaded**, not the file — while keeping the hard cap for hand-maintained docs (where TanStack/intent's "Do not simply raise the limit" evidence still stands).

### Fork 2 — deletion test vs. our mandatory "Failure it prevents" clauses

Their deletion test (`AGENTS.md:124-132`, verified verbatim): a line exists only if it (1) states a falsifiable constraint, (2) counters a known default tendency, or (3) supplies missing domain knowledge — and **"do not append motivational rationale to a directive that already stands on its own."** That last clause is in genuine tension with our house invariant: their view — rationale is padding when the rule is concrete; ours — the failure mode is what lets a future editor judge whether the rule still applies. Not blendable by default; adjudicate.

## Findings (consolidation-pass inputs; all verified against the clone)

### P-1 — Inline the trigger; a paraphrase suppresses the load · code-grounded, incident #714 · → chain-audit row + consolidation

Load-bearing routing lived only in a reference; agents rendered ce-plan's menu, acknowledged the user's pick in prose, and **stopped** (`docs/solutions/skill-design/post-menu-routing-belongs-inline.md`, `related_issue: …/714`, regression test `tests/skills/ce-plan-handoff-routing.test.ts:21`). Two lessons: (a) always-fire instructions belong inline; never inline a *summary* of a reference — "an agent that already has a workable inline version judges it 'has enough' and never opens the file" (`AGENTS.md:134-145`); (b) **"Call /X" is ambiguous** between "tell the user to type it" and "fire the Skill tool now" — name the platform's invocation primitive. *Reconciliation note:* reader 3 flagged the menu duplicated inline+reference as an un-parity-tested drift vector; the test file shows the duplication is the deliberate #714 fix with the SKILL.md side pinned — intentional, and still a one-sided guard.

### P-2 — "A soft rule plus visible exceptions is the specific combination that fails" · code-grounded, PR #747 · → consolidation

The ce-prefix convention was prose-only with visible legacy counterexamples; a new skill shipped unprefixed (`ce-prefix-required-for-skills-and-agents.md:26-28`). Now enforced with an explicit exception registry. **Third sighting** of mechanical-enforcement-over-prose (D-017 hook, intent's validator) — and the causal claim is the new part: it names *which* prose rules to promote first (the ones with visible exceptions). Companion pattern: **registry-with-staleness-sweep** — editorial judgment lives in a reviewed exception list (exact-match, written justification) with a stale-entry test, after regex-grading prose failed (`tests/skill-conventions.test.ts:114-119,760-775`).

### P-3 — Eval methodology for skill-prose changes · measured · → folded into [pressure-test ticket](../../tickets/pressure-test-behavior-prose.md)

Never trust N=1 (their 60-trial eval documented two confidently-wrong N=1 reads; headline metric = **variance reduction**, `safe-auto-rubric-calibration.md`); **paired blind old-vs-new injection** separates improvement / no-regression / already-emergent-at-this-tier (`paired-old-vs-new-injection-skill-evals.md`); **fixtures must be discriminating** — a case both versions pass proves nothing (`fake-cli-harness…md:35,41`); grade from the transcript, never the self-report (`frontier-model…md:94-97`).

### P-4 — Sibling-callability as a second explicit-invoke criterion · code-grounded · → consolidation (sharpens D-034)

Bidirectional registries tested both ways: user-invoked skills must have `disable-model-invocation: true`; pipeline callees must NOT, "because pipelines or sibling skills call them" (`tests/skill-conventions.test.ts:145-175,686-702`). Our D-034 cut (context-load vs cognitive-load) misses this: flipping the flag on a chain callee silently breaks the chain. In the artifact: 7/27 skills carry the flag — pipeline orchestrators + side-effectful tools, never judgment skills; the flag doubles as a headless-mode signal (`ce-plan/SKILL.md:87`).

### P-5 — Don't name instruction files on the read path · soft, well-argued · → chain-audit row

Runtime skills describe "what to look for in the agent's existing context," never "open CLAUDE.md" — redundant (harness auto-injects), brittle (filename differs per harness), and a prompt-injection-shaped smell (`AGENTS.md:95-101`). Precise carve-outs: write-backs need a named target; **fresh subagents don't inherit instructions, so they may be told to open files** — which maps exactly onto our verifier-independence rule.

### P-6 — Verifier-independence, implemented mechanically · code-grounded · → consolidation

The orchestrator's own quick scan enters review-merge as `fast-pass`: capped at anchor 50, never counts toward cross-reviewer promotion, never seeded into reviewer prompts — "seeding them would manufacture the false agreement this cap exists to prevent" (`ce-code-review/SKILL.md:449-454`, verified verbatim). Our CLAUDE.md "withhold your reasoning" rule, with teeth. Companions: **quote-the-line gate** (high-confidence findings carry the verbatim motivating line or get demoted, `:538,568`); persona **jurisdiction boundaries** (each reviewer lists what it does NOT flag and who owns it — 3rd sighting of negative-scope, after gstack FP-rules and their own personas); **fail-closed UNKNOWN** (a missing signal surfaces as `UNKNOWN`, "never as a silent `0` that reads as 'trivial'", `:281`).

### P-7 — Smaller verified conventions · → consolidation inputs

- **Runtime vs authoring context split** — repo-root AGENTS.md is authoring context; runtime behavior belongs in the skill's own files (`AGENTS.md:89-91`). Names our D-013/D-019 line more crisply than we do; one-sentence adoption candidate.
- **Rule-writing meta-lesson** — "a single empirical finding is not an authoring rule until validated against the spec and 2-3 independent implementations" (`bundled-script…md:76`) — a documented failure mode of rule-writing itself; direct upgrade candidate for our failure-mode bar (grounds the parked Plausible/Silent/Grounded item).
- **Contradictory absolutes across phases: the model follows the later rule**; "when available" tool phrasing is an escape hatch the model takes (`compound-refresh-skill-improvements.md:28-43`).
- **Pass paths, not content, to subagents; phrasing alone can 7× tool calls** (14 vs 2 for two phrasings of the same instruction, `pass-paths…md:80-84`) — directly relevant to `/mine`'s own reader dispatch.
- **Skill-caching trap** — plugin skills cache at session start; same-session edit-and-reinvoke tests *pre-edit* content (`AGENTS.md:112-120`). Our symlink mechanics differ, but the same-session-tests-stale-content class deserves a line in our verification rules.
- **Stateful/git skills are state machines, not narratives** — 10 named non-hypothetical edge cases; "clean-tree shortcuts are the highest-risk part" (`git-workflow…md:144-231`). Bears on our end-session flow and scaffolded git rules.
- **Anchored discrete rubrics beat continuous confidence** (floats clustered 0.68–0.72 = false precision; 5 behavioral anchors, `confidence-anchored-scoring.md`) — llm-council relevance.

## D-063 — third sighting, recorded not re-proposed

The full solutions **pipeline** is now documented (creation via `ce-compound` with schema-validated frontmatter + a triage filter — "most bugs are localized mechanical fixes; compounding those clutters docs/solutions/"; consumption via a `learnings-researcher` pass that greps frontmatter and converts hits into plan constraints; maintenance via `ce-compound-refresh` drift triage). **Substrate observation that strengthens the decline for Lens A:** the evidence density leans on infrastructure we deliberately lack (GitHub issues/PRs, a test runner, eval harnesses); their own triage filter concedes the clutter failure D-063 predicted. D-063's revisit trigger (our own retro data showing a recurring class) is unchanged.

## Dedup

Negative-scope / what-not-to-flag → 3rd sighting (gstack row); mechanical-enforcement → 3rd (intent row, D-017); failure-mode grounding upgrades → 3rd (devtools row); name==dir → 2nd (intent). **The accumulation itself is the finding:** the parked skill-craft buckets' rule-of-2 gates have tripped across four independent sources → the consolidation pass is queued rather than a fifth bucket parked.
