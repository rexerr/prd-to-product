## Retro — 2026-05-10 — Build-defaults brief

Continuous-mode exploration started after session D, ending in a single brief at [`docs/build-defaults-brief.md`](../build-defaults-brief.md). 152 lines, no skill changes, no code. The brief is the entry point for a future implementation session.

## What surfaced this session

The conversation walked through three distinct framings before landing on the right one. Each reframe came from the user and pushed me to drop my prior framing.

1. **My first framing — best-practice audits.** I proposed building audit-shaped skills for things like cross-reference links, `paths:` globs, hooks contract. The user redirected: "not audit, verification in the coding process that should be built in the template."
2. **My second framing — verification gates / hooks.** I worked through verify-vs-prompt-vs-sentinel-vs-rule-only for a pre-commit verification hook. The user redirected again: "I don't know enough to have an opinion. I just want to make sure that if I build a project with this tool, it will know what to do."
3. **My third framing — procedural guidance, not enforcement.** Acknowledged that the gap is *opinionated build procedure* (smallest-deployable-first, vertical slice, test-first, etc.), not verification gates. The user accepted this framing.
4. **The deeper user statement.** "I wouldn't know if it stumbles. I have just been refining and learning and iterating on the project makeup to make sure it's building the best way."

That fourth statement reframed the whole conversation. The meta-problem the user named: they cannot evaluate agent quality at the code level, so the skill's continuous-mode discipline ("wait for real failure modes, then fix") has a broken feedback loop *for them specifically*. They can't see stumbles. Stumbles will surface as projects that take longer than they should, or never ship, or ship with hidden debt — none of which are observable as discrete failure events.

## Why this is structurally different from prior work

The skill's existing principles assume the user is a competent evaluator of agent output. They are, for context-file structure — they audited two projects and produced sharp findings. But at the *code* level, they're explicitly not. The skill's rules earn their existence by citing failure modes the user has observed; that mechanism doesn't work for failures the user can't observe.

The response: borrow opinions that are validated *externally* — by 30 years of software engineering practice, by AGENTS.md research, by Anthropic insider sources — and bake them in as scaffolded defaults rather than waiting for user-observation to confirm them. This is a meaningful expansion of the skill's epistemic basis. Up to now every rule traced back to a failure mode the user (or this repo's own dog-fooding) had hit. The build-defaults bundle traces back to external evidence instead.

## What the brief proposes

Six candidate opinions, each with a failure mode, an external source, a landing site in the skill, and a "when this might be wrong" entry:

1. Smallest deployable first (*Continuous Delivery*, Humble & Farley, 2010).
2. Vertical slice over horizontal (*Pragmatic Programmer*, Hunt & Thomas, 1999).
3. Test-first for logic (Beck, 2002 — narrowed claim).
4. Visual-first for UI (already shipped; included for completeness).
5. Check / test pre-commit (prose, not hook — resolution from the verify-vs-prompt discussion).
6. Defer abstraction until the third instance (Rule of Three; Roberts via Fowler, 1999).

Plus: a "pilot one first" recommendation (start with item 1, the highest-conviction lowest-cost opinion), open questions for the implementation session, and a suggested first prompt for that session.

## The verify-vs-prompt resolution worth preserving

Item 5 in the brief came from a side conversation that resolved the verification-hook question. Worth recording because it was non-obvious and may need to be referenced again:

- **Verify shape** (hook runs the command before commit) — too slow, conflicts with mid-session verification work, false positives erode trust.
- **Prompt shape** (hook asks "did you run X?") — bypassable; the same model that hallucinates success will hallucinate the answer.
- **Sentinel shape** (hook checks for a proof-of-recent-verification file) — works but introduces a new coordination contract; complex for first stateful hook in the skill.
- **Rule-only** (sharpen `session-discipline.md`, no hook) — vulnerable to the hand-builder-skips-prose failure that our own new forcing-function principle predicts.

The resolution: ship rule-only first, watch one or two real sessions, escalate to sentinel only if rule-only fails. This sequencing matches the continuous-mode discipline — act on evidence, not on the principle alone — and reframes the forcing-function principle: it says *defaults are load-bearing*, not *every rule needs a hook*. Hooks fit when the failure mode lives at the tool-call layer; they don't fit when the failure lives in agent reasoning. This distinction is worth adding to `principles.md` as a one-line addition during the brief's implementation session.

## What's queued

One session: implement the brief, starting with the pilot opinion (item 1). Suggested first prompt is in the brief itself. Hard scope: the pilot is one template + ROADMAP scaffold update, ~50 lines. Inside the bug-fix cap.

The other five opinions wait for the pilot's evidence — did smallest-deployable-first actually catch the failure mode on a real project? If yes, ship the next. If no, revise before continuing. Standard continuous-mode discipline applied at the bundle level.

## Decisions made this session

- **Treat external evidence as a legitimate basis for skill rules**, not just observed-internal failure modes. This is the most important decision; it expands the skill's epistemic basis to cover failures the user can't observe.
- **Ship the build-defaults bundle as scaffolded *procedure*, not enforcement.** The opinions land as rules and templates, not as new hooks. The forcing-function principle still says defaults are load-bearing — but defaults can be prose-shaped when the failure mode lives in reasoning rather than tool calls.
- **Pilot before bundle.** Don't ship all six at once. Start with item 1; watch for the failure mode the brief claims it prevents; expand only if the pilot earns its existence.
- **Write the brief first, implementation later.** The opinions are too prescriptive to land silently. The brief is the cache transfer for the explicit conversation that has to happen before any opinion ships.

## Sources

- This conversation's chapter "Session C: act on 4 promoted items" → follow-up on verification gates (2026-05-10). Same chapter, separate sub-discussion.
- Brief produced this session: [`docs/build-defaults-brief.md`](../build-defaults-brief.md).
- HTML-brief as the structural model: [`docs/html-over-markdown-brief.md`](../html-over-markdown-brief.md).
- Recent retros that frame the meta-problem: [`2026-05-10-continuous-mode-iteration-1.md`](2026-05-10-continuous-mode-iteration-1.md), [`2026-05-10-continuous-mode-iteration-2.md`](2026-05-10-continuous-mode-iteration-2.md).
