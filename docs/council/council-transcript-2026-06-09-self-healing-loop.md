# Council transcript — Self-Healing Plan Review Loop

**Date:** 2026-06-09
**Question:** Should Rex build the "Self-Healing Plan Review Loop," and at what scope? Is the mechanism sound; is the volume critique decisive; is fold-into-existing-retros the right call; is trialing it on a separate live project (llm-council) smart de-risking or signal-dilution; what's the single highest-leverage first move?

This council was run on the *original design* plus *Claude's counter-proposal* together.

---

## Framed question

Should Rex (a solo developer) build a "Self-Healing Plan Review Loop" — a system that captures the feedback he gives when reviewing Claude Code's implementation plans, tags it by theme, counts it, and fires a STOP gate when a tag crosses a threshold (default 10) so he runs a human "improvement sprint" that folds the fix back into Claude Code's context so the same feedback stops recurring? It would live as a parallel `docs/plan-reviews/` subsystem in a repo already meta-system-dense whose core principle is "earn a guardrail with evidence from the log, not instinct." Claude counter-proposed a lighter path: fold tagged feedback into existing session retros, grep as the counter, build the machinery only after a tag trips by hand. Rex also wants to trial the system on a different live project (his llm-council tooling) before committing it to the home repo.

---

## Advisor responses (de-anonymized)

### The Skeptic
The mechanism has a flaw the counter-proposal undersells: at 5-15 items/week with 8 tags, you are dividing roughly 10 events across 8 bins. A tag hits 10 only after weeks. By then the "recurrence" you detect is contaminated by every CLAUDE.md edit, skill change, and mood shift in between — you cannot attribute the trip to a stable pattern versus noise. This isn't a thermostat; it's a thermostat reading a room where someone keeps moving the thermometer. Worse: the system's own success destroys its signal. Promote a rule, reset the counter — now that class can't re-trip for weeks even if your fix was wrong. You've built an instrument that goes quiet exactly when you'd want to know the fix failed. The central irony is the kill shot and it's correct: you have zero count proving "I fix the same things repeatedly." If it were true, you could name the top-3 recurring problems right now without any system — so name them. The hidden-dependency point compounds this: back-propagation needs a planning-prompt artifact that doesn't exist. The "teeth" are vaporware. The separate-project trial is signal-dilution, not de-risking. Highest-leverage first move: spend ten minutes listing your actual recurring plan-review failures from memory. If the list is short and obvious, fix those directly and build nothing.

### The Architect
Build nothing yet. You are optimizing the wrong variable. The variable that actually determines whether any of this pays off is "does a planning-prompt artifact exist to fold fixes into?" Back-propagation is the teeth, and the teeth bite into an artifact that doesn't exist. You're designing a thermostat with no furnace wired to it. So reframe: the problem isn't "capture feedback." It's "I have no durable planning surface, so every plan starts from CLAUDE.md cold and re-earns the same corrections." Build the furnace first. Create a single `planning-prompt.md` (or a plan-review checklist the drafter reads). That's the missing artifact, useful on day one independent of any loop, and where 80% of recurring feedback would actually land. Simplest first move: for the next ~15 plan reviews, append one tagged line to your existing retro. No new directory, no script, no banner. Grep it. That costs an hour and produces the count the proposal lacks. Testing on llm-council first is signal-dilution — test it where the feedback actually lives.

### The Stranger
The proposal is a recursion: Rex is using his plan-review loop to design a system that captures lessons from his plan-review loop. The first artifact he should produce is not a taxonomy. It is one honest count of how many times in the last month he actually re-typed the same feedback. He has not produced it. That absence is the whole verdict. Words that wouldn't survive outside Rex's head: "thermostat for context engineering," "back-propagate," "actuator," "STOP banner," "improvement sprint" — control-systems metaphors dressed as a build spec. A thermostat is worth building because a house has thousands of temperature events a day and no human watching. Rex generates 5-15 events a week and is personally watching every one. You do not install a thermostat in a room you are already sitting in with your hand on the heater. What the one affected person will actually experience: writing markdown entries, maintaining 8 drifting tags, glancing at a counter that says "3 of 10" for two months before it fires. That is a second loop of work bolted onto the first. Highest-leverage first move: for two weeks, append one tagged line to your existing retro each time you re-give feedback. Then count.

### The Long View
The repo's principle is "earn a guardrail with evidence not instinct." The most expensive thing you own here is not the plan-review loop — it's that principle's credibility. Build this subsystem on instinct and you've spent the one rule that makes every other rule in this dense meta-system trustworthy. Three years out, the question isn't "did the thermostat reduce recurrence" — it's "is the log still load-bearing, or did it become a place where ceremony goes to look like rigor." Now the asset that compounds: this thing is a product candidate. An internal tool fails quietly; a scaffolded skill that ships premature ceremony into every future project fails in every clone, and you inherit a taxonomy that drifts under eight tags at a volume where it can't earn its keep. The depreciating asset is the markdown subsystem you'd build now. The compounding asset is the evidence that the mechanism works at solo throughput — and you have zero of that today. Highest-leverage first move: add the plan-review feedback line to existing retros, grep weekly, do nothing else for a month. The separate-project trial is signal-dilution.

