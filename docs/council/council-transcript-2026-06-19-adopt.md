# Council transcript — design-system-adopt: build the skill, or ship a rule?

**Date:** 2026-06-19
**Anonymization mapping:** A=The Long View, B=The Stranger, C=The Veteran, D=The Skeptic, E=The Architect

---

## Framed question

Should Rex (single-developer, markdown-only Claude Code skill workspace) build a new `design-system-adopt` skill that ingests a finished "Claude Design" artifact (a real ~1,200-line prop-driven React component library) and preserves it at three levels — tokens, components, AND composition/fidelity — accepting that it crosses his existing `design-system-bootstrap` skill's deliberate invariant ("never feature components")? Bootstrap + a planned audit mode stays for greenfield/small cases.

**Grounded failure (the-council):** the design→app handoff harvested ONLY token values; zero components were adopted, every page rebuilt inline, composition drifted 100%. "We enforced token compliance, we never enforced design fidelity; the unenforced axis drifted every time."

**Sub-questions:** (1) is "port existing" safe where "improvise" is not? (2) can composition fidelity be enforced by a skill/rule, or only a human gate? (3) is the fix a lightweight discipline + import rule rather than a heavy generator? (4) ROI for a single-dev workspace?

---

## Advisor responses (de-anonymized)

### The Skeptic
Composition fidelity is unenforceable by a markdown skill, and that's the flaw that sinks the heavy version. In the-council the design existed, the components existed, and a human-plus-agent loop with a linter STILL rebuilt every surface inline. The drift wasn't caused by a missing skill — it was caused by the path of least resistance being "write fresh JSX." A `design-system-adopt` skill ships markdown; it cannot ship a build-time diff gate, block a PR, or force an agent to open the reference. So it says "compose from these, diff against the design" — and the next agent rebuilds inline because it's faster and nobody's watching. You'd encode the unenforced axis a second time and call it enforcement. Sub-question 1 is a trap: "port not invent" sounds safe, but JSX-to-app translation IS invention — routing, state wiring, data fetching, slot composition. The component boundary is where improvisation re-enters. Bootstrap's invariant was "agents handed a design artifact improvise," and adopt hands an agent a design artifact. Enforceable only if something mechanical checks it. Build that check first. If you can't name the mechanical enforcer, the skill is theater, and a 300-line generator is theater with a budget. Ship the rule, wire the gate, see if fidelity holds for one cycle.

### The Architect
Composition fidelity is the entire problem, and tokens-plus-components doesn't touch it. Even if adopt ports TarotCard perfectly, an agent building a page still decides HOW to arrange TarotCard, Channel, and Waveform — invented fresh every time. You can port a component library and still get 100% composition drift, because composition lives in the page, not the library. So sub-question 1 is a trap: porting components is necessary and safe, but it solves the cheap half. The expensive half — layout/structure — has no artifact to port unless the Claude Design system ALSO shipped the assembled pages, not just the component kit. Reframe: the variable you're optimizing isn't "should the skill write components." It's "what is the reference of record, and is it present at the moment of composition." The drift happened because the finished design was ABSENT from the build context. Nothing was looked at because nothing was there to look at. Simplest first move that proves it: skip the skill. Next handoff, drop the actual rendered Claude Design pages (screenshots + component source) into the repo as `design/reference/`, add one rule — "every new surface diffs against its reference page before commit; no reference, no merge." Run it once. If fidelity holds, your fix was presence + a gate, not a generator. If it drifts anyway, you've proven composition needs a human review gate, and no skill saves you. Either outcome kills a wrong variable cheaply.

### The Stranger
Composition fidelity drifted "100% of the time" — but I can't see a single number behind that. How many surfaces? Three pages or thirty? "Citable failure" is doing a lot of work for one project observed once. A failure you can name in a quotable sentence is not the same as a failure you've measured. Before building a skill to fix drift, I'd want to know the drift was big enough to hurt anyone. Who is actually affected? One developer, on his own projects. There is no team, no handoff to a stranger who never saw the design. The "we" in "we enforced token compliance" is one person. So the real question isn't "can a skill enforce fidelity" — it's "why didn't Rex, the only person in the loop, open the design and copy the components when he wrote the app?" If the answer is "I forgot / it was easier to retype," a skill won't fix a habit; it'll be another file he forgets to invoke. Unspoken assumption: that the components are worth preserving as-built. TarotCard, Waveform, Channel sound bespoke to one app. "Reusable library" describes their form, not their reuse. Have any been reused across two projects? If not, "adopt and preserve fidelity" is preserving a thing used once. Build the thin discipline-rule — reversible, tests the habit; if Rex still rebuilds inline anyway, you've learned the generator would've been forgotten too, cheaply.

