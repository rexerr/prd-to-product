# Retro — 2026-06-22 11:47 CDT — Docs-routing template change (D-055)   (3rd session of the day)

Built board Seq-2 ([docs-routing](../../tickets/archive/docs-routing.md)) end to end: the `context-engineering` doc-routing rule + `docs/README.md` map + intake Q24a. Full process arc — `/furnace-plan` (preflight + blind `Explore` review) → two Cowork `/plan-review` rounds → build → verify → log → retire.

## What was completed

- **The change** (committed `c37f5ff`): `## Where new docs go` rule in both shapes (flat AGENTS inline; modular `session-discipline.md`), intake **Q24a** (`artifact_skills_list`, steering-line-only pre-seed), always-emit `docs/README.md` map, `docs/research/` riding the rule, `decisions.md` "Inline compressed OPTIONAL form" spec + "Doc-routing pre-seed" section + inclusion-table row + state-map keys. Regenerated `examples/output-small/` (+ new `docs/README.md`); medium/large abbreviated sketches render the modular section prose.
- **[D-055](../DECISIONS.md)** logged + mirrored to [`DECISIONS_ACTIVE.md`](../DECISIONS_ACTIVE.md) (marker D-054→D-055).
- **Retirement ritual:** ticket `git mv`'d to `tickets/archive/`, links re-depthed (`../`→`../../`, one followed and confirmed), `BACKLOG.md` row dropped and the `next` lane re-sequenced contiguous (1–5).

## Failure this session

- **Tag:** none shipped — but two real defects and one process miss were caught *before* commit by the review loop (the loop working as designed).
- **Artifacts (named):**
  1. **Process miss (mine, Rex-caught):** I gated the `docs/README.md` map to modular and waved off the consequence with *"fine, just noting it."* That hand-wave hid a **verification orphan** — the only full fixture (`output-small/`) is flat, so a modular-only map would have shipped with no red-capable coverage. Rex: *"whenever you say 'its fine, just noting it' means we are not doing something properly the first time."* → reversed to always-emit (product + verification align). Saved as a memory tell.
  2. **Cowork round-1 (real bug):** my routing draft hardcoded `DECISIONS_ACTIVE.md` as a root anchor, but that doc is gated on Q23 — every other reference to it is OPTIONAL-wrapped. Would have named an unemitted doc in any Q23=No project. → gated via `decisions_active_anchor`.
  3. **Cowork round-2 (mechanism gap):** the gate used an inline open/close span that `decisions.md`'s OPTIONAL spec never defined. → switched to the line-202 compressed form **and** documented that form in `decisions.md` so a template isn't leaning on an undefined drop behavior.
- **Tool or agent?** All three are agent-judgment (mine), caught by the harness's review layers (furnace blind review + Cowork). The furnace preflight's own value showed in cheap catches (wrong substitution analog — `path_scoped_rule_list` is inline, not block — fixed by reading both consumption sites).
- **Does it generalize?** The "fine, just noting it" tell does — it recurs whenever I rationalize a flaw instead of fixing it. Captured as a Claude-local memory (working-discipline, not a repo rule). The other two were design-specifics, now closed.
- **→ The change it demands:** none beyond what landed. The review loop already enforces the catch; no new repo rule warranted (over-applying would be CF-01 sprawl).

## Files changed

- `skills/context-engineering/`: `templates/claude-rules-flat-AGENTS.md.template`, `templates/claude-rules-modular/session-discipline.md.template`, **NEW** `templates/docs/README.md.template`, `generator/intake.md`, `generator/decisions.md`, `examples/output-small/AGENTS.md`, **NEW** `examples/output-small/docs/README.md`, `examples/output-medium-abbreviated.md`, `examples/output-large-abbreviated.md`.
- `docs/DECISIONS.md` (+D-055), `docs/DECISIONS_ACTIVE.md` (mirror + marker).
- `BACKLOG.md` (row dropped, re-sequenced), `tickets/docs-routing.md` → `tickets/archive/`.

## Key decisions made

- **[D-055](../DECISIONS.md).** Three forks settled with Rex: pre-seed = steering-line-only (R2); map = always-emit (not gate-to-modular); decision ID = `D-NNN`, no pre-assignment (re-grep at write time per furnace Check 1a — only ticket IDs went slug-based, [D-048](../DECISIONS.md)).

## Verification (what it did and didn't cover)

- **Did:** structural dry-run of the flat path against `output-small/` — zero `PARAMETERIZE`/`OPTIONAL` marker leaks in rendered output (grep, hard gate); `DECISIONS_ACTIVE` anchor drops for Q23=No, kept for Q23=Yes; `research/` in rule + map; rule↔map cross-refs resolve; template marker balance (1 open/1 close per gate); D-055 cross-ref targets exist; moved-ticket link followed and resolves.
- **Did NOT:** the modular path has no full-tree fixture (none exists — separate backlog item); coverage there is the rendered prose in the abbreviated sketches, not a diffable tree. The `council`-opted artifact-block-present state is verified by dry-run reasoning + an illustrative sketch, not a committed full render. Generation is non-deterministic so all diffs are structural, not byte-exact.

## Open items

- Modular full-output-tree fixture remains a deferred backlog item (not pulled into this scope).
- `/mine` dogfood still owed (its own D-055-earmark is now free since docs-routing took D-055; `/mine` takes the next number when it lands).

## Next session

- Board Seq 1 is `/mine` — **dogfood it on a real source** (the first real mine doubles as its red-capable verification). On GREEN: log its decision (next free `D-NNN`), mirror the binding bits, archive `tickets/mine.md`.
