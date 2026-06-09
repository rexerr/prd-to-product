# Council transcript — 2026-06-09 — Adopting Claude Design handoffs

## Framed question

Should the `prd-to-product` skill kit add a NEW SIBLING SKILL (`design-handoff-adopt`) to ingest Claude Design handoff bundles (HTML/CSS/JS prototypes + an existing token-CSS design system + screenshots + sometimes a PRD) and codify them into the kit's conventions? Alternatives: (B) a second *mode* inside the existing `design-system-bootstrap` skill; (C) no new capability — handle each bundle as a one-off; (D) defer until a second bundle appears. The kit is a single-developer workspace of single-purpose, markdown-only skills that don't auto-compose (chained by hand; an `/idea-to-product` orchestrator is proposed but unbuilt). Mechanical part = token transcription (`:root` → two-tier `tokens.css`, preserve `oklch()`, Tailwind off); judgment parts = multi-aesthetic reconciliation + pixel-perfect component recreation. Claude Design ships its own README instructing implementing agents. Pressure-test: is "extract/transcribe, don't generate" repeatable or bespoke? Does a 4th node deepen the chain-composition weakness? Honest ceiling?

Brief: [`docs/design-handoff-adopt-brief.md`](../design-handoff-adopt-brief.md).

## Anonymization mapping (for audit)

`{"A": "The Veteran", "B": "The Stranger", "C": "The Architect", "D": "The Long View", "E": "The Skeptic"}`

---

## Advisor responses (de-anonymized)

### The Skeptic
"Extract, don't generate" is not a skill — it's a transcription chore wearing a skill costume. What actually varies run to run: which aesthetic is a theme variant vs. dead-end; whether a screenshot is canonical or scratch; how a bespoke component decomposes; what the PRD says to keep. Every one is human judgment Claude Design's own README already steers. The repeatable 20% (copy `:root` verbatim into two-tier `tokens.css`, flip Tailwind off) is a 30-line slash command, not a fourth skill. Three failure modes: (1) **Fidelity trap** — the kit's two-tier shape won't be isomorphic to a 40-token oklch/motion/font system; mapping their structure onto yours mutates it, and a lossy "adopt" is strictly worse than using the bundle as-is (two sources of truth drift). (2) **N=1** — designing a reconciliation procedure from one bundle hard-codes its quirks as "the format." (3) **Chain debt** — a fourth non-composing node in a chain whose headline weakness is non-composition. Honest ceiling: reliably copies tokens and sets a flag; everything distinctive stays human. **Verdict: D, leaning C. Defer.**

### The Architect
"Adopt vs. bootstrap" is the wrong axis — it's a tool-handoff problem. Claude Design already emits a README telling agents how to implement. The kit's job isn't to re-implement that README; it's to translate the bundle into the kit's conventions so the rest of the kit can grip it. Decompose into three jobs of different repeatability: (1) **Token transcription** — deterministic; a skill earns its keep. (2) **Multi-aesthetic reconciliation** — pure human judgment; the skill can only surface the fork and ask. (3) **Pixel-perfect recreation** — the README's job; duplicating it is the trap. Honest answer: **B, narrowed** — an "adopt" mode in `design-system-bootstrap` scoped to job #1, job #2 as a prompt, job #3 delegated to the README. Smallest experiment: hand-transcribe the real bundle's tokens into `tokens.css` now, timing yourself. Mechanical → build the mode. Judgment calls → the README was the leverage, not the skill.

### The Stranger
Private vocabulary ("handoff bundle," "two-tier tokens.css," "qventus class," "oklch") hides the real question. Claude Design already ships a README telling an agent how to implement the bundle. So who is the user of `design-handoff-adopt`? One developer, maybe three times a year. You'd build, document, regression-test, and maintain a fourth skill to translate an artifact that comes with its own instructions into a house format that exists only because you invented it. Plainly: "Should I write a permanent tool to reformat a thing that already knows how to be implemented?" The answer is no. Token transcription is a script, not a skill; the judgment parts are what the README already hands a human-plus-agent. **Pick D.** Do the next bundle as a one-off, write down what was mechanical, only then consider extracting a script.

### The Long View
"Extract, don't generate" only compounds if the kit owns the artifact downstream. Three years out the binding question is who maintains the design system after adoption. Claude Design keeps shipping bundles; its README keeps improving; output gets richer every release. A skill whose core job is transcription races a moving target you don't control — depreciates fast. What compounds is the reconciliation layer — the two-tier `tokens.css` convention, write guard, doc structure. The durable asset isn't "adopt"; it's "the kit has an opinion about how an external design system gets governed once it's in." A fourth sibling deepens non-composition debt; the unbuilt orchestrator gets harder because adopt and bootstrap are mutually-exclusive entry modes (a routing decision). Option B pays that debt down: one skill, two entry modes, one routing target. Opportunity cost: skill #4 is weeks not spent on the orchestrator, the actual bottleneck. **Build the mode (B); defer the standalone.**