### The Long View
Composition divergence didn't drift because nobody built the right tool — it drifted because three years of incentives all point at "rebuild inline." An adopt skill ships once, but the gravity that beat it last time keeps pulling every session. Inline JSX is the local minimum — faster to type, no import to reconcile, no design file to re-open. A markdown skill cannot out-pull that gravity at build time; only a gate the agent must pass through can. Play it forward: build the heavy generator and in three years you own a second skill that overlaps bootstrap, contradicts its headline invariant, and depreciates every time Claude Design changes its export shape — future-Rex pays the tax of remembering which, the root-pile sprawl your CLAUDE.md legislates against. Generators rot; the ported library rots faster. What compounds instead is the rule and the failure citation — "when a Claude Design system ships real components, adopt the files and compose from them — never rebuild; the unenforced axis drifts every time" — which survives export-format churn and ports to the next design tool. Pick option 3: thin wiring plus an always-on fidelity rule, teeth being a human diff-against-design review gate. Don't build the generator until you've run the rule manually three times. A rule you delete costs nothing; a skill you maintain costs forever.

### The Veteran
Composition fidelity drifted because nobody was forced to look at the design — and a skill cannot force that. The pattern I've watched a dozen times: teams enforce the cheap-to-check axis (tokens, a linter) and declare the expensive-to-check axis "covered" because a tool now exists. Building adopt risks repeating the exact failure one level up — generated component files satisfy "components were ported," composition drifts again, except now you trust it less because a skill blessed it. The standard playbook is right here and your case is not special: the fix for "components got rebuilt instead of imported" is wiring, not a generator. Copy the component files in, add an always-on rule — "a design library exists at X/; import from it, never rebuild a surface it already covers; rebuilding requires a cited reason." That rule cites its failure mode (100% composition drift, the-council), exactly your house style; ~20 lines, reversible, ports the real components rather than a generator's idea of them. Be honest on enforcement: tokens were enforceable because compliance is mechanically checkable; fidelity is a judgment call, so it lands on a human review gate, not a skill. ROI: single-dev workspace, reversible problem, real fix is a rule. Don't build the heavy skill; ship discipline + import rule, watch two real handoffs, then ask whether a generator earns its keep.

---

## Peer review (de-anonymized)

**Vote tally — Strongest:** The Architect ×5. **Biggest blind spot:** The Stranger ×3, The Long View ×2.

### Reviewer 01 — The Skeptic
- **Strongest:** The Architect — isolates the true variable (the finished design absent from build context at composition time) and proposes a one-cycle test that kills the wrong answer cheaply.
- **Biggest blind spot:** The Stranger — its "were these reused" challenge misreads the goal: the artifact is the deliverable's fidelity to its own design, not cross-project reuse.
- **What all five missed:** None asks whether Claude Design could ship the assembled pages/layout as a portable artifact — composition leverage may be upstream in what the tool exports. And none reconciles against Rex's DECISIONS process: crossing "never feature components" is exactly the costly, hard-to-reverse fork CLAUDE.md says to council AND log, not quietly ship.

