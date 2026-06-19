# Retro — 2026-06-19 00:01 CDT — plan-review craft/voice rewrite   (1st session of the day)

Continuation of the 2026-06-18 plan-review rehost ([prior retro](2026-06-18-plan-review-rehost.md)). After Plan 1 shipped, Rex read the skill and judged it badly written — "not how skills are normally written, especially the intro." This session was the craft pass that followed.

## What was completed

- **Grounded a style rubric in four sources before rewriting** (Rex asked "how do I know you researched this enough?"): skill-creator's own authoring guide + its grader rubric, a 7-skill corpus mine (4 first-party bundle skills + Rex's own furnace-plan/prd-creator/context-engineering via an Explore agent), and the repo's craft cribs (C-15, CF-01, C-17). Produced a cited rubric (verb-first opening, imperative voice, hoist binding rules, failure-tags, explain-why-not-MUSTs, close with scope).
- **Full craft/voice rewrite** of `skills/plan-review/SKILL.md`: first-person-Rex confessional → imperative-to-the-model with Rex in third person; buried hard rule → hoisted top section; added `*Failure it prevents:*` tags and a closing `## What this skill is not`. 216 → 111 lines (part reflow — the old file was hard-wrapped — part genuine cuts).
- **Reframed honesty from exhortation to forcing functions** (Rex's catch — see Failure): cut "be honest / never oversell," made the two latent mechanisms load-bearing instead — **citation-or-demote** (an unanchored claim drops to "Could not verify," can't pose as a finding) and the **bounded verdict** ("safe" is not an available output).
- Regenerated the deploy zip from the final skill (the earlier zip was built from the pre-craft-pass version).

## Failure this session

- **Tag:** none landed (all three misses were caught in working-tree iteration, before any commit) — but the craft lesson is real and recurring.
- **Name the artifact:** three things Rex had to catch, same root: **I default to exhortation and meta-prose in skill text instead of forcing functions and plain instructions.**
  1. Framed the rewrite target as conforming to "your house template / your taste" — but those templates were *prior Claude output*, not Rex's fixed taste. He corrected: don't treat them as unchangeable.
  2. Wrote a section literally titled "honesty contract" that *asked* the model to "be honest / never oversell." Exhortation — the exact thing skill-creator's guide and furnace-plan's whole philosophy reject. Rex: *"I don't think asking it to be honest will make it honest."*
  3. Over-corrected #2 into a meta-essay explaining *why* exhortation fails ("what keeps it trustworthy is not your good intentions…"). Rex: *"this sentence is gobbledygook."* I'd smuggled our design conversation into the skill.
- **Tool or agent?** Agent judgment — a prose-craft default, not a tooling gap.
- **Does it generalize?** Yes, strongly. It's a class: when writing instructions for a model, I reach for persuasion and rationale-narration instead of (a) a forcing function that makes the wrong path structurally visible, or (b) a plain directive. The skill should *contain the mechanism*, not *argue for the behavior*.
- **→ The change it demands:** none as a repo rule yet (Rule of Two — this is the first clean instance logged). A candidate guardrail if it recurs: a furnace/skill-authoring check — "every behavioral instruction is a forcing function or a plain directive, not an exhortation; the skill never narrates its own design rationale." Watch for a second instance before landing it.

## What verification did and did NOT cover

- **Did:** gate greps green ("Questions for me" → 0, host-mechanic strings → 0, trigger phrases intact, no stale "honesty contract" cross-refs); all behavior-bearing mechanics grep-confirmed present and unchanged (3 bucket defs, only-log-furnace-plans, the disjointness rule, stop-loop rule, staleness check, the 7 checks, both examples, the verdict); dangling cross-reference fixed; regenerated zip byte-matches the working tree; sections re-read with Rex.
- **Did NOT:** **no evals were run.** skill-creator's own method is draft → test on real prompts → human review → iterate; this rewrite is validated by craft reasoning + Rex's read, **not** by measured review quality. The claim "this is better written" is a structural/taste judgment, not a benchmarked one. And Cowork live behavior is unverified — the skill isn't deployed.

## Files changed

- `skills/plan-review/SKILL.md` — craft/voice rewrite (uncommitted at retro-write; committed with this retro).
- `skills/plan-review.zip` — regenerated (gitignored; local deploy artifact only).

## Key decisions made

- No new `D-NNN` — this is a prose/voice refactor of an already-decided skill (D-042 covers hosting + host-agnostic). No new binding constraint.
- Structural call: plan-review is a *judgment/review* skill, not a *generator/procedure* skill, so it deliberately does **not** use the prd-creator `Binding contracts → Procedure` skeleton.

## Open items

- **Deploy (Rex, in Cowork) — STILL PENDING, now with the craft-pass skill.** Upload `skills/plan-review.zip` (regenerated this session) via Settings → Skills; confirm it updates; smoke-test `/plan-review`. The earlier zip is superseded.
- **Plan 2** — unchanged: the subagent-reviewer loop in furnace-plan + ledger `Reviewer` column (open with `/furnace-plan`).
- **No evals ever run on this skill** — if review quality matters enough, skill-creator's eval loop is the real validation. Not done; flagged.

## Next session

- To deploy/validate: just the Cowork upload + smoke test (no skill needed).
- To build Plan 2: `/furnace-plan` in a fresh session.
