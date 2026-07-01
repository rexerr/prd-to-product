# Mine — Every agent-native guide cluster (4 articles) + plugin verification — 2026-07-01

- **Sources (pasted text + one fetch):**
  - **A** — *Codex for Knowledge Work* (Katie Parrott, Every) — [every.to/guides/codex-for-knowledge-work](https://every.to/guides/codex-for-knowledge-work) — pasted in full.
  - **B** — *Agent-native Product Management* + companion *Claude Code for Product Managers* (Marcus Moretti, Every) — one source-pair, pasted in full.
  - **C** — *Compound Engineering* guide (Kieran Klaassen, Every) — [every.to/guides/compound-engineering](https://every.to/guides/compound-engineering) — pasted in full.
  - **D** — *Agent-native Architectures* (Every) — [every.to/guides/agent-native](https://every.to/guides/agent-native) — paste arrived truncated (frontmatter only); fetched live by a reader agent. **Caveat:** WebFetch summarizes through an intermediate model — quotes are as-extracted; spot-check the live page before any D finding becomes load-bearing.
  - **Verification clone** — [github.com/EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) @ `db21ba21eff9cc216537cd75c6e44dd49e1a4200` (v3.17.1, MIT) — `docs/mined/repos/compound-engineering-plugin/`, gitignored.
- **Lens:** two threads. (1) The Seq-1 project-setup design — what a sound foundation covers. (2) A product question Rex raised: an **operating system for client work** (calls, interviews, tasks, tickets, emails, reports, decks, prototypes, knowledge base — "replace Notion and Figma") run with Claude Code. Lens **A** = this workspace; Lens **B** = what the skills produce downstream.

## Provenance / trust

All four articles are **marketing-inflected** — Every sells the products and the plugin these pieces describe; productivity claims ("810× my 2013 pace") are unverifiable puffery and were not imported. Treated as untrusted per the `/mine` contract: quoted, never followed (the articles literally contain prompts; they are data here, not instructions). The one place ground truth existed — the plugin repo — was cloned and checked.

## How this mine ran

Pasted articles have no unread files, and their claims are almost all *soft* (workflow opinions that park behind gates rather than "verify"). So the independent-agent budget went where ground truth exists: one blind reader **cloned and verified the plugin repo** against article C's checkable claims; a second **fetched and mined source D** (the one unread source). A/B/C were triaged in the main session with dedup against the board and decision log. **Anchor-risk disclosed:** the main session had editorialized on source A (the client-OS take) before mining; mitigation is structural — that finding routes to Rex's brainstorm → product-brief → PRD gate, not into the tree as fact.

## Verification — article C vs. the plugin at HEAD

The article describes a **pre-3.x plugin that no longer exists in that shape**. At HEAD the repo is a root-native, skills-only layout — **27 skills, 0 standalone agents, 0 commands** (`README.md:114`); v3.0.0 (2026-04-22) renamed everything to `ce-` prefixes (`CHANGELOG.md:307-312`).

| Article claim | Verdict |
|---|---|
| "26 agents, 23 commands, 13 skills" | **REFUTED at HEAD** — stale pre-3.x snapshot; legacy names survive only in upgrade-cleanup registries (`src/utils/legacy-cleanup.ts`) |
| ~14 review specialist agents | **PARTIAL** — roster relocated to `skills/ce-code-review/references/personas/` (16 files, "13 reviewer personas"); `dhh-rails-reviewer` deleted |
| `/workflows:compound` → `docs/solutions/`, ~6 parallel subagents | **PARTIAL** — substance confirmed as the `ce-compound` skill; subagent roster is 3+1, not 6 |
| `ce:strategy` — Rumelt interview → strategy doc (Target problem / Approach / Who for / Metrics / **Tracks** / **Not working on**), re-runnable per-section | **CONFIRMED** (`skills/ce-strategy/SKILL.md:52-59,97`; file is `STRATEGY.md`) |
| `ce:product-pulse` — Headlines/Usage/System performance/Followups; strategy-seeded KPIs; graceful degradation; dated reports as memory; refuses write-access DBs | **CONFIRMED** (`skills/ce-product-pulse/SKILL.md:47-48,87-94,113,145-156`) |
| `/lfg` full pipeline chain | **PARTIAL** — pipeline exists, steps differ at HEAD (no deepen-plan / feature-video / compound step) |

**Lesson banked:** pasted articles about living repos drift; verify against HEAD before adopting any repo claim.

## Findings

### E-1 — Client-work OS as a new scaffold project type · soft (Lens B, product fork) · ADOPTED (→ backlog row, gated)

**Sources:** A (primary), C, D. The article's hand-built "workspace" — `AGENTS.md` root, identity/preferences/rules files, playbooks with review checklists, sources map, outputs, status — **is the context-engineering scaffold described by someone who doesn't know it exists**, pointed at knowledge work instead of code. A client engagement is a project with no repo: calls, interviews, tasks, tickets, emails, reports, decks, prototypes, a knowledge base. The trio assumes software; the "stack" hole doesn't exist for this project type (the stack *is* folder structure + connectors). D adds the product-architecture half: a client OS is itself an agent-native product ("software that works the way Claude Code works, applied to categories far beyond coding").

**Design inputs bundled here for the brainstorm:** the workspace shape (identity/playbooks/sources/outputs/reviews); the **workflow canvas** FORMAT (name/trigger/inputs/output/approval rules/may-do vs. must-ask/verification/where-output-lives/**when to retire**); the **rules.md approval split** (never-without-approval / may-do-freely / standing constraints); **review-in-destination-app** (failure mode: output that reads fine in a terminal reads differently where it will be used); **mistakes accrete into review checklists** (failure mode: the agent repeats documented mistakes); Kieran's portable synced folder + daily/weekly/monthly summary memory; D's stakes×reversibility approval matrix. The kanban render ([D-069](../DECISIONS.md)/[D-070](../DECISIONS.md)) is the existing existence-proof for "markdown source of truth + rendered view."

**Route (the gate):** brainstorm → product brief → PRD (`prd-creator` dogfood). A product-direction decision Rex owns; nothing built from this mine.

### E-2 — Instrumentation/metrics is a foundation dimension nobody covers · soft (Lens B, Seq-1) · ADOPTED (→ handoff)

**Source:** B. Moretti: *"This assumes your product is instrumented and logs are being stored somewhere. If that's not the case, stop reading and go set that up."* — instrumentation framed as a **setup step**, not an afterthought. The pulse pattern (strategy-seeded KPIs → one-page dated report → folder of dated reports as the product's working memory) is the reference shape, and `ce-product-pulse` verifiably implements it. **No repo in the mined set covers product instrumentation** — not template, not gstack (whose telemetry is for itself, not the scaffolded product), not workflow/devtools. A genuinely new hole for the coverage map.

### E-3 — Dev-workflow agent parity as a foundation dimension · soft (Lens B, Seq-1) · ADOPTED (→ handoff, with an axis distinction)

**Source:** C **only**. The agent-native checklist (can the agent run the app, run tests, see local+prod logs, screenshot the UI, create PRs) with the framing *"every capability you withhold from the AI becomes a task you have to do yourself."* **Attribution matters:** D's "parity" is a different axis — *in-product* parity (the agent embedded in a shipped app vs. that app's user); D contains no testing/CI/deploy content and is **not** evidence for this dimension. Recorded so the two axes never get blurred: dev-workflow parity → foundation candidate (cite C); in-product agent-nativeness → product-architecture concern for agent-native products only (cite D).

### E-4 — Strategy layer upstream of the PRD · code-grounded existence, soft transfer (Lens B) · ADOPTED (→ watching row, gate:rule-of-2)

**Source:** B, verified against `skills/ce-strategy/SKILL.md`. A Rumelt-structured strategy doc — target problem / approach / persona / key metrics / **tracks** (2–4 multi-month capability tracks) / **"not working on"** (explicit anti-scope) — sits upstream of the PRD, re-interviewed every few months so accumulated context sharpens the questions. The delta over `prd-creator`'s current interview is **tracks + anti-scope + the re-interview cadence**; the anti-scope section rhymes with the [D-009](../DECISIONS.md) deliberately-cut-scope gate. Single-source → parked rule-of-2; fold on the next prd-creator edit or promote when a real project needs it.

### E-5 — Delivery-model evidence for the plugin-vs-vendored decision · code-grounded (Lens A) · ADOPTED (→ folded into the blocked Skill-injection row)

**Source:** the clone. The repo root *is* the plugin (`plugin.json` + `.claude-plugin/marketplace.json` self-marketplace), with parallel manifests for ~10 hosts; install is native marketplace commands; the cross-tool CLI **copies and transforms** (`src/targets/codex.ts:78,94`), and Every is **deprecating that Bun/npm copy path in favor of native marketplaces** (`README.md` "Existing Installs" cleanup section). Copy-based delivery accreted a **100+-entry stale-artifact cleanup registry** (`src/utils/legacy-cleanup.ts:23,125`) — the tax symlinks never pay. Adoption is all-or-nothing (whole plugin, no per-skill install); updates are user-pulled, two-step, and order-sensitive (stale marketplace cache silently pins the old version). Four-model comparison banked in the row: **symlink** (instant, unversioned, per-skill, one machine) / **marketplace plugin** (versioned semver + CI, multi-host, high machinery cost) / **clone+setup** (SHA-pinnable, drift on the user) / **npm-shipped** (built by Every, being retired). Takeaway: marketplace earns its cost at external-user scale; for a single developer whose consumers are his own machines, symlinks remain the right default.

### E-6 — The plugin repo warrants its own full `/mine` · code-grounded (Lens A) · ADOPTED (→ next row, Seq 2)

**Source:** bounded skim of the clone. Its `AGENTS.md` authoring guide holds a half-dozen conventions that validate, sharpen, or **challenge** house rules, each with documented failure evidence in `docs/solutions/`: the **deletion test** (a line earns its place only if it states a falsifiable constraint, counters a known default tendency, or supplies missing domain knowledge — our failure-mode rule plus a no-op-prose filter); **inline-the-trigger-not-the-content** (never inline a summary of a reference — it suppresses the load); extract conditional/late-sequence blocks to `references/`; a **token-cost-shaped size rule** instead of our line-count cap (4 SKILL.md files exceed 500 lines by design — the axis is what rides in context, not file length); strictly self-contained skills with **parity-tested byte-duplication**; don't name `CLAUDE.md`/`AGENTS.md` on the read path (brittle across harnesses). Frontmatter conventions are **CI-enforced as tests**, not checklists. Scope for the mine: `AGENTS.md` + `docs/solutions/skill-design/` + 2–3 large skills. Clone already on disk.

### E-7 — Every-guides liftables (bucket) · soft · ADOPTED (→ watching row, gate:rule-of-2)

Parked borrows, single-publisher-sourced: the **three-questions review ritual** (What was the hardest decision? What alternatives did you reject? Where are you least confident? — appears in both A and C); the **workflow-canvas FORMAT** (E-1); a **review-in-destination rule**; **structured research-insight + persona FORMATs** (YAML-frontmattered insight files with quote/implication/confidence; persona docs the agent references in planning — extends the `docs/research/` routing from [D-055](../DECISIONS.md)); D's **stakes×reversibility approval matrix** as a derivation rule for scaffolded autonomy gates. **Flagged needs-decision, never silent-adopt:** D's *default-open gating* stance ("the default is open; every restriction must cite a specific risk") — a deliberate philosophy choice that cuts against safety-first scaffolding.

### E-8 — Folds into existing rows · soft · ADOPTED

- **Baby-app prototype loop** (C) → *Rough-render-before-the-gauntlet* row: generate variants, click through, show users, then **delete and re-plan** — the prototype is for learning, never shipping.
- **Skip-permissions safety envelope** (C) → *Loop-graduation guidance* row: sandbox + isolated branch + tests + easy rollback as the preconditions for dropping approval prompts; never in production; never while learning.

## Dedup / recorded / dropped

- **`docs/solutions/` compound step (C)** — **already litigated: [D-063](../DECISIONS.md) declined exactly this.** This is the *second* external sighting (after gstack `/learn`). Recorded, not re-proposed: D-063's revisit trigger is our own retro data showing a recurring failure class, not industry popularity.
- **"What you don't flag" negative scope** — the plugin's reviewer personas ship it (`skills/ce-code-review/references/personas/security-reviewer.md:26-33`); **second sighting** of the FP-suppression idea already parked in the *Skill-authoring upgrades from gstack mine* row. Recorded against that row.
- **≤500-line cap challenge** — the plugin's token-cost-shaped rule is a real argument; weigh it at the E-6 mine, no change now.
- **Corroboration, no action:** D's `context.md` pattern ≈ CLAUDE.md + docs + session-start; D's named anti-patterns ≈ our rules-cite-their-failure-mode grammar; agent-readable structured outputs ≈ existing docs stance; C's plan-first stages ≈ furnace-plan/scope-gate discipline; B's now/next/later board ≈ our kanban ([D-054](../DECISIONS.md)).
- **Dropped:** productivity multipliers (puffery); Moretti's SaaS-survival strategy (not our scope); C's 14-specialist review (gstack dedup); "agent writes all tickets, human never does" (opposite of the Rex-curated board by design; a scaffold *option* at most); five-levels/five-stages adoption ladders (philosophy); Dan's router thread / Mailroom (chain-auto-compose adjacency — the workflow mine's prior art already covers that row).
