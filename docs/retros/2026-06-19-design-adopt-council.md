# Retro — 2026-06-19 07:31 CDT — design-adopt council (composition-fidelity extension to D-008)   (2nd session of the day)

## What was completed

- Started from a token-weight question (turning off the Cowork `design` plugin) and an offer to harvest its `accessibility-review` / `design-system` skills. Traced it into the real pain: `design-system-bootstrap` greenfield-only premise vs. Rex's "arrive with a finished Claude Design system" workflow.
- **Grounded investigation of `sites/the-council`** (two read-only Explore passes). First pass misread the system as "healthy" by grading token discipline; corrected axis on Rex's pushback. Confirmed: the bundle shipped a real ~1,200-line prop-driven React library, **0% adopted**, every surface rebuilt inline, **composition diverged 100%**, only token values survived. Evidence in [council transcript](council/council-transcript-2026-06-19-adopt.md).
- Ran a full **LLM Council** (5 advisors + 5 reviewers + chairman) on "build a `design-system-adopt` skill?" → **5/5 don't build; ship a product-side import rule + presence + a split (mechanical/human) gate.** Artifacts: [report](council/council-report-2026-06-19-adopt.html), [transcript](council/council-transcript-2026-06-19-adopt.md), [data](council/council-data-2026-06-19-adopt.json), [mapping](council/mapping-2026-06-19-adopt.json).
- **Discovered the concept was already decided** — [D-008](DECISIONS.md), 2026-06-09. Per [D-027](DECISIONS.md) (concept-keyed, append-don't-mint) recorded the verdict as an **extension of D-008**, not a new D-NNN.
- Extended [D-008](DECISIONS.md) with the composition-fidelity dimension; upgraded [`design-handoff-adoption.md`](design-handoff-adoption.md) (new finding section + reworked playbook + a ready-to-drop `.claude/rules/design-adoption.md` import rule); light extension to the [D-008 active mirror](DECISIONS_ACTIVE.md). No kit skill built (decline holds).

## Failure this session

- **Tag:** lost context
- **Name the artifact.** I convened a full 11-agent LLM Council on "should the kit adopt Claude Design bundles" **without first reading [D-008](DECISIONS.md)**, which decided exactly that concept on 2026-06-09 via two prior councils. The new council's headline verdict ("don't build the adopt skill") therefore **restates D-008**; only the composition-fidelity dimension was net-new. Cost: ~11 duplicated subagent spawns of deliberation that [D-027](DECISIONS.md)'s "read before re-proposing" rule exists precisely to prevent.
- **Lesson → change.** The guardrail already exists (D-027); this was a failure to *apply* it, not a missing rule. **Tool or agent?** Agent (me) — before councilling/re-proposing any concept, grep `DECISIONS.md` for it first. **Does it generalize?** Yes, but the rule is already written and binding — adding a second copy would be the accretion the repo's kill-watch warns against. **→ No new guardrail.** Recorded here as the citable instance of D-027 being skipped; if it recurs, *then* D-027 needs a stronger prompt (a pre-council checklist), per its own Revisit-if.

## What went right (worth keeping)

- The **grounded Explore passes overturned both my first read and Rex's memory** — "healthy token discipline" and "tokens didn't carry over" were both wrong; the truth (tokens carried, components+composition didn't) only emerged from reading the actual files. Vindicates the repo's grounded-over-theory stance.
- The duplicate council still **earned the composition-fidelity dimension** D-008 genuinely lacked (D-008 was tokens-only), so the session is net-positive despite the process miss — the extension is real new knowledge, not ceremony.

## Scope

Docs-only: [DECISIONS.md](DECISIONS.md) (D-008 extension), [design-handoff-adoption.md](design-handoff-adoption.md), [DECISIONS_ACTIVE.md](DECISIONS_ACTIVE.md), this retro, + council artifacts under `council/`. No skill/code touched; decline from D-008 stands.
