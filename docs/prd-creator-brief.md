# Working brief: PRD-creator skill

Working brief for Claude Code. The next skill in the sequence after context-engineering.

## Goal

A Claude skill that takes a working brief or rough project idea and produces a structured PRD via interview-driven question flow. The PRD is the input that feeds context-engineering's cluster 0; the two skills compose.

## What this skill is for

Most projects start with a sentence or two ("I want to build X") and not a PRD. The user holds the rest in their head: who it's for, what problem it solves, what's deferred, what's already decided, what success looks like. Writing a good PRD takes hours and is the kind of task where AI-assisted iteration genuinely helps. This skill structures the elicitation so the resulting PRD has the shape downstream skills (and humans) can rely on.

## Inputs

The skill should accept any of:

- A one-paragraph idea ("I want to build a council that helps founders make decisions").
- A working brief (problem statement, audience, rough scope).
- A research dump or interview transcript.
- A Notion / Google Doc / message thread excerpt.
- A combination of the above.

The skill does not require structured input. It runs interview-style questions to fill in what's missing.

## Outputs

A single `PRD.md` file at the path the user names (default `docs/PRD.md`). Structure should match the shape that context-engineering already knows how to consume — see `epost-assessment/docs/PRD.md` and `epost-intelligence-feed/docs/PRD.md` for working exemplars. At minimum:

- Product summary (one paragraph).
- Target users.
- Core problem.
- Main workflow (numbered steps).
- Out of scope.
- Deferred capabilities (V2-and-beyond).
- Architecture / stack overview.
- Decisions already made (numbered, format that DECISIONS.md can absorb).
- Open questions.
- Success metrics or done-when criteria.

Brand and voice content lives in the PRD or in a separate file depending on the user's preference. Ask.

## What this skill is NOT

- Not a context-engineering skill. Different scope. The output of this skill becomes the input of that one.
- Not a design-system bootstrap. If the brief includes brand assets, capture them in the PRD's appendix or a sibling file. Do not generate token CSS.
- Not a code generator. The PRD is product strategy and architecture, not implementation.
- Not a decision-maker. The skill elicits the user's decisions, structures them, and produces a PRD. It does not invent decisions the user has not made.

## Architecture (mirror context-engineering)

Same five-piece shape that worked for context-engineering:

- `SKILL.md` — trigger phrases, procedure, file map. Under 500 words.
- `principles.md` — rationale and conventions. Deferred-loaded per the SKILL.md procedure.
- `generator/` — `intake.md` (clustered question flow), `decisions.md` (output structure rules), `output-summary.md` (post-generation report).
- `templates/` — the PRD template plus any optional companion templates (brand/voice appendix, decisions seed list).
- `examples/` — three transcripts (small / medium / large) plus one full output PRD for the small case.
- `NOTES.md` — internal notes, regression test definitions, parked ideas.

Read `context-engineering/SKILL.md` and `context-engineering/principles.md` to absorb the pattern. Do not copy content; copy shape.

## Question flow design

The interview is the heart of this skill. Cluster shape proposal (refine in build):

- **Cluster 0: source material** — same as context-engineering. "Do you have a working brief, transcript, or notes? Paste, link, or say none."
- **Cluster 1: elevator pitch** — one paragraph, who/what/why.
- **Cluster 2: user and problem** — who is this for; what specifically are they struggling with; what do they currently do instead.
- **Cluster 3: scope and shape** — what is V1, what is explicitly NOT V1, what is the smallest valuable thing to ship.
- **Cluster 4: workflow** — step-by-step happy path through the product.
- **Cluster 5: stack and architecture** — what is decided, what is open. (This will feed context-engineering's later questions about AI surfaces, design system, etc.)
- **Cluster 6: decisions already made** — anything binding the user has already committed to. Format as candidate D-001..D-N for the eventual DECISIONS.md.
- **Cluster 7: deferred and out of scope** — V2 ideas, anti-goals, things the user has rejected.
- **Cluster 8: brand and voice** — tone, vocabulary, audience considerations. Optional; skip if irrelevant.
- **Cluster 9: success criteria** — concrete, measurable, done-when. If the user can't answer this, flag as an open question.
- **Cluster 10: open questions** — what does the user still need to figure out before building.

This is a starting point. Refine cluster boundaries during build based on what the exemplar PRDs (assessment, feed) actually contain.

## Question contract (carry from context-engineering)

- One cluster at a time. Do not dump every question at once.
- 2 to 4 options for branching questions; up to 3 questions per call.
- Free-text fills ask one at a time.
- Cluster 0 always asks for source material first, even if material is already in conversation context (lesson from context-engineering Pass 1.7).
- After every cluster, summarize what was captured before moving on.
- Confirm the proposed PRD outline before writing the file.

## What to read before building

In priority order:

1. This brief.
2. `handoff.md` (the skill-build handoff at the same path).
3. `context-engineering/SKILL.md` and `context-engineering/principles.md` (architectural pattern reference).
4. `epost-assessment/docs/PRD.md` (a real PRD that fed a real project).
5. `epost-intelligence-feed/docs/PRD.md` (another real PRD; more complex shape).
6. `the-council/docs/PRD.md` if accessible (a real PRD that fed context-engineering's most recent validation run).

Do not audit these as a Phase 0. Read them to inform building, not to produce a findings doc.

## Definition of done for the build

The skill is complete when:

1. Folder exists at `~/.claude/skills/prd-creator/` (or symlinked from a source repo) with all five required pieces.
2. Running the skill on a real project idea produces a PRD that context-engineering can consume via cluster 0 with no edits to the PRD-creator output beyond domain-content fills.
3. The validation run (pick one real project the user wants to start) produces a PRD the user would actually use, not just one that's structurally complete.
4. The output PRD shape matches the shape that context-engineering's cluster 0 extraction logic expects (named sections, numbered decisions, etc.).

## Out of scope for the first build

- Multi-PRD comparison or iteration across versions.
- Research synthesis (the skill ingests provided source material; it does not run research).
- Stakeholder alignment workflows (the skill is single-user).
- PRD review or critique (separate skill, possibly worth building later).

## Style requirements for the PRD output

Every PRD this skill produces should follow these style rules. They are the same rules Rex uses for everything else, applied to the PRD output specifically.

- Sentence-case headers, H1/H2/H3 only.
- No em dashes.
- No Oxford commas.
- No colons in titles.
- AP style.
- Specific over generic. "Approve and skip are the only triage actions" beats "Triage should be simple."
- Cite specific files or sources when describing decisions or constraints.
- Every paragraph earns its tokens.

## Execution recommendation

Pass 1: SKILL.md + principles.md + templates/ (the PRD template) + NOTES.md. Stop for review.
Pass 2: generator/ (intake, decisions, output-summary) + examples/.
Pass 1.5 if needed for any patches before Pass 2.

This is the same two-pass shape that worked for context-engineering.

## When to ask vs when to proceed

Default to proceeding. Only stop and ask when:

- The exemplar PRDs (assessment, feed) suggest a shape the brief contradicts.
- A cluster boundary is genuinely unclear and the wrong call would force restructure later.
- The brief is wrong about something material.

Do not ask permission to begin. Read the brief, read the references, plan the work, execute.
