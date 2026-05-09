# PRD-creator notes

Internal notes for the skill build. Not loaded by the skill at runtime. Not user-facing.

## Build state

Passes 1, 2, and 2.1 shipped. Full skill structure complete: SKILL.md, principles.md, templates/, generator/, examples/, NOTES.md.

Symlinked into `~/.claude/skills/prd-creator/` after the field-society-demo validation run.

Validation run completed against `~/Sites/field-society-demo/` (Field Society Parkway Planter). Output PRD and BRAND.md passed regression tests 1 through 7. One real bug surfaced and patched in Pass 2.1: routed-elsewhere visual-aesthetic content (watercolor stickers, pixel Stardew) was silently dropped from the output. Patch added explicit routing rule in `decisions.md` and mandatory summary flag in `output-summary.md`. Regression tests 9 and 10 added.

Hand-off test (regression 8) completed against the same project. Context-engineering ran cleanly against PRD.md and BRAND.md as cluster 0 source. Cluster 1 (project name, description), cluster 2 (AI surfaces extracted as form-interpreter and vibe-copy from D-007/D-008), cluster 4 (voice and tone fully extracted from BRAND.md), cluster 5 (per-decision DECISIONS_ACTIVE promotion) and cluster 6 (PRD content fills) all extracted as confirm-or-correct without asking the user to restate. PRD-creator's PRD was preserved verbatim with a four-line cross-references append. Hand-off contract holds. Both skills compose as designed.

## Context-engineering gap surfaced during hand-off

Worth flagging back to context-engineering's NOTES.md and patching when that skill is next touched, not now.

Context-engineering's PRD template covers seven sections: product summary, target users, core problem, main workflow, out of scope, deferred capabilities, and cross-references. PRD-creator emits eleven: those seven plus version 1 scope, architecture and stack, decisions already made, open questions, and success criteria. The two templates have drifted. During the field-society-demo hand-off, the skill correctly detected the collision and proposed preserving the PRD-creator output verbatim with a cross-references append — exactly the right call. But the long-term fix is to update context-engineering's PRD template to the eleven-section shape so the collision does not recur.

The gap is a context-engineering Phase 2 patch, not a PRD-creator concern. Flagged here so the next session that opens context-engineering knows.

## Pass 2 design choices

Decisions made during Pass 2 build, recorded so the next session does not relitigate.

- **Cluster boundaries.** Consolidated the brief's 11 clusters to 8 (clusters 0 through 7). Merged "user and problem" into the elevator pitch (cluster 1) since the three are tightly coupled. Folded "deferred capabilities" into the scope cluster (now cluster 3) since users naturally produce in-and-out-of-scope items in the same breath. Replaced the dedicated open-questions cluster with a sweep at the end of every cluster. Replaced the dedicated decisions cluster with running capture across clusters 1-4 plus a cold review pass (cluster 5). Validation run will tell us if 8 is still too many.
- **Source-material handling.** Cluster 0 reads pasted material, summarizes what was found, but does not pre-fill any cluster's answer. The skill asks every cluster's questions anyway. This matches the context-engineering Pass 1.7 lesson. Pre-fill-then-confirm shape is parked.
- **Decision capture timing.** Collect-as-you-go across clusters 1-4. Review cold in cluster 5 with explicit ID assignment. The user reviews the running list in a single batch read-back, not one decision at a time, since they are reviewing not deciding.
- **Confirmation step before writing.** Final summary names every section that will emit and its source cluster. Names every section that will be skipped and why. Names brand-placement choice (inline vs sibling) explicitly. Wait for explicit user confirmation before writing.

## Brand content lifecycle across the three skills

Where brand-related content lives across the skill sequence. Worth keeping straight because the three skills could collide on filenames if not.

