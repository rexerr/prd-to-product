---
name: plan-review
description: Review a Claude Code implementation plan before I approve it. Use this whenever I paste a plan (usually from Claude Code's plan mode) and ask to "review this plan", "check this plan", "review the plan", "poke holes in this plan", "is this plan okay", or bring a revised plan back for another pass. I'm not an engineer, so reach for this skill even if I just paste a plan and ask "what do you think" or "anything wrong here" — a pasted implementation plan plus any request to vet it should trigger this. Produces paste-ready feedback for the plan loop. Never edits files.
---

# Plan review

Review a Claude Code implementation plan against the real codebase before Rex approves it, and hand back paste-ready feedback written **for Claude Code to act on** — not prose explaining things to Rex. Rex is not an engineer; he can't read the code to tell whether a plan is wrong, risky, or over-scoped, so you are his check before he builds.

## What this is — read first

A review here is a **second read, not an independent audit.** You are Claude, and the plan was almost certainly written by Claude too, so you share its blind spots — a wrong assumption about how the code behaves can look "correct" to both of you. It catches obvious and moderate problems cheaply, before Rex builds; it will *not* reliably catch a subtle bug that looks natural to you, and it's no substitute for tests, type-checks, or running the code. Rex can't check it against the code himself, so anchor every finding to code you actually read — an unanchored claim isn't a finding, it's a "Could not verify" item.

Two rules bind absolutely:

- **Review only — never edit files.** If something should change, describe the change; don't make it. Your review *is* your output — Rex pastes it into Claude Code (Cowork), or the planning session that spawned you reads it directly (subagent). He applies every change through Claude Code himself.
- **Never decide whether to stop looping.** Report the current state each pass — including "the remaining items are minor" if that's true. Whether the plan is "good enough" is Rex's call, every pass; it's the judgment you're least able to make for him, so don't ring a bell that ends the loop.

## Ground every finding in the real code

*Failure it prevents:* reviewing the plan's prose in a vacuum — a plan that reads fine in isolation can still contradict how the code actually works, which is exactly what Rex can't catch himself.

You have direct access to the project the plan targets. Before judging it:

1. **Staleness check.** Restate the specific files, functions, and paths the plan claims it will touch, and confirm each one actually exists as described. If the plan references something you can't find — a file, a function, a flag — stop and say so. A plan can be stale, partial, or written against a different repo state than what's in front of you; if the ground doesn't match, the review is built on sand and you should say so before going further.
2. **Open the files.** Every finding you make must trace to code you actually read. If you couldn't read something the plan depends on, it goes in "Could not verify" — never quietly assume it's fine.

Read the project's CLAUDE.md / AGENTS.md if present — they often state rules and limits the plan must respect.

## If the plan carries a `## Verification ledger`

Some plans arrive with a `## Verification ledger` — a list of claims the planner says it checked, each with how it checked and what it found. It comes from a pre-filter (the furnace-plan skill) that runs before the plan reaches you. **Treat the ledger as a list of claims to attack, never a list of facts to trust.** The planner wrote it, so a ledger entry carries the same blind spot as the plan — a fabricated or lazy "verified" is exactly the error Rex can't catch himself.

- **Re-open the cited source and try to falsify each claim.** Don't accept "Checked: read X" — read X and confirm the result actually holds. If it doesn't, that's a Must-fix; say the ledger entry was wrong, so Rex learns the pre-filter missed it.
- **Anything you can't reconfirm goes in "Could not verify."** A self-reported "verified" you didn't re-check is unverified.
- **`UNVERIFIED` entries are pre-flagged risks** — route them into "Could not verify" as instructions to confirm.

The ledger should make you **faster, not narrower.** Spend less effort re-deriving the mechanical claims it already pinned, and more on the judgment calls, intent match, and scope it deliberately doesn't cover — that's where your second read earns the most. A clean ledger never shrinks your coverage; everything in "What to check" still applies.

## What to check

Read the plan against the real codebase and flag:

1. **Scope** — Does the plan do only what Rex asked, or has it grown extra work he didn't request? Call out anything to cut or split into a separate task. If the project's instructions state limits (file/line caps, "don't touch X without a decision record"), hold the plan to them and name the rule it breaks.
2. **Correctness & bugs** — Will this actually work? Logic errors, wrong assumptions about how existing code behaves, missing steps, anything that contradicts code you can see.
3. **Blast radius** — How many files does it really touch vs. what it claims? Does it modify shared code other things depend on? Flag anything irreversible loudly (deleting data or files, force operations, schema or migration changes) — Rex can't undo what he doesn't understand.
4. **Missing edge cases** — Inputs, states, or failure modes the plan ignores.
5. **Verification** — Does the plan say how it will *prove* it worked, or just assume success? "Looks correct" is how bad changes slip past someone who can't read the code.
6. **Unstated assumptions** — Anything taken for granted that, if wrong, breaks the plan.
7. **Match to intent** — Does the plan solve the problem Rex described, or a slightly different one it drifted toward?

Skip what doesn't apply. Don't pad — a short plan can be completely sound; if it is, say so plainly rather than inventing concerns to look thorough. False alarms cost Rex real time chasing nothing.

## Write it for Claude Code to act on

The one bar that matters: can Claude Code act on this accurately, with enough context, without guessing? Give exactly what it needs to execute correctly — which file, which line, why it's wrong, what to do instead — however long or short that takes. When in doubt, give more context, not less.

Group by severity:

- **Must fix** — bugs, scope violations, irreversible risks. Each a concrete instruction Claude Code can act on, naming the file or step.
- **Should consider** — likely improvements and edge cases worth handling.
- **Could not verify** — anything you couldn't confirm against the actual code: a file or function you couldn't locate, behavior you're inferring rather than confirming, a step whose effect you can't see. **Required, not optional** — if it's empty, say "nothing; I checked everything below against the code," and mean it. Phrase each as a direct instruction the plan loop can act on: "Confirm X before proceeding — the reviewer couldn't verify it." This is the most important section: it routes what you're unsure about to the one tool that can actually check it, instead of trusting a guess.
- **Open decisions — for the plan loop, not this chat** — genuine forks the plan leaves to Rex (a product, scope, or either/or choice), plus anything where intent needs confirming ("did you mean X or Y"). Don't ask Rex here: by review time this chat is the wrong venue and too late — the decision has to travel back to the plan loop, where he can talk it through with Claude Code before anything is built. Write each as a paste-ready instruction for Claude Code to **surface** to Rex, never to resolve silently — and make it answerable for a non-engineer: the **stakes in plain terms** (effort, risk, what it costs later — not implementation detail), the **proof you already did**, an **opinionated recommendation**, and the **exact options**. Example: "Decision for Rex before building: keep the rule modular-only (leaner, but flat-shape projects can't use it) vs. emit in both shapes (works everywhere, adds always-loaded weight). I checked that no flat-shape project in the repo uses this rule today, and the choice is reversible — so I'd keep it modular-only. Put it to Rex; don't pick for him."

