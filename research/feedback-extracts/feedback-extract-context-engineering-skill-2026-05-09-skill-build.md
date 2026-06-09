# Plan-Review Feedback Extract — context-engineering-skill (build prd-creator + design-system-bootstrap, validate)

## Provenance
- source: Claude Code
- project: context-engineering-skill (the skills repo, pre-rename to prd-to-product)
- conversation: build prd-creator, run end-to-end validation on field-society-demo, then build design-system-bootstrap
- dates: 2026-05-09
- plans reviewed: 4 (prd-creator Pass 1/2; validation review; design-system-bootstrap Pass 1/2)
- corrections captured: 3

## Corrections

### C1
- verbatim: "i worry its using my two past projects as the basis for the design system but im not sure i built those correctly, should i be worried?"
- normalized: The design-system skill was lifting specifics from Rex's existing (possibly wrong) projects instead of encoding standard best practice; later confirmed as a real bug.
- tag: bad-substitution
- theme: skill-overfits-to-existing-projects
- where_fix_lives: skill:design-system-bootstrap
- repeated_in_convo: no
- promotable: yes
- note: Rex flagged it as a risk; the assistant only caught it after he raised it.

### C2
- verbatim: "we can use tailwind and shadcn, i dont want to restrict if its the right tool"
- normalized: The skill baked in a hard "No Tailwind / No shadcn" restriction that over-constrained future projects.
- tag: over-engineering
- theme: over-restrictive-default
- where_fix_lives: skill:design-system-bootstrap
- repeated_in_convo: no
- promotable: maybe

### C3
- verbatim: "i think im too late. its creating it already, we will have to come back and revise after."
- normalized: The build started generating before Rex's open concern (over-fitting) was resolved — acted ahead of a pending decision.
- tag: scope-creep
- theme: acted-before-open-concern-resolved
- where_fix_lives: planning-prompt
- repeated_in_convo: no
- promotable: maybe

## Conversation summary
- top themes here: skill-overfits-to-existing-projects, over-restrictive-default, acted-before-concern-resolved
- dominant where_fix_lives: skill:design-system-bootstrap / planning-prompt
- promotable / one-off split: 1 promotable, 2 maybe
- one honest sentence: A productive build session with mostly confirm/clarify turns; the real corrections cluster on the skill over-fitting to Rex's existing projects and over-restricting tooling.
