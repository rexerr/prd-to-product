# LLM Council transcript — 2026-06-08 — Improving the kit (effectiveness × accuracy)

## Framed question

How should "the kit" be improved to maximize effectiveness (idea→shipped throughput) and accuracy (correct, non-hallucinated, non-destructive output), and what ONE thing should be prioritized first? The kit is a SOLO developer's (Rex) personal idea→shipped system inside Claude Code: three composable markdown-only skills (prd-creator → context-engineering → design-system-bootstrap) + an agent-process harness. Win = PERSONAL LEVERAGE, not a commercial product. Observed failures: chain doesn't auto-compose; skills need explicit @path input; prd-creator leaks internal jargon and once hallucinated provenance; a "qventus near-miss" where a naive auto-orchestrator would have CLOBBERED a hand-authored design system (caught because a human was in the loop); verification has only ONE flat-shape regression baseline, modular shape can only be eyeballed. Candidate brainstorm top-5: (1) /idea-to-product orchestrator, (2) collaborator-feel interview pass, (3) generator self-test harness, (4) stack-aware skill injection, (5) project-type recipes + shared kit-core.

## Anonymization mapping (for audit)

```
A = The Long View
B = The Veteran
C = The Architect
D = The Stranger
E = The Skeptic
```

---

## Advisor responses (de-anonymized)

### The Skeptic
#3 (self-test harness) ranked too low for the wrong reason. Every other item writes more generator surface area — orchestration, branching, de-jargon, injection. You're pouring concrete on a foundation you cannot inspect: the modular shape has NO baseline, so you cannot tell whether a change improved output or silently corrupted it. That is the actual accuracy failure — jargon leaks and cold questions are symptoms you happened to catch; the hallucinated provenance is the one you caught, and the terrifying question is how many you didn't. The #1 candidate — auto-orchestrator with "skip if exists" branching — is exactly the destructive conditional logic that MUST have a regression test before it touches a real repo. No undo on overwriting your hand-authored design system. Direct-on-main, solo, no review — the harness is the only safety net left. Sequence forced: harness first, then orchestrator. #1 before #3 is shipping the loaded gun before the safety.

### The Architect
Every observed failure is a trust failure. You're not optimizing throughput — you're optimizing how much output you can ship without re-reading it. Speed is downstream of trust. A meta-orchestrator that runs faster while you still audit every artifact isn't leverage; qventus proves auto-composition without trust is destructive. So #1 is the most dangerous move: chaining unverified steps compounds error — a hallucination in PRD.md propagates into CLAUDE.md into tokens.css, blast radius three skills deep with no diff to catch it. Highest-leverage variable is verifiability — #3. Smallest first move that proves it: take the qventus project and one clean project, run the existing skills, commit both output trees as golden baselines. Now every future change is diff-gated. That single afternoon converts "eyeball and hope" into "diff and know" and makes #1 safe to build later. Harness first, orchestrator second.

### The Stranger
#3 is underrated at third. "Effectiveness" and "accuracy" are stated co-equal, but the brainstorm ranks four speed/UX items above the one accuracy item — quietly assuming throughput is the binding constraint. It isn't. The qventus near-miss is the tell: an orchestrator that clobbers a hand-authored design system destroyed irreplaceable work. Cost asymmetry is total: a missed speed gain costs minutes; one destructive run costs a day plus trust in the whole kit. The unspoken assumption is that the orchestrator can be built safely without a baseline to verify against — building the dangerous thing on the unmeasured thing. Who's affected: Rex six months from now, running /idea-to-product on a project he's stopped watching closely BECAUSE the kit earned his trust — exactly when an unverified branch silently overwrites real tokens. Build #3 first; #1 inherits a diff-verifiable guarantee.

### The Long View
#3, the self-test harness, reframed as the precondition that makes everything else safe to build. Three-year view: effectiveness compounds; accuracy decays unless something holds it in place. Every improvement increases the surface area where a silent regression can hide. One baseline, modular eyeballed — each change raises the probability of wrong/destructive output you won't catch until a real project eats the damage. qventus was a coin flip you happened to win. Build the orchestrator first and you've automated the chain before you can verify it — wrapped the clobber failure mode in one command and removed the human pause that caught it. A diff-on-every-change harness makes your future self faster and bolder; you ship #1/#2/#4 in half the time because you stop hand-auditing. Build the harness, then automate fearlessly.

### The Veteran
The standard playbook for workflow friction says build the orchestrator — that's why #1 is at #1. Resist it. I've watched this a dozen times: wrapping a chain that misbehaves at each link makes the wrapper inherit every defect, harder to debug unattended. You can't safely automate what you can't verify, so #3 wins. Build flat+modular baselines and the diff gate first. I'll concede the case is special: solo tool, no users, a bug only costs an afternoon — the argument for speed on #1. But "only costs an afternoon" is the rationalization that precedes deleting a real design system. Order: harness → orchestrator → interview polish. Do not reorder.

---

## Peer review (de-anonymized)

**Vote tally — strongest:** The Stranger ×3, The Architect ×2.
**Vote tally — biggest blind spot:** The Long View ×2, The Veteran ×2, The Architect ×1.

