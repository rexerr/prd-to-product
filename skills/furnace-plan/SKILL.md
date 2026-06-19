---
name: furnace-plan
description: "EXPLICIT-INVOKE ONLY — do NOT auto-select. Use ONLY when Rex types /furnace-plan or names \"furnace-plan\" directly. Invoke with a task or with no argument right after agreeing on a next step (\"ok, furnace-plan that\") — with no task it plans the work just proposed in the conversation. Authors the plan in plan mode, then before presenting it self-applies a verification preflight and appends a verification ledger. The ledger is built to be attacked by Rex's Cowork plan-review skill — this is a pre-filter that catches mechanical errors at authoring time so fewer reach Cowork, NOT a replacement for Cowork review."
---

# furnace-plan

## First action (mandatory) — enter plan mode

The moment this skill is invoked, **call the `EnterPlanMode` tool before doing anything else** — before reading a file, running a probe, or restating the task. Do not begin work in normal mode and switch later; the whole discipline below assumes you author inside plan mode from the first step.
*Failure it prevents:* drafting (or worse, starting to execute) the task outside plan mode, so the preflight and ledger get bolted on after the fact instead of governing the authoring.

A plan-authoring discipline. Plan the task normally inside plan mode, but **before you present the plan (before `ExitPlanMode`), run the verification preflight below on your own draft and append a verification ledger to the plan.**

## Why this exists

An 83-session audit of Rex's planning history found ~57% of plans drew a revision, dominated by one preventable class: **plans that assert things they never verified** — vacuous verification steps, codebase facts the plan never read, platform mechanics never probed. Every one of those was caught downstream by a separate reviewer (Cowork), never by the plan author. This skill moves the cheap mechanical catches to authoring time so the round-trip carries fewer bugs.

It does **not** make you a sufficient reviewer of your own plan — you can't reliably catch your own blind spot, which is exactly why Cowork stays in the loop. Your job here is narrow: force the reads, refuse to assert what you didn't check, and write down what you verified so Cowork can attack it.

## What you're planning

The task may come as an argument, or not at all. Often Rex invokes this right after you proposed a next step and he said "ok, plan that" — in that case plan the work just proposed and agreed in the conversation, you do not need him to restate it. If a task argument is given, plan that instead. Either way, the preflight runs before you present.

## Self-skip — bow out when the furnace adds nothing

You are already in plan mode (the mandatory first action stands — this is an in-plan check, never a reason to skip entering it). Before drafting the full plan, judge whether the task actually needs the furnace: if it's a **trivial change** — roughly one file, no multi-session fog, no unverified tool/platform mechanic, no recorded-decision boundary in play — say so and **offer to drop the discipline** and implement directly (or hand back to a lighter path) rather than run a preflight and ledger over a one-line edit. If Rex confirms, exit; if the task is non-trivial or he wants the furnace anyway, proceed.
*Failure it prevents:* turning the furnace into ritual overhead — a full preflight + ledger ceremony bolted onto work too small to carry a planning bug.

## The preflight — run on your own draft before presenting

For each check: if it fails, **do the read/probe NOW and fix the plan before presenting.** It is expected and correct for this preflight to send you back to open a file or run a probe before you are allowed to call `ExitPlanMode`. A plan that fails any check does not get presented.

**1. Cite every codebase claim to a read you actually ran this session.**
Every "X is missing", "no files modified", "these mirror each other", every count, filename, or content claim must trace to a grep/read you performed *this session* — not memory, not inference from a filename. If you haven't read it, you don't know it.
*Failure it prevents:* "Step 7 — replacing AGENTS.md with @CLAUDE.md loses content. AGENTS.md isn't a pure pointer today." A plan built on imagined repo state.

**1a. Sub-case — string-equality & decision-number claims: quote BOTH sides, re-read at write time.**
When a claim asserts two strings match, or that an id/number is the next free one (the next `D-NNN`), re-grep the source **at the moment you write the entry** and quote both sides from *that* read — not an earlier-in-session grep. Decision numbers and file contents move when parallel work lands mid-session, so re-check `docs/DECISIONS.md` (and `skills/furnace-plan/trial-ledger.md` for earmarked numbers) immediately before writing.
*Failure it prevents:* "next = D-041" asserted from a grep that went stale after CF-13 consumed D-041 — the real number was D-042 (Cowork-caught; n=2 with the stale D-018→D-020 id).

