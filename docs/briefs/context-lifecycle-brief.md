# Context lifecycle — investigation brief

**Status:** Proposed. No edits made. Foundation change → a future `D-NNN` per [D-001](../DECISIONS.md), council-grade. Sequenced behind crib-adoption work.

## Why this exists

The repo's project management lives in one dense [`BACKLOG.md`](../../BACKLOG.md) read whole at every session start, alongside [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md) and the newest retro. The diagnosed defect (Rex, 2026-06-19): **nothing ever leaves the hot set.** Backlog and decision log grow monotonically, so every session re-pays an ever-rising token cost to load context, and there is no mechanism to retire completed work or superseded decisions. This isn't "tickets vs. one file" — it's a missing *lifecycle*.

Two prior passes fed this brief:
- **Council** ([`../council/council-report-2026-06-19-pm-system.html`](../council/council-report-2026-06-19-pm-system.html)) — settled the easy part: do **not** adopt external trackers (Linear/Jira/Issues) or an HTML app for a solo+agent workflow. But it landed on "split the file in place (thin index on top, archive below)," which is **wrong**: with the archive below in the same always-read file, the agent still reads it whole — token cost unchanged. The council reasoned without the context-engineering evidence.
- **Research** ([`../../research/context-lifecycle-research-2026-06-19.md`](../../research/context-lifecycle-research-2026-06-19.md)) — 25 claims verified 3-0, 0 killed. Corrects the council and validates the folder-of-tickets direction.

## What the research establishes

1. **Keep the session-start hot set small** — "context rot": recall degrades as tokens rise (gradient, not cliff). Load the *smallest high-signal set*.
2. **Just-in-time retrieval** — keep lightweight identifiers (an index, paths, status tags) always loaded; pull full content on demand. An index + tickets folder *is* this pattern.
3. **Claude Code already works this way** — it loads only the first 200 lines / 25KB of its memory file at startup; deeper topic files are read **on demand**. The current "read the whole BACKLOG.md" fights the platform's own convention.
4. **ADR lifecycle** — decisions are marked `proposed/accepted/deprecated/superseded`, not deleted: built-in active-vs-stale tiering.
5. **Archive, don't delete** — Anthropic managed-agents: *"it is difficult to know which tokens the future turns will need."* Hard-delete only when the why is provably captured elsewhere.
6. **Agents read partially** (`Read` offset/limit, `Grep` paths-only) — so discrete, greppable, status-tagged files enable targeted retrieval; one dense file forces a full read.
7. **Spec Kit** is the markdown-native precedent: ordered per-task files, one unit of work per file — no database (fits this repo's markdown-only invariant).

## The proposed structure

Markdown-only (no database/plugin — that would break [D-001](../DECISIONS.md)):

```
BACKLOG.md              ← thin ALWAYS-LOADED index: one line per ACTIVE ticket
                          (id · title · status · next action · link). Bounded by work-in-flight.
tickets/
  0042-<slug>.md          ← full context per ticket; read ON DEMAND when picked up
  0043-<slug>.md          ← frontmatter `status: ready|active|blocked` (greppable)
  archive/
    0039-<slug>.md        ← DONE tickets move here; dropped from index, still retrievable
DECISIONS_ACTIVE.md     ← hot tier: only accepted/active decisions
DECISIONS.md            ← full cold log; nothing deleted
retros/                 ← unchanged (already self-limiting: only newest read)
```

Three moving parts:
1. **Backlog = thin index + tickets folder.** Index lists only *active* work → bounded by work-in-flight, not total history. Each ticket carries the full "context to act."
2. **Decisions get ADR status.** When a decision is superseded, it drops from `DECISIONS_ACTIVE.md` (hot) but stays in `DECISIONS.md` (cold). **This is the retirement mechanism that was missing — demotion, not deletion.**
3. **An explicit retirement ritual** (e.g. folded into `/end-session`): done ticket → `tickets/archive/`; superseded decision → drop from ACTIVE. The reason nothing leaves the hot set today is there's no *step* that demotes things.

**Hard rule:** archive, don't delete. Hard-delete a ticket only when its decision/retro provably captures the why; even then, archiving is nearly free for local files. Default to archive.

## Open questions (resolve in design, before any migration)

1. **The index grows too.** Listing only *active* items mostly bounds it; at scale, consider generating it rather than hand-maintaining. **Recommended:** start hand-maintained + active-only; revisit if it bloats.
2. **Markdown "querying" without a DB.** Options: greppable `status:` frontmatter / naming convention (`0039-done-*.md`) / separate index file. **Recommended:** frontmatter `status:` tag (greppable) + the index as the human-facing queue; accept that the index is the one hand-synced surface, kept honest by the retirement ritual.
3. **Delete-vs-archive test.** **Recommended:** delete only if a `D-NNN` or retro names the ticket's outcome; otherwise archive.
4. **Decision-tier threshold.** **Recommended:** a decision drops from ACTIVE when superseded by a later `D-NNN` or marked deprecated — a judgment call at retirement time, not an automatic rule.

## Migration approach & failure modes

- **The real risk is cross-references.** CLAUDE.md warns relocating docs breaks ~75–90 cross-references. **Mitigation:** tickets keep their *own* files and the index only *links*; the bulk of the existing reasoning stays where it already lives (DECISIONS.md, retros), so migration is mostly *extraction of one-line queue entries + pointers*, not bulk relocation. Audit per-item first (is the "why" already in DECISIONS/retros?) to confirm it's extraction, not duplication.
- **Don't create a third copy of the "why."** Tickets point into DECISIONS/retros; they don't restate them.
- **Index drift.** The index can fall out of sync with ticket files. The retirement ritual is the anti-drift mechanism; a periodic grep of `status:` vs. index entries catches drift.
- **Over-engineering.** Solo+agent doesn't need backloghq's database or quarterly buckets. Start with the simplest markdown version; add machinery only when a real failure appears (Rule of Two).

## Out of scope

- Implementing the structure. This is investigation + proposal; the redesign is a separate, scope-gated, `D-NNN`-and-likely-council session.
- Changing the markdown-only invariant. The proposal stays markdown.
- The HTML roadmap app (council-killed) and external trackers (council-killed).

## Suggested first move when promoted

Run the **per-item audit** (read-only): for each BACKLOG item, classify "actionable line" + "where the why already lives (DECISIONS/retros)" + "what would be orphaned by extracting it." That single pass tells you whether this is cheap extraction or needs reasoning rehomed first — and is the red/after baseline the repo's verification discipline requires.
