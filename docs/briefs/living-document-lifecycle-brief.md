# Living-document lifecycle — when a doc needs an index

**Status:** pattern named 2026-06-20, first instance shipped ([D-048](../DECISIONS.md)). Parent brief over two instances: [`context-lifecycle-brief.md`](context-lifecycle-brief.md) and [`docs-structure-and-artifact-routing-brief.md`](docs-structure-and-artifact-routing-brief.md).

## The problem

Living documents accrete. `BACKLOG.md` grew until a whole-file read blew the 25K cap; `DECISIONS_ACTIVE.md` was on the same path, slower. The instinct is "this doc is bloated, rewrite it" — but the bloat *regenerates* unless the underlying lifecycle is fixed. This brief names the pattern so future docs inherit the fix instead of re-discovering it.

## The distinction that makes it tractable

Not all living docs accrete the same way. Two shapes, two different fixes:

- **Append-only event logs** — retros, council transcripts, audits, the furnace trial-ledger. Things that happened at a point in time and never change. **Already solved** in this repo by one file per event in a dated folder (`docs/retros/`, `docs/council/`, `docs/audits/`). No retirement ritual needed — nothing in them is ever "current vs. stale," and you never re-read an old retro every session.
- **Living registries** — `BACKLOG.md`, `DECISIONS_ACTIVE.md`, parking lots, the crib trackers. A *mutable set of currently-relevant items*. This is the class that rots, because it's read often and nothing ever leaves.

So the real target is narrow: **registries in the hot set with no retirement step.**

## The three-signal graduation trigger

A doc should graduate to *thin index + on-demand parts + retirement ritual* when all three hold:

1. **Read every session** (in the hot set) — the cost multiplier; a doc read monthly can be fat, a doc read every session can't.
2. **Registry-shaped** — a set of items, not a narrative.
3. **No step that removes things** — the **leading indicator**. Size is only the *lagging symptom*; by the time it's over the cap, the missing-retirement cause has been there for months.

The recognizer is a sentence an agent or human applies, **not software** — building a "doc-needs-structure detector" would be the premature generalization this repo declines (two real instances, Rule of Two). Graduate on recognition; tooling only earns its place at the third hand-run.

## The shape every graduation takes

Identical each time:

- **Thin always-loaded index** — one line per active item (the binding rule / the next action), pointer to the detail.
- **On-demand parts** — the full context lives in a per-unit file read only when needed (`tickets/<slug>.md`; for decisions the full `DECISIONS.md` entry already plays this role).
- **Retirement ritual** — a mandatory `/end-session` step that demotes finished work; **archive, don't delete**; **thin-on-touch** so the hot set can't re-accrete.

## The unification

Three in-repo efforts are the **same shape**, not three rocks:

- **Context-lifecycle** (this instance) — bound what session-start *loads*. Shipped via [D-048](../DECISIONS.md).
- **Docs-structure routing** — bound where new docs are *placed* at birth (the companion: birth-routing + growth-graduation). See [`docs-structure-and-artifact-routing-brief.md`](docs-structure-and-artifact-routing-brief.md).
- **`/mine` output** — mined-crib trackers are registries too; they inherit the shape for free once named.

Recognizing this is the win: name the pattern once, apply it wherever the trigger fires, design nothing new per instance.
