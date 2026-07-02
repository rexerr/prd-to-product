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
| Product **instrumentation / metrics** *(added 2026-07-01)* | **Not covered by anything mined** — no repo in the Track-2 set touches it (gstack's telemetry serves itself, not the scaffolded product). Reference shape: Every's product-pulse pattern — instrumentation framed as a *setup step* ("if not instrumented, stop and set that up"), strategy-seeded KPIs → dated one-page reports → a folder of pulses as the product's working memory ([mine](../mined/2026-07-01-every-agent-native-guides.md)) |
| **Agent-environment parity** (dev-workflow: agent can run the app/tests, see logs, screenshot, PR) *(added 2026-07-01)* | **Not covered** — surfaced by Every's compound-engineering guide ("every capability you withhold becomes a task you do yourself"). **Attribution note:** cite that guide only — Every's *agent-native architectures* guide is a different axis (in-product parity for agent-native products; a product-architecture concern, not a foundation gate) ([mine](../mined/2026-07-01-every-agent-native-guides.md)) |

## 5. The reframe: compose, don't freeze

The likely answer is **not** "Rex authors a foundation skill" and **not** "do nothing." It's probably a **thin connective layer we own** that, per project type, *pulls in the right existing/maintained capabilities* (starters, security-audit, test-harness, stack setup) and *verifies they ran* — composition over authorship. Design that against evidence, not theory.

## 6. Next session — three review tracks (the actual work)

**Track 1 — Review real projects (ground the premise). → DONE 2026-07-01, premise VERIFIED** ([findings](project-setup-track1-findings.md)). Read two projects across two stacks and two lifecycle stages: `seance` (native iOS, shipped) and `cat-tracker`/Strays (RN/Expo, frozen at the trio→build seam — no `package.json`/Expo yet, the gap shown *live*). The setup categories (stack standup, deploy, tests, secrets, backend/instrumentation, agent-parity) **recur across both while every specific differs** — the signature that earns a thin, stack-aware connective layer (Rule-of-Two satisfied); rules out "do nothing" and "one hardcoded checklist." Three design constraints surfaced: the layer's job is **sequencing + standup, not just checking**; instrumentation/backend are **project-type-conditional**; "verify it ran" must **route to the capable actor** (agent often can't run/judge the check). Two handoff coverage-map corrections: security was *understated* (seance did secrets-hook + privacy manifest + export-compliance), audits ran but were never guaranteed.

  *Original framing:* Look at Rex's actual builds — the shipped **Swift app** and any others — and map: what did setup actually require? What broke or was missing (security, tests, stack, rules)? Is the same gap *recurring* (which would make a connective layer earned, per Rule-of-Two) or one-off? This resolves the unverified premise from §3.