- **PRD-creator (this skill).** Cluster 8 elicits voice content (tone attributes, audience, vocabulary, voice examples). Decision logic picks placement: inline `## Brand and voice` appendix in `PRD.md` for three or fewer items, sibling `docs/BRAND.md` from `templates/BRAND.md.template` for more. The skill writes the file. No separate task downstream.
- **Context-engineering (next skill).** Reads the PRD and the optional `BRAND.md`. If `BRAND.md` exists, scaffolds a path-scoped voice-and-tone rule under `.claude/rules/` that points the agent at it during user-facing copy generation. See `context-engineering/principles.md` voice-and-tone rule pattern.
- **Design-system-bootstrap (parked).** Different scope. Takes a brand book or Figma file. Produces `tokens.css` plus seed components plus optionally a design-system doc describing token semantics. Visual brand only: colors, type, spacing, components. Not voice.

The split is voice (PRD-creator) vs visual (design-system-bootstrap). Voice belongs at PRD time because the material is in the user's head when they are scoping the product, and writing it down forces useful decisions. Visual brand needs different inputs and produces different outputs, so it gets its own skill.

Naming collision risk. Both skills could want a `BRAND.md`. Resolve before design-system-bootstrap starts. Lean: design-system-bootstrap emits `docs/DESIGN_SYSTEM.md` (matches `epost-assessment/docs/UI_SYSTEM.md` precedent), so `BRAND.md` stays voice. Decide when that skill starts, not now.

## Regression tests

Run these against the skill after any change to the templates, the intake flow, or the decision logic. Failure means the change broke a load-bearing pattern.

1. **Canonical section names.** Generated `PRD.md` contains H2 sections in this order: product summary, target users, core problem, main workflow, version 1 scope, out of scope, deferred capabilities, architecture and stack, decisions already made, open questions, success criteria. Optional sections (brand and voice, supporting documents) appear only when their conditions are met.
2. **Sentence-case headers.** Every H1, H2, H3 in the output is sentence-case. No Title Case. No colons in titles.
3. **Numbered decisions.** "Decisions already made" contains at least one entry formatted `**D-001** <statement> Rationale: <rationale>`. IDs are sequential with no gaps.
4. **Cluster 0 ran first.** The transcript shows the source-material question before any other cluster, regardless of what the user pasted earlier in the conversation.
5. **Confirmation before write.** The transcript shows a "here is the proposed outline" step with explicit user confirmation before any file is written.
6. **Brand placement logic.** When cluster 8 produces three or fewer items, content lands inline as a "Brand and voice" appendix in `PRD.md`. When it produces more, content lands in `BRAND.md` and the PRD's "Supporting documents" section links to it. Never both.
7. **No invented decisions.** Every D-NNN entry traces to a user statement in the transcript. No "we'll use Vercel" appears unless the user said so.
8. **Hand-off check.** Running the context-engineering skill against the produced PRD, cluster 0 extracts product summary, target users, core problem, and architecture overview without prompting the user to restate them.
9. **Routed-elsewhere flag.** When the user mentions visual-aesthetic, design-token, illustration-style, or other content that belongs to a different skill (design-system-bootstrap, context-engineering rule scaffolding), the post-generation summary names that content explicitly per `decisions.md` "Routed-elsewhere content." Silent dropping is a regression. This was a real bug surfaced in the field-society-demo validation run; do not let it return.
10. **User-delegated criteria.** When the user says "come up with some" in cluster 6 or 7, the skill proposes options for review rather than inventing decisions. Acceptable because the user delegated and reviewed. The output summary notes provenance with one line per `output-summary.md` rule 3.

## Parked

These are out of scope for V1 of the skill. Revisit if a real run surfaces a need.

- Multi-PRD comparison or version diffs.
- Research synthesis (the skill ingests, does not collect).
- Stakeholder alignment workflows. The skill is single-user.
- PRD review or critique. Possible separate skill.
- Pre-fill from source material before asking clusters. Tied to the open Pass-2 question above; defer until the default shape (ask-anyway) has run on a real project.
- Resume logic for an interview abandoned partway. Mirror context-engineering's stance: revisit if a real run gets abandoned.
- Templates for non-product PRDs (research plans, design briefs, RFCs). Different scope.
