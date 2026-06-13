# Council transcript — Plan-review furnace: build now or validate first?

**Date:** 2026-06-12
**Evidence pack:** [`research/feedback-extracts/PATTERNS.md`](../../research/feedback-extracts/PATTERNS.md) (83-session plan-review mining audit)
**Report:** [`council-report-2026-06-12-furnace.html`](council-report-2026-06-12-furnace.html)

---

## Framed question

Should Rex build a plan-time "furnace" prompt NOW (a markdown planning prompt seeded with rules R1–R4 targeting plans that assert things they never verified), or run ONE MORE VALIDATION BATCH first to confirm the patterns are stable?

Evidence: an 83-session audit found ≥57% of plan-review rounds (102 of 178) drew a revision, dominated by a preventable "asserts-what-it-never-verified" class (~40–50 rounds). Known weaknesses: a large share of revisions are external reviews Rex pasted in (not his own catches); the [P]reventable/[H]ealthy-friction split is his single unverified judgment call; counts are a floor, not a point estimate. Repo philosophy: "earn a guardrail with evidence from the log, not instinct." The furnace is a cheap, deletable markdown prompt. Rex's lean: run cold sessions WITHOUT external review to isolate his own catch profile first.

---

## Anonymization mapping (for audit)

```
A → The Architect
B → The Long View
C → The Veteran
D → The Skeptic
E → The Stranger
```

Reviewers saw responses by letter only.

---

## Advisor responses (de-anonymized)

### The Skeptic — *Validate first*
The data isn't measuring what the furnace is supposed to fix. You audited a blended stream where a large share of "revisions" are external reviews Rex pasted in. R1–R4 are fitted to *what an external reviewer flags*, not *what Rex's own plans reliably miss* — build on that and you've hardcoded a stranger's review profile into your plan-authoring prompt. Worse, the [P]/[H] split is a single unverified judgment call by the person who most wants the furnace to exist; motivated reasoning lives exactly there. If a third of "preventable" rounds are actually healthy friction, the furnace suppresses the questions Rex needs his plans to raise — an invisible failure. The repo's own law convicts you: 32 promotable rounds out of 102, ±5, a known under-captured channel is instinct wearing a spreadsheet's clothes. Cheap to write, expensive to *trust*. Validate first.

### The Architect — *Build narrow now*
Plan-review revisions are a downstream symptom; you're optimizing the wrong axis. The furnace doesn't need R1–R4 to be *stable* — it needs ONE thing true: that a plan forced to cite what it verified produces fewer "asserts-what-it-never-checked" rounds (T1+T2+T6, ~40–50, a single mechanical class). A plan that reads the file before asserting its contents is correct whoever caught the lie. Pasted-review contamination poisons R5–R7, NOT the verification-citation core. So: write the furnace now, scoped to ONLY verification-citation, drop the [P]/[H] judgment calls. Then build and validation become one act — run the next 10 sessions with it on, count T1/T2/T6 recurrence. Build narrow; let the batch grade it.

### The Stranger — *Build nothing yet*
The audit mines the wrong unit. A large share of rounds are pasted external reviews, so R1–R4 profile "things some reviewer flagged," not "my plans miss X" — a population the prompt will never face at authoring time. "Furnace" is undefined as a mechanism. If it's genuinely that cheap, why deliberate at all? The [P]/[H] split targets a category boundary nobody has tested. The whole population is one developer, future-Rex, in cold sessions. The cleanest validation isn't re-mining the contaminated log — it's the cold-session probe: run plans *without* external review and watch what HE actually misses. Build nothing until that separation exists.

### The Long View — *Wait, protect baseline*
Building now is the cheaper-looking mistake. The furnace's real cost isn't the markdown — it's installing a filter before calibrating the lens. From then on you can't tell whether revisions dropped because the furnace works or because it suppresses the [H] friction you want. The instrument contaminates the measurement it was built from. What compounds is a *clean Rex baseline* — your own catch profile, uncontaminated — reusable forever to validate every future furnace, rule, and skill. R1–R4 tuned to a blended signal depreciate the moment your reviewer mix changes. And 32 promotable rounds against your stated bar is violating your own constitution on instinct; do it once and the bar means less every time. Wait. Build from clean Rex.