**Track 2 — Review the TanStack codebases Rex flagged.** *Not yet reviewed — these are priors from repo descriptions only; confirm by actually reading them. The `intent` clone is already on disk at `docs/mined/repos/intent/`; the others need cloning (gitignored, per `/mine`).* Rex's instinct: some of this work may already be done for us.
  - **[TanStack/template](https://github.com/TanStack/template)** — ~~**strong candidate. Review first.**~~ **REVIEWED 2026-07-01 → prior FALSIFIED** ([mine](../mined/2026-07-01-tanstack-template.md)). It is a scaffold for authoring an open-source **library/package**, *not* an app-foundation starter (README.md:40: *"a starting point for new TanStack libraries"*). The name collision seeded the wrong prior. **Drop "fork TanStack/template" from the option space**; the app-foundation question stays open — read a TanStack **Start/Router app** starter instead. **But the mine paid off — one decision-grade model for the connective layer:** a sound foundation = an *enumerated set of orthogonal CI gates*, each catching one failure class (lint · dep-consistency · dead-code · doc-links · tests · **types-as-a-gate** · bundle · provenance), which maps ~1:1 onto the trio's gaps *and* fits our "every rule cites its failure mode" idiom → emit a `test:ci`-style gate list **per project type**, each annotated with its failure mode (spine of "compose don't freeze"; enriches Build-defaults item 5). Second bound: **security scopes light** — even this mature repo has no vuln/secret/CodeQL scan; its whole posture is provenance + install-script allowlist + SHA-pinned actions + Renovate (→ backlog row).
  - **[TanStack/workflow](https://github.com/TanStack/workflow)** — **REVIEWED 2026-07-01** ([mine](../mined/2026-07-01-tanstack-workflow.md)). Prior *confirmed* for project-setup (a durable-execution runtime; deploy adapters are runtime-hosting shims, not deploy setup) — **but refuted for orchestration:** it carries the maintainers' own `research/AI_ORCHESTRATION_INTEGRATION.md`, a reference design for an AI-agent orchestrator on a durable engine = **direct prior art for chain-auto-compose** (durable log → derived state → approval-pause → idempotent resume). Folded into that board row.
  - **[TanStack/devtools](https://github.com/TanStack/devtools)** — **REVIEWED 2026-07-01** ([mine](../mined/2026-07-01-tanstack-devtools.md)). Prior *confirmed* for the core (dev-only debugging shell, out of scope) — **but two test/QA-hole reference shapes surfaced:** (1) an **e2e Playwright-harness pattern** (shared `DevtoolsPage` page-object + `SELECTORS` fanned across 8 framework apps) — a concrete model for "how a scaffolded project proves it works," complementing gstack's `/qa` test-bootstrap; (2) **a11y as a CI-QA dimension** (axe-core/WCAG) the scaffold should *prompt for* (as a CI-runnable check, not the dev-time plugin). Plus a skill-craft yield from its intent-generated `skill_spec.md` (→ board row).
  - **Test/QA hole — now has concrete reference shapes:** gstack `/qa` (bootstraps a test framework + CI when absent) + devtools e2e harness (shared page-object structure) + an a11y check. When the connective layer is designed, the test dimension is the best-evidenced of the trio's holes.
  - Open question to answer by reading: *"Are template/workflow/devtools explicitly doing the setup/foundation work Rex asked for?"* — `template` plausibly yes; the other two probably no. Verify, don't guess (the originating session's repeated failure).
  - **[garrytan/gstack](https://github.com/garrytan/gstack)** — **REVIEWED 2026-07-01 → the decision-grade input** ([mine](../mined/2026-07-01-gstack.md)). A dogfooded, MIT, markdown-only "software factory" (~35 slash-command roles). It **closes 4 of the trio's 5 holes** with *substantive* commands — security (`/cso` OWASP+STRIDE), audit (`/review` parallel specialists), test/QA (`/qa` real browser + bootstraps a test framework), deploy (`/setup-deploy`→`/ship`→`/land-and-deploy`→`/canary`), plus real `PreToolUse` blocking hooks (`/guard`). It **shares the 5th hole: stack scaffolding** — gstack explicitly refuses ("Not even scaffolding," `office-hours/SKILL.md:1690`), confirming stack-init is the one gap *nobody* fills (look to a TanStack Start/Router app starter). Its maintenance plumbing (VERSION channel + install-type-aware upgrader + fail-safe SessionStart auto-update + versioned migrations) is the **existence-proof the §3 council doubted** — a solo non-engineer *can* keep a downstream fleet current. **The compose-vs-build fork sharpens to a third option: compose the *methodology* as a reference architecture (~200 lines of portable maintenance bash + capability blueprints); do NOT vendor the *artifact*** — a gstack clone drags in Bun, a compiled browser stack, an ML classifier, 74 bins, Supabase telemetry, gbrain, and a router preamble that would fight our CLAUDE.md discipline (and breach the D-013/D-019 don't-import-internal-machinery line).
  - **→ Recommend a council at the actual compose-vs-build decision** (costly + hard to reverse, per the "recommend a council at genuine forks" rule). The mine fed the fork; it did not settle it. Guard captured: do **not** import gstack's "Boil the Ocean" no-scope-gate / no-file-cap ethos — it is the philosophical opposite of our scope-gate discipline.

**Spec drafted → 2026-07-01** ([spec](../briefs/project-setup-skill-spec.md)). A `/project-setup` skill (4th sibling, after context-engineering) that composes maintained tools per stack. **Rex correction folded in (supersedes the council's hand-notes baseline): Rex is not the developer — Claude is; engineering verification routes to Claude/CI, Rex judges only look-right / works / ship.** v1 = RN/Expo recipe only, proven by standing up Strays for real; cruft-drift-binding parked OUT of v1. Awaiting spec approval → build.

**Council → DONE 2026-07-01** ([report](../council/council-report-2026-07-01-project-setup.html) · [transcript](../council/council-transcript-2026-07-01-project-setup.md)). Verdict: **COMPOSE not build; VENDOR now (plugin/marketplace later); defer starter-lane + iOS-submission with a "pick the company-backed maintained option when Rex can't judge staleness" rule.** Direction is high-confidence (survives every objection). The *mechanism* (cruft linked-template + verification-routing table) is low-to-moderate confidence — the peer round exposed **three unverified load-bearing premises**: (1) a "capable actor" who can judge a red verification rung may not exist (owner delegates all engineering judgment → routing may terminate at a blind judge = theater); (2) cruft's `cruft update` may propagate *pins* not *questions*, contradicting the capture-questions-not-answers guardrail; (3) "nobody sells the glue" at N=2 is equally consistent with "the glue isn't worth building" — no one priced it against hand-writing setup notes twice. **Gated first step: hand-write the verification-routing table for ONE frozen seam and test whether Rex can read a deliberately-failed rung** — that single test resolves premises #1 and #3. Not logged as a `D-NNN` (like the prior foundation council, it's a gated direction, not a committed build).

**Track 3 — Deep online research (insights + inspiration). → DONE 2026-07-01** ([research](project-setup-track3-research.md)). Headline: **the market sells every *capability* (all trio holes have maintained, CLI/config-driven tooling — Expo/EAS, XcodeGen/Tuist/Fastlane/xcodes/mise, Vitest/Playwright/Maestro, GitHub-defaults+Gitleaks/Renovate/Semgrep/zizmor); nobody sells the *glue*** (per-project-type composition + verification). Confirms "compose don't freeze." Gaps a thin layer owns: version reconciliation, "no-harness→bootstrap-one," sequencing, credentials, the verify-it-ran gate. Two patterns to steal: **cruft's linked-template drift model** (fits our port-back/brownfield-drift rows) and **the verify-it-ran ladder** (doctor probes + Terraform `check` live assertions + GitHub `needs:` success-gating DAG). Delivery evidence: AI-agent variation = context injection (Claude Code plugins/marketplaces, GA'd Oct 2025) not file templating; borrow Nx's plugin+composable-generator extensibility. Independent corroboration of Track 1: iOS headless CI is *industry-broken* on Xcode 26 (not a seance quirk).

  *Note:* the bundled `/deep-research` harness hit its known schema bug; salvaged via a direct 5-agent web fan-out. *Prior partial (still valid):* the Every agent-native guide cluster ([mine](../mined/2026-07-01-every-agent-native-guides.md)) added the instrumentation/metrics + agent-parity coverage-map dimensions and the strategy-layer-upstream-of-PRD candidate.

  *Original framing:* What's out there for setting up iOS / React Native / web apps *for success* — existing skills, starters, security/audit/test tooling, "production-ready foundation" systems? Frame it around "what a sound project-setup layer covers, and who already does it well."

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
