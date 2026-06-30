# Handoff — Project-setup system (the trio is necessary, not sufficient)

**Written:** 2026-06-30 · **For:** the next session · **Status:** open question, not a decision.

Start a fresh session and read this first. It captures a question that kept getting framed too small in the originating session — and the deeper reason *why*, which §0 fixes before anything else.

---

## 0. Do this FIRST — fix the recurring lens bug (before the repo eval)

**The recurring failure (≈3× on 2026-06-30):** the agent kept collapsing the work down to *improving this repo's skill `.md` files* (frontmatter, prose, validation) instead of *improving what the skills produce for Rex's future projects*. Each time, Rex had to re-widen the frame.

**Root cause (honest, not deflecting):** the always-loaded context — `CLAUDE.md` / `AGENTS.md` / `BACKLOG.md` / `DECISIONS_ACTIVE.md` / latest retro — describes prd-to-product by its **artifact** ("skill-development workspace," "the product is installable skills," "markdown-only," "no deployed application") and its **rules**, but **never states its telos**: that the skills exist so Rex's *downstream projects* succeed. Artifact foregrounded + purpose absent ⇒ the path of least resistance at every session start is "optimize the artifact." The loud, repeated **markdown-only** invariant reinforces the misread by making *markdown* feel like the goal rather than the output format. So this isn't random forgetfulness — the repo's own context points the agent at the wrong altitude, every session, for every tool. (Agent's own miss too: it should ask "in service of what?" when setting a lens, instead of taking the repo's self-description literally.)

**Why prose-alone won't hold:** this repo's own principle says load-bearing rules get read as guidelines under attention pressure — the fix must be structural, prominent, and cite its failure mode, not a polite reminder.

**The fix — PROPOSED, gated on Rex (it is agent-config; do NOT land without approval):** add a "what this is FOR" block at the TOP of `CLAUDE.md`, mirrored into `AGENTS.md` (so it binds Codex too). Draft to approve/edit:

> ## What this is FOR (read before setting any lens)
>
> The product is skills — but skills are the *means*. The end is **Rex's future projects succeeding**: real apps and systems, on a sound stack, shipped well, built with Claude Code. Judge every piece of work — mining, building, designing, reviewing — by one test: **does it change what the skills produce for a downstream project?** Polishing a skill's own markdown (frontmatter, prose, validation) counts only if it changes that downstream output. "Markdown-only" is the skills' *output format*, not the goal.
>
> **Failure it prevents:** collapsing the work down to tidying this repo's `.md` files instead of improving the projects the skills exist to build (observed 3× on 2026-06-30, each requiring Rex to re-widen the frame). Catch yourself optimizing a skill artifact → stop and ask *"what downstream project outcome does this change?"* If the answer is "none," it is probably the wrong work.

**Sequencing:** land this **before** the repo eval (§6 track 2). If the corrected lens isn't in place first, reading template/workflow/devtools risks a 4th instance.

**Second-order win (flag, don't do now):** this is a generic context-engineering lesson — scaffolded projects should state their *telos / north-star*, not just their architecture. It likely ports into the `context-engineering` scaffold (per the repo's "port self-improvements back to the skill" rule).

---

## 1. The real question (stated at full size)

prd-to-product is Rex's toolkit for **building real software with Claude Code** — apps (mobile/web), new skills, knowledge work. Rex is a designer, not an engineer, and **delegates engineering judgment — including stack choice and setup — to Claude.**

The real question is **not** "should we build a foundation skill?" It is:

> **How does a project go from `context-engineering` (planned + AI-context scaffolded) to a built app that has the right stack chosen, security checked, audited, tested, and ruled — and how does Rex *know* those things are actually in place and exercised?**

The trio (`prd-creator` → `context-engineering` → `design-system-bootstrap`) is **necessary but not sufficient.** It plans and scaffolds *context and rules*; it does not establish or exercise *stack, security, audits, or tests*. That's a multi-hole gap across the whole build path, not one "foundation" hole.

## 2. Where the originating session kept mis-framing (read this so you don't repeat it)

- **Mis-frame 1:** treated "what helps Rex's projects" as "what tidies the skill markdown." Wrong — the value is the *projects*, not the skill files. ("Markdown-only" describes the skill *artifacts*; it is not a lens for what's relevant.)
- **Mis-frame 2 (the load-bearing one):** framed the foundation question as four options — A) author a code skill, B) expand context-engineering to write code, C) stack-specific skills, D) do nothing — **all of which assumed *Rex* authors and solo-maintains the skill.** It never put **"compose / adopt existing, externally-maintained build skills"** on the table. So the council's "skills rot, a non-engineer can't keep them current" argument was aimed at the wrong target: *consuming* a maintained Expo / RN / security / testing skill is **not** freezing your own snapshot — someone else maintains it. **The 100s of build skills out there are not unnecessary; the council was never asked about them.**

## 3. The one council nugget worth keeping (and its blind spot)