### Reviewer 02 — The Architect
- **Strongest:** The Architect — composition lives in the page, not the library; turns it into a one-cycle test that resolves either way.
- **Biggest blind spot:** The Stranger — risks dismissing a real named failure on a technicality; never asks whether the absent reference (not Rex's discipline) was the cause.
- **What all five missed:** None costed the dominant single-dev cost — the recurring attention tax of one more skill/rule vs the one-time cost of copying components by hand. All converge on "rule + human gate" without confronting that Rex is the only gate and already failed to open the design once, so the gate's enforcer is the same unreliable habit.

### Reviewer 03 — The Stranger
- **Strongest:** The Architect — locates the reference-of-record-absent mechanism, yielding a cheap falsifiable test rather than another rule.
- **Biggest blind spot:** The Stranger — nearly dismisses fidelity as a non-problem while missing that composition drift hurts even a single-use app's quality.
- **What all five missed:** None separates intra-app consistency (page 2 vs page 1 — snapshot/lint-checkable WITHOUT a human) from design-fidelity-to-source (needs a human). Different enforcers; cheapest win is the former. And none costs re-export staleness: the Claude Design source regenerates on every change, so a committed "reference of record" silently goes stale.

### Reviewer 04 — The Long View
- **Strongest:** The Architect — turns the diagnosis into a presence-plus-gate test that falsifies the variable cheaply either way.
- **Biggest blind spot:** The Long View — frames it all as incentive gravity and rule-vs-generator while never noticing even a perfect ported library leaves composition unported.
- **What all five missed:** None asks whether a dev who already failed to open the design will honor a self-imposed "diff against reference, no merge" gate — every recommendation relocates the same unenforced discipline from "copy components" to "pass the gate," inheriting the exact failure it diagnoses.

### Reviewer 05 — The Veteran
- **Strongest:** The Architect — locates the mechanism (missing artifact is the assembled reference pages, not ported components) and proposes a presence-plus-gate test.
- **Biggest blind spot:** The Long View — never asks whether the bespoke components are reused anywhere, so argues to preserve fidelity for possible one-offs.
- **What all five missed:** All accept the agent should preserve the design's composition, but none asks whether the original Claude Design pages are themselves the spec worth holding to — whether a one-dev single-app artifact deserves fidelity enforcement at all vs letting composition legitimately evolve per surface. The only gate-staffer is the same person who skipped the design last time.

---

## Chairman synthesis

### Recommendation headline
Don't build the heavy `design-system-adopt` skill — ship a ~20-line always-on import rule plus a present, cheap human diff-against-source gate, log the invariant-crossing as a decision regardless, and only revisit a generator after the rule survives three real handoffs.

### Where the council agrees
Near-total consensus on the diagnosis: (1) composition fidelity is the real problem and it is NOT in the library; (2) a markdown skill cannot mechanically enforce fidelity; (3) the fix is wiring, not a generator; (4) the root cause was ABSENCE of the design from the build context, not a missing tool.

### Where the council clashes
Little clash on the verdict — all five say "don't build the heavy skill, ship the rule." Divergence is on whether even the rule works: the Skeptic (theater without a mechanical enforcer), the Stranger (maybe no real problem), vs the Architect/Long View (presence + gate probably works, and proves the variable cheaply either way). Nobody defends the generator.

### Blind spots the council caught
(1) Two "compositions" conflated — intra-app consistency (mechanically checkable) vs fidelity-to-source (needs a human). (2) The gate's enforcer is the same habit that already failed. (3) Re-export staleness — the reference goes stale on every redesign. (4) The invariant crossing must be a logged D-NNN decision per CLAUDE.md, even for the lightweight rule.

### The recommendation
Build the rule, not the skill — and don't pretend the rule is self-enforcing. Skip the 300-line generator (overlaps bootstrap, contradicts its invariant, rots on export changes, solves only the cheap half). Build the rule around the reviewers' two distinctions: (1) **split composition** — make intra-app consistency mechanical (a session-start check / emitted hook that greps for inline re-implementations of already-imported components), and make fidelity-to-source a human gate that survives by being **cheap and present** (rendered reference pages live in-repo, rule fires every new-surface session) rather than relying on diligence; (2) **address staleness** — re-snapshot the reference on each design change with a dated marker, flag surfaces diffed against a stale reference; (3) **log a D-NNN decision** recording the invariant crossing either way. ROI favors the deletable rule over the maintained generator in a single-dev workspace. The Stranger's "is this real?" is answered by running the rule for three handoffs.

### The one thing to do first
On the NEXT real design→app handoff, before writing any rule or skill: drop the rendered Claude Design pages (screenshots + component source) into the repo as `design/reference/`, copy the real component files in, and add one ~20-line always-on import rule citing its failure mode (100% composition drift, the-council). Run one cycle, then decide whether anything heavier earns its keep. Open the D-NNN decision entry as part of the same change.
