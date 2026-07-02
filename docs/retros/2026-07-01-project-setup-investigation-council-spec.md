# Retro — 2026-07-01 23:40 CDT — Project-setup investigation: Track 1 + Track 3 + council + skill spec   (4th session of the day)

**Dominant failure tag: goal drift** — the work stayed on the right *topic* but drifted in *altitude and framing*. I ran a rigorous engineering investigation for a user who is a designer delegating all engineering to Claude, and (a) let the analysis get deep enough into tool jargon that Rex twice lost the thread ("i have no idea really what you are talking about"), and (b) framed the council with a baseline — "just hand-write setup notes twice" — that directly contradicts the project's own stated premise (Rex is not the developer). The premise was *in* my own framing ("delegates ALL engineering judgment") yet I didn't enforce it, so the council spent a whole fork on it and Rex had to correct it by hand. Stated-but-unenforced premise = the drift.

## What happened

Picked up the Seq-1 board item (Project-setup system). Ran the handoff's three tracks to a decision:

1. **Track 1 — review real projects (premise verified).** Read `seance` (native iOS, shipped) via a blind-reader fan-out + its `CLAUDE.md`, and `cat-tracker`/Strays (RN/Expo, frozen at the trio→build seam — no `package.json`/Expo yet). Setup categories recur across both with different specifics → thin stack-aware layer earned. Wrote [`project-setup-track1-findings.md`](../handoffs/project-setup-track1-findings.md).
2. **Track 3 — deep research.** Bundled `/deep-research` failed on its **known schema bug** (memory `deep-research-synthesis-loop-bug`) — died at the scope phase, nothing salvageable. Salvaged via a direct 5-agent web fan-out (one per track). One sub-agent misbehaved (spawned its own children, returned a "waiting" placeholder); caught it and re-tasked it via SendMessage to do the work itself. Wrote [`project-setup-track3-research.md`](../handoffs/project-setup-track3-research.md): market sells every capability, nobody sells the glue.
3. **Council** on the four forks (5 advisor + 5 reviewer + chairman). Verdict: COMPOSE not build; VENDOR now; defer starter-lane/submission with a maintained-option rule. Peer round was unusually decisive — every reviewer flagged the same unverified premises. [Report](../council/council-report-2026-07-01-project-setup.html) + [transcript](../council/council-transcript-2026-07-01-project-setup.md).
4. **Rex correction + spec.** Rex struck the council's hand-notes baseline ("i am never hand authoring... im not the developer, you are"). Folded that in as the spec's first principle and drafted [`project-setup-skill-spec.md`](../briefs/project-setup-skill-spec.md): a 4th `/project-setup` skill, v1 = RN/Expo recipe proven by standing up Strays.

Four commits (`cc49d61`, `a42df6b`, `0082061`, + this retro), committed-no-push through the session per Rex's instruction, pushed at close.

## What verification did and did NOT cover

- **Did:** every board edit re-rendered via `render-backlog-kanban.py` (0 tag warnings throughout); `check-live-links.py` clean after every doc batch (116→119 live docs, no broken links); HTML report opened in-browser (per file-delivery rule); council anonymization mapping saved for audit; the deep-research salvage re-tasked the misbehaving agent rather than accepting its placeholder.
- **Did NOT:** **no dry-run substitution against `output-small/`** — zero skill/template *product* was edited; everything landed as research docs, a council, a spec, and board rows. Track-1/Track-3 factual claims rest on reader authority + the sources cited (not independently re-verified line-by-line by me). The council's three unverified premises are explicitly *un*resolved by design — the spec's next step (stand up Strays for real) is what tests them. Self-verified — no independent sub-task verifier on the synthesis or the spec.

## Patterns worth keeping

- **cat-tracker as a "frozen at the seam" data point beat the shipped app for this question.** An in-progress project shows the gap live; the shipped one shows it healed-over. Reach for a mid-flight project when the question is about a *transition*, not an outcome.
- **The council earned its keep on premises, not the verdict.** The direction (compose/vendor) was near-unanimous from the advisors; the *value* was the peer round surfacing three load-bearing unverified premises no single advisor caught — including one (`capable actor may not exist`) that Rex's own correction then resolved.
- **Salvaging a broken bundled harness with a direct agent fan-out worked cleanly** — same output shape, no schema layer to hang on. Worth remembering the next time a bundled workflow dies.

## Failure / deviations / calls

- **The altitude miss is the real lesson.** For a designer-delegator, lead every deep-analysis turn with the plain-language conclusion and *keep* the engineering detail in appendices/tables — don't make Rex mine jargon to find the decision. The recovery (plain re-anchor + the "you're not the developer" correction) produced a *better, simpler* spec than the pre-correction framing, so the miss was caught in time — but it cost two round-trips.
- **Stated-but-unenforced premise.** I had "Rex delegates all engineering judgment" in the council framing and still let "hand-write notes" stand as a baseline. When a framing contains a hard constraint about the *user*, enforce it against every option before convening — a premise you state but don't apply is worse than one you omit.
- **No `D-NNN` logged — deliberate.** Like the prior foundation council, this is a *gated direction*, not a committed build; it becomes a real decision once the Strays pilot resolves the premises. Noted in the handoff + spec so the call is auditable. DECISIONS_ACTIVE marker untouched (through D-072), correct.
- **Deviation: heavy multi-agent spend** (5 research + 5 advisor + 5 reviewer + 1 chairman + readers). Justified — Rex explicitly opted into deep-research and the council; fan-outs kept raw material out of the main window.

## Port-back check

The `/project-setup` skill, once built, is itself the port target (it's product). The generic lesson here — *state the user's operating model as a first-class constraint and enforce it against every option* — is a council/framing discipline, not a scaffold rule; not porting it. No scaffold-template change this session.
</content>