### The Veteran — *Build narrow, then test*
The standard playbook says wait, and 32/102 doesn't clear Rex's own evidence bar — I've watched a dozen people build the controller before the measurement was stable and burn three cycles untangling tool from noise. BUT this case is different in cost structure: tuning a guardrail to noise only hurts when it's expensive to write, expensive to rip out, or silently embedded in a pipeline. A deletable markdown prompt is none of those. The real question is the cheapest thing producing a clean signal. Do both in order: write a thin furnace seeded with ONLY R1–R4 (the T1/T2/T6 core that doesn't depend on the [P]/[H] split), then run the cold batch as the test of *that artifact*. The furnace is the hypothesis the batch falsifies. Don't promote R5–R7 until cold data clears them.

---

## Peer review (anonymized → de-anonymized)

**Votes — strongest:** The Veteran ×4, The Architect ×1.
**Votes — biggest blind spot:** The Long View ×5 (unanimous).

The unanimous blind spot: the Long View's "furnace permanently contaminates the signal" claim — refuted by every reviewer on the grounds that a markdown prompt toggles off per session, so it is not the embedded, irreversible filter the argument assumes.

### What the council collectively missed (the high-value round)

1. **No false-negative oracle.** The cold batch is graded BY Rex — the same party who owns the [P]/[H] split. It measures the *precision* of his catch profile and never its *recall*: lies that ship because nobody caught them stay invisible. *(Reviewer 1)*
2. **A free discriminating test no advisor proposed: re-tag the existing 102 rounds by who-caught-it (Rex vs. pasted reviewer).** Sizes the contamination directly, no new sessions. And the ~40–50 "never-verified" rounds are *most likely* Rex's own catches — which would collapse the contamination objection entirely. *(Reviewers 4 & 5, independently)*
3. **Can a plan-time prompt even fix this?** The failure is the model not reading files before asserting — an agentic-execution gap a *planning* prompt may not reach. The batch must instrument whether the furnace changes behavior at all, not just whether revisions drop. *(Reviewer 3)*
4. **"Contamination" may be the wrong frame.** Pasted reviews catch real defects regardless of source; the question is which catches a plan-time prompt can *preempt*, not whose catch it was. *(Reviewer 3)*
5. **Passive instrumentation is cheaper than either pole** — log verification-citation recurrence in the current loop without building the furnace OR running a separate batch. *(Reviewer 2)*

---

## Chairman synthesis

**Headline:** Write the narrow furnace now — scoped to only the R1–R4 verification-citation core — and let the next cold batch grade it, because a deletable markdown file is the hypothesis, not the irreversible bet your evidence bar is built to guard.

**Recommendation:** Build the narrow furnace now (siding with Architect + Veteran), but do the free precursor first. The evidence bar exists to stop you embedding expensive, hard-to-remove machinery on a noisy signal — a per-session-toggleable markdown prompt is none of those, and applying the wait-rule here over-applies judgment into ritual. The irreversible fork would be freezing the [P]/[H] boundary and promoting R5–R7 — which you should NOT do. Scope the furnace to ONLY the verification-citation discipline (cite what you read before asserting codebase facts or platform mechanics); that core is contamination-proof and clears the bar on its own merits. Then the next ~10 sessions with it on ARE the validation batch.

**The one thing to do first:** Re-tag the existing 102 rounds by who-caught-it — Rex vs. pasted reviewer — for the T1/T2/T6 "never-verified" class only. Free, no new sessions, and it directly sizes the contamination on the exact core you'd build from. Mostly Rex's catches → contamination objection collapses, build immediately. Mostly pasted-in → you've learned the furnace targets a stranger's profile before writing a line.
