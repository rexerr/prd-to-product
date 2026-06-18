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
12. Testing decisions
13. Brand and voice (optional, see below)
14. Supporting documents (optional)

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
- **No volatile code locations in the PRD.** Do not pin implementation file paths, line numbers, or verbatim code. They go stale the moment files move or get renamed, and a PRD that references them rots silently while reading as if it is still accurate. One carve-out: inline a short prototype-derived snippet only when it encodes a decision more precisely than prose can, a state machine, schema, reducer, or type shape, trimmed to the decision-rich part. Citing a decision or a named source doc by reference (as the style rule above does) is fine. The ban is on volatile code, not on references. **Failure it prevents:** a PRD that pinned `app/api/route.ts:42` or pasted a component becomes wrong on the first rename, and the reader cannot tell the stale line from the live ones.
- **Testing decisions name what a good test is, not test code.** The testing decisions section states the external behaviors to verify, which parts of the system matter most, and any prior art the tests model. If V1 ships no automated suite, that is itself a testing decision: say so and name how V1 is verified instead (a manual pass, a live validation window). It is a decision record, not a test plan.

## Recommend a stress-test before locking high-stakes scope

The interview collects and structures; it does not pressure-test. When the PRD is about to lock a decision that is **costly to get wrong and hard to reverse** — the core differentiator, the V1/V2 cut line, a load-bearing scope decision, or reconciling a conflicting PRD from another source (e.g. a Claude Design bundle) — recommend a structured multi-perspective review (an LLM-council-style pass, if such a skill is available) *before* finalizing, rather than rubber-stamping the interview's first synthesis. Recommend it; do not auto-run it, and do not invoke it for routine wording or reversible edits. The failure mode this prevents: a plausible-but-unexamined scope decision hardening into the PRD because the interview surfaced it but never challenged it. This is a hand-off to a separate critique pass — the skill itself still does not critique the PRD (see below).

## What this skill does not do

- Does not propose product strategy or invent decisions the user has not made.
- Does not run research, scrape sources, or synthesize transcripts the user has not provided.
- Does not generate code, design tokens, or implementation specs.
- Does not scaffold rule files or docs structure around the PRD. That is the context-engineering skill.
- Does not review or critique an existing PRD. Possible separate skill, parked.
- Does not support multi-PRD comparison, version diffs, or stakeholder alignment workflows. The skill is single-user.
