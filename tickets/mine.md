---
slug: mine
status: next
seq: 2
title: /mine — codify the source-agnostic mining process
---

# /mine

Mines **any source** — a repo (URL or local path), a dumped-docs pile, a design export, a research dump — for value and saves the findings into our system. Codifies the refined mining `Workflow`: stage source → inventory (+ license for repos) → triage fan-out → adversarial-verify every integrate/implement pick → synthesize into a source-organized tracker (**lens A** → cribs/roadmap) or the project's own surfaces (**lens B** → its BACKLOG/context). The name is deliberately broader than the old `/repo-miner` — the engine is source-agnostic.

## Current state

- **Rule-of-Two met** (Steinberger ×3 rounds + Pocock/designer ×2 passes, 2026-06-17). Past the codify threshold.
- **A-vs-B fork RESOLVED** (devils-advocate 2026-06-18): A (crib lens — "what should I steal into my tooling?") and B (project lens — "what does this project need?") are two *lenses* on one shared **engine** (stage → fan-out read → triage → adversarial-verify → tracker + amend one plan), not competing skills. Only the triage lens and output home differ.

## Next

Resolved to **proceed** (devils-advocate 2026-06-21 — verdict Proceed with guardrails). The graveyard and unproven-loop attacks collapsed once the design was clarified: **output becomes adoptable work, not an archive**, and the cribs pipeline already proves the loop end to end. Build via `/furnace-plan` (a real authoring task; plan presented for approval before any edit). Form fork **resolved → explicit-invoke skill** (not a playbook): [D-034](../docs/DECISIONS.md#d-034) makes an explicit-invoke skill cost nothing in-window, removing the playbook's only advantage. Order vs the docs-routing item is Rex's call (see Dependency).

## Resolved shape (2026-06-21, post-DA)

- **Portable global explicit-invoke skill** (lives in `~/.claude/skills/`, like `furnace-plan`; runs in any project; reads the host project's context to set the relevance lens). Not scaffolded per project.
- **Output is proposed work, never an archive.** Every mine ends in candidate board rows / tickets / fixes in the host project (lens B) or tooling cribs (lens A), each carrying the finding, source citation, confidence note and a proposed lane. Rex adopts through the normal gate. No read-later folder to rot — the same path cribs already take.
- **Tiered verification by source ground-truth.** A code/repo claim is checked against the repo and can become a fix directly. A soft claim (tip, opinion, thread) cannot be proven, so it enters as a **time-boxed experiment ticket with an explicit kill condition** (try X for a week, keep only if it measurably helps) — never a silent fix, never labeled "verified." This is how new-model / new-technique advice enters, as a falsifiable bet.
- **Reuse the cribs adoption gate** (Rule-of-Two / decision discipline). Propose, never auto-apply.
- **Success metric = adopted work shipped, not stuff captured.** A thin tally (mined finding → adopted ticket → shipped improvement), like the crib roadmap or furnace ledger. Self-cleaning leading indicator: if mines stop producing adopted work, the skill isn't earning its keep.
- **v1 scope:** repos + paste-or-URL (pasted text covers YouTube transcripts, Reddit threads, anything Rex drops in). Design/visual mining is a **separate later skill** (vision + site-scraping for design systems/components, a natural feed into DSB adopt mode). New source types earn their way in on real need.

## Storage model (where mined repos live)

- **Committed (the durable reference):** `docs/mined/<date>-<source>.md` — findings + source URL + **pinned commit SHA** + license + the proposed tickets. This *is* the thing referenced ongoing, and it makes the mine reproducible.
- **Local cache, gitignored (regenerable):** `docs/mined/repos/<name>/` — shallow clone pinned to the SHA, browsable on disk, **never committed**. The skill writes the `.gitignore` entry for `repos/` on first run in a project.
- **Why not commit the repos:** permanent history bloat, license drag, nested-`.git` mess — and zero gain, since the findings doc + pinned SHA re-clone the exact code on demand.
- **Alternative (Rule-of-Two):** a shared `~/.mine/cache/` to dedupe clones across projects; switch only if re-cloning the same repos becomes a real annoyance.

## Dependency / sequence (Rex's call — not a hard prerequisite)

`/mine`'s landing behavior should follow the docs-routing principle already settled by research: the skill writes generic, defers to the project's declared landing zone, and proposes one (`docs/mined/`) if none exists. Because `/mine` proposes-and-waits in the no-convention case, it is **not blocked** on the context-engineering docs-routing scaffold change — either build order works. Docs-routing-first buys a settled convention (less rework); `/mine`-first gives docs-routing a real consumer to design against.

## Open

- B likely resolves into a `context-engineering` *extension* + a convention (broader source-type intake + an "append actionable items to BACKLOG" step), not a new skill — probably avoiding the `CF-22`/`CF-23` router cost entirely.
- Build the engine as: stage source → fan-out read → triage through the lens → adversarial-verify every keeper → return draft tickets → (on adoption) amend the *one* plan, pointer-not-copy (`C-19`).

## Engine gotchas (the encoded scar tissue — the real value, not the mechanics)

Surgical-not-blanket depth ([D-022](../docs/DECISIONS.md#d-022) — full 6-lens pass only on skill-authoring/governance skills, single-lens whole-skill triage for the off-domain mass); adversarial-verify every integrate/implement pick; dedup against existing `C`/`CF`/`DG` cribs (cite overlap, don't re-mint); **synthesis agents must RETURN drafts, never Write product** (the gate that failed 2026-06-17 — a synth agent wrote 23 cribs straight into the doc); don't-merge-trackers (D-022); consolidate skeptically (watch rubric inflation/fragmentation); tracker FORMAT (failure-it-prevents · surface · tier · status · parked); scratch cleanup.

## Why (pointers)

[2026-06-17-pocock-designer-cribs-and-roadmap](../docs/retros/2026-06-17-pocock-designer-cribs-and-roadmap.md); [cribs-adoption-roadmap](../docs/cribs-adoption-roadmap.md).