### Reviewer 01 — The Skeptic
- **Strongest:** The Stranger — names the cost asymmetry explicitly and locates the exact future moment the failure detonates.
- **Biggest blind spot:** The Long View — frames the harness purely as a precondition, never confronts its own "bug only costs an afternoon" counterargument.
- **What all five missed:** Golden-tree diffing catches STRUCTURAL regressions but is blind to the two named HALLUCINATION failures (jargon leak, fabricated provenance), which are semantic and would pass a byte-diff against a baseline that itself contains the jargon.

### Reviewer 02 — The Architect
- **Strongest:** The Architect — reframes every failure as a trust failure and lands a concrete one-afternoon move.
- **Biggest blind spot:** The Veteran — concedes the strongest counterargument then waves it away with a slogan.
- **What all five missed:** The qventus near-miss is a "never-overwrite-hand-authored-files" INVARIANT; a one-line refuse-if-exists guard buys most of the safety in minutes, faster than dual baselines.

### Reviewer 03 — The Stranger
- **Strongest:** The Stranger — names the temporal mechanism (trust → Rex stops watching → destructive run lands unobserved).
- **Biggest blind spot:** The Long View — a golden-baseline diff does nothing to prevent the clobber class, which needs a no-overwrite guard, not a diff.
- **What all five missed:** All five conflate TWO mechanisms under "#3 the harness": a regression-diff and a destructive-write guard. The qventus near-miss is the latter; a diff harness would NOT have stopped it, so "harness first" leaves the headline failure unaddressed.

### Reviewer 04 — The Long View
- **Strongest:** The Architect — names the root cause (trust) and the cheapest concrete first move.
- **Biggest blind spot:** The Veteran — "do not reorder" rigidity while conceding the bug only costs an afternoon.
- **What all five missed:** LLM-generated markdown may not be deterministic enough for a diff-based harness — re-running yields non-identical-but-valid output, so a naive golden-tree diff fires false positives and trains Rex to ignore it.

### Reviewer 05 — The Veteran
- **Strongest:** The Stranger — attacks the question's own framing (co-equal goals vs 4:1 ranking) with a concrete trust-erosion scenario.
- **Biggest blind spot:** The Architect — committing the qventus tree as a golden baseline walks into both traps: non-determinism and no-prior-baseline.
- **What all five missed:** A "golden baseline diff" may be incoherent for a non-deterministic generator; the harness needs SEMANTIC/INVARIANT assertions (no-overwrite, no-jargon-leak, provenance-grounded). qventus was caught by a HUMAN PAUSE a diff cannot replicate; #2's interview fixes were never weighed as a parallel quick win.

---

## Chairman synthesis

### Recommendation headline
Before building any automation, make the kit non-destructive by default and check output for jargon/provenance — the headline failure (clobbering hand-authored work) is a write-guard problem, not a diff problem.

### Where the council agrees
Unanimous on direction: safety and verifiability before automation. The orchestrator (#1) is the most dangerous thing to build first — it wraps an unverified chain in one command and removes the human pause that caught qventus. Effectiveness is downstream of trust; chaining unverified steps compounds error three skills deep. Forced sequence: verification/safety first, orchestrator second, interview polish third.

### Where the council clashes
No real clash on direction. The peer review sharpened the recommendation enough that "build #3" as the advisors stated it is wrong in three ways: (1) "the harness" fuses a regression-diff and a destructive-write guard — qventus is the write-guard case, which a diff would not have caught (first-run clobber, no prior baseline); (2) a naive byte-diff is incoherent for a non-deterministic LLM generator and would train Rex to ignore false positives; (3) the diff is blind to the semantic hallucination failures (jargon, provenance) the question weights equally.

### Blind spots the council caught
Mechanism conflation (write-guard ≠ diff); non-determinism breaks naive diffing; diff is blind to hallucination; the human pause is what actually saved qventus; #2 interview fixes were never weighed as a parallel quick win.

### The recommendation
Build verification as INVARIANT ASSERTIONS, not a golden-tree byte-diff, sequenced by cost-to-safety ratio:
1. **Non-destructive guardrail first (hours):** generator refuses to write where a hand-authored file already exists — skip-if-exists + dirty-tree check, surface a diff for consent. Smallest move that closes the qventus headline failure; survives removal of the human pause.
2. **Invariant/semantic checks (a day):** no-overwrite-of-existing-files, no-jargon-leak (grep the internal-jargon list), provenance-grounded (every cited fact traces to a given input).
3. **Modular structural baseline (as invariants, not byte-diff):** assert files exist, required sections present, cross-refs resolve.
4. **Then orchestrator (#1), then interview polish (#2)** — #2 overlaps step 2 and can ride alongside.
Do not commit the qventus tree as a golden baseline.

### The one thing to do first
Add a non-destructive write guard to the generator: refuse to write any file that already exists on disk, emit the proposed content as a diff, and require explicit consent to overwrite. Closes the qventus clobber failure in hours and is the precondition that makes everything else — including the orchestrator — safe to build.

---

*Council session — 2026-06-08. Report: `council-report-2026-06-08.html`.*