**2. Make every verification step able to fail, and able to reach what it claims to test.**
For each verify item, state the observation that would make it RED. Include the unchanged/default path and the failure path, not just the happy path. Measure claimed wins; don't assert them. If a check would pass even when the thing it tests is broken, it's theater — replace it.
*Failure it prevents:* "The live abort-path test doesn't test the abort path — a bad key rejects instantly and never arms the timeout." / "The script may run zero tests and report green."

**3. Probe unverified platform/tool mechanics as step 0.**
If the design rests on a tool/SDK/platform/MCP behavior you have not empirically confirmed this session, the probe is the FIRST step and its result is allowed to fork the plan. Never schedule it at step 8 of a plan that collapses if it fails.
*Failure it prevents:* "Headline: `ask` hangs in headless mode — so it deadlocks the very orchestrator it's meant to unblock." / "verify `paths:` empirically before step 1, not at step 8."

**4. (Boundary check, droppable) Diff the plan against recorded decisions and this session's agreements.**
If the project has a decisions log, name every recorded decision the plan touches; flag any reversal as an explicit sign-off item, never a silent change; confirm nothing agreed earlier this session was dropped. Skip when there's no decisions log to check against.
*Failure it prevents:* "that is not the full plan. where is the bit about housekeeping?" / a plan that re-commits the exact crash a prior decision exists to avoid.

## The verification ledger — append this to the plan

The ledger is the interface to Cowork. It is part of the plan document, so it travels with the plan when Rex copies it for review. Append it as the final section:

```
## Verification ledger
- Claim: <a load-bearing factual claim the plan makes>
  Checked: <the exact read/grep/probe — quote the verbatim line(s) you read, not a paraphrase of having read them; or "could not confirm">
  Result: <what you found; if it changed the plan, say which step>
- Claim: ...
  Checked: ...
  Result: ...

NO UNRESOLVED DECISIONS
```

**Terminal sentinel (mandatory).** The ledger's last line is non-optional: it must be either `NO UNRESOLVED DECISIONS` (unbolded, verbatim) or an enumerated block listing every skipped or unresolved decision. A skipped `AskUserQuestion`, or any fork the plan could not settle, goes there explicitly — never silently defaulted to the recommended option. It may not be a bolded or reworded variant (anti-gaming: a styled near-match reads as "done" while hiding a live choice). *Failure it prevents:* a real fork silently resolved to its default, so the plan looks complete but buried a decision the human never saw.

**Honesty rule (load-bearing).** A fabricated "verified" is worse than an honest "unverified" — it converts a catchable bug into an invisible one. If you could not confirm a claim, write `Checked: could not confirm` and `Result: UNVERIFIED` and either make it a probe step or flag it for Cowork. A short honest ledger beats a long green one. Cowork will adversarially attack this ledger; assume every entry will be checked.

## Sign-off items — hand off a decision, never a bare question

When the plan hits a genuine product/scope/intent fork the furnace can't resolve, do **not** escalate a bare "what do you think?". Do all the autonomous work first, then present each item decision-ready: **the stakes in plain language · the proof you already completed · an opinionated recommendation · the exact options.** Every unresolved item here must also appear in the ledger's terminal sentinel above, so it can't be dropped on the way to Cowork/Rex.
*Failure it prevents:* offloading the analysis back onto Rex/Cowork at the decision point — a fork handed over with no homework done.

## What this is not

- Not a replacement for Cowork review. Every plan still goes to Cowork. The ledger shrinks and targets what Cowork must check; it does not let anyone skip the review.
- Not a license to narrow Cowork's scope. Cowork keeps full coverage — the ledger just tells it where you already looked.
- Not the judgment-call layer. Genuine product/scope/intent decisions are NOT for the furnace to resolve — surface them as decision-ready **Sign-off items** (above) and let Cowork and Rex own them.
