# Brainstorm — the kit as a personal-leverage system (idea → shipped)

**Date:** 2026-06-08
**Skill:** brainstorm-ideas-new (initial discovery)
**Framing (set by Rex):**
- **Scope:** Full system — the 3 skills (`prd-creator` → `context-engineering` → `design-system-bootstrap`) + the agent-process harness (session-start/end, hooks, permissions, autonomy charter, skill-injection).
- **Segment:** Solo builders / indie devs (Rex and people who work like him).
- **The win:** Personal leverage — make idea→shipped dramatically faster. Not (yet) a product for others.

Because the win is leverage-not-revenue, ideas are weighted toward: (a) removing the biggest real friction Rex hits, (b) fast to validate on his next real project, (c) compounding — the kit gets better at serving him over time. Most are grounded in observed failure modes already in `BACKLOG.md`, not invented.

---

## 15 ideas across three lenses

### Product Manager (throughput / leverage / what to build for max idea→shipped speed)

1. **`/idea-to-product` meta-orchestrator** — one command runs the whole chain end-to-end, with smart branching: skip the PRD interview if a brief/PRD already exists, skip design-bootstrap if a token system already exists (the qventus near-miss), stop at the right scaffold depth. The kit's whole premise is composition, but composition is currently the *user's* manual job.
2. **Stack-aware skill injection** — at scaffold time, map stack + primary output to a curated skill set, install a tiny active set, park the rest, promote per phase (the doc reviewed this session). Compounds: every new project auto-arrives armed with the right domain skills.
3. **Retro-mined self-improving backlog** — the kit reads its own retros + BACKLOG across all of Rex's projects and surfaces "here's the friction you hit most; here's the highest-leverage fix." The roadmap writes itself from real usage.
4. **Project-type recipes / presets** — pre-baked end-to-end configs for the types Rex actually builds (Swift/iOS like Séance, web/React, skill-building, static-HTML prototype). One pick → harness + skills + ROADMAP shape tuned, instead of re-answering the same interview every time.
5. **Prototype → product "graduation" path** — a capability that takes a validated prototype and hardens it in place (deploy-shell, tests, CI, the build-defaults backlog items) on demand. Don't re-scaffold; evolve.

### Product Designer (the solo builder's *experience* of the kit — Rex is the user)

1. **Conversational input auto-detection** — kill the `@/path/to/brief.md` plumbing. Skills scan cwd (`BRIEF.md`, `docs/`, common names), confirm what they found, proceed. The single most-hit friction in validation.
2. **De-jargon the interviews** — "Cluster 0," "0a/0b," "D-NNN" never reach the user. Interviews read as natural conversation, not a form with the seams showing. Makes the kit feel like a collaborator.
3. **Propose-then-consent default** — when the brief already covers a topic, draft the answer and show it for edits instead of asking cold. Respects Rex's prep and collapses interview length on thorough inputs. (Fixes the "ask anyway" overcorrection.)
4. **Instant re-entry surface** — a tight, consistent "where we are" view across every project (last-retro one-liner, next ROADMAP item, gated items, uncommitted state). Solo builders thrash between many repos; make context-switch-back instant. (Builds on `/session-start`.)
5. **Progressive disclosure of the harness** — don't dump full CLAUDE.md ceremony on a day-one project. Start minimal; reveal rules/hooks/gates as the project earns them (commit-gate appears once a UI exists; deploy-shell once a live URL is the deliverable). Match weight to maturity so the scaffold never feels heavier than the work.

### Software Engineer (technical capabilities / platform)

1. **Shared kit-core spec** — the skills duplicate conventions (OPTIONAL markers, renumber rule, paired-write, SKILL.md template, Gotchas). Extract one shared spec + lint so a convention change lands once, not N times. Kills drift.
2. **Generator self-test harness** — auto-generate *both* flat and modular example trees from canonical inputs on every change and diff against committed baselines. Closes the modular-regression gap structurally instead of hand-maintaining two trees.
3. **MCP/plugin-aware skill resolution** — the injection installer detects which candidate skills are plugins (enable/disable) vs need vendoring (`cp`/manifest), and promotes accordingly. Solves the blocking plugin-vs-vendor design question logged this session, plus a `vetted-on` refresh ritual.
4. **Project-state spine** — a single state object (stack, deploy_target, design_shape, phase, gated surfaces) that all three skills + the harness read/write, instead of re-deriving from files. Makes orchestration clean and stops the kit re-asking what it already knows.
5. **Hooks-as-guarantees upgrade** — finish the stdin-inspection fix for `block-deploy`/`block-worktree`, and emit opt-in scoped hooks (`/careful`, pre-commit check/test) from the already-captured commands. Turns prose rules into enforced guarantees.

