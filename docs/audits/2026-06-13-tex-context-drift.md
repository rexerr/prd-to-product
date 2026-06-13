# Context-drift audit — `tex` (pilot #3)

**Date:** 2026-06-13 · **Type:** one-off, read-only, by-hand (brownfield audit pilot #3)
**Target:** `/Users/rexc/Sites/tex` — git repo, **actively worked today** (last commit 00:08), single-dev, Claude-only, produces HTML demos (no app/product code), no `.env` committed, no deploy target.
**Method:** same as pilots #1–2 — diff against the current `context-engineering` standard, classify by KIND.

> **Verdict up front: `tex` is OUT OF SCOPE for a context-drift audit.** It was never scaffolded by `context-engineering`. Its `CLAUDE.md` self-describes as a *"light ritual harness"* (commit `d2eac9d`) — a deliberately minimal, hand-authored harness for **skill curation** (evolving the `frontend-er` skill), not product building. Diffing it against the modular/flat scaffold standard produces a **false-positive cascade**: nearly every "gap" is an intentional omission. This report exists to record *why* it's out of scope — which is the single most useful thing pilot #3 produced.

---

## What `tex` actually is

A skill-curation workspace. Structure (all hand-authored, fit to purpose):
- **Flat 24-line `CLAUDE.md`** — project intro + "Where things live" + "Operating rules (the rituals)" + "Conventions". Not the `@AGENTS.md` pointer; there is no AGENTS.md.
- **`.claude/`** — only `commands/end-session.md` + `launch.json`. No rules, no settings, no session-start.
- **`docs/`** — a single running-log (`skill-review-2026-06-11.md`) serving as decision register + backlog + parking lot, plus a superpowers handoff. No PRD/ARCHITECTURE/DECISIONS/retros.
- **Work artifacts** — `frontend-er-demos/*.html`, `contact-sheet.html` (convergence tool), `council-outputs/`, `.skill-review/pressure-test/`.

Its rituals are real and self-consistent: no-rule-without-an-observed-failure, convergence-review every ~3 builds, verify-the-artifact-not-the-self-report, log-every-decision, `/end-session`. The "Read first" line in CLAUDE.md **is** its session-start ritual, inline — so even the "missing session-start command" is covered by design.

---

## Why a checklist diff would be actively wrong here

A naive present/absent diff against the standard reports ~12 "gaps": no AGENTS.md, no `.claude/rules/`, no session-start command, no DECISIONS/DECISIONS_ACTIVE, no retros dir, no permissions seed, no hooks, no memory note, no autonomy charter, etc. **Every one is intentional** — `tex` chose a lighter structure on purpose, and "No new rule without an observed failure behind it" is an explicit anti-scaffold stance. Reporting these as drift would:
- erode trust in the audit completely (12 false positives, 0 real findings), and
- tempt a "fix" that **bloats a workspace deliberately kept minimal** — the exact opposite of its design intent.

The only genuinely-checkable items (does its *own* chosen ritual set have internal holes?) come back clean: its session-start is inline, its decision log exists (just not named `DECISIONS.md`), `/end-session` is present.

---

## The finding: pilot #3 adds a GATE the 5-field profile was missing

Pilots #1–2 (both *were* context-engineering scaffolds) produced a 5-field project profile that gated the judgment tier. I predicted a 3rd pilot would "mostly confirm." It didn't — because `tex` is the first target that **never opted into the standard**, which neither earlier project could surface.

**New profile field 0 (a gate, evaluated before the other five): `opted-into-the-standard?` — i.e. was this project scaffolded by `context-engineering` / does it intend to track the standard?**

- If **no** → the project is out of scope. The checklist diff is meaningless as "drift." At most the audit may emit a *non-gating advisory* ("you could adopt X"), never a defect report. Default: report "not a drift target" and stop.
- If **yes** → proceed to the 5-field profile and classify as in pilots #1–2.

Detection signals for the gate (cheap, file-level): presence of the `@AGENTS.md`-pointer pair or a modular `.claude/rules/` tree; a `docs/DECISIONS.md` in the skill's shape; scaffold-fingerprint sections in AGENTS.md/CLAUDE.md. `tex` has none — it has a hand-rolled flat CLAUDE.md whose section names ("the rituals") don't match the template.

**Why this matters for the build decision:** without field 0, `/audit-context` is not just noisy on a hand-rolled repo — it is *harmful* (false-positive cascade + bloat temptation). This is a stronger reason to gate carefully than anything pilots #1–2 surfaced, and it validates holding the build until the design is right.

---

## Three-pilot synthesis

| | epost (#1) | field-society (#2) | tex (#3) |
|---|---|---|---|
| Scaffolded by CE? | yes | yes | **no — hand-rolled harness** |
| Under git | yes | no | yes |
| Multi-agent | yes (Codex) | no | no |
| Product code | yes | no | no (HTML demos) |
| Secrets/.env | yes | no | no (env var only) |
| Deploy target | yes | no | no |
| Audit outcome | 4 real backports | 6 backports (thinner project) | **out of scope** |

- **Safe-backport tier: rubric-stable** across the two in-scope projects (6 items).
- **Judgment tier: flips on the 5-field profile** (hooks / memory-fit / non-Claude rule).
- **Gate (field 0): opted-into-standard?** — without it the whole audit mis-fires on hand-rolled repos. **This is pilot #3's contribution.**

Final shape for `/audit-context` if ever built: **(0) gate on opted-into-standard → (1) read 5-field profile → (2) diff → (3) classify by profile.** Step 0 is non-optional; it's the difference between a useful tool and a harmful one.

---

## Open decisions (for Rex)

**(a) Fix anything in `tex`?** **No** — it's out of scope and correctly minimal by design. No action.

**(b) Build `/audit-context`?** Pilot #3 *reinforces* the existing "hold" decision and sharpens the spec (the field-0 gate). Three by-hand pilots now fully define the design; the build still waits on proven *demand* (a real drift-fix need biting), not on more design signal.
