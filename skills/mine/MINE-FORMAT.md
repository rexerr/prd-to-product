# /mine output formats

The shapes `/mine` emits, so adopted findings slot into the host project (and this repo) with zero reformatting. `/mine` **returns** these as drafts; the main session writes them only on adoption.

## 1. Committed mined-doc — `docs/mined/<date>-<source>.md`

A header, then the findings.

```
# Mine — <source name> — <date>

- **Source:** <URL or local path>
- **Pinned:** <commit SHA — for repos>
- **License:** <license — for repos>
- **Lens:** <the host project's focus this mine was filtered through>

## Findings
<one or more of the shapes below>
```

## 2. Lens-A crib row (learnings for our tooling)

For findings that improve *our own tooling*. Matches the existing crib trackers verbatim:

```
| ID | Crib | Failure it prevents | Tier | Landing surface | Status |
```

- **Tier:** `integrate` (extend an existing mechanism) · `implement` (net-new structure) · `investigate` (gated on an open question).
- **Status — 3-state row legend:** `Proposed` · `Adopted (→ D-NNN)` · `Declined`. (`Parked` is a *subsection bucket* for deferred items, **not** a row-status value.)
- IDs are namespaced per source and never renumbered; gaps left by merges are intentional.

## 3. Lens-B proposed work (host-project needs)

For findings the host project should act on. A board row (matches `BACKLOG.md`):

```
| Item | Lane | Seq | Next | Refs |
```

- **Lane:** `next | watching | backlog | icebox` (a fresh proposal is rarely `active`); `Seq` only for the actionable lanes.

Plus a ticket card when the item carries working context (matches `tickets/README.md`):

```
---
slug: <kebab-case-slug>
status: <lane>      # mirrors the board Lane
title: <short title>
---
```

## 4. Soft-source experiment ticket

For a soft claim (tip / opinion / thread) with no ground truth to check against. It enters as a falsifiable experiment, never a "verified" fix:

```
---
slug: <kebab>
status: backlog
title: Experiment — <the tip, stated as a hypothesis>
---

- **Source:** <cited URL or origin>
- **Try:** <the concrete change to trial>
- **Kill condition:** <the observation that ends it — e.g. "drop if not measurably better after one week">
```

The **Kill-condition is mandatory.** *Failure it prevents: a soft tip masquerading as a verified improvement and never being retired.*
