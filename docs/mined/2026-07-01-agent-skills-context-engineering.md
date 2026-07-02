# Mine — Agent-Skills-for-Context-Engineering (muratcankoylan) — 2026-07-01

- **Source:** https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
- **Pinned:** `175cee7c25b5d98d919369f53427c646cdd86d93`
- **License:** MIT
- **Lens:** Skill-development workspace — this is the closest sibling we have ever mined (a shipped 15-skill *context-engineering* plugin + an autonomous research-to-skill harness). Filtered through: our skill-craft, the `context-engineering` scaffold, the pressure-test ticket, the blocked skill-delivery decision, harness/loop-graduation, `llm-council`, and Rex's new personality-product intent.
- **Method:** four blind readers (skills-craft · researcher OS · evaluation/LLM-judge · packaging/examples), facts-only with file:line cites; synthesis + verification in the main session. 8 load-bearing claims re-checked verbatim against the clone (all confirmed).

## Orientation — why this one is different

Every prior Track-2 mine falsified its own name-level description ("app-code library, little to transfer" → gold). This source is the opposite risk: it is *so* on-domain (it teaches the exact discipline we ship) that the danger is over-harvesting overlap. The readers were told to flag overlaps explicitly, and most findings below are **enrichments to existing rows, not net-new** — with three exceptions that are genuinely decision-grade: a **measured prose→behavior benchmark** (pressure-test), a **resolved delivery fork that rejects our symlink approach**, and a **worked personal-OS artifact** for the personality product. Because this mine touches ~9 existing rows, the [row-gloss accretion watch](../retros/2026-07-01-remainder-mines-and-router.md) is live — the landing recommendation (bottom) leans on **Seq-2 consolidation running next** and **new standalone rows**, not ref-piling.

---

## Findings (namespaced ASCE-N)

### The three decision-grade findings

#### ASCE-5 — MEASURED evidence that skill-description wording changes agent behavior · **verified (code/data)** · → pressure-test ticket

The repo ran a **600-run router benchmark** (4 frontier models × 50 ground-truth prompts × 3 replications) that measures which skill an agent picks per prompt. Critically, `settingSources: []` makes the router see **only the frontmatter `description`, not the SKILL.md body** — a clean isolation of the prose variable. Rewriting three skills' descriptions moved top-1 routing accuracy measurably; e.g. `context-fundamentals` **0.255 → 0.489 (+23.4pp)** (`CHANGELOG.md:43`, `:99-116`; prompts at `researcher/benchmarks/router/prompts.jsonl`; runner `researcher/scripts/render_router_report.py` with `--baseline` delta flag).

This is the **most direct external instance yet of the exact experiment our pressure-test ticket is trying to design** — prose-change → measured behavior-change, with a control. It hands us a ready methodology to copy: (a) a ground-truth prompt set covering positive controls, adversarial boundary pairs, combined-skill prompts, negative controls; (b) `settingSources:[]` to isolate description-vs-body; (c) per-skill top-1 with delta-vs-baseline tables; (d) `--concurrency N` runner (60min→15min); (e) per-run progress logging so a stalled sweep is visible (their v1 silently stalled at 566/600). **Honest limit:** this measures *routing/activation* (does the right skill fire), not *in-task behavior* once loaded — the repo explicitly defers body-effect measurement to an unbuilt "Stage 3 effectiveness benchmark" (`CHANGELOG.md:55`). Our pressure-test cares about both; ASCE-5 nails the activation half.

#### ASCE-6 — Skill-delivery fork RESOLVED, and it rejects symlinks · **verified (code)** · → blocked delivery-decision row

The repo faced the exact fork our [skill-injection-by-project-type row](../../BACKLOG.md) is blocked on, and landed on: **one bundled plugin** (all 15 skills in a single `plugins[]` entry, `source: "./"`, `strict:false`, explicit `skills[]` array — `.claude-plugin/marketplace.json:11-34`) discoverable by **both** the Claude marketplace manifest **and** the Open Plugins manifest (`.plugin/plugin.json` → `"skills": "./skills/"`), plus documented **directory-copy vendoring** (`cp -R skills/<name> .claude/skills/`). Three load-bearing specifics:

