# Plan-Review Feedback Extract — epost-assessment (result-card UI follow-up)

## Provenance
- source: Claude Code
- project: epost-assessment
- conversation: Batch D headline + result-card UI restructure (ScoreRing, callout, color audit)
- dates: 2026-06-01
- plans reviewed: 2 (headline-as-hero plan; result-card restructure plan) + a long visual-iteration tail
- corrections captured: 4

## Corrections

### C1
- verbatim: "why did you change the readiness level 'building momentum' to purple? i meant the eyebrow. that should still be reflective of the score color silly."
- normalized: Assistant applied a color change to the wrong element — misread which element "readiness level" referred to.
- tag: bad-substitution
- theme: misapplied-instruction-wrong-element
- where_fix_lives: planning-prompt
- repeated_in_convo: yes
- promotable: maybe
- note: Same shape as "dont make 'your answers' purple" later — instruction targets get misassigned.

### C2
- verbatim: "it looks like a bug has been introduced. what is wrong with the left edges of the info boxes under risks and wins? its like cut off"
- normalized: A styling change introduced a visual regression that was presented for review without being caught.
- tag: missing-read-before-write
- theme: introduced-unverified-regression
- where_fix_lives: code
- repeated_in_convo: no
- promotable: maybe

### C3
- verbatim: "i think its a bad headline. also it doesn't look like a headline. maybe we need to call it out differently our pull it out of the box?"
- normalized: Proposed AI headline failed both on copy quality and on visual treatment.
- tag: other
- theme: output-quality-miss
- where_fix_lives: code
- repeated_in_convo: no
- promotable: no
- note: Largely project-specific design taste; not obviously rule-promotable.

### C4
- verbatim: "ok, you are right, 300 in the boxes is too light since they are so close in size."
- normalized: A weight choice the assistant made (300 everywhere) lost the title/body distinction.
- tag: other
- theme: lost-hierarchy-from-global-change
- where_fix_lives: code
- repeated_in_convo: no
- promotable: no

## Conversation summary
- top themes here: misapplied-instruction-wrong-element, introduced-unverified-regression; otherwise heavy normal design iteration
- dominant where_fix_lives: code / planning-prompt
- promotable / one-off split: 0 promotable, 2 maybe, 2 one-off
- one honest sentence: This was mostly legitimate design iteration (new directions, not corrections); the two genuine corrections are "wrong element got the change" and "a regression slipped through unverified" — both verification/comprehension, not project-specific.