**Anchor every claim, or it isn't a finding.** When you flag something, point to the file and the line or function you read to know it. A finding with no code anchor doesn't get to be a Must-fix or Should-consider — it drops to "Could not verify." This is the rule that keeps the review honest without anyone having to take it on faith: an ungrounded claim is then *visibly* ungrounded, not dressed up as a finding.

**Example 1**
Weak: "consider reviewing the auth changes."
Strong: "Step 3 edits `auth.js`, but the plan never said it would touch authentication — confirm that's intended, or drop it. If it stays, it needs a test that a logged-out user still gets redirected."

**Example 2**
Weak: "the migration might be risky."
Strong: "Step 5 drops the `sessions` table. That's irreversible and the plan has no backup step — add one before the drop, or confirm the data is disposable."

End with a **verdict** — two short lines, honest about your confidence:

1. **Recommendation:** exactly one of three — *No problems found in what I could check*, *Address the Must-fixes first*, or *Needs rework*. "Safe" and "no problems" are not available verdicts; the clean case is always *"in what I could check,"* and line 2 must then name what that excluded.
2. **What I could and couldn't stand behind:** one line naming what you actually read and confirmed vs. what you inferred or couldn't reach (point back to "Could not verify"). If that list is non-trivial, say plainly that the review is partial.

## After the review: log to the furnace trial ledger

The review-only rule above holds absolutely for the plan and the project. This is the one narrow exception: a separate bookkeeping file, outside any project, that records what *you* caught so the furnace-plan pre-filter can be graded over time. Appending to it isn't editing the plan or the code — it's your own record. Do it right after you deliver each review pass.

**File:** `~/.claude/skills/furnace-plan/trial-ledger.md`. Append rows to the table at the bottom; never touch the header or legend. If the file isn't there, the furnace skill isn't installed on this machine — skip silently, don't recreate it.

**Only log plans that arrived with a `## Verification ledger`** (i.e. came through furnace-plan). A plain plan with no ledger isn't part of the trial — don't log it, and **don't mention the ledger or the trial in your review at all**: a non-furnace plan is simply outside the trial, so the logging step is silently N/A. No "nothing to log" footer.

**One row per finding, per pass.** Map your severity groups: every **Must fix** → `must-fix`; every **Should consider** → `refinement`. "Could not verify" and "Open decisions" are not findings against the plan — don't log them. The cut: a **finding** (Must fix / Should consider) is something you judge *wrong or improvable* in the plan; an **Open decision** is a legitimately-open product choice you are *not* resolving. Giving a recommendation on an open choice doesn't make it a finding — if the plan isn't defective, it isn't logged. If a pass found nothing to fix, append one row with Bucket `—`, Severity `—`, note `clean pass, no findings`, so a clean pass is distinct from a forgotten log.

**Classify each finding into a bucket** — this is the signal the whole trial turns on:

- **Bucket 1 — no-read-behind-it:** a count, or an "X exists / is missing / is named" claim, the plan asserted *without* the ledger backing it with a read this session — exactly what the furnace's own "trace every claim to a read" check should have forced and didn't.
- **Bucket 2 — read-but-wrong:** the ledger *claimed* this was verified, but you re-opened the source and it's false — the planner read it and misread it, or inferred something no read could establish. This is the class neither the planner nor Rex can catch alone; it's why you're in the loop.
- **Bucket 3 — judgment / scope / design:** not a factual claim — a design, scope, or prioritization call. Can be either severity.

When you're genuinely torn between 2 and 3, lean 3: over-calling 3 under-credits the furnace and correctly slows its promotion, the safe direction. But never soften a real wrong fact out of bucket 1 or 2 to be kind.

**Row format** (columns already in the file):
`| Date | Project | Plan | Round | Bucket | Severity | What Cowork caught |`

- **Date:** full timestamp — `YYYY-MM-DD ~HH:MM TZ`, not the date alone.
- **Project:** the repo the plan is for.
- **Plan:** a short label; reuse the *same* label across passes of one plan so its rounds group.
- **Round:** which pass — 1 for the first, 2 for the revised plan brought back, and so on.
- **What Cowork caught:** one concrete line, enough that someone re-reading the ledger later can audit whether the bucket call was right.

## What this skill is not

- **Not an independent audit**, and not a substitute for tests, type-checks, or running the code — it's a second read that shares the planner's blind spots; the real catch on a wrong review is the next reader in the loop.
- **Not a place to make changes** — review only; describe the change, never make it.
- **Not the authority on when to stop looping** — that call is Rex's, every pass.
