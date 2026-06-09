# Plan-Review Feedback Extract — seance (portal animation / breathing-hands hero)

## Provenance
- source: Claude Code
- project: seance
- conversation: P6 portal open-animation, then pivot to ASCII-orb + breathing-hands home hero
- dates: 2026-06-08
- plans reviewed: 3 (portal-open animation plan; hero re-composition; orb-native follow-up)
- corrections captured: 5

## Corrections

### C1
- verbatim: "Figma was not pulled. CLAUDE.md makes this a hard rule … The plan cites 34:5739 … from memory and describes the black bar / Archivo from recollection."
- normalized: Plan built/cited a screen from memory instead of pulling the Figma node, violating an existing hard CLAUDE.md rule.
- tag: missing-read-before-write
- theme: ignored-existing-claude-md-rule
- where_fix_lives: claude-md
- repeated_in_convo: no
- promotable: maybe
- note: Rule already EXISTS and was ignored — this is an enforcement gap, not a missing rule.

### C2
- verbatim: "As written, beat 1 has a flash baked into its flash-mitigation. … staticFallback renders the hardcoded RadialGradient, not a frozen frame of the live WebGL drift."
- normalized: The plan's mitigation for a risk didn't actually do what it claimed — the "frozen still" fell back to a gradient, reintroducing the flash it was meant to prevent.
- tag: unstated-assumption
- theme: mitigation-doesnt-do-what-it-claims
- where_fix_lives: planning-prompt
- repeated_in_convo: no
- promotable: maybe

### C3
- verbatim: "its like you are not listening to me. not a circle. the full screen, every part. … the background should be animated."
- normalized: Assistant repeatedly implemented a scaled-up circle when Rex's stated intent was a full-screen takeover; intent was misread across several iterations.
- tag: goal-drift
- theme: design-intent-misread
- where_fix_lives: planning-prompt
- repeated_in_convo: yes
- promotable: maybe
- note: Hard to rule-fix; candidate "restate the visual intent in your own words before building" check.

### C4
- verbatim: "why are you not checking in the simulator?"
- normalized: Assistant presented UI changes for review without first running them in the simulator to verify.
- tag: missing-read-before-write
- theme: not-verifying-on-device-before-presenting
- where_fix_lives: claude-md
- repeated_in_convo: no
- promotable: yes

### C5
- verbatim: "ok. this looks crappy still. maybe we kill this functionality. its not necessary and the jankiness is hurting the identity not helping the experience"
- normalized: Assistant kept iterating a janky animation forward instead of flagging early that it wasn't clearing the quality bar.
- tag: over-engineering
- theme: pushed-janky-feature-instead-of-flagging
- where_fix_lives: planning-prompt
- repeated_in_convo: no
- promotable: maybe
- note: Borderline — partly a product call by Rex, partly "should have surfaced the fidelity risk sooner."

## Conversation summary
- top themes here: design-intent-misread (recurred), not-verifying-on-device, ignored-existing-rule (Figma), mitigation-doesnt-do-what-it-claims
- dominant where_fix_lives: planning-prompt / claude-md
- promotable / one-off split: 1 promotable, 3 maybe, 1 borderline
- one honest sentence: Real pattern here — stated visual intent was misread repeatedly and changes were presented without device verification; both are recurring, not one-off.
