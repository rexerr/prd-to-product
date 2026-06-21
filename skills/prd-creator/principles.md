# PRD-creator principles

The conventions this skill follows, and the rationale behind them. Read this when you want to understand why a template is shaped the way it is, or when you hit an edge case the templates and the intake flow do not cover. Do not read it on every skill invocation.

## What this skill is for

Most projects start with a sentence or two and not a PRD. The user holds the rest in their head: who it is for, what problem it solves, what is deferred, what is already decided, what success looks like. Writing a good PRD takes hours, and the elicitation work is where AI-assisted iteration genuinely helps. The skill structures that elicitation so the resulting PRD has a shape downstream skills and humans can rely on.

The skill writes a PRD. It does not invent product strategy, run research, generate code, or scaffold the rule files around the PRD. The next skill in the sequence (context-engineering) consumes this skill's output.

**Self-skip when the interview adds nothing.** The full clustered interview earns its cost on a real product with decisions to elicit. For a *trivial single-feature* PRD — one capability, nothing genuinely undecided — the skill should say so and offer a lighter path (a short direct PRD, or only the sections that carry content) rather than run all clusters. The failure this prevents: heavyweight elicitation ceremony on work too small to need it, which reads as form-processing and wastes the user's turns.

## Why interview-driven, not template-fill

A blank template plus "fill it in" produces a thin PRD. The user writes for the section in front of them and stops. The interview asks for what is in their head before pointing them at a section, which surfaces material the template would have left out. It also forces the user to make a decision when they have been holding two options open, because the skill asks one question at a time and waits.

The interview is the heart of this skill. The template is the format the answers land in.

## Position-aware placement in the output PRD

The U-shaped attention curve penalizes information placed in the middle of long context, so the output PRD pulls the load-bearing pieces to the top and the bottom: the reader knows what this is and who it is for in the first thirty seconds (top), and the last thing they see is what is unresolved and what "done" looks like (bottom). Structure and detail sit in the middle.

The canonical section order that realizes this shape is the skeleton in `PRD-FORMAT.md` — the ordering authority, not re-listed here. If the PRD grows past V1, new sections go in the middle; the top and bottom anchors stay.

## The cluster contract

Carried from context-engineering. Holds for every cluster in `generator/intake.md`.

- One cluster at a time. Do not dump every question at once.
- Up to three questions per call within a cluster. Free-text fills ask one at a time.
- Branching questions offer two to four options, never more. If the answer space is genuinely larger, ask free-text instead.
- Cluster 0 always asks for source material first, even when material appears to be in conversation context. Do not silently absorb pasted text or named files. When material is present, the sanctioned behavior is draft-and-present: draft each covered cluster's answer from the material and show it for the user to confirm or edit, rather than asking cold (which makes the user re-state what they already wrote) or absorbing silently (which produces a shallow PRD). See `generator/intake.md` cluster 0 for the full three-way distinction.
- After every cluster, summarize what was captured in two or three sentences. The user corrects before the next cluster starts.
- Confirm the proposed PRD outline before writing the file. Name every section and its source cluster.
- **Questions expose the skill's reasoning, never originate the user's decisions.** Three interview-form rules (actionable detail in `generator/intake.md` "How to run a cluster"): a decision question opens with *what changes if you pick differently*; the skill names a recommended option only among ones already presented or drafted from source material, while genuinely open elicitation stays a bare question; and a contradiction between a user answer and the brief is surfaced as one forced choice, not absorbed. **Why:** a human edits faster than they author and can attack a stance that is on the table, but the moment the skill proposes a *product decision the user has not made* it crosses from eliciting into inventing — the line D-010 and "does not invent decisions" both draw.

## Interview conduct: stay in natural language, stay grounded

Two conduct rules for the interview itself, distinct from the output PRD's style.

