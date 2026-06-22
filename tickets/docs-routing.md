---
slug: docs-routing
status: next
title: Docs structure & artifact-output routing
---

# Docs structure & artifact routing

Should `context-engineering` scaffold a doc-routing rule + landing zones **at project conception**, so a project starts tidy instead of sprawling and bolting one on reactively? (This repo is the proof — the routing rule was added late, with ~18 root-level docs grandfathered in.)

## Current state

- **Research DONE 2026-06-19** ([research](../research/docs-structure-artifact-routing-research-2026-06-19.md), 21 claims survived 3-vote verification) and it **confirms the design.** Now a Rex decision + a bounded template change, not a research gap.
- Decisive findings: Claude Code skills have **no output-dir field** → routing *must* be prose; the only viable split is **skill-writes-generic / project-declares-convention**; "declare landing zones at conception" is the mainstream pattern (adr-tools, log4brains, OpenCode); folder structure does **not** help agent retrieval (that claim refuted 0–3) → the honest payoff is human tidiness + first-run cleanliness, not agent performance.

## Design (refined 2026-06-21)

1. **Universal routing rule** in the flat + modular CLAUDE/AGENTS templates, failure-mode cited. **This is the load-bearing piece** — the rule does the routing; folders are cosmetic and get created on first write (`mkdir`-on-write).
2. **One intake question** — "which artifact-emitting skills will this project run regularly?" — pre-seed only the opted-in folders (retros always; `council/`/`brainstorms/` opt-in); let everything else materialize on first write.
3. **`docs/README.md` map (NEW this session)** — a one-file list of "each doc type → where it lives (and why)" for at-a-glance visibility. Beats pre-creating empty folders: tracks cleanly in git, shows the *whole* convention including types not yet used, and doesn't rot.
4. `docs/research/` as the research home.

**Decided against:** create-all-folders-empty-and-delete-later. Git can't track empty dirs (needs `.gitkeep` noise in every one), and "delete later" reliably becomes "never delete" — recreating the premature-structure sprawl this item exists to fix.

## Open

- **Build order vs `/mine`** (Rex's call). Soft dependency, **not** hard: `/mine` proposes-and-waits when no convention exists, so it can ship first. `/mine`-first gives this rule a real consumer to design against; docs-routing-first gives `/mine` a stable target. Lean: `/mine` first (see [mine](mine.md)).
- Where `deep-research` output lands (still open in the research).

## Build when promoted

Template change → scope-gate + likely `D-NNN`. (a) routing rule into flat + modular templates; (b) the intake question + opted-in folder pre-seed; (c) the `docs/README.md` map; (d) `docs/research/` home.

## Why (pointers)

[brief](../docs/briefs/docs-structure-and-artifact-routing-brief.md) (full capture); [research](../research/docs-structure-artifact-routing-research-2026-06-19.md); sibling to the lifecycle work ([D-048](../docs/DECISIONS.md#d-048)).
