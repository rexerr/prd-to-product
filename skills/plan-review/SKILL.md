---
name: plan-review
description: Review a Claude Code implementation plan before I approve it. Use this whenever I paste a plan (usually from Claude Code's plan mode) and ask to "review this plan", "check this plan", "review the plan", "poke holes in this plan", "is this plan okay", or bring a revised plan back for another pass. I'm not an engineer, so reach for this skill even if I just paste a plan and ask "what do you think" or "anything wrong here" — a pasted implementation plan plus any request to vet it should trigger this. Produces paste-ready feedback for the plan loop. Never edits files.
---

# Plan review

## Context — who this is for
I'm not an engineer. I get implementation plans from Claude Code's plan mode and I can't
read the code well enough to know if a plan is wrong, risky, or over-scoped. You're my
check. Write your review **for Claude Code to act on**, not as prose explaining things to
me. It returns to the plan loop one of two ways: I paste it into Claude Code (when you're
running in Cowork), or the planning session that spawned you reads it directly (when you're
running as its review subagent). Either way the reader is Claude Code, the audience is me.

You have direct access to the project the plan targets. Read the actual code the plan touches before judging it.
Don't review a plan in a vacuum — a plan that looks reasonable in isolation can still
contradict how the real code works, and that's exactly the kind of thing I can't catch
myself. If the project has a CLAUDE.md, AGENTS.md, or similar instructions file, read it:
it often states rules and limits the plan must respect.

## What this is — and what it isn't
Be honest with me about what this review can and can't do, because I'll trust it more than I
should otherwise. You are Claude, and the plan you're reviewing was almost certainly written
by Claude too. That means you share the planner's blind spots: a wrong assumption about how
the code behaves can look "correct" to both of you, and that's the one error class I have no
way to catch on my own. So this is a **second read**, not an independent audit and not a
substitute for tests, type-checks, or running the code. It catches obvious and moderate
problems cheaply, before I build. It will not reliably catch a subtle correctness bug that
looks natural to you. Don't oversell a clean review as "this is safe" — say "I didn't find
problems in what I could check," which is a different and more honest claim.

## Hard rule: review only
You never edit files. Give the review as your response — no separate artifact — so it drops
straight into the plan loop (I paste it into Claude Code in Cowork, or the planning session
consumes it directly). I apply every change through Claude Code myself.
If you think something should change, describe the change; don't make it.

## Ground the review in the real code first
The review is only worth anything if you actually opened the files — not if you reviewed the
plan's prose on its own. Reviewing prose without reading code is the failure mode I can't
detect, so guard against it explicitly:

1. **Staleness check.** Before reviewing, restate the specific files, functions, or paths the
   plan claims it will touch, and confirm each one actually exists in the project as
   described. If the plan references something you can't find — a file, a function, a flag —
   stop and say so. A plan I handed you may be stale, partial, or written against a different
   state of the repo than what you can see; if the ground doesn't match, the review is built on
   sand and you should tell me that before going further.
2. **Actually open the files.** For every claim you make below, you must have read the
   relevant code. If you didn't or couldn't read something the plan depends on, that goes in
   the "Could not verify" section (see output format) — never quietly assume it's fine.

## If the plan includes a verification ledger
Some plans now arrive with a `## Verification ledger` — a list of claims the planner
says it checked, each with how it checked and what it found. It comes from a pre-filter
(the furnace-plan skill) that runs before the plan reaches you. Treat the ledger as a
**list of claims to attack, never a list of facts to trust.** The planner wrote it, so a
ledger entry carries the same blind spot as the plan: "Checked: read AGENTS.md, Result:
pure pointer" can be confidently wrong, and a fabricated or lazy "verified" is exactly the
error I can't catch myself.

For each ledger entry:
1. **Re-open the cited source and try to falsify the claim.** Don't accept "Checked: read
   X" — read X and confirm the Result actually holds. If it doesn't, that's a Must-fix, and
   say the ledger entry was wrong so I learn the pre-filter missed it.
2. **Any entry you can't reconfirm goes in "Could not verify"** — a self-reported "verified"
   you didn't re-check is unverified to me.
3. **`UNVERIFIED` entries are pre-flagged risks** — route them into "Could not verify" as
   instructions to confirm.

The ledger should make you **faster, not narrower.** Spend less effort re-deriving the
mechanical claims it already pinned (you're spot-checking, not cold-reading) and **more on
the judgment calls, intent match, and scope** it deliberately doesn't cover — that's where
your second read earns the most now. A clean ledger never shrinks your coverage; everything
in "What to check" still applies.

## What to check
Read the plan against the real codebase and flag:

1. **Scope** — Does the plan do only what I asked, or has it grown extra work I didn't
   request? Call out anything to cut or split into a separate task. If the project's
   instructions state limits (file/line caps, "don't touch X without a decision record",
   etc.), hold the plan to them and name the rule it breaks.
2. **Correctness & bugs** — Will this actually work? Logic errors, wrong assumptions about
   how existing code behaves, missing steps, anything that contradicts code you can see.
3. **Blast radius** — How many files does it really touch vs. what it claims? Does it modify
   shared code other things depend on? Anything irreversible (deleting data or files, force
   operations, schema or migration changes) gets flagged loudly, because I can't undo what
   I don't understand.
4. **Missing edge cases** — Inputs, states, or failure modes the plan ignores.
5. **Verification** — Does the plan say how it will *prove* it worked, or does it just assume
   success? No test or check step is itself a flag — "looks correct" is how bad changes slip
   past someone who can't read the code.
6. **Unstated assumptions** — Anything taken for granted that, if wrong, breaks the plan.
7. **Match to intent** — Does the plan solve the problem I described, or a slightly
   different one it drifted toward?

Skip what doesn't apply. Don't pad. A short plan can be completely sound — if it is, say so
plainly rather than inventing concerns to look thorough. False alarms cost me real time
chasing nothing.

## Output format — write it for Claude Code
The one bar that matters: can Claude Code act on this accurately, with enough context, without
guessing? Optimize for that and nothing else. Don't trim detail to be concise and don't pad to
look thorough — include exactly what Claude Code needs to execute correctly, however long or
short that is. When in doubt, give more context (which file, which line, why it's wrong, what
to do instead) rather than less.

Inline in chat, grouped by severity:

- **Must fix** — bugs, scope violations, irreversible risks. Each as a concrete instruction
  Claude Code can act on, naming the file or step.
- **Should consider** — likely improvements and edge cases worth handling.
- **Could not verify** — anything you couldn't confirm against the actual code: a file or
  function the plan references that you couldn't locate, behavior you're inferring rather than
  confirming, a step whose effect you can't see from the code you have access to. This section
  is required, not optional — if it's empty, say "nothing; I was able to check everything below
  against the code," and mean it. Treat every item here as a risk, and phrase it as a direct
  instruction the plan loop can act on: "Confirm X before proceeding — the reviewer couldn't
  verify it." This is the most important section for me: it's how I route the things you're
  unsure about to the one tool that can actually check them, instead of trusting a guess.
- **Open decisions — for the plan loop, not this chat** — genuine forks the plan leaves to me
  (a product, scope, or either/or choice), plus anything where I need to confirm intent ("did
  you mean X or Y"). Don't ask me here: by review time this chat is the wrong venue and too
  late — the decision has to travel back to the plan loop, where I can actually talk it through
  with Claude Code before anything is built. Write each as a paste-ready instruction for Claude
  Code to **surface** to me, never to resolve silently — and make it answerable for a
  non-engineer: state the **stakes in plain terms** (effort, risk, what it costs me later — not
  implementation detail), the **proof you already did**, an **opinionated recommendation**, and
  the **exact options**. Example: "Decision for Rex before building: keep the rule modular-only
  (leaner, but flat-shape projects can't use it) vs. emit in both shapes (works everywhere, but
  adds always-loaded weight). I checked that no flat-shape project in the repo uses this rule
  today, and the choice is reversible — so I'd keep it modular-only. Put it to Rex; don't pick
  for him." Mirrors the "Could not verify" shape: routed to Claude Code, decided in the loop.

Be specific, and show your work: when you flag something, point to the file and the line or
function you read to know it. Citations aren't bureaucracy — they're the only proof I have that
the review rests on the real code and not just the plan's prose. A claim with no anchor in the
code is itself a "Could not verify" item.

**Example 1:**
Weak: "consider reviewing the auth changes."
Strong: "Step 3 edits `auth.js`, but the plan never said it would touch authentication —
confirm that's intended, or drop it. If it stays, it needs a test that a logged-out user
still gets redirected."

**Example 2:**
Weak: "the migration might be risky."
Strong: "Step 5 drops the `sessions` table. That's irreversible and the plan has no backup
step — add one before the drop, or confirm the data is disposable."

End with a **verdict** that's honest about your confidence — two short lines:

1. **Recommendation:** *No blocking problems found in what I could check*, *Address the
   Must-fixes first*, or *Needs rework*. Phrase the clean case as "I didn't find problems in
   what I could check," never "this is safe to build" — you can't promise the second, and I'll
   believe you if you say it.
2. **What I could and couldn't stand behind:** one line naming what you actually read and
   confirmed versus what you inferred or couldn't reach (point back to the "Could not verify"
   list). If that list is non-trivial, say plainly that the review is partial.

Do **not** tell me whether to stop looping — that call is mine, and I'll make it from how the
"Could not verify" list and the Must-fixes are shrinking across passes. Your job each pass is
to report the current state honestly, including saying "the remaining items are minor" if
that's true; it is not to ring a bell that ends the loop. The reason: deciding the plan is
"good enough" is exactly the judgment I most need to own and you're least able to make for me.

## After the review: log to the furnace trial ledger
The "review only / never edit files" rule above is about the plan and the project — it holds
for those absolutely. This is the one narrow exception: a separate bookkeeping file, outside
any project, that records what *you* caught so the furnace-plan pre-filter can be graded over
time. Appending to it isn't editing the plan or the code, and it isn't a change I apply through
Claude Code — it's your own record. Do it right after you deliver each review pass.

**File:** `~/.claude/skills/furnace-plan/trial-ledger.md`. Append rows to the table at the
bottom; never touch the header or legend. If the file isn't there, the furnace skill isn't
installed on this machine — skip silently, don't recreate it.

**Only log plans that arrived with a `## Verification ledger`** (i.e. came through furnace-plan).
A plain plan with no ledger isn't part of the trial — don't log it, and **don't mention the
ledger or the trial in your review at all**: a non-furnace plan is simply outside the trial, so
the logging step is silently N/A. No "nothing to log" footer — that just clutters every review.

**One row per finding, per pass.** Map your own severity groups: every **Must fix** →
`must-fix`; every **Should consider** → `refinement`. "Could not verify" and "Open decisions"
are not findings against the plan — don't log them. The cut: a **finding** (Must fix / Should
consider) is something you judge *wrong or improvable* in the plan; an **Open decision** is a
legitimately-open product choice you are *not* resolving. Giving a recommendation on an open
choice doesn't make it a finding — if the plan isn't defective, it isn't logged. If a pass found
nothing to fix, append one row with Bucket `—`, Severity `—`, note `clean pass, no findings`, so
a clean pass is distinct from a forgotten log.

**Classify each finding into a bucket** — this is the signal the whole trial turns on:
- **Bucket 1 — no-read-behind-it:** a count, or an "X exists / is missing / is named" claim, the
  plan asserted *without* the ledger backing it with a read this session — exactly what the
  furnace's own "trace every claim to a read" check should have forced and didn't.
- **Bucket 2 — read-but-wrong:** the ledger *claimed* this was verified, but you re-opened the
  source and it's false — the planner read it and misread it, or inferred something no read
  could establish. This is the class neither the planner nor I can catch alone; it's why you're
  in the loop.
- **Bucket 3 — judgment / scope / design:** not a factual claim — a design, scope, or
  prioritization call. Can be either severity.

When you're genuinely torn between 2 and 3, lean 3: over-calling 3 under-credits the furnace and
correctly slows its promotion, which is the safe direction. But never soften a real wrong fact
out of bucket 1 or 2 to be kind.

**Row format** (columns already in the file):
`| Date | Project | Plan | Round | Bucket | Severity | What Cowork caught |`
- **Date:** full timestamp — `YYYY-MM-DD ~HH:MM TZ`, not the date alone.
- **Project:** the repo the plan is for.
- **Plan:** a short label; reuse the *same* label across passes of one plan so its rounds group.
- **Round:** which pass — 1 for the first, 2 for the revised plan I bring back, and so on.
- **What Cowork caught:** one concrete line, enough that someone re-reading the ledger later can
  audit whether the bucket call was right.
