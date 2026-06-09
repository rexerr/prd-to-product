# Plan-Review Feedback Extract — ha-controller (PRD interview + HA audit)

## Provenance
- source: Claude Code
- project: ha-controller
- conversation: brainstorm → prd-creator → context-engineering → first HA audit for the Home Assistant controller
- dates: 2026-06-05
- plans reviewed: 2 (PRD; context-engineering scaffold) + audit kickoff
- corrections captured: 2

## Corrections

### C1
- verbatim: "so this is not a tool. this just a claude project ill work out of when i do this work. make sense? i could use cowork too pointed at this folder"
- normalized: Assistant kept framing the product as a standalone tool/app when Rex's actual shape is "a Claude Code/Cowork project folder I work out of."
- tag: unstated-assumption
- theme: misframed-product-shape-app-vs-claude-project
- where_fix_lives: skill:prd-creator
- repeated_in_convo: no
- promotable: maybe
- note: Recurs across projects (qventus "do we even need an app", squirreled "idea to product") — a standing assumption that the output is an app.

### C2
- verbatim: "i do not want to go to individual bulb controls in apple home or google. i want to control colors in hue or in ha with scenes."
- normalized: Re-stated an architecture preference the audit plan had started to drift away from.
- tag: goal-drift
- theme: re-stated-drifting-architecture-preference
- where_fix_lives: context
- repeated_in_convo: no
- promotable: no
- note: Borderline — partly a normal domain decision rather than a correction of a bad plan.

## Conversation summary
- top themes here: misframed-product-shape (app vs Claude-project)
- dominant where_fix_lives: skill:prd-creator
- promotable / one-off split: 0 promotable, 1 maybe, 1 one-off
- one honest sentence: The keyword filter flagged this session high (10) but it is overwhelmingly normal interview answers; only ~2 are real corrections, the notable one being the recurring "assume it's an app" framing.