---

## Top 5 prioritized (weighted: removes real friction · fast to validate · compounding)

### 1. `/idea-to-product` orchestrator  *(PM-1)*
**Why #1:** It's the kit's entire reason to exist as a *system* rather than three tools. Validation shows users (including sophisticated ones) expect one command to run the chain and skip the manual hand-offs. Highest leverage per unit of build, and Rex feels the difference on the very next project.
**Key assumptions to test:**
- That a single orchestrator beats manual sequencing *for Rex specifically* (he may actually prefer the control of running each stage).
- That the branching logic (skip-PRD-if-brief, skip-bootstrap-if-tokens-exist) is reliable enough not to clobber real work — the qventus case proves a naive auto-runner would have destroyed a hand-authored token system.
- That orchestration earns its maintenance cost vs. the cheaper fixes (auto-detect input + better cluster-0 routing) getting 80% of the benefit.

### 2. "Collaborator-feel" interview pass  *(Designer 1+2+3 bundled)*
**Why #2:** Three cheap, repeatedly-hit frictions — explicit-attach plumbing, vocabulary leaks, ask-cold-on-a-thorough-brief — that together make the kit feel like a form instead of a partner. All validated, all in one `intake.md` pass, all testable on the next PRD run.
**Key assumptions to test:**
- That auto-detection guesses the right source file often enough that "confirm what I found" doesn't become its own friction.
- That propose-then-consent doesn't slide back into silent absorption (the failure mode "ask anyway" was protecting against).
- That removing internal IDs from user-facing text doesn't cost the kit traceability it actually relies on.

### 3. Generator self-test harness (flat + modular auto-baselines)  *(Eng-2)*
**Why #3:** Meta-leverage. It makes every *other* improvement on this list safe and fast to ship, and it closes the exact gap we hit this session (no modular baseline → group-5's modular branch could only be eyeballed). A kit Rex iterates on weekly needs its own regression spine.
**Key assumptions to test:**
- That example trees can be generated deterministically enough to diff cleanly (template substitution is LLM-driven today — is it reproducible?).
- That the maintenance saved exceeds the cost of building + trusting the baselines (a wrong baseline is worse than none).
- That two baselines (flat + modular) are enough, or whether the matrix explodes (design_shape × deploy_target × ai_surfaces…).

### 4. Stack-aware skill injection w/ plugin-vs-vendor resolution  *(PM-2 + Eng-3)*
**Why #4:** Compounding — every new project arrives pre-armed with the right domain skills, the Séance pattern generalized. But it's gated on a real design question (plugin enable/disable vs vendored `cp`), so the *mechanic* must be validated before the feature.
**Key assumptions to test:**
- That per-project active/parked is even controllable for plugin-sourced skills (it may not be — plugins may load globally).
- That a curated manifest stays fresh enough to trust (the `vetted-on` rot risk).
- That the context-cost problem it solves is real *for Rex's* projects, not just in principle (it's real — ~70 plugin descriptions load every session right now).

### 5. Project-type recipes + shared kit-core  *(PM-4 + Eng-1)*
**Why #5:** Encodes the answers Rex gives the same way every time (a Swift app, a static prototype, a skill repo), and a convention change lands once across all skills. Lower urgency than 1–3 but high compounding once the kit is used across many projects.
**Key assumptions to test:**
- That Rex's projects cluster into a small, stable set of types (vs. each being a snowflake that defeats presets).
- That a shared kit-core doesn't over-couple the three skills (each is supposed to stay single-purpose and independently runnable).
- That preset defaults don't silently bake in wrong assumptions a fresh interview would have caught.

---

## What dropped off the top 5 (and why)
- **Retro-mined self-improving backlog (PM-3)** — highest *ceiling*, but speculative and slow to validate; revisit once 1–3 land.
- **Graduation path (PM-5)** — depends on the build-defaults items, which are themselves pending real-project evidence.
- **Instant re-entry surface / progressive disclosure (Designer 4/5)** — genuinely good DX, but `/session-start` already covers the floor; marginal until project count grows.
- **State spine (Eng-4) / hooks-as-guarantees (Eng-5)** — Eng-4 is a prerequisite that the orchestrator (#1) will force into existence anyway; Eng-5 is partly done and lower-friction.

## Connection to existing BACKLOG
#1 = fix-candidate A (idea-to-product). #2 = the aggregated `prd-creator` intake.md pass. #3 = the "no modular-shape example tree" item. #4 = the skill-injection-by-project-type item + its blocking design question. None of these are new debt — this brainstorm ranks work already on the board by leverage.
