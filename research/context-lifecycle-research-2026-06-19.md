# Research — Bounding agent session-start context (backlog + decision lifecycle)

**Date:** 2026-06-19
**Method:** `deep-research` harness — 6 search angles, 24 sources fetched, 111 claims extracted, top 25 adversarially verified (3 votes each; 2 refutes kills). **25 confirmed, 0 killed.** 10 findings after synthesis.
**Driving question:** How do practitioners keep the working context for a long-running AI coding agent bounded as a solo project accumulates history — specifically the lifecycle of task backlogs and decision logs — so session-start load stays small while old context stays retrievable on demand?

This is the permanent citation record for [`docs/briefs/context-lifecycle-brief.md`](../docs/briefs/context-lifecycle-brief.md). The brief is the actionable proposal; this file is the evidence.

---

## One-paragraph synthesis

Practitioners running long-horizon AI coding agents converge on one principle: **load the smallest high-signal token set at session start and retrieve everything else on demand**, because context degrades with length ("context rot") and the window is a finite, depleting budget. The dominant pattern is a **hot/cold split** — always-loaded lightweight metadata (a count, an index, name+description stubs) registers what exists, while full content is pulled just-in-time via file reads, queries, or tool calls. For task backlogs, the agent-native state of the art replaces the single dense markdown file with a queryable per-project store where status fields let the agent find active vs. done work without scanning files, and a dedicated archive buckets completed items into read-only segments retrievable on demand; **Spec Kit** shows the markdown-only equivalent (ordered per-task artifacts). For decisions, the **ADR lifecycle** marks records proposed/accepted/deprecated/superseded rather than deleting them — a built-in active-vs-stale tiering. The crucial caution: **archive, don't delete** — irreversible pruning risks dropping tokens a future turn needs.

---

## Findings (all verified 3-0)

### 1. Keep the hot set small — "context rot" is real (high confidence)
*Sources: [Anthropic — Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Anthropic cookbook — context engineering](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools)*

Anthropic, verbatim: *"as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases"* ("context rot"), and *"good context engineering means finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."* Corroborated by Chroma's 2025 study (all 18 frontier models degrade) and Stanford's "lost-in-the-middle" (Liu et al. 2023, 30%+ U-shaped recall drop). **Caveat from the source:** it's a *gradient, not a hard cliff* — so an over-large hot set degrades gracefully, not catastrophically.

### 2. Just-in-time retrieval: lightweight identifiers loaded, content on demand (high)
*Sources: [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool), [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)*

Anthropic, verbatim: *"Rather than pre-processing all relevant data up front, agents built with the just-in-time approach maintain lightweight identifiers (file paths, stored queries, web links, etc.) and use these references to dynamically load data into context at runtime using tools."* Agent Skills make it concrete: metadata (name+description, ~100 tokens/skill) is always loaded; *"the rest remain on the filesystem consuming zero tokens"* until read. **An index-plus-tickets folder IS this pattern.** Calibration: Anthropic recommends a *hybrid* (preload some for speed, explore the rest) — which an index+tickets structure already is.

