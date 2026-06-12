# Handoff brief: superpowers patterns → context-engineering skill

> **Provenance note (added at reconciliation, 2026-06-11):** this brief was written 2026-06-11 in a separate review session (source clone `tex/.skill-review/superpowers/`, from [github.com/obra/superpowers](https://github.com/obra/superpowers) — disposable, likely deleted; the `skill-authoring-principles` memory it cites lives in that session's project, not this repo). Rex pasted it into the prd-to-product session the same evening and it was reconciled into `BACKLOG.md` — see the items on pressure-testing prose (Pattern 1 method detail), rationalization tables (Pattern 2), and the scaffold-level candidates entry (Patterns 2–4 applications). It is a **second independent extraction of the same source** as the 2026-06-11 in-repo review ([retro](retros/2026-06-11-external-resource-reviews.md)), converging on the same items — the convergence-as-promotion-evidence signal that retro said to watch for. Body below is verbatim.

---

**Date:** 2026-06-11
**For:** a future session invoked with `/context-engineering` (or asked to improve that skill). This doc is the complete brief — it is self-contained because the source clone (`tex/.skill-review/superpowers/`, from obra/superpowers) is disposable and may already be deleted.

## The job

Fold four patterns from the superpowers plugin into the **context-engineering** skill (`~/.claude/skills/context-engineering/`). That skill scaffolds AGENTS.md, CLAUDE.md, `.claude/rules/`, and docs/ for new AI-assisted projects. The patterns below can improve it in two places:

1. **The artifacts it generates** — rules files and CLAUDE.md sections that *resist rationalization* instead of just stating rules.
2. **Its own process** — a verification step before it declares the scaffold done, and optionally a pressure-test offer for any discipline-enforcing rules it writes.

The session doing this work decides what goes where; this doc supplies the material, not the design.

## Constraints

- **Harvest, don't install.** Do not install superpowers; do not vendor its files. Extract the ideas into context-engineering's own voice and structure.
- **Don't import its tone.** Superpowers uses "your human partner", "lying", "you'll be replaced". House style doesn't. Keep the mechanisms, drop the theatrics.
- **House rule: "never by default, always by decision"** — prefer this framing over absolute bans (the reviewed repos contradicted their own bans).
- **House authoring principles** (from the 2026-06-11 skill review; also in memory as `skill-authoring-principles`):
  - Three layers per skill: *whys* for generative decisions, *rationalization counters* at pressure points, *mechanical counts* at the ship gate.
  - Description = WHEN, never WHAT. A description that summarizes the workflow gets executed *instead of* the body. Keep triggers narrow and verb-specific.
  - Pressure-test with subagents before shipping; run a baseline without the change to capture rationalizations verbatim.
  - Examples become defaults — label illustrative examples as "illustrations, not a menu."

---

## Pattern 1 — Skill-TDD / pressure-testing (from `writing-skills/testing-skills-with-subagents.md`)

Core claim: **writing behavioral documentation IS TDD.** If you didn't watch an agent fail without the rule, you don't know the rule prevents the right failure.

| Phase | Action | Success criteria |
|---|---|---|
| RED | Run scenario WITHOUT the rule/skill | Agent fails; rationalizations documented **verbatim** |
| GREEN | Write minimal rule addressing those specific failures | Agent now complies |
| REFACTOR | Re-test; capture NEW rationalizations; add explicit counters | Agent still complies; no new loopholes |

**Writing pressure scenarios:**
- Bad: "You need to implement a feature. What does the rule say?" (academic — agent recites)
- Good: combine **3+ pressures** — time, sunk cost, authority, economic stakes, exhaustion, social ("looking dogmatic"), pragmatic ("pragmatic vs dogmatic").
- Force a concrete A/B/C choice; real constraints (specific times, file paths); "What do you do?" not "What should you do?"; no easy out via "I'd ask the user."
- Frame as real: "IMPORTANT: This is a real scenario. Choose and act."

**Meta-testing** when an agent reads the rule and violates anyway, ask it: "How could that rule have been written to make the right answer unambiguous?" Three diagnostic answers: (1) "it WAS clear, I ignored it" → needs a foundational principle like "violating the letter is violating the spirit"; (2) "it should have said X" → add X verbatim; (3) "I didn't see section Y" → organization problem, surface it earlier.

**Bulletproof =** agent chooses correctly under max pressure, cites the rule as justification, acknowledges the temptation. **Not bulletproof =** new rationalizations, "hybrid approaches", arguing the rule is wrong.

**Application idea:** context-engineering could pressure-test the CLAUDE.md/rules it generates (RED baseline with a subagent on the new scaffold before finalizing), or at minimum emit rules pre-hardened with the counters below.

## Pattern 2 — Rationalization tables (the hole-plugging prose pattern)

For each observed rationalization, plug it four ways:

1. **Explicit negation in the rule.** Not "write the test first" but: "Wrote code before the test? Delete it. No exceptions: don't keep it as 'reference', don't 'adapt' it while writing tests, don't look at it."
2. **An Excuse → Reality table row:** `| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |`
3. **A Red Flags list entry** — symptoms that you're ABOUT to violate: "keep as reference", "spirit not letter", "just this once".
4. **Description/trigger updated** with violation symptoms, so the rule loads when the agent is mid-rationalization.

Generic counters don't work ("don't cheat"); specific negations do ("don't keep it as reference"). Counters must come from *observed* rationalizations (Pattern 1), not imagined ones.

**Application idea:** any discipline rule context-engineering writes into a scaffold (testing policy, commit policy, "ask before X") should ship with at least a small Excuse→Reality table and red-flags list, seeded from the well-known rationalizations above.

## Pattern 3 — The verification gate (from `verification-before-completion/SKILL.md`)

Iron law: **no completion claims without fresh verification evidence** — if you haven't run the verifying command in this message, you can't claim it passes.

The gate function:

```
BEFORE claiming any status:
1. IDENTIFY  the command that proves the claim
2. RUN       it fresh and complete
3. READ      full output, exit code, failure count
4. VERIFY    output actually confirms the claim — if not, state actual status with evidence
5. ONLY THEN make the claim, with the evidence
```

Claim → evidence mapping (excerpt): tests pass → test output with 0 failures (not "should pass"); build succeeds → exit 0 (not "linter passed"); bug fixed → original symptom re-tested (not "code changed"); subagent completed → diff inspected (not the agent's success report).

Red flags: "should/probably/seems to", expressing satisfaction before verifying, trusting agent reports, partial checks, "just this once."

**Application ideas:** (a) a verification-gate rule is a strong candidate for the default `.claude/rules/` scaffold — it's project-agnostic and high-value; (b) context-engineering itself should gate its own "scaffold complete" claim (e.g., re-read each generated file, check cross-references resolve).

## Pattern 4 — Adversarial reviewer subagent prompt (from `requesting-code-review/code-reviewer.md`)

A reusable prompt template for dispatching a review subagent against a git range. Structure worth keeping:

- Inputs: what was implemented, the plan/requirements, base..head SHAs.
- Check dimensions: plan alignment (deviations flagged as intentional-or-not), code quality, architecture, testing ("tests verify real behavior, not mocks"), production readiness.
- **Calibration section:** categorize by actual severity (not everything is Critical); acknowledge strengths first — accurate praise makes the rest of the feedback trusted; flag when the *plan* is wrong rather than the implementation.
- Output contract: Strengths / Issues (Critical = must fix, Important = should fix, Minor) each with file:line + what + why + how / Recommendations / verdict ("Ready to merge? Yes | No | With fixes" + 1–2 sentence reasoning).
- Hard rules: no "looks good" without reading; no vague feedback; always a clear verdict.

**Application idea:** ship this as a template in the scaffolded `docs/` (or a rules file describing when to dispatch it), so projects built on the scaffold get a ready-made review-agent prompt.

---

## Out of scope / do not do

- Do not edit `~/.claude/skills/context-engineering/` before reading the whole skill and its templates — these patterns must be adapted to its existing structure, not bolted on.
- Do not add superpowers' contributor-process content (PR policy, harness bootstrap) — irrelevant to scaffolding.
- Do not let any new description text summarize workflow (CSO rule above).
- After integrating, pressure-test at least one generated artifact (Pattern 1) before calling it done — and verify per Pattern 3.
