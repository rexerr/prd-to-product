# Council transcript — 2026-06-24 — Batch B: port the one-board kanban model into the context-engineering scaffold?

Report: [`council-report-2026-06-24-batch-b.html`](council-report-2026-06-24-batch-b.html) · Data: [`council-data-2026-06-24-batch-b.json`](council-data-2026-06-24-batch-b.json)

## Framed question

Should the `context-engineering` scaffold templates be changed so every newly-scaffolded project is BORN with the one-board kanban work-tracking model (one row per unit; lanes active/next/watching/backlog/blocked/icebox; Seq ordering; board-is-the-roadmap; thin-on-touch; retire-don't-re-accrete; detail in `tickets/<slug>.md`) — instead of the older multi-section backlog shape (Build plan / In progress / Backlog / Open decisions / Later / Done) it ships today? Graduation machinery already exists (backlog outgrows the session-start read → thin index + `docs/tickets/` + retirement ritual); the mismatch between today's shape and that target is a **soft seam** (generic `status` frontmatter, not hardcoded lanes), not a hard contradiction. Proven in the meta-repo, unproven on arbitrary scaffolded projects. Costly + hard to reverse. Options: **(A)** full port now · **(B)** keep simple multi-section default · **(C)** reduced/optional — lanes-no-Seq, or ship the model as the graduation target rather than the day-one default.

Gated on this council per [D-054](../DECISIONS.md); board row 40.

## Verdict (chairman)

**Keep the simple multi-section backlog as the day-one default; rewrite the existing graduation rule to migrate INTO the one-board kanban — but verify first that real scaffolded projects ever actually trigger graduation, because the whole compromise dies if they don't.**

Option **C, "adopt at graduation" variant**, day-one stays simple and Seq-free; the graduation rule's target becomes "thin index + one-board kanban (named lanes) + tickets," each lane citing its failure mode, closing the soft seam (generic `status` → named lanes). **Provisional on a premise check** — see first step.

**First step:** verify two unverified load-bearing premises before writing any rule change — (1) the actual horizon/size distribution of real scaffolded projects, and (2) whether the graduation trigger has *ever* fired outside the meta-repo. No downstream data → that's the finding: keep B, add one lightweight observation hook so the next few real projects generate the signal; only then rewrite the target.

## Council alignment

| Advisor | Position | Core argument |
|---|---|---|
| The Skeptic | Default B; kanban as graduation target | Meta-repo is the maximum-favorable case and bloat is already handled, so day-one Seq solves a non-existent problem and fails the failure-mode-citation rule. |
| The Architect | Option C at graduation | The fork is *when* a project pays the cost, not *which* template — keep the simple default, repoint the graduation rule at named lanes. |
| The Stranger | Option C at graduation | An outsider handed a six-lane Seq board before writing a line of code experiences governance as overhead — birth is the wrong moment, graduation is right. |
| The Long View | Option B, wait for signal | Scaffolds are a distribution decision; porting a young, unstabilized model hard-couples the installed base to a future migration liability. |
| The Veteran | Option C, lanes not Seq, at graduation | Lanes are cheap and legible, but Seq + accretion rituals are the expensive operator-dependent part — ship as an earned upgrade. |

## Anonymization mapping (audit)

`A → The Long View · B → The Veteran · C → The Skeptic · D → The Architect · E → The Stranger`

## Peer review

**Votes — unanimous:** strongest = **The Architect** (5/5, the trigger-not-template reframe + the smallest concrete move); biggest blind spot = **The Long View** (5/5, pure inaction strands the proven model and leaves the graduation target half-defined).

**What the council collectively missed (the high-value catch):** every advisor assumed, without a shred of evidence, that (1) the **median scaffolded project is a solo weekend app** that never outgrows a flat backlog, and (2) the **graduation trigger actually fires** on real downstream projects. Both are load-bearing: if the skill mostly serves longer-horizon products, Option A gets materially stronger; if graduation never fires in the wild, "adopt at graduation" is Option B in a compromise costume. A secondary catch: even the graduation target may export an **operator-dependent practice** (the retirement ritual works here because Rex runs it). → This is why the chairman made premise-verification the first step and rated confidence moderate, not high.

## Full advisor responses

See [`council-data-2026-06-24-batch-b.json`](council-data-2026-06-24-batch-b.json) `advisors[]` for the verbatim responses (not duplicated here per the reference-don't-restate rule).

## Note

Pre-convening fact-gate caught one overstatement from the port-debt sweep: the retirement ritual uses a **generic `status` frontmatter field**, NOT enumerated lane vocabulary — so the scaffold's internal inconsistency is a *soft seam*, not the hard contradiction the sweep reported. The framing was corrected before advisors ran.