1. **Explicit anti-symlink stance:** *"The repository does not commit `.agents/skills` or `.cursor/skills` symlinks because symlinks are fragile on Windows and in plugin packaging"* (`CHANGELOG.md:16`; `README.md:149`). This is a **direct counter-data-point to our entire delivery model** — we symlink skills into `~/.claude/skills/` (both our dev setup and the shape we'd scaffold). Their reason (Windows + packaging fragility) is real for a *distributed* plugin; less so for our *single-dev-local* symlinks, but it's the strongest external signal yet that symlink-delivery doesn't generalize.
2. **One-plugin-not-many rationale:** Claude Code caches each plugin's `source` dir separately, so N plugins pointing at `source:"./"` each cache a full repo copy — bundling avoids cache duplication (`CLAUDE.md` Plugin Architecture).
3. **Two-manifest parity gate:** `validate_repo.py --strict` checks that both manifests name the same bundled plugin and resolve to the same 15 skills (`CHANGELOG.md:13`); `validate_platform_compat.py` simulates `.cursor/.claude/.codex/.agents` directory-copy installs (`CHANGELOG.md:14`).

**Recommendation:** when the delivery row unblocks, this is council-grade input — it's a complete, shipped, multi-host delivery model that contradicts our default. Also flag the **flat-file anti-pattern** they call out: never collapse `SKILL.md` into `.claude/skills/name.md` — it breaks relative `references/` paths (`README.md:179`).

#### ASCE-9 — `digital-brain-skill`: a worked personal/personality OS, built *by applying the skills* · **verified (code)** · → personality product + client-work-OS row

`examples/digital-brain-skill/` is literally *"a structured personal operating system for managing digital presence, knowledge, relationships, and goals"* for *"founders building in public, content creators, and tech-savvy professionals"* (`SKILL.md:9`) — i.e. a concrete reference architecture for **the personality product Rex wants to build**. Architecture worth stealing wholesale as a starting point:

- **Six modules:** `identity/ content/ knowledge/ network/ operations/ agents/` (`SKILL.md:60-67`).
- **3-level progressive disclosure:** L1 metadata (always) → L2 module instructions (on-demand) → L3 data files (as-needed) (`:32-38`).
- **File-format strategy:** JSONL = append-only logs; YAML = config; Markdown = narrative; XML = complex prompts (`:42-48`). **Append-only integrity:** never delete, mark `"status":"archived"` (`:49-54`) — the same durable-memory discipline supermemory sells as a product, done as flat files.
- **`HOW-SKILLS-BUILT-THIS.md`** is a *provenance walk*: each of 10 parent skills → the specific design decision it produced (e.g. Tool Design → "4 comprehensive scripts vs 15+ micro-tools"). **`x-to-book-system/`** does the same in the other direction: a full multi-agent `PRD.md` + a `SKILLS-MAPPING.md` table binding each PRD/architecture decision to the source skill that justified it (`examples/x-to-book-system/`).

Two payoffs: (1) a **concrete build-reference for the personality product** (modules + progressive disclosure + append-only JSONL is a credible v1 that needs no memory-vendor), and (2) the **PRD→skill-chain traceability table** is a pattern for our own prd-creator→context-engineering chain (document which skill justified each decision).

### Skill-craft cluster → feeds Seq-2 consolidation

#### ASCE-1 — Per-link "Read when:" load-gating · **verified (code)**
Every `references/` link *and* every cross-skill link carries a `- Read when: <condition>` clause telling the agent whether to load it (`skills/context-degradation/SKILL.md:217-222`). Sharper than our references/ split — it gates *when* to spend the tokens, not just *that* overflow exists. New sub-pattern for our references/ convention.

#### ASCE-2 — Inline `claim-*` provenance backed by a claims register · **verified (code)**
Numeric/benchmark/vendor claims must carry an inline `claim-*` ID backed by `researcher/claims/index.jsonl`, *"or they should be softened and moved to dated reference material"* (`template/SKILL.md:108`). The register schema: `claim_id, claim_text, owning_skill, source_url, retrieved_at, evidence_strength (primary|secondary|anecdotal|derived), volatility (low|medium|high), last_reviewed` (`claims/README.md:5-16`); a daily job flags high-volatility claims past review (`loop_daily.py:99-116`). This is a **machine-checkable "claim rot" defense** — distinct from our "every rule cites its *failure mode*" (that governs rules; this governs *external facts*). Candidate skill-craft borrow and a possible scaffold trait (a claims register for AI-authored factual claims).

#### ASCE-3 — Failure modes in a dedicated **Gotchas list**, not inline · **verified (code)** · *feeds an existing fork*
They mandate a `## Gotchas` section — *"the highest-signal content in any skill"* — with a fixed grammar (numbered, **bold title**, "what goes wrong + what to do instead"), rather than our inline-on-every-rule convention (`template/SKILL.md:83-88`; confirmed `tool-design/SKILL.md:251`, `context-optimization/SKILL.md:168`). This is a real fork for the Seq-2 consolidation's existing "deletion-test vs failure-mode clauses" question: **list-of-gotchas vs failure-mode-per-rule** are two different placements of the same discipline. Note: their own self-audit found Gotchas coverage was only 31% before a fix (`docs/skills-improvement-analysis.md:133`) — a concentrated section is easier to *omit* than inline clauses.

#### ASCE-4 — "Do not activate" routing block + **tested** activation boundaries · **verified (code)**
All 15 skills carry a "Do not activate" block that routes adjacent work to the owning sibling by name, with the failure stated: *"prevents broad skills from stealing activation from narrower skills"* (`template/SKILL.md:12`). Enforced by a deterministic regression test — `check_activation_cases.py` ranks skills by prompt overlap and passes a case only if `expected_primary_skill` is top-3 AND no `rejected_skills` are top-3 (`:81-110`). Feeds both skill-craft (suppression grammar) and the chain-handoff-audit / `/which-skill` router rows (a *tested* routing boundary, not just documented).

#### ASCE-12 — YAML-safe frontmatter portability gotcha · **verified (code)**
11/15 skills had unquoted `description:` values containing colons that strict parsers (Cursor, Claude Code, Codex) reject; v2.3.1 quoted them all and added a parser gate (`CHANGELOG.md:9`). Concrete cross-host gotcha for our scaffold + skill-craft: emit YAML-safe quoted descriptions and validate frontmatter across host parsers.

### Harness cluster → harness-proposals / loop-graduation / chain-auto-compose

#### ASCE-7 — A fully-worked deterministic autonomous harness · **verified (code)**
The `researcher/` OS is a production instance of nearly every principle those three rows care about:
- **8-state machine** `initialized→retrieved→evaluated→proposed→novelty_checked→validated→pr_ready→closed` (`research_loop.py:24-33`); machine state in `run-state.json`, human narrative in append-only `THREAD.md` — *"State governs automation, thread governs humans"* (`insights/auto-research-experiment.md:203`).
- **Deterministic-only continuous loop:** never invokes LLMs, no non-whitelisted network, advances ≤1 transition per invocation, parks anything needing judgment, returns exit-78 no-op when no safe work (`loop_step.py:1-15`).
- **Locked surfaces (anti-gaming):** rubrics, mechanism registry, both manifests, and the validator cannot be edited during scoring (`research_loop.py:24-32`); rubric rule *"Agent may propose changes, but cannot use the changed version to score the same proposal"* (`harness-change.md:13-18`).
- **Loop budgets / kill-conditions:** `max_active_runs:3, max_runs_per_day:6, max_parked:12, max_failures_per_day:5` — exceed → stop destructive work, bookkeeping only (`config.json:5-10`, `loop_step.py:334-357`).
- **Fetch safety:** `--allow-fetch` off by default; http/https only, reject redirect-scheme-change, `MAX_FETCH_BYTES=1.5MB`, 30s timeout (`loop_step.py:57,189-199`).
- **Human-approval boundaries:** `--reviewed-by` required to promote a mechanism; PR-prepared-not-merged; park-on-HUMAN_REVIEW/REJECT (`research_loop.py:161,509-510`).
- **Adversarial goldens that assert the gates trip:** self-approved rubric change → `human_review_stop`; mutable benchmark; unretrieved cited evidence → `run_readiness_fail`; reworded duplicate → `novelty_human_review` (`benchmarks/goldens/adversarial-goldens.json`).

For **loop-graduation** this is a second, richer safety-envelope instance (budgets + deterministic loop + fetch-gating + park-not-fail) alongside Every's skip-permissions + lfg's bounded-iterations. For **chain-auto-compose**, the durable-append-log + state-governs-automation split is a third prior-art. For **harness-proposals kill-watch**, it's direct evidence that these ideas ship.

#### ASCE-8 — LLM-as-judge bias-mitigation toolkit · **verified (code)** · → pressure-test grader + llm-council
A production judge stack: **position-swap 2-pass** with the *identical-response-must-TIE* invariant locked by a test (`pairwise-compare.ts`; `evaluation.test.ts:126`); multi-shuffle majority; **PoLL median** aggregation (robust to outliers); **cross-model judge** for self-enhancement bias (*"use a different model family than the agent being evaluated"*); anonymization/blind eval; length-normalization; **evidence-before-score** ordering; confidence calibration (*"Never 100% confident"*); and the load-bearing gate *"Run deterministic validation before LLM judgment … so invalid artifacts cannot be laundered by a favorable LLM score"* (`evaluation/SKILL.md:34,147`) — a **near-verbatim match to our consensus-laundering defense**. Rubrics use hard gates *before* weighted scoring, forced-override rules, and *"if the model cannot produce valid JSON, log it and route to human review instead of silently fixing"* (`content-curation.md:62`). Feeds pressure-test (grader design), llm-council (bias mitigation + laundering defense), and the decision-verdict-grammar row (graded vocabularies, tiered thresholds 0.7 general / 0.9 high-stakes). **Honest near-miss:** repeated sampling is of the *judge* (swaps, shuffles, panels), not the *agent under test* — there is **no `pass^k`** counterpart here; don't claim one.

### Recorded as observations / declines (so a future mine doesn't re-triage)

#### ASCE-10 — AGENTS.md as durable workspace memory · **observation**
Their `AGENTS.md` is a durable cross-agent memory (learned preferences incl. tone, learned facts, operating defaults, pointer to append-only accepted/rejected ledgers) — *not* a thin CLAUDE.md pointer like ours (`AGENTS.md:1-43`). It doesn't contradict our memory-vs-repo cut (AGENTS.md is cross-tool, so durable cross-agent memory there is consistent with "repo holds cross-tool") — but we deliberately keep AGENTS.md thin and split durable memory into `docs/` + Claude-local auto-memory. Their model is a coherent alternative, not an improvement for us. Recorded, not proposed.

#### ASCE-11 — Content-level CE rules · **mostly decline (shape-not-content invariant)**
The skills state many actionable context rules (compaction at 70-80% utilization; critical constraints at start/end not middle; signal-density test; never-compress-tool-schemas; ≥50 stratified eval cases; tool 8-param cap; actionable error messages). These are good, but our scaffold **scaffolds shape not content** (architecture rule 3 — the generator never writes product content), so we would not emit them. The only carve-out: they could inform the `context-engineering` skill's *own explanatory guidance* about what good context hygiene looks like — low priority. Recorded as reference.

---

## Verification — did / didn't

- **Did:** four blind readers over four zones with file:line cites and forced overlap-flagging; 8 decision-driving claims re-checked verbatim against the pinned clone — symlink rejection (`CHANGELOG.md:16`/`README.md:149`), the 600-run benchmark + `settingSources:[]` isolation + the +23.4pp delta (`CHANGELOG.md:43,99-116`), the "Read when:" gating (`context-degradation/SKILL.md:217-222`), the `claim-*` rule (`template/SKILL.md:108`), `LOCKED_SURFACES` (`research_loop.py:24-32`), digital-brain's personal-OS framing (`SKILL.md:9`), AGENTS.md-as-memory (`AGENTS.md:1-12`), and Gotchas-as-section (`tool-design/SKILL.md:251`). All confirmed.
- **Did NOT:** deep-read every one of the 15 skills' bodies (read SKILL.md structure + representative content); did not run their Python gates or the benchmark; did not read every `researcher/` script line-by-line (read the state machine, novelty gate, rubrics, config, and the scripts' enforced gates). Reader citations beyond the 8 re-checked were accepted on reader authority. Two internal contradictions the readers surfaced are treated as **soft** (not adopted as fact): rubric variance-reduction hedged in prose but hard-coded "40-60%" in a script; judge model `gpt-4o` in code vs `gpt-5.2` in README. No product files edited — this doc is the only artifact until adoption.