- **Internal scaffolding stays internal.** The cluster numbers, the sub-question structure, and the draft `D-NNN` IDs are the skill's machinery. User-facing copy never names them. Speak in natural language: "the quick pitch," not "cluster 1"; present a drafted decision for confirmation without narrating its draft ID. Confirmed `D-NNN` IDs surface to the user only at the cluster 5 read-back and in the written PRD, where they are part of the deliverable. **Failure it prevents:** exposing the machinery reads as the skill processing a form rather than understanding the user, which erodes trust in the interview.
- **No temporal or provenance claims about source material.** When summarizing a brief or notes, describe what the material contains, never speculate about when it was written or how stale it might be ("written a while ago," "your thinking may have sharpened since"). Cite a date only if the material itself states one. **Failure it prevents:** a confident but ungrounded claim about provenance ("the brief is from days ago") is often wrong and undermines trust in everything else the skill asserts.
- **Diagnose, don't validate (anti-sycophancy).** The interview tests the user's thinking; it does not agree with it. The actionable posture — a banned-hedge list with sharper replacements, take-a-position-and-name-what-would-change-it, and steelman-then-challenge — lives in `generator/intake.md` "How to run a cluster" (it must be in context while the interview runs). **Why:** a weak premise that survives review by sounding acknowledged rather than tested is goal-drift wearing politeness; an opinion the user can attack surfaces the flaw, a neutral restatement hides it. **Carve-out:** this is bound to *challenging premises*, never to inventing product direction — prd-creator pushes on a vague answer, it does not propose a strategy the user hasn't chosen (the anti-invention contract holds; cf. the brainstorm skill, which forbids judgment during divergence — prd-creator has no divergence phase to protect).

## The hand-off contract with context-engineering

The output PRD is the input to the context-engineering skill's cluster 0. Two load-bearing pieces — **named sections** (context-engineering extracts product summary, target users, core problem, and architecture overview *by canonical section name*, so don't rename; add subsections instead) and the **numbered decision seed list** (`D-001`.. one per decision, the format `DECISIONS.md` is later scaffolded from) — are specified, with the canonical section list and order, in `PRD-FORMAT.md`. The rules and the section list live there; what matters here is *why* they're load-bearing: a downstream extractor keys on the section names and the decision-ID shape, so both are part of the deliverable's contract, not cosmetic.

## When the brand-and-voice material lives in a sibling file

Cluster 8 elicits brand and voice content. The decision logic at `generator/decisions.md` chooses the placement.

- If the user produces three or fewer items (a tone descriptor, an audience note, a do-not-use list), inline as an appendix in the PRD.
- If the user produces a substantive set (named tone attributes, vocabulary lock list, voice examples, audience segments), emit a sibling `docs/BRAND.md` from `templates/BRAND.md.template` and link to it from the PRD's "Supporting documents" section.

Default to inline. Sibling file is the upgrade path when the material outgrows an appendix.

## Style for the output PRD

Every PRD this skill writes follows a fixed house style — sentence-case headers, no em dashes, no Oxford commas, no colons in titles, AP, specific-over-generic, cite-your-sources, every-paragraph-earns-its-tokens. The full failure-cited rules live in `PRD-FORMAT.md` "Style rules"; this is a signpost, not a second copy — do not restate the bodies here.

The exemplar PRDs at `epost-assessment/docs/PRD.md`, `epost-intelligence-feed/docs/PRD.md`, and `the-council/docs/PRD.md` were written before this style was codified. They use Title Case headers and longer prose. Match their shape and discipline. Do not match their formatting.

## Conventions for writing PRD content

What goes in the sections, not just how it looks — imperatives-not-principles, out-of-scope-as-explicit-cuts, deferred-points-forward, open-questions-name-what-would-change-the-build, concrete-success-criteria, no-volatile-code-locations (with the decision-snippet carve-out), and testing-decisions-name-a-good-test. The full failure-cited rules live in `PRD-FORMAT.md` "Content conventions"; this is a signpost, not a second copy — do not restate the bodies here.

## Recommend a stress-test before locking high-stakes scope

The interview collects and structures; it does not pressure-test. When the PRD is about to lock a decision that is **costly to get wrong and hard to reverse** — the core differentiator, the V1/V2 cut line, a load-bearing scope decision, or reconciling a conflicting PRD from another source (e.g. a Claude Design bundle) — recommend a structured multi-perspective review (an LLM-council-style pass, if such a skill is available) *before* finalizing, rather than rubber-stamping the interview's first synthesis. Recommend it; do not auto-run it, and do not invoke it for routine wording or reversible edits. The failure mode this prevents: a plausible-but-unexamined scope decision hardening into the PRD because the interview surfaced it but never challenged it. This is a hand-off to a separate critique pass — the skill itself still does not critique the PRD (see below).

## What this skill does not do

- Does not propose product strategy or invent decisions the user has not made.
- Does not run research, scrape sources, or synthesize transcripts the user has not provided.
- Does not generate code, design tokens, or implementation specs.
- Does not scaffold rule files or docs structure around the PRD. That is the context-engineering skill.
- Does not review or critique an existing PRD. Possible separate skill, parked.
- Does not support multi-PRD comparison, version diffs, or stakeholder alignment workflows. The skill is single-user.