### The Veteran
Without auto-composition this is a fourth standalone node you invoke by hand on a bundle already in a folder. Standard playbook: don't build the inverse skill, write the README's procedure into a slash command. Most "ingest an existing system" tools collapse into bespoke judgment every run. Pressure-test (1) is the whole ballgame: only one part is mechanical — parsing `:root` into two-tier `tokens.css`, preserving `oklch()` verbatim, wiring theme variants is deterministic and better than freehand because it can't drift or hallucinate a palette. Everything past transcription is judgment; pixel-perfect recreation is what the README already hands the agent. Honest ceiling: reliable token adoption, advisory everything else. This isn't a sibling skill — it's a **token-adopt command plus a documented manual recreate step.** Build the mechanical 20% under the write guard; leave 80% as guided prose. **Verdict: not (A); scoped command, closest to (B).**

---

## Peer review

**Votes — strongest:** The Architect ×4, The Skeptic ×1. **Biggest blind spot:** The Long View ×2, The Veteran ×2, The Stranger ×1.

### What the council collectively missed
- **Fidelity / lossy-isomorphism (4 of 5 reviewers).** Even the "mechanical" 20% may be lossy: if the two-tier `tokens.css` can't losslessly hold a 40-token oklch/motion/font system, transcription itself manufactures drift between two sources of truth — which would argue against adopting the tokens at all, not just against a skill.
- **Versioned-bundle re-adoption lifecycle.** Every advisor treats the bundle as static; the real recurring cost is re-adopting an *updated* bundle into an *already-edited* `tokens.css` — a diff/merge problem, not a one-time extract.
- **The unexamined premise that the kit should own the tokens at all.** The bundle ships a working prototype + its own README; the highest-value move may be to consume it natively and let the kit govern only what it already owns.
- **The Long View's smuggled premise.** It justifies mode-over-sibling via an orchestrator the kit has explicitly not built — possibly a phantom requirement, since the kit's premise is hand-chaining.

### Individual reviews
1. **(Skeptic-seat)** strongest: Architect (decomposition + correct ownership + cheap timed test); blind spot: Long View (orchestrator-as-bottleneck smuggles in unbuilt capability); all-missed: kit-as-target taken as given; lossy-isomorphism may mean don't ingest at all.
2. **(Architect-seat)** strongest: Architect (cleanest decomposition + the one empirical test); blind spot: Long View (orchestrator may be a phantom requirement); all-missed: nobody confronts the fidelity trap to its conclusion.
3. **(Stranger-seat)** strongest: Architect (reframes axis, falsifiable experiment); blind spot: Stranger (names lossy-mapping risk then ignores it); all-missed: re-adoption is a diff/merge lifecycle, and "preserve oklch, Tailwind off" may not be stable across releases.
4. **(Long-View-seat)** strongest: Architect (only one to reframe + falsifiable test); blind spot: Veteran ("scoped command, closest to B" conflates command vs mode); all-missed: nobody asks whether the kit should own the tokens at all vs. merely reference them.
5. **(Veteran-seat)** strongest: Skeptic (the fidelity trap reframes the "safe" part as risky); blind spot: Veteran ("build the 20%" rests on the false premise that mapping is clean); all-missed: the strategic premise — bend the bundle into house format at all — goes unquestioned.

---

## Chairman synthesis

**Recommendation headline:** Don't build a fourth skill — and before building anything, run a one-hour timed hand-transcription of the real bundle to prove the "mechanical" token-adopt is actually lossless.

**Recommendation:** Do not build `design-handoff-adopt` as a fourth sibling skill (unanimous). Side with the Architect's decomposition gated by the Skeptic's fidelity test. Sequence: (1) Resolve ingest-at-all empirically — hand-transcribe the bundle's `:root` into the two-tier `tokens.css` and check losslessness; if it mutates the oklch/motion/font structure, **do not adopt** — keep the bundle authoritative, let the kit reference it, govern only what the kit already owns. (2) If and only if lossless and fast, build the mechanical 20% as a **slash command under the write guard** (not a skill, not a DSB mode — a command is the smallest artifact and avoids the routing-mode debt); scope to parse `:root`, preserve `oklch()`, fold into two-tier `tokens.css`, Tailwind off; leave reconciliation as an advisory prompt and recreation delegated to the README. (3) Don't design a reconciliation procedure from this one bundle (N=1); treat the re-adoption/diff-merge lifecycle as an open question for bundle #2.

**The one thing to do first:** Open the real Claude Design bundle and hand-transcribe its `:root` custom properties into the kit's two-tier `tokens.css`, on a timer. Test one thing: does every token (oklch, motion, font) land losslessly? Lossless and under ~30 min → build the token-adopt command. Lossy or fighting the structure → don't adopt; keep the bundle authoritative.

### Council alignment

| Advisor | Position | Core argument |
|---|---|---|
| The Skeptic | Defer, fidelity-first | Transcription is a command not a skill, and mapping a 40-token system onto the two-tier shape is lossy — adopt may create a second drifting source of truth. |
| The Architect | Narrowed mode/command | Decompose into three jobs by repeatability, automate only deterministic transcription, run a timed hand-transcription to settle build-vs-defer. |
| The Stranger | Defer (D) | It's a permanent tool to reformat an artifact that already ships its own README — do the next bundle as a one-off first. |
| The Long View | Build the mode (B) | Transcription races a moving target; the durable asset is the kit's governance layer, and one skill with two modes pays down orchestrator debt. |
| The Veteran | Scoped command (~B) | Build the mechanical 20% under the write guard; leave the judgment-laden 80% as guided prose — a command, not a sibling skill. |

---

*Council session — 2026-06-09. Report: [`council-report-2026-06-09-design-handoff.html`](council-report-2026-06-09-design-handoff.html).*