Council artifacts (this session): [report](../council/council-report-2026-06-30-foundation.html) · [transcript](../council/council-transcript-2026-06-30-foundation.md).

- **Keep (guardrail, not roadmap):** don't freeze *your own perishable engineering judgment* (specific auth lib, CI config, SDK pins) into a skill *only you* maintain — that rots, and a non-engineer can't see when it's gone stale. Capture the **question** ("is auth wired to current best practice?"), which doesn't rot, not the **answer**, which does.
- **Blind spot the peer round caught:** the whole anti-build case rested on an **unverified premise** — that the foundation need is a one-app hunch rather than a structural step every project hits. *Nobody verified it.* That premise is track 1 below.
- **Net:** the council answered a question one size too small. Use its guardrail; discard its scope.

## 4. Coverage map — trio + built-ins vs. what projects actually need

| Need | Where it stands today |
|---|---|
| Appropriate **stack** | **Not covered** — context-engineering takes stack as a given input; nothing chooses or stands it up |
| Proper **code rules** | **Covered** — this is what context-engineering scaffolds |
| **Security** checks | **Thin** — a few commit-blocking hooks; no actual audit |
| **Code audits** | **Partial** — built-in `/code-review`, `/security-review` exist, but not project-aware or guaranteed to run |
| **Tests** | **Not established** — rules can *reference* tests; nothing sets up a harness or gates coverage |

## 5. The reframe: compose, don't freeze

The likely answer is **not** "Rex authors a foundation skill" and **not** "do nothing." It's probably a **thin connective layer we own** that, per project type, *pulls in the right existing/maintained capabilities* (starters, security-audit, test-harness, stack setup) and *verifies they ran* — composition over authorship. Design that against evidence, not theory.

## 6. Next session — three review tracks (the actual work)

**Track 1 — Review real projects (ground the premise).** Look at Rex's actual builds — the shipped **Swift app** and any others — and map: what did setup actually require? What broke or was missing (security, tests, stack, rules)? Is the same gap *recurring* (which would make a connective layer earned, per Rule-of-Two) or one-off? This resolves the unverified premise from §3.

**Track 2 — Review the TanStack codebases Rex flagged.** *Not yet reviewed — these are priors from repo descriptions only; confirm by actually reading them. The `intent` clone is already on disk at `docs/mined/repos/intent/`; the others need cloning (gitignored, per `/mine`).* Rex's instinct: some of this work may already be done for us.
  - **[TanStack/template](https://github.com/TanStack/template)** — **strong candidate.** A maintained starter template is *exactly* the "someone else keeps the foundation current" model the council ignored. If it stands up a sound stack + structure + configs, adopting/forking it may be most of the "foundation" answer. **Review first.**
  - **[TanStack/workflow](https://github.com/TanStack/workflow)** — "type-safe durable execution for agents and workflows." Reads as a *feature/runtime library*, not project setup — likely tangential unless an app needs durable workflows. Confirm by reading, don't assume.
  - **[TanStack/devtools](https://github.com/TanStack/devtools)** — "framework-agnostic devtools panel." A debugging/observability UI — QA-adjacent but not foundation/setup. Likely tangential. Confirm by reading.
  - Open question to answer by reading: *"Are template/workflow/devtools explicitly doing the setup/foundation work Rex asked for?"* — `template` plausibly yes; the other two probably no. Verify, don't guess (the originating session's repeated failure).

**Track 3 — Deep online research (insights + inspiration).** What's out there for setting up iOS / React Native / web apps *for success* — existing skills, starters, security/audit/test tooling, "production-ready foundation" systems? Pull insights and inspiration for our system. The `/deep-research` skill fits this; frame it around "what a sound project-setup layer covers, and who already does it well."

## 7. Connects to existing backlog (Rex's own board already half-agrees)

This is the through-line behind three parked rows — fold them into the design:
- **Skill injection by project type** (`blocked`, gate:needs-decision) — auto-add the right skills per project type; blocked on plugin-vs-vendored delivery. *This is likely the spine of the connective layer.*
- **Chain auto-compose** (`watching`) — an orchestrator that chains skills automatically. [D-014]
- **Skill ecosystem gaps (Thariq 9-category)** (`watching`) — kinds of skill not yet held.

## 8. Method discipline (carry these in)

- **Compose existing maintained skills > author-and-freeze our own.** Author only the thin connective layer, and only on evidence of repeated need.
- **Ground every claim in a real project or a really-read source.** Do not assert what a repo/skill does from its description (the originating session's repeated miss). Read it.
- **State the question at full size before answering.** If an answer only addresses "build skill y/n," it's too small.

## 9. Session artifacts + state

- Uncommitted in the working tree (originating session, nothing committed): the `/mine` doc [`docs/mined/2026-06-30-tanstack-intent.md`](../mined/2026-06-30-tanstack-intent.md) + 3 board rows; the two council artifacts (§3); this handoff + its board row.
- The council was **not** logged as a `D-NNN` decision — it's a guardrail, not a settled call.
