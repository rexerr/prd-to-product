# Plan-Review Feedback Extract — prd-to-product (doc consolidation + squirreled validation relay)

## Provenance
- source: Claude Code
- project: prd-to-product
- conversation: docs audit → BACKLOG.md consolidation, then relayed feedback from a squirreled validation run of prd-creator
- dates: 2026-05-11
- plans reviewed: 2 (docs-consolidation plan; relayed skill behavior during validation)
- corrections captured: 5

## Corrections

### C1
- verbatim: "the text also is too technical. i dont need to know its 'cluster 0' or use 0a. etc. be more human, hand hold, dont expose how the sausage is made unless they ask"
- normalized: The skill exposed its internal scaffolding vocabulary (cluster 0, 0a) to the user instead of a conversational surface.
- tag: other
- theme: exposes-internal-jargon
- where_fix_lives: skill:prd-creator
- repeated_in_convo: yes
- promotable: yes
- note: Raised 3x ("again clusters info. this should be more conversational").

### C2
- verbatim: "why is it forcing me to do this? i dont want to list capabilities. isnt that the whole point of the brief? … doesnt my brief tell you what it is? why do i need to?"
- normalized: The skill ignored the provided brief and re-asked Rex to supply content already written down.
- tag: other
- theme: ignores-source-brief
- where_fix_lives: skill:prd-creator
- repeated_in_convo: yes
- promotable: yes
- note: Same theme as qventus C1 — re-asks-info-already-in-source. Strong cross-project recurrence.

### C3
- verbatim: "how does it know it was written days ago? thats not true, it was written in the last hour. where is getting this interpretation?"
- normalized: The skill asserted a fabricated fact (the brief was "written days ago") it had no basis for.
- tag: other
- theme: temporal-hallucination
- where_fix_lives: planning-prompt
- repeated_in_convo: no
- promotable: yes

### C4
- verbatim: "skills should auto-detect input" / "when i start i just want to open the folder and run the prd creator skill. it should look in its home folder for a brief…"
- normalized: The skill should detect an existing brief in the working folder instead of asking cold.
- tag: other
- theme: should-auto-detect-input
- where_fix_lives: skill:prd-creator
- repeated_in_convo: no
- promotable: yes

### C5
- verbatim: "i thought the prd creator skill and the design system were sub skills within the greater context engineering, or more accurately the prd-to-product skill … maybe it should be more accurately labeled as idea to product skill"
- normalized: The skill set's naming/composition didn't match Rex's mental model (expected one umbrella skill that chains the others).
- tag: other
- theme: skill-naming-and-composition-mismatch
- where_fix_lives: decisions
- repeated_in_convo: no
- promotable: maybe

## Conversation summary
- top themes here: ignores-source-brief (recurred), exposes-internal-jargon (recurred), temporal-hallucination, should-auto-detect-input
- dominant where_fix_lives: skill:prd-creator
- promotable / one-off split: 4 promotable, 1 maybe
- one honest sentence: The richest source of promotable signal — the validation surfaced repeated, rule-shaped skill failures (re-asks despite a brief, leaks internal jargon, hallucinates a date), several of which recur in other projects.
