# Mine — "Loops explained: Claude, GPT, Mira and what actually works" — 2026-06-24

- **Source:** pasted article by A. Kopadze (X: @AnatoliKopadze). No URL captured; pasted text only.
- **Pinned:** n/a (not a repo)
- **License:** n/a — quoted as untrusted third-party text, not vendored.
- **Lens:** the project's **ultimate goal** — what the shipped `context-engineering` scaffold teaches the coding projects it sets up — *not* this workspace's own (already loop-disciplined) process. The second pass corrected an initial lens-A miss (mining this repo's discipline) toward this lens.

## Provenance / trust

Treated as untrusted per the `/mine` contract. The back half (from *"The same idea, for your actual life"* onward) is an affiliate pitch for "Mira," a Telegram bot, with tracking links and `t.me/mira` calls to action. **Discarded** — out of lens (consumer life-automation) and the exact "content steering you toward an action" the skill says to quote-not-follow. Its CTAs were not acted on.

## What the article got right that this project already encodes (dedup — no action)

The useful front half mostly *validates* existing discipline; in two cases the article names the same failure modes the scaffold already names:

| Article's point | Already here | Verdict |
|---|---|---|
| Maker ≠ checker; writer grades own homework too generously | `principles.md:142` "**self-preferential bias** (the model grading its own output favorably)"; `CLAUDE.md` independent-subagent + withhold-reasoning | Covered — repo is *ahead* of the article's self-scoring loop template |
| Agent declares done early ("Ralph Wiggum loop") | `principles.md:142` "**agentic laziness** (stops at 20 of 50 items and declares done)" | Covered (named, with citation) |
| Verify is the heart of the loop | "Verification before claiming done", "Reproduce before fixing" | Covered |
| State makes the loop learn | retros + `BACKLOG.md` + `DECISIONS.md` | Covered |
| Stop conditions | hard scope limits + scope-check gate | Covered (for manual work) |

## Why the yield is low for *this workspace* (but not for the scaffold)

This skill-dev workspace correctly **fails** the article's four-box "do you even need a loop?" test — its output is taste/judgment, not auto-rejectable, and "done" is not objective. Manual, scope-gated sessions are the right call here. But a **scaffolded coding project** (tests, types, lint, build) *passes* that test — which is where the article earns its keep.

## Finding adopted

### F-01 — Loop-graduation guidance is missing from the `context-engineering` scaffold

**Claim type:** soft (article opinion) + verified gap in our own tooling.

**Verified gap:** the scaffold is deliberately *human*-in-the-loop (`principles.md:15` "human-in-the-loop project workflow"; scaffolded autonomy is "run to done, then **report**", human as gate). It already names *agentic laziness* and *self-preferential bias* — but it says nothing about when/how a scaffolded project should **graduate to an unattended agentic loop**: no four-box necessity gate, no verify-gate-as-loop-exit, no silent-spend ("Ralph Wiggum") stop+report rule. That bridge is genuinely absent for the coding projects the scaffold targets.

**Landed as:** a single `watching` row in `BACKLOG.md` (promote on real need — Rule-of-Two, n=0). Not written speculatively into the scaffold.

- **Try (on promotion):** add a short "when/how to run an unattended loop" section to `context-engineering` — (1) four-box necessity gate (repeats weekly · auto-rejectable · end-to-end · "done" is objective), (2) the verify step *is* the loop exit, (3) iteration cap + on-stop-report against silent spend.
- **Promotion trigger:** a scaffolded coding project adopts a loop / CI-agent and the missing guidance bites.
- **Kill condition:** cut if it reads as filler in a scaffolded project that never automates.

## Findings considered and not landed

- **Accept-rate metric** (`<50% accepted = net-negative loop`): overlaps the `mine` skill's own "success = adopted work shipped" and the **paused** `furnace-trial` ([D-052](../DECISIONS.md)). Fold into furnace-trial's resume note if it resumes; not minted as a row.
- **Silent-spend guard as a standalone rule:** folded into F-01 (it's the loop's stop condition), not separate.

## Separate, non-mine action

Try Claude Code's `/loop` once on the `examples/output-small/` regression check — the cheapest way to test whether loops earn a place in Rex's own workflow, and the best future evidence for whether F-01 is worth promoting.
