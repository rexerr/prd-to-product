# Council transcript — 2026-07-01 — Project-setup connective layer (build vs compose, delivery)

**Report:** [`council-report-2026-07-01-project-setup.html`](council-report-2026-07-01-project-setup.html) · **Feeds:** [`../handoffs/project-setup-system-handoff.md`](../handoffs/project-setup-system-handoff.md), Track-1/Track-3 findings.

## Framed question

What shape should a "project-setup connective layer" take for prd-to-product's Claude Code skill ecosystem — how much to BUILD vs COMPOSE, and how to DELIVER it (plugin/marketplace vs vendored)? Owner (Rex) is a designer who delegates ALL engineering judgment to Claude. A two-project review (seance native-iOS shipped; Strays RN/Expo frozen at the trio→build seam) verified a recurring gap between the trio (which plans+scaffolds) and standing up stack/security/tests/deploy. Deep research found the market sells every individual CAPABILITY as maintained tools but NOBODY sells the per-project-type composition+verification GLUE. Guardrail (prior council): capture durable QUESTIONS not perishable ANSWERS; composing externally-maintained tools is not freezing. Hard constraint: verification often can't run in the agent's shell (iOS CI industry-broken on Xcode 26) so it must route to a capable actor. Four forks: (1) build vs compose the glue; (2) delivery plugin/marketplace vs vendored; (3) starter lane per stack; (4) iOS submission Fastlane vs Xcode Cloud.

## Anonymization mapping (for audit)

`A = The Veteran · B = The Stranger · C = The Long View · D = The Skeptic · E = The Architect`

## Verdict (chairman)

**COMPOSE the glue and VENDOR it now — but build nothing until you prove a specific human can actually read a red verification rung, because the whole routing design silently assumes a "capable actor" the premise says doesn't exist.**

Direction (compose over build; vendor over plugin; defer #3/#4 with a maintained-option rule) is **high-confidence** — it survives even if the premises fail. The specific mechanism (cruft + a verification-routing table) is **low-to-moderate confidence**, because the peer round exposed three unverified load-bearing premises:

1. **A "capable actor" to judge a red rung may not exist** — the owner delegates all engineering judgment, so the routing may terminate at a blind judge (unfalsifiable theater).
2. **cruft's `cruft update` may propagate pins, not questions** — structurally contradicting the "capture questions not answers" guardrail (asserted by 4 advisors, verified by none).
3. **"Nobody sells the glue" at N=2 is equally consistent with "the glue isn't worth building"** — nobody priced the abstraction against just hand-writing setup notes twice.

**First step:** hand-write the verification-routing table for one real frozen seam (Strays' RN seam or seance's iOS gap) — columns: *check / who judges it / what red looks like / what green looks like* — then physically test whether Rex can read a deliberately-failed rung. If he can't tell actionable from noise, redesign around CI-as-judge or don't build. If it unfreezes the seam, the layer is real — build outward from that proven instance.

## Peer-review vote tally

- **Strongest:** The Long View ×3, The Skeptic ×2
- **Biggest blind spot:** The Skeptic ×2, The Veteran ×2, The Long View ×1

## What the council collectively missed (highest-value output)

- **No advisor established that a "capable actor" who can judge a red verification rung actually exists** — every recommendation except the Skeptic's assumes one. (Reviewers 1, 3)
- **"cruft propagates only shape/questions" was asserted, never verified** — the compose-with-cruft consensus may rest on a mechanism that can't honor the guardrail. (Reviewers 1, 2)
- **"Nobody sells the glue" treated as verified whitespace by all five** — at N=2 equally consistent with "unsellable/unneeded"; whether to build ANYTHING vs hand-notes went unasked. (Reviewers 1, 2, 4, 5)
- **The compose verdict is an unpriced abstraction** — no one costed the checklist+routing-table maintenance against writing per-project notes by hand twice. (Reviewer 5)
- **"iOS CI broken/PTY wall" was treated as eternal** — itself a perishable fact the guardrail warns will rot. (Reviewer 4)

---

## Advisor responses (de-anonymized)

### The Skeptic
The composition thesis is sound; the delivery mechanism is where this dies. The fatal flaw hides in Fork #1's own hard constraint: verification "must route to the capable actor — owner's eye, GUI, or CI," but the capable actor is a designer who delegates ALL engineering judgment to Claude. So the verify-it-ran ladder terminates at a human who cannot judge whether the rung passed. "Route to the owner's eye" is a null instruction when the eye can't read the signal. The iOS PTY wall isn't the real wall — the JUDGMENT wall is. Who confirms `cruft check` failing in CI means something actionable vs noise? Not Rex. So either CI becomes the judge (and now you're maintaining CI config — the exact perishable-pin rot the guardrail forbids), or the ladder is theater. Second: cruft's linked-template model contradicts the guardrail — `cruft update` propagates template CHANGES, meaning the template carries answers concrete enough to propagate (pins). You can't simultaneously (a) capture only durable questions and (b) run a drift-propagation mechanism — a question has nothing to propagate. Third: "nobody sells the glue" for a two-project single-designer sample isn't whitespace — it's a market of one; the composition surface changes faster than any single maintainer can track. You'd become the under-resourced Fastlane you're wary of. Next step: before ANY build, write down who judges each verification rung when red — by name. If it's "Rex" and Rex can't read it, stop.

### The Architect
COMPOSE the glue; author only the composition manifest and the verification-routing table — nothing that pins a version. The whitespace isn't a capability gap, it's an ORCHESTRATION + JUDGMENT-ROUTING gap, so building tools would put you in a maintenance business you can't staff. Borrow cruft's linked-template model but bind it to EXTERNALLY-MAINTAINED templates (Obytes for RN, Tuist for iOS), not one you author — so `cruft update` pulls the maintainer's fixes, not Rex's rotting pins. The only thing you write is the durable QUESTION set and the verify-it-ran ladder. Reframe the hard constraint: the PTY wall isn't a bug to engineer around, it's the DEFINING FEATURE. The layer's real job is "route each verification to the actor who can actually judge it." That table (agent-shell / owner's-eye / GUI / CI) IS the product. Fork #2: vendored, decisively — plugins pay off at N-projects and multiple consumers; you have one developer. Vendoring drifts, but `cruft check` in CI turns drift into a visible signal. #3/#4: defer with a rule — company-backed maintained option when Rex can't judge staleness (Tuist over XcodeGen; Xcode Cloud over Fastlane). Biggest risk: the routing table ossifies into stale prose. Counter: at N=2 this is over-engineering a pattern not a product. Refuse to build until the table earns it. Next step: hand-write the verification-routing table for Strays' frozen seam — four columns, real checks. If it unfreezes Strays, the layer is real.