### 3. Agent-native backlogs are queryable stores with status fields, not one dense file (high; single-source)
*Source: [backloghq/backlog](https://github.com/backloghq/backlog)*

A current, actively-maintained Claude Code plugin stores tasks in a per-project DB with auto-increment IDs and status fields; agents discover work by querying filters (`status:pending`, `+ACTIVE`, `+BLOCKED`, `+READY`) rather than scanning files. **Caveat:** single data point — treat the *specific* "database over markdown" convention as one well-documented implementation, not industry consensus. The transferable lesson (status-tagged, discoverable-without-scanning) holds even if you stay in markdown.

### 4. Completed items move to time-bucketed archive segments, retrievable read-only (high; single-source)
*Source: [backloghq/backlog](https://github.com/backloghq/backlog)*

`task_archive` = *"Move old completed/deleted tasks to quarterly archive segments"*; companion `task_archive_list` / `task_archive_load` ("read-only inspection") complete the lifecycle: move out of the active set, retrieve on demand. Directly models the candidate fix (archive a ticket when done).

### 5. Session-start should load only lightweight metadata — Claude Code enforces this itself (high)
*Sources: [Claude Code memory docs](https://code.claude.com/docs/en/memory), [backloghq/backlog](https://github.com/backloghq/backlog)*

Claude Code's own memory docs, verbatim: *"The first 200 lines of MEMORY.md, or the first 25KB, whichever comes first, are loaded at the start of every conversation… Topic files like debugging.md or patterns.md are not loaded at startup. Claude reads them on demand."* backloghq's SessionStart hook surfaces a *pending-task count*, not contents. **This is the strongest evidence for the proposed design — and the current "read the WHOLE BACKLOG.md at session start" runs directly against this built-in 200-line/25KB convention.**

### 6. ADR lifecycle retires decisions by status, not deletion (high)
*Source: [Nygard ADR template (joelparkerhenderson)](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md)*

The canonical template's Status field: *"proposed, accepted, rejected, deprecated, superseded, etc."* "Deprecated"/"superseded" are the built-in mechanism for retiring a decision without deleting it. **Caveat:** the template lists these as examples, not a formal state machine — "lifecycle" is a mild characterization. This is the best transferable model for a `DECISIONS_ACTIVE.md` (hot) / `DECISIONS.md` (full) split: a superseded decision drops from the active tier, stays in the full log.

### 7. Archive, don't delete — the hard guardrail (high)
*Source: [Anthropic — Managed agents](https://www.anthropic.com/engineering/managed-agents)*

Durable context lives *outside* the active window (append-only event log / memory files), retrieved on demand by positional slices or file reads. Critical, verbatim: *"irreversible decisions to selectively retain or discard context can lead to failures. It is difficult to know which tokens the future turns will need"* — and these are *"recoverable only if they are stored."* **This tempers the candidate fix's "or delete a ticket when done": delete only when decisions/retros genuinely capture the why; otherwise archive (nearly free for local files).**

### 8. Three composable context primitives: compaction, tool-result clearing, memory (high)
*Sources: [Anthropic cookbook](https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools), [Memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)*

Compaction (distill a window into a high-fidelity summary), tool-result clearing (drop re-fetchable results, keep the record the call happened — empirically cut peak context ~48%), and memory (persistent external notes across sessions). The prescribed **multi-session pattern**: bootstrap a progress log + checklist; *"each new session opens by reading those memory artifacts… recovers the full state of the project in seconds, without needing to re-explore."* Anti-bloat guidance: *"rename or delete files that are no longer relevant. Do not create new files unless necessary."*

### 9. Agents read partially and search on demand — structure for targeted retrieval (high)
*Source: [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference)*

`Read`, verbatim: *"When a whole-file read exceeds the token limit, Read returns the first page with a PARTIAL view notice… how to read more with offset and limit."* `Grep` default output is *"files_with_matches: file paths only."* **Implication:** a folder of discrete, greppable, status-tagged ticket files lets the agent find the one it needs without ingesting the whole backlog — whereas one dense file forces a full read or fragile offset reads. (Confirms: partial reading is a real capability; the lever is structure.)

### 10. Spec Kit = the markdown-native template for bounded per-unit artifacts (high)
*Source: [GitHub Spec Kit](https://github.github.com/spec-kit/)*

Agent work as a four-phase chain (Spec → Plan → Tasks → Implement), each phase emitting a separate Markdown artifact that feeds the next; tasks are one-unit-of-work-per-file in a `tasks/` folder. Verbatim: *"Each phase produces a Markdown artifact that feeds the next — giving your AI coding agent structured context instead of ad-hoc prompts."* **The published, markdown-only validation of ordered per-ticket files** — no database needed (relevant given this repo's markdown-only invariant). Covers decomposition but *not* an explicit archival step; pair with findings 6 & 7 for the full lifecycle.

---

## Caveats (from the report)

- **Uneven source strength.** The hot/cold *principles* (1, 2, 7, 8, 9) rest on multiple Anthropic **primary** sources — high confidence. The backlog *structure* specifics (3, 4, 5) lean heavily on **one tool** (backloghq) — one well-documented implementation, not consensus. The decision lifecycle (6) is **human-team practice transferred** to agents; agent-native ADR conventions are thin in the corpus.
- **Fast-moving field.** Sources dated 2025–2026, referencing the memory tool, context-editing API, MEMORY.md limits. Exact thresholds may shift.
- **Gradient, not cliff.** Over-large hot set degrades gracefully — the cost of *not* fixing this is slow, not sudden.
- **Delete is conditional.** Hard-delete is safe only if decisions/retros truly capture the why; default to archive-retrievable.

## Open questions (genuinely unresolved — carried into the brief)

1. **The index grows too.** A one-line-per-ticket index also accretes — at what point does it need its own summarization, and should it be *generated* rather than hand-maintained? (Mitigant: index only *active* items → bounded by work-in-flight, not history.)
2. **Markdown-only "querying."** With no database, what's the most reliable status mechanism — greppable frontmatter tags, a naming convention (`0039-done-*.md`), or a separate index file — and what minimizes drift between index and ticket files?
3. **Delete-vs-archive test.** What concretely proves "the decision/retro fully captures the why" so deletion is safe?
4. **Decision-tier threshold.** When does a deprecated/superseded decision drop out of `DECISIONS_ACTIVE.md` — a rule or a per-case judgment?

## Full source list (24 fetched)

Primary: Anthropic effective-context-engineering, Anthropic cookbook (context engineering), Anthropic memory-tool docs, Anthropic managed-agents, Claude Code memory docs, Claude Code tools-reference, Agent Skills overview, backloghq/backlog, Nygard ADR template, GitHub Spec Kit. Plus blogs/secondary: Martin Fowler (ADR), taskmd, mindstudio (×3), victordibia newsletter, llamaindex "files are all you need", lethain "agents and large files", datastudios (Claude Code memory), hidekazu-konishi (ADR ops), ctaverna (ADR), dev.to (markdown memory), emelia.io (superpowers).
