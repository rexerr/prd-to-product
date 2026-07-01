# Retro — 2026-07-01 16:48 CDT — Track-2 mining marathon: 4 repos + the Every cluster + the CE-plugin slice   (1st session of the day)

**Dominant failure tag: none** — with one near-miss worth recording loudly (below), caught by Rex, not by me.

## What happened

Five `/mine` runs, five commits, every adoption through propose-and-wait:

1. **TanStack/template** (`c0ac1e5`) — prior **falsified**: a library-authoring scaffold, not an app starter (three blind readers converged unprimed). Adopted the enumerated-orthogonal-CI-gates model into the project-setup handoff + 2 rows.
2. **garrytan/gstack** (`b9f77b3`) — the decision-grade Track-2 input: fills 4 of the trio's 5 holes substantively; shares the 5th (nobody scaffolds the stack); its maintenance plumbing is the existence-proof the 06-30 council doubted. Fork reframed to *compose the methodology, don't vendor the artifact*; council recommended at the decision point.
3. **workflow + devtools** (`e1df2dd`) — both "likely tangential" priors **refuted at the margins**: workflow carries direct chain-auto-compose prior art (its maintainers' own AI-orchestration research docs); devtools yielded the e2e-harness reference, a11y-as-QA-dimension, and three failure-mode spec enrichments from its intent-generated `skill_spec.md`.
4. **Every agent-native guide cluster** (`72d3881`, 4 articles + a verification clone) — the client-work-OS product fork (routed brainstorm → brief → PRD), two new Seq-1 coverage dimensions (instrumentation/metrics; dev-workflow agent parity — with the in-product-vs-dev-workflow axis distinction recorded), and the finding that the articles' plugin claims had **drifted from HEAD** (27 skills / 0 agents now).
5. **CE-plugin authoring slice** (`a9dd84f`) — the richest skill-craft source yet: evidence base graded 9-incident/7-measured/4-design with falsified hypotheses recorded; two forks banked for adjudication (≤500-line cap vs. conditionality discipline; deletion-test vs. mandatory failure-mode clauses); chain-handoff audit row (#714 class); eval methodology folded into the pressure-test ticket.

**Board structure changed meaningfully:** `next` is now Seq 1 project-setup design → Seq 2 CE-plugin *remainder* mine → Seq 3 **skill-craft consolidation pass** (the five parked buckets' rule-of-2 gates have tripped across four independent sources — the accumulation itself was a finding).

## The near-miss (record this pattern)

I proposed running workflow + devtools as one lightweight combined "confirm-or-discard" pass because their priors said *tangential*. **Rex refused:** "you think that and then we miss stuff." He was right twice over — both repos yielded adopted work a skim would have missed (the orchestration research dir; the `skill_spec.md`). This is the same failure class the intent mine had already named ("the IP was in the files whose titles didn't advertise it") and I still walked toward it. Rex later generalized it into board policy on the remainder row: *every skipped source has proven worthy on return.* **Lesson: a prior from a repo's name/description sets the mine's hypothesis, never its depth.**

Two smaller honesty items: (a) I editorialized on the Codex article a turn before mining it — anchoring risk, disclosed in the mined doc, mitigated only because the finding routes to a gate; next time, mine first, editorialize after. (b) One verification grep (V4, the #714 cite) initially "found nothing" because my pattern was too narrow — recovered by rechecking before grading the claim, which is the right reflex, but a lazier session would have marked a true claim refuted.

## Verification — what it did and didn't cover

- **Did:** every repo claim adopted was checked against its pinned clone (template `22ed194`, gstack `11de390`, workflow `602cdec`, devtools `92f69d0`, CE-plugin `db21ba2`) — including the easy-to-get-wrong negatives (no vuln-scanning in template; no stack-scaffolding anywhere in gstack; nine CE citations spot-checked verbatim). Blind-reader independence held (readers got facts + dedup inventory, never my valuations; convergent verdicts were unprimed). `render-backlog-kanban.py` after every board edit (0 tag warnings throughout); `check-live-links.py` clean (116 docs) after every doc batch.
- **Did NOT:** article claims stayed *soft* by design — parked behind gates, not "verified" (the WebFetch-summarization layer on the agent-native guide is flagged in its mined doc). gstack's `/qa` browser binary is architecturally confirmed but not executable-verified (build artifact absent from the clone). No skill/template product files were edited this session — everything landed as mined docs, board rows, handoff updates, and one ticket fold — so no dry-run substitution against `output-small/` was applicable.

## Deviations / calls

- **One session, five mines** — against the "new session for a new task" norm. Deliberate: the dedup inventory (what's parked in which row) was the expensive context, and it compounded across mines; readers kept the raw material out of the main window. It worked, but this is near the ceiling — the consolidation pass and the remainder mine should each get a fresh session.
- **Re-scoped instead of retired** (Rex's call): the completed plugin-mine row became the remainder row rather than leaving the board — correct under archive-don't-delete instincts, and it encodes the near-miss lesson where the next session will read it.
- **No decisions logged** — deliberate: all three big calls were routed to their proper gates (council / consolidation / brainstorm) rather than banked mid-mine. D-072 marker untouched and current.
