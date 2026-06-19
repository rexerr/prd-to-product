# Council transcript — Ticket + queue vs. the dense single-file BACKLOG

**Date:** 2026-06-19

## Framed question

Should Rex — a designer running a SOLO skill-development repo whose main collaborator is an AI coding agent (Claude Code), no team, no deployed app — replace his current project management (a single dense `BACKLOG.md` where each item is an 800+ word entry fusing a prioritized "what's next" list WITH a deep reasoning archive, read whole by the agent at every session start) with an industry-standard ticket + queue model (per-file tickets, a structured file, an HTML app, or Linear/GitHub Issues)? Or is the dense single file actually well-suited to a solo-human-plus-agent workflow, making tickets pointless ceremony?

Constraints: a standing invariant ([D-001](../DECISIONS.md)) requires markdown for context files the agent reads at session start; CLAUDE.md warns relocating docs breaks ~75–90 cross-references.

---

## Anonymization mapping (for audit)

```json
{"A": "The Veteran", "B": "The Long View", "C": "The Skeptic", "D": "The Architect", "E": "The Stranger"}
```

---

## Advisor responses (de-anonymized)

### The Skeptic
Tickets-per-file fails the one constraint that actually governs this repo: the agent's session-start read. A single read gives the agent priority ordering plus reasoning in one shot; splitting into N ticket files forces an index lookup then fan-out reads to reconstruct the why — strictly more tokens, more round-trips, and it reintroduces the "lost context between sessions" failure CLAUDE.md legislates against. There's no second human to assign a ticket to. But the status quo isn't clean: the real defect is the *fusion* — an 800-word entry welding "do this next" to a decision archive buries the actionable signal in prose the agent re-pays for every session. The HTML-app fix is a trap (collides with D-001; building product to manage a workspace). Don't migrate — split the two jobs inside markdown: thin top-of-file queue + archive below or in `docs/`. Cheap, reversible, no cross-reference breakage.

### The Architect
Tickets vs. dense BACKLOG is the wrong axis — this is a context-engineering problem. Two artifacts with opposite read-frequencies and lifespans were fused: the queue is read every session and changes constantly; the archive is read rarely and is append-only. You pay archive cost at queue frequency. Don't import the ticket *model*; import the one property that makes tickets work — separation of live queue from dead record. Simplest first move: thin top section (one line per item: title, status, next action, link), prose pushed down or into the retros/decisions you already cross-reference. Skip Linear/Issues (outside repo, break D-001) and the HTML app. Optimize session-start tokens per decision. Split the file; measure the read.

### The Stranger
Per-ticket files force the agent to discover which files matter — something it's bad at. The single-file read matches how this collaborator ingests context. But "fuses two jobs" is the tell: a per-session queue welded to a rarely-read archive means paying the archive's token cost on every resume. "Industry standard" carries no authority here — Linear/Issues solve multi-human coordination (shared visibility, assignment, status) this workspace doesn't have. Two readers, Rex and the agent; neither needs handoff, both need fast resume. Don't adopt tickets — split queue from archive. The HTML app is ceremony in a costume; breaks D-001.

### The Long View
The whole-file session-start read compounds against you. BACKLOG.md grows monotonically; in three years the actionable "what's next" is a thin signal buried in deep sediment of why-we-did-things, re-read every session at rising cost — a slow leak that worsens as the project succeeds. The two jobs depreciate at opposite rates: the queue is perishable, the archive appreciates. Fusing them drags the durable layer through a perishable-frequency re-read. Split: thin queue + the archive you already have (DECISIONS.md, retros). Don't build the HTML app (JSON island fights D-001's spirit; a UI surface to maintain forever). Reversibility cuts toward acting now — cross-references get harder to untangle the longer you wait.

### The Veteran
The dense single-file BACKLOG is the right tool; "professionalizing" is the trap. I've watched this migration a dozen times — six months later a Linear board nobody grooms, tickets rotting because context lives elsewhere, two reads to do one thing. Tickets solve coordination problems you don't have (handoffs, assignment, manager visibility); a solo operator pays every amortized cost alone with zero payoff. The agent resumes cold and works better with reasoning adjacent to action — the fusion is the *feature*. The real pain is only that prioritization is buried in prose: add a thin prioritized index on top, leave dense entries below. 30-minute edit, fully reversible, zero cross-reference breakage. Kill the HTML app.

---

## Peer review (de-anonymized)

**Vote tally — Strongest:** The Long View ×4, The Architect ×1.
**Vote tally — Biggest blind spot:** The Veteran ×4, The Long View ×1.

- **Reviewer (Skeptic):** strongest = Architect (reframes to the variable to optimize + ends on a measurable test); blind spot = Long View (overstates urgency for a low-risk edit). *All missed:* nobody specifies the discipline that stops the split from re-fusing over time; nobody asks whether queue + archive could just be two files read selectively.
- **Reviewer (Architect):** strongest = Long View; blind spot = Veteran (inlining keeps the tax). *All missed:* nobody defines the cut line where the queue links *into* DECISIONS.md/retros without making a third copy of the "why"; nobody proposes measuring session-start tokens before/after as the gate.
- **Reviewer (Stranger):** strongest = Long View; blind spot = Veteran. *All missed:* nobody verifies whether the agent truly ingests all 800-word entries; reasoning may already be duplicated in DECISIONS.md/retros (fix = dedup, not restructure); nobody flags the ~75–90 cross-reference breakage risk.
- **Reviewer (Long View):** strongest = Long View; blind spot = Veteran. *All missed:* "cheapest today / no cross-reference breakage" asserted, not checked against CLAUDE.md's own 75–90-reference warning.
- **Reviewer (Veteran):** strongest = Long View; blind spot = Veteran. *All missed:* if the archive moves OUT of the always-read set, the agent loses the inline "why" it resumes cold with — the split only works if link-following fires on the right items, and nobody defines a mechanism or test; nobody measures current tokens first.

---

## Chairman synthesis

**Headline:** Keep one markdown file but split it in two layers — a thin top-of-file priority queue over the dense reasoning archive — and do not adopt tickets, an external tool, or the HTML app.

**Recommendation:** Restructure `BACKLOG.md` in place — thin priority-ordered queue at the top (one line per active item: title, status, next action, link), dense reasoning kept below in the same file. No tickets, no Linear/Issues, no HTML app. The only governing constraint is the agent's session-start read; the genuine defect is paying archive-weight tokens to extract a queue-weight signal every session. Keeping the archive in the same file means anchors don't move (the ~75–90 cross-references keep resolving), stays markdown (honors D-001), and adds no UI surface. A 30-minute reversible edit. Two disciplines make it durable: (a) the queue links *into* existing DECISIONS.md/retros rather than restating them (pointer, not a third copy); (b) a one-line rule that queue entries stay one line and reasoning lives below/in the archive (guards against silent re-fusion).

**First step:** Before editing, measure the actual session-start token cost of reading BACKLOG.md today and confirm whether its reasoning is already duplicated in DECISIONS.md/retros — that tells you whether this is a restructuring job or a deduplication job, and gives you the before/after baseline the repo's verification discipline requires.
