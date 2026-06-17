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

## The preflight — run on your own draft before presenting

For each check: if it fails, **do the read/probe NOW and fix the plan before presenting.** It is expected and correct for this preflight to send you back to open a file or run a probe before you are allowed to call `ExitPlanMode`. A plan that fails any check does not get presented.

**1. Cite every codebase claim to a read you actually ran this session.**
Every "X is missing", "no files modified", "these mirror each other", every count, filename, or content claim must trace to a grep/read you performed *this session* — not memory, not inference from a filename. If you haven't read it, you don't know it.
*Failure it prevents:* "Step 7 — replacing AGENTS.md with @CLAUDE.md loses content. AGENTS.md isn't a pure pointer today." A plan built on imagined repo state.

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
  Checked: <the exact read/grep/probe you ran, or "could not confirm">
  Result: <what you found; if it changed the plan, say which step>
- Claim: ...
  Checked: ...
  Result: ...
```

**Honesty rule (load-bearing).** A fabricated "verified" is worse than an honest "unverified" — it converts a catchable bug into an invisible one. If you could not confirm a claim, write `Checked: could not confirm` and `Result: UNVERIFIED` and either make it a probe step or flag it for Cowork. A short honest ledger beats a long green one. Cowork will adversarially attack this ledger; assume every entry will be checked.

## What this is not

- Not a replacement for Cowork review. Every plan still goes to Cowork. The ledger shrinks and targets what Cowork must check; it does not let anyone skip the review.
- Not a license to narrow Cowork's scope. Cowork keeps full coverage — the ledger just tells it where you already looked.
- Not the judgment-call layer. Genuine product/scope/intent decisions are NOT for the furnace to resolve — surface them in the plan as sign-off items and let Cowork and Rex own them.