### The Stranger
Compose, don't build. Deliver as a PLUGIN. Defer #3/#4. The load-bearing fact: "verify-it-ran ladder"/"PTY wall" means the agent literally cannot see whether what it set up works. The only user is Rex — a designer who cannot judge when an engineering pin is stale; his lived experience of a self-built glue layer is: works twice, then silently rots, no eye to catch it. BUILD is disqualified not on effort but on maintainability-by-this-specific-human. Compose externally-maintained tools (cruft for drift-binding, doctor-probes reporting to Rex's eye/CI, not the agent's shell). The durable thing you author is the question checklist per stack, never the answers. Delivery: plugin, because vendored copies drift and Rex can't see the drift; the plugin is the one channel where "cruft check in CI" can nag him. Biggest risk: even the composition layer names tools that die (Fastlane #29713). Counterargument: a checklist with no runnable teeth is just a nag Rex ignores. Next step: write the per-stack verification checklist — questions only, zero pins — test against Strays' frozen seam.

### The Long View
Compose, don't build; VENDOR FIRST, plugin later; defer #3/#4 with a decision rule. Three years out, what compounds is not the glue — it's the QUESTION SET. Specific pins depreciate to zero on a 6–18 month clock; you'll be wrong about Fastlane-vs-Xcode-Cloud within a year regardless. What survives is the durable checklist and the routing. Author that; borrow everything executable. Second-order effect: if you BUILD the glue, you inherit a maintenance liability only you can service — a non-engineer maintaining perishable config is the exact rot the prior council warned against. Composing cruft + doctor-probes + CI DAGs means someone else eats the upgrade treadmill; that asymmetry decides fork #1 alone. Delivery: vendor now — plugins GA'd nine months ago, young, conventions will churn; vendoring is reversible and you gain real usage from seance/Strays before freezing a distribution shape. Adopt cruft's linked-template model so vendored copies aren't orphaned. Biggest risk: the verification-routing abstraction is genuinely hard and you'll under-build it. Counter: composition means N brittle external dependencies. Next step: write the durable question-set checklist for one stack (RN/Strays) — no pins.

### The Veteran
Compose, don't build; vendor now, marketplace later; defer #3/#4 with a decision rule. The obvious move is to write a big helpful setup skill — the trap, the "freeze perishable judgment" failure the prior council flagged; setup scripts rot into liabilities. The skill authors the checklist of durable questions per stack and the composition ORDER, and shells out to externally-maintained tools for every answer. Adopt cruft's linked-template model conceptually. Adopt the verify-it-ran ladder — but the agent cannot judge iOS CI in its own shell, so verification is a ROUTING artifact: names who checks (owner's eye / GUI / CI green), asserts the specific symptom, refuses to self-certify. That's the whole product. Vendor now — the GA marketplace packaging tax isn't worth it before two consumers; you have two projects. Let `cruft check` in CI be your drift alarm. #3/#4: Defer with a rule. iOS: Xcode Cloud until you outgrow the free 25 hrs — Fastlane's "#29713 is this dead?" is the tell. Starters: official-minimal for RN, XcodeGen for iOS — single-maintainer simplicity you can read. Biggest risk: verification ladder becomes checkbox theater. Counter: two projects may not generalize. Next step: write the iOS durable-question checklist from seance's actual gap.

## Peer reviews (de-anonymized)

**Reviewer 1** — strongest: The Long View (durable question-set is the only compounding asset while pins depreciate); blind spot: The Long View (never resolves the cruft/guardrail contradiction). *All missed:* nobody establishes a capable actor exists; nobody questions whether market-of-one is opportunity or a too-fast-moving surface.

**Reviewer 2** — strongest: The Long View (time-axis argument, tightest chain); blind spot: The Skeptic (surfaces the two contradictions). *All missed:* nobody verified cruft propagates questions not pins; nobody asked whether the whitespace is niche vs hard-to-staff.

**Reviewer 3** — strongest: The Long View (maintainability-asymmetry + depreciation clock); blind spot: The Skeptic (sharpest structural critique). *All missed:* even a pure question-set needs Rex to judge red/green, so the Skeptic's contradiction sinks every response; at N=2 this may be a personal workflow not a product.

**Reviewer 4** — strongest: The Skeptic (exposes the fatal recursion); blind spot: The Veteran (names concrete pins while endorsing questions-only). *All missed:* whether to build ANYTHING vs hand-notes went unasked; "iOS CI broken" treated as eternal though itself perishable.

**Reviewer 5** — strongest: The Skeptic (drives the guardrail to its hardest conclusion); blind spot: The Veteran (concrete pins vs questions-only). *All missed:* "nobody sells the glue" never checked; the compose verdict is an unpriced abstraction vs hand-notes-twice.
</content>
