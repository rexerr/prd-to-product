# Retro — 2026-06-24 09:58 CDT — furnace blind-review hardening (D-065); cross-session commit-sweep collision   (2nd session of the day)

`/furnace-plan`'d and shipped the Seq-1 board item: hardened the `furnace-plan` blind-review setup against the author-improvisation failure that the [morning session's retro](2026-06-24-no-jargon-leak-scan.md) flagged. The fix lowers the friction of a clean reviewer handoff (verbatim two-slot prompt template + pinned model tier) rather than pretending to remove author freedom. Logged [D-065](../DECISIONS.md#d-065). The session also surfaced a genuine concurrency hazard — a parallel Claude-Code session committed into the same working tree and swept my uncommitted decision-log hunk into its own commit.

## What was completed

- **Blind-review hardening shipped** — [`skills/furnace-plan/SKILL.md`](../../skills/furnace-plan/SKILL.md) "The blind review" (lines 89–110): (a) a verbatim copy-paste reviewer-prompt template with exactly two author-filled slots (`{plan-path}`, `{acceptance-criteria}`); (b) reviewer pinned to the Opus tier as a stable tier *alias* (never a version id); (c) a criteria-slot guard banning **both** leak shapes — line-reference *and* named-finding; (d) an author self-check that makes a non-honored model-pin **visible** (confirm the reviewer ran on the pinned tier; flag explicitly if the surface dropped the override) rather than betting on silent cross-surface behavior.
- **Honest framing + deferred hook** — the change is framed as friction-lowering, not freedom-removal (there is no runner enforcing the template). The PreToolUse model-pin guard hook is deferred and **gated on recurrence** of a tainted handoff. A devil's-advocate pass established the hook is the only true freedom-removal but can enforce only the mechanical half (model), never the semantic half (poisoned criteria).
- **`plan-review/SKILL.md` deliberately untouched** — the rubric governs *how* the reviewer judges (anchor every claim), never *what* to check; the leak was the author telling the reviewer what to find, which has no home near the reviewer. (Settles the ticket's open question.)
- **Paperwork** — [D-065](../DECISIONS.md#d-065) logged (refines D-043, not mirrored — visible by reading the skill); DECISIONS_ACTIVE marker bumped to D-065 + added to the skip-list; ticket archived to [`tickets/archive/`](../../tickets/archive/furnace-blind-review-hardening.md) (links re-depthed) and its board row retired with the `next` lane resequenced; an n=1 watching row added for the commit-sweep hazard.

## Process this session — both review gates worked, and the morning's failure did NOT recur

The morning retro's failure was a tainted blind review (findings handed to the reviewer as an answer key; unpinned weak model). This session ran it clean **by following the very discipline being authored**: one read-only `Explore` reviewer, prompt = plan path + task-goal criteria + rubric pointer only, model pinned. Opus was 529-overloaded server-side, so the reviewer ran on **Sonnet** — the plan's specified Opus-unavailable fallback and a capable tier, a legitimate graceful-degradation, not the weak-default failure. The blind reviewer caught real gaps (named-finding leak shape uncovered; model claim grounded only in schema not runtime) that were fixed before Cowork. Cowork's `/plan-review` then caught the load-bearing one — the model-pin was probed in this session's surface, not necessarily the one furnace-plan runs in — which drove the visible-degradation self-check. Two independent gates, each caught something the other didn't.

## Failure this session — tag: lost context (cross-session concurrency collision)

**A parallel Claude-Code session committed into the same working tree mid-task and swept my uncommitted work into its commit.** I edited `docs/DECISIONS.md` (the D-065 append) and left it unstaged while finishing the SKILL.md edit. The other session ran a broad `git add` / `commit -a` and its commit `d3c006d` ("Fix 4 broken internal links in live docs") absorbed my D-065 hunk (its "13 insertions" to DECISIONS.md = my entry).

- **Tool or agent?** Neither mine alone — an environment/coordination gap. Two agents in one working tree with no staging discipline between them. My own staging was explicit (named paths, never `-a`), which is why my SKILL.md + DECISIONS_ACTIVE edits stayed mine; the other session's broad add is what crossed the streams.
- **Damage:** none to content — D-065 is correct and all cross-references resolve. The blemish is provenance: my decision entry sits in a commit message about link fixes, and the furnace change is split across two commits (D-065 in `d3c006d`, SKILL+ACTIVE in my `78bb97c`).
- **Why I didn't untangle it:** `d3c006d` is local-only (unpushed), so a rewrite was technically possible — but the other session is *live*, and rewriting its history while it holds its own view of HEAD invites a worse collision. History rewrite is gated on Rex regardless. Left as-is; recorded here for provenance.
- **Does it generalize?** n=1. Per the repo's Rule-of-Two / anti-accretion discipline (the sibling [D-018](../DECISIONS.md#d-018) ledger-sweep hook is itself parked at n=1), no guardrail built. Added a watching row: on a 2nd sweep, add an explicit-path-staging rule to `CLAUDE.md` ("never `git add -A`/`commit -a`; stage named paths"). The cheap generic fix is already what I do by habit; the gap is that it isn't yet a written rule binding every session.

## Verification — what it did and didn't cover

- **RED-capable, observed:** post-edit greps over the SKILL.md section — template slots present (`{plan-path}`/`{acceptance-criteria}`), model pin present as a tier alias, `contains ONLY` → 0 (old prose gone), `removes the degree of freedom` → 0, self-check + both criteria-guard pairs present; DECISIONS_ACTIVE marker reads D-065 + skip-list names it + D-065 entry in DECISIONS.md. Full section re-read for coherence; D-035 citation and symlink rubric-path confirmed intact.
- **Runtime probe:** model-alias acceptance confirmed live this session — `model: opus` accepted-and-routed (529 = capacity, not invalid-model), `model: sonnet` ran to completion.
- **Did NOT cover:** whether a *Claude Code CLI* subagent spawn honors a per-spawn `model: opus` override (probed only in this session's surface — Cowork's load-bearing Could-not-verify). The fix does not rely on a cross-surface guarantee: the self-check makes a dropped pin visible instead. Also not covered: no executable harness enforces that a future furnace author actually copies the template verbatim — same trust model the rest of the markdown-only skill runs on.

## Key decisions

- **[D-065](../DECISIONS.md#d-065)** — blind-review handoff gains a verbatim two-slot template + pinned Opus tier alias + dual-shape criteria guard + visible-degradation self-check; refines (not reverses) D-043; model-pin guard hook deferred and gated on recurrence; `plan-review/SKILL.md` untouched. Not mirrored (visible by reading the skill).

## Next session

- **Open slice on the board (now Seq 2):** provenance-grounded check (council item 2c) — the remaining half of the invariant/semantic-checks item, likely sharing the no-jargon-leak scan's pre-write gate.
- **Watching:** cross-session commit-sweep guard — fires on a 2nd sweep.
- **Untracked `scripts/` directory** left in the working tree by the other session — not mine; Rex to handle.
