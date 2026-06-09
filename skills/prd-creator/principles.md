# PRD-creator principles

The conventions this skill follows, and the rationale behind them. Read this when you want to understand why a template is shaped the way it is, or when you hit an edge case the templates and the intake flow do not cover. Do not read it on every skill invocation.

## What this skill is for

Most projects start with a sentence or two and not a PRD. The user holds the rest in their head: who it is for, what problem it solves, what is deferred, what is already decided, what success looks like. Writing a good PRD takes hours, and the elicitation work is where AI-assisted iteration genuinely helps. The skill structures that elicitation so the resulting PRD has a shape downstream skills and humans can rely on.

The skill writes a PRD. It does not invent product strategy, run research, generate code, or scaffold the rule files around the PRD. The next skill in the sequence (context-engineering) consumes this skill's output.

## Why interview-driven, not template-fill

A blank template plus "fill it in" produces a thin PRD. The user writes for the section in front of them and stops. The interview asks for what is in their head before pointing them at a section, which surfaces material the template would have left out. It also forces the user to make a decision when they have been holding two options open, because the skill asks one question at a time and waits.

The interview is the heart of this skill. The template is the format the answers land in.

## Position-aware placement in the output PRD

The U-shaped attention curve penalizes information placed in the middle of long context. The output PRD pulls the load-bearing pieces to the top and the bottom.

- Top: product summary, target users, core problem. The reader knows what this is and who it is for in the first thirty seconds.
- Bottom: open questions, success criteria, supporting documents pointer. The last thing the reader sees is what is unresolved and what "done" looks like.
- Middle: scope, workflow, architecture, decisions, deferred capabilities. Structure and detail.

Apply the same shape if the PRD grows past the V1 template. New sections go in the middle. The top and bottom anchors stay.

## The cluster contract

Carried from context-engineering. Holds for every cluster in `generator/intake.md`.

- One cluster at a time. Do not dump every question at once.
- Up to three questions per call within a cluster. Free-text fills ask one at a time.
- Branching questions offer two to four options, never more. If the answer space is genuinely larger, ask free-text instead.
- Cluster 0 always asks for source material first, even when material appears to be in conversation context. Do not silently absorb pasted text or named files.
- After every cluster, summarize what was captured in two or three sentences. The user corrects before the next cluster starts.
- Confirm the proposed PRD outline before writing the file. Name every section and its source cluster.

## The hand-off contract with context-engineering

The output PRD is the input to the context-engineering skill's cluster 0. Two pieces of the contract are load-bearing.

- **Named sections.** The context-engineering skill extracts product summary, target users, core problem, and architecture overview by section name. The template uses the canonical names below. Do not rename sections to match a project's local idiom. Add subsections under canonical names instead.
- **Numbered decision seed list.** The "decisions already made" section uses `D-001`, `D-002`, ..., one per decision, with a one-line rationale each. The format is the format `DECISIONS.md` will absorb later. The seed list is not a duplicate of `DECISIONS.md`, which does not exist yet at PRD time. It is the source the context-engineering skill draws from when scaffolding `DECISIONS.md`.

Canonical section names, in order:

1. Product summary
2. Target users
3. Core problem
4. Main workflow
5. Version 1 scope
6. Out of scope
7. Deferred capabilities
8. Architecture and stack
9. Decisions already made
10. Open questions
11. Success criteria
12. Brand and voice (optional, see below)
13. Supporting documents (optional)

## When the brand-and-voice material lives in a sibling file

Cluster 8 elicits brand and voice content. The decision logic at `generator/decisions.md` chooses the placement.

- If the user produces three or fewer items (a tone descriptor, an audience note, a do-not-use list), inline as an appendix in the PRD.
- If the user produces a substantive set (named tone attributes, vocabulary lock list, voice examples, audience segments), emit a sibling `docs/BRAND.md` from `templates/BRAND.md.template` and link to it from the PRD's "Supporting documents" section.

Default to inline. Sibling file is the upgrade path when the material outgrows an appendix.

## Style for the output PRD

Every PRD this skill writes follows these rules. They are the user's house style, applied to the PRD specifically.

- Sentence-case headers. H1 for the document title. H2 for canonical sections. H3 for subsections only when the section has more than one distinct piece. Do not use H4 or deeper.
- No em dashes. Use commas, periods, or parentheses.
- No Oxford commas.
- No colons in titles.
- AP style.
- Specific over generic. "Approve and skip are the only triage actions" beats "Triage should be simple."
- Cite specific files, sources, or prior decisions when describing constraints. "Per D-003 we ship on Vercel" beats "We ship on Vercel."
- Every paragraph earns its tokens. If a sentence does not change a reader's understanding, cut it.

The exemplar PRDs at `epost-assessment/docs/PRD.md`, `epost-intelligence-feed/docs/PRD.md`, and `the-council/docs/PRD.md` were written before this style was codified. They use Title Case headers and longer prose. Match their shape and discipline. Do not match their formatting.

## Conventions for writing PRD content

These shape what goes in the sections, not just how they look.

- **Imperatives, not principles, in scope and decisions.** "V1 ships single-user, no auth" is a decision. "Keep V1 simple" is not. If the statement cannot be checked, rewrite it until it can.
- **Out of scope is a list of explicit cuts, not a vague boundary.** Each item names what was considered and rejected for V1.
- **Deferred capabilities point forward.** Each item is a candidate for V2 or later, not a "maybe never." If the user wants "maybe never," it goes in out of scope.
- **Open questions name what would change the build.** A question that does not change a decision belongs in a discussion thread, not the PRD.
- **Success criteria are concrete.** "10 users complete the workflow without help" beats "users find it intuitive." If the user cannot answer a criterion concretely, capture it as an open question instead.

## Recommend a stress-test before locking high-stakes scope

The interview collects and structures; it does not pressure-test. When the PRD is about to lock a decision that is **costly to get wrong and hard to reverse** — the core differentiator, the V1/V2 cut line, a load-bearing scope decision, or reconciling a conflicting PRD from another source (e.g. a Claude Design bundle) — recommend a structured multi-perspective review (an LLM-council-style pass, if such a skill is available) *before* finalizing, rather than rubber-stamping the interview's first synthesis. Recommend it; do not auto-run it, and do not invoke it for routine wording or reversible edits. The failure mode this prevents: a plausible-but-unexamined scope decision hardening into the PRD because the interview surfaced it but never challenged it. This is a hand-off to a separate critique pass — the skill itself still does not critique the PRD (see below).

## What this skill does not do

- Does not propose product strategy or invent decisions the user has not made.
- Does not run research, scrape sources, or synthesize transcripts the user has not provided.
- Does not generate code, design tokens, or implementation specs.
- Does not scaffold rule files or docs structure around the PRD. That is the context-engineering skill.
- Does not review or critique an existing PRD. Possible separate skill, parked.
- Does not support multi-PRD comparison, version diffs, or stakeholder alignment workflows. The skill is single-user.
