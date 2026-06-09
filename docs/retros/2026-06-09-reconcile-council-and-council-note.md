# Retro — 2026-06-09 09:21 CDT — PRD reconciliation council + "recommend a council at forks" note (D-009)   (4th session of the day)

## What this session did

Started as a follow-up question to the D-008 bookkeeping (3rd session) and turned into a real decision arc. Rex asked whether the kit has — or should have — a question that asks "do you have a Claude Design project to share?" That surfaced the live tension in his shifted workflow (Claude Design is becoming his default front door), drove an LLM Council on how to reconcile a bundle PRD with an interview PRD, and ended by shipping a `recommend-a-council-at-forks` note across the kit + this repo (D-009).

Decision/research work plus a small multi-file kit change. Outcome: **D-009 logged; the council note shipped to five places; reconciliation mechanism decided (KIND-routing + scope-gate); council-as-primitive rejected.**

## The arc

1. **Q: is there an on-ramp for Claude Design bundles?** Grepped the skills — nothing mentions Claude Design / bundle / handoff. The closest door is DSB's Cluster 0 Q0a (brand assets), which would *accept* a bundle and then mis-handle it (force its ~40 tokens / 6 fonts through the scale-first template). So the kit has no real on-ramp, and the nearest existing one is actively wrong for bundle input.
2. **Narrowed to "tokens-only on-ramp, leave the PRD alone"** — on the assumption the bundle PRD is inferior to an interview PRD.
3. **Rex corrected the crux:** because Claude Design lets him prototype and *see*, the bundle PRD often carries *superior* features/layouts; the interview PRD is stronger on strategy/scope/rationale. Neither overwrite nor ignore works — reconciliation is additive and judgment-heavy. He also floated the broader idea: wire the council into the kit's decision points.
4. **Ran a full LLM Council** ([report](../council/council-report-2026-06-09-reconcile.html) / [transcript](../council/council-transcript-2026-06-09-reconcile.md)) on two questions: (Q1) reconciliation mechanism, (Q2) council-as-primitive — with a reflexivity clause (if the council can't earn its keep here, that's evidence against Q2).
5. **Council verdict** (unanimous; Skeptic strongest 4/5, Long View biggest blind spot 5/5):
   - **Q1:** options (a) diff-and-adjudicate and (d) feed-into-intake are the *same loop at different layers* — the real risk is **scope-clobber** (prototype enthusiasm laundering deliberately-cut scope back in) plus a **self-adjudication bias** (the operator adjudicating is the one who made the prototype). Answer: human diff-and-adjudicate, section-keyed, **route deltas by KIND** — pure additions presumptively safe; scope-contradictions held as a **scope-gate** framed "you decided to cut this." Build nothing structural (consistent with D-008).
   - **Q2:** unanimous **no** to a wired-in primitive — ceremony, hard external-plugin dependency (portability), and a "primitive" saved only by peer review is a procedure to babysit. The one council-in-the-system form they endorsed: a *recommendation gated by a threshold*.
6. **Shipped D-009** — the recommend-don't-auto-run note in five places + the reconciliation finding.

## What landed (D-009)

- **Recommend-a-council note** in: this repo's [`CLAUDE.md`](../../CLAUDE.md); the scaffolded session-discipline of `context-engineering` ([flat template](../../skills/context-engineering/templates/claude-rules-flat-CLAUDE.md.template), [modular template](../../skills/context-engineering/templates/claude-rules-modular/session-discipline.md.template), [example](../../skills/context-engineering/examples/output-small/CLAUDE.md)); and a [`prd-creator` principle](../../skills/prd-creator/principles.md). Each cites its failure mode (architecture rule 2).
- **Decision logged:** [D-009](../DECISIONS.md) + [active mirror](../DECISIONS_ACTIVE.md), capturing both the council-placement decision and the Q1 reconciliation finding.
- Two deliberate design choices, both from the council's warnings: **scaffolded output is tool-agnostic** ("if such a skill is available" — never hardcodes the plugin, neutralizing the portability objection), and **the gate is tight** (costly-to-get-wrong AND hard-to-reverse — keeps it from becoming ritual).

## Misses / notes

- **My first instinct was wrong, twice this week + once today.** Council #1 and #2 on 2026-06-09 killed my opening proposals (the design-handoff skill), and this session my "leave the PRD alone" narrowing rested on a false assumption Rex corrected. The council (and Rex) caught all three. That track record is *itself* the evidence cited in the D-009 note.
- **Reflexivity caveat (honest):** Reviewer 5 flagged that the framing pre-selected a council-worthy question, so the reflexivity test was non-falsifiable as run — yet the council still voted itself down on independent grounds (portability + babysitting). Recorded in the transcript so it isn't laundered into a cleaner result than it was.
- **Verification is best-effort on the template change:** `examples/output-small` is a *compressed* rendering, not a literal substitution of the flat template, so the diff-against-example contract is weaker here than for a 1:1 template. Added the matching compressed bullet by hand and confirmed position; noted the limitation rather than claiming a clean dry-run diff.
- The bundle's strongest "this is superior" signal is in the **screenshots**, not the prose — a council blind-spot catch worth remembering before anyone invests in prose-merge tooling.

## Handoff — for a future session

- The **KIND-tagging reconciliation** (pure-addition vs scope-contradiction) is deferred to ~3 by-hand uses before encoding (Rule of Two/Three). First real use = next time a bundle and an interview PRD both exist.
- D-009's **revisit-if**: if the recommendation note proves dead text or ritual on real projects, loosen it or gate it behind an intake question.
- Still open from earlier (unchanged): the bundle-PRD on-ramp is intentionally *not* built; tokens-only `cp` is the product-side path (D-008); prd-creator intake.md aggregate fix; `block-deploy-cli.sh` / `block-worktree.sh` stdin fix.

## Commit / push

This session's artifacts — the reconciliation council set (data/report/transcript/mapping), D-009 in both decision files, the council note in five places, and this retro — committed and pushed together. No `the-council` changes.