### The Veteran
The obvious move is the standard playbook: when feedback evaporates and you repeat mistakes, build a capture-and-promote loop. I have watched a hundred solo developers build exactly this. The failure mode is reliable: the meta-system outlives the problem. You build the andon cord, honor it twice, and six months later you're maintaining `scripts/review-pulse` and reconciling tag drift against a problem you'd have solved by just remembering. The volume critique is decisive and not close. Andon cords, Kaizen counters, CI-for-prompts earn their keep at a volume where memory provably fails. Toyota's line throws thousands of events; you throw 5-15 a week. The repo already told you the answer: "earn a guardrail with evidence, not instinct." The proposal violates the house rule on move one. What survives: the taxonomy and the WHERE-it-lives tag — real and cheap. Adopt the lighter path; build the parallel subsystem only when grep shows a tag tripping by hand. Highest-leverage first move: add the tagged line to retros for two weeks. Let the log earn the system — or kill it.

---

## Anonymization mapping (for audit)

```json
{"A": "The Veteran", "B": "The Stranger", "C": "The Skeptic", "D": "The Long View", "E": "The Architect"}
```

## Peer review round

**Votes:** The Skeptic won "strongest" **5/5**. Biggest blind spot: The Veteran ×3, The Architect ×2.

- **Reviewer 1 (Skeptic):** strongest = Skeptic (only one to land the statistical kill shot + cheapest falsifying test); blind spot = Architect (furnace-first green-lights infrastructure on the same instinct the principle forbids). *All missed:* the two-week retro-tagging trial is itself a guardrail adopted on instinct — and the two real assets (cheap WHERE-it-lives taxonomy vs. the counter/STOP machinery the volume critique kills) are conflated; the right move may be to ship the tag and never build the trigger.
- **Reviewer 2 (Architect):** strongest = Skeptic; blind spot = Veteran (tagging presupposes a stable category set Rex can't yet name). *All missed:* plan-review feedback may not be the right capture point — much is project-specific and unpromotable; and "fold one tagged line into retros" still adds friction to a workflow whose complaint is ceremony.
- **Reviewer 3 (Stranger):** strongest = Skeptic; blind spot = Veteran (never engages that the promotion target doesn't exist). *All missed:* none asks whether the feedback is recurrence-shaped vs. one-off; if one-off, no threshold ever justifies the machinery and the trial just defers the null. None reframes toward improving the baseline planning prompt so fewer corrections are needed.
- **Reviewer 4 (Long View):** strongest = Skeptic; blind spot = Architect (assumes the recurring-feedback problem is real and worth a durable surface). *All missed:* the cost of the measuring act — tagging during a low-volume trial trains attention onto friction and can manufacture the signal; the count measures throughput of annoyance, not wasted time.
- **Reviewer 5 (Veteran):** strongest = Skeptic; blind spot = Veteran (never interrogates whether the counter yields a valid signal at 8 tags). *All missed:* the lighter retro-grep path inherits the same n-too-small attribution problem; no one specifies what count justifies building vs. killing.

---

## Chairman synthesis

### Recommendation headline
Build nothing — answer "what do I re-correct?" from memory today; only if you genuinely can't should you append a tagged line to existing retros for two weeks, because the subsystem (and arguably the trial too) fails your own "evidence not instinct" rule at solo volume.

### Where the council agrees
Unanimous: don't build the parallel subsystem now; the volume critique is decisive; the kill shot is the missing count; back-propagation has no target; the separate-project trial is signal-dilution; it violates the house rule on move one; the taxonomy / WHERE-it-lives tag is the one cheap salvage.

### Where the council clashes
One fault line on the first *constructive* move: the Architect's "build the `planning-prompt.md` furnace first" (useful day one, where most feedback would land) vs. the other four's "build nothing yet, get the count / recall it from memory." Peer review flags the Architect as the chief blind spot here — it assumes the problem is real before it's counted.

### Blind spots the round caught
The retro-tagging trial is itself an instinct-adopted guardrail; the count may be uninterpretable at this volume (n too small, no kill/build threshold defined); the feedback may be one-off and unpromotable, not recurrence-shaped; the act of measuring can manufacture the signal; tagging adds ceremony to a workflow whose complaint is ceremony.

### The recommendation
Skip data collection; answer from memory first (ten-minute falsifying test). Mark each recurring correction as stable/promotable vs. one-off. (1) If you can name 2-3 stable promotable patterns → fix them directly, folding into CLAUDE.md or a new `planning-prompt.md`; build no machinery. (2) If you can't, or they're all one-off → drop the proposal. (3) If genuinely unsure and you still want the count → append one tagged line to *existing retros* only, and pre-commit to kill/build numbers. Don't run the llm-council trial. Keep the Architect's furnace, but gate it behind the memory check.

### The one thing to do first
Spend ten minutes writing down the recurring plan-review corrections you give, from memory, marking each "stable/promotable" or "one-off." If you can name 2-3 stable ones, fix them directly (CLAUDE.md or a new `planning-prompt.md`) and build no machinery. If you can't, the system is solving a phantom — drop it.

---

*Council session — 2026-06-09. Report: [council-report-2026-06-09-self-healing-loop.html](council-report-2026-06-09-self-healing-loop.html)*
