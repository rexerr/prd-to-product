# Build defaults — investigation brief

## Why this exists

The `context-engineering` skill scaffolds context files (rules, docs, hooks) but does not currently scaffold *build procedure* — the order in which a project's phases should land, the test discipline that applies, the deploy-first vs feature-first sequencing, the abstraction-deferral rule. Every scaffolded `ROADMAP.md` is a stub the user fills in by hand.

The user has named a meta-problem with this gap: they cannot evaluate agent quality at the code level, so the continuous-mode discipline ("wait for real failure modes to surface, then fix") has a broken feedback loop for them specifically. Stumbles won't surface as observable failures; they'll surface as projects that take longer than they should, or never ship, or ship with hidden technical debt the user can't see. The skill cannot rely on user observation to discover what to fix.

The response: borrow opinions that are already validated externally. Bake them in as scaffolded defaults rather than waiting for user-observation to confirm them. This brief catalogs the candidate opinions, names their external sources, and proposes how each would land in the skill if accepted. It does not pre-decide. The next session reviews the bundle, accepts or rejects each opinion explicitly, and ships the survivors.

## The opinion bundle

Six candidates. Each entry: the opinion, the failure mode it prevents, the external source it cites, where it would land in the skill, when it might be wrong.

### 1. Smallest deployable first

**Opinion.** Phase 1 of any project that has a deploy target is "ship a hello-world to production. Confirm the URL works in a browser. Tag the commit." No feature work begins until production has been touched.

**Failure mode it prevents.** The 6-months-of-work-and-no-deploy-story trap. Production-environment surprises (CDN config, env-var loading, build-step quirks) caught at month 6 instead of day 1. Feature work that assumes a deploy story that doesn't exist.

**Source.** *Continuous Delivery*, Humble & Farley (2010). "Deploy on day one" is canonical. The Lean Startup MVP principle (Ries, 2011) makes the same case from a product angle. 15+ years of consensus across engineering and product literature.

**Where it lands.** `ROADMAP.md.template` gets a stack-aware Phase 1 that varies by `deploy_target`. For Vercel: "git push to GitHub; verify auto-deploy fires; open the Vercel URL; embed a `<h1>` with the project name." For Fly / Railway: parallel. For `deploy_target == "none"`: skip — the opinion only applies when production is reachable.

**When it might be wrong.** Spike or prototyping work that explicitly will never deploy. The intake question `deploy_target == "none"` already gates this; no additional override needed.

### 2. Vertical slice over horizontal

**Opinion.** Build one feature end-to-end (data layer → API → UI) before scaffolding the next feature. Phase 2 is one slice, not five tables.

**Failure mode it prevents.** The "all infrastructure, nothing connects" trap. Five data models scaffolded, no UI; five UI components built, no data flowing; integration surprises caught after the foundation is poured.

**Source.** *The Pragmatic Programmer*, Hunt & Thomas (1999), "Tracer Bullets" chapter. XP / agile literature broadly. Re-derived independently many times.

**Where it lands.** `ROADMAP.md.template` Phase 2 prompts: "pick one user-facing flow from the workflow list. Build the data model it needs, the API route it needs, the UI it needs, end-to-end. Confirm the flow works in production. Then start Phase 3 with the next flow." Also a one-line addition to `session-discipline.md.template`: "Within a phase, finish one vertical slice before starting another. Do not scaffold N tables or N components in parallel."

**When it might be wrong.** A project with a known-canonical data model (e.g., a migration from an existing system) where building the schema first is genuinely the right move. Rare. The rule can be overridden inline in the project's own ROADMAP; the template just provides the default.

### 3. Test-first for logic

**Opinion.** For logic with a clear input → output contract (parsers, scoring engines, classifiers, data transforms), write the failing test before writing the function. UI components and integration code are exempt; the visual-confirmation gate covers them.

**Failure mode it prevents.** Untested logic ships; agent hallucinates correctness; bugs surface in production. The "the code looks correct" failure mode the skill already names — but specifically targeted at the kind of code where automated testing actually works.

**Source.** *Test-Driven Development by Example*, Kent Beck (2002). More contested than #1 and #2 — DHH and others have pushed back on TDD-as-religion — but the narrowed claim (test-first for logic with clear contracts, exempt for UI/integration) survives the pushback.

**Where it lands.** New `.claude/rules/test-discipline.md` template, path-scoped to logic directories (e.g., `lib/**/*.ts`, `app/api/**/*.ts` for Next.js; equivalents per stack). New intake question: `enforce_test_first` (default true). A one-line addition to the recency block in AGENTS.md.template: "Logic work: write the test first." Gated on `stack_has_testing_framework` (derivable from intake — Next.js / React-Vite / Python all have one; Node-CLI sometimes does; `other` asks).

**When it might be wrong.** Pure-prototype work where the cost of writing the test exceeds the cost of throwing away the code. Solo dev exploring an unfamiliar API where the contract isn't known yet. Both are legitimate exemptions; both can be handled by the user temporarily setting `enforce_test_first: false` in the project's own config, or just ignoring the rule for the exploration phase and reinstating it for build phase.

### 4. Visual-first for UI (already in skill)

**Opinion.** UI changes require running dev server + visual confirmation before commit. Already shipped.

**Source.** This skill's own `principles.md`. Listed here only to name it as part of the complete bundle.

**Where it lands.** Already in `session-discipline.md.template`, the recency block in `AGENTS.md.template`, and the `block-worktree.sh` hook when `uses_visual_confirmation_gate == true`. No changes.

### 5. Type-check / lint pre-commit (prose, not hook)

**Opinion.** Before committing logic changes, run `<check_cmd>` and quote the output in the commit response. Do not commit if it fails. This is the resolution from the verify-vs-prompt conversation (2026-05-10): rule-only first, sentinel-or-hook later if the rule fails.

**Failure mode it prevents.** Type errors and lint failures shipped to CI / prod; agent claims "done" without running a command that's literally listed in the AGENTS.md Commands section. The AGENTS.md paper's strongest empirical finding (commands work when explicit) applied to the verification step.

**Source.** The AGENTS.md paper (already cited in `principles.md`). Standard engineering practice. The specific rule-only-no-hook framing was developed in this repo's 2026-05-10 verify-vs-prompt discussion.

**Where it lands.** Addition to the "Verification before claiming done" section of `session-discipline.md.template`. One-line addition to the AGENTS.md.template recency block (or a new bullet under the existing Verification line): "Logic work: run `<check_cmd>` and `<test_cmd>` before commit; quote the result." Gated on the commands existing — if `check_cmd == "(none)"` and `test_cmd == "(none)"`, suppress the rule.

**When it might be wrong.** Projects with no check/test commands (the `other + none` case). The gate handles this.

### 6. Defer abstraction until the third instance

**Opinion.** Do not create utility files, shared hooks, or abstractions until the third instance of the pattern appears. Two similar functions is acceptable duplication; three becomes the abstraction. Applies to product code only — not rule files, not docs.

**Failure mode it prevents.** Premature abstraction. Utility files written for two callers that ossify the wrong contract; shared hooks built before the use case is understood; abstractions that have to be rewritten when the third real use case differs from what was extracted.

**Source.** "Rule of Three" — Don Roberts, in *Refactoring* (Fowler, 1999, attributed). WET (Write Everything Twice) discussions in opposition to DRY-as-religion. Strong consensus in the refactoring literature; matches the continuous-mode discipline the skill itself uses for rule changes.

**Where it lands.** A short section in `session-discipline.md.template` under a new heading "Defer abstraction." One sentence in the principles file linking the rule to continuous-mode discipline (the same pattern applied to code). No intake gating — applies universally to product code.

**When it might be wrong.** A migration from a system where the abstraction is already proven. Code that's deliberately built as a library for external use (different evaluation context). Both are rare in the projects this skill targets.

## What this brief is NOT proposing

- A verification *hook*. The 2026-05-10 verify-vs-prompt discussion resolved this: rule-only first, sentinel-or-hook later if the rule fails. Item 5 is prose; not a new hook.
- A specific testing framework. Item 3 says "write the test"; it doesn't say "use Jest." Framework choice stays project-specific.
- Changes to the existing visual-confirmation gate or the three block-X hooks. Those work; leave them.
- Phase scaffolding that locks the user into a 6-phase shape. The proposal is opinionated *defaults* in `ROADMAP.md.template`; users can override per-project.

## Where each opinion lands — implementation summary

| # | Opinion | Template / file | Intake gate |
|---|---|---|---|
| 1 | Smallest deployable first | `ROADMAP.md.template` (new Phase 1 scaffold, stack-aware) | `deploy_target != "none"` |
| 2 | Vertical slice over horizontal | `ROADMAP.md.template` Phase 2+ prompt; `session-discipline.md.template` one-liner | None — universal |
| 3 | Test-first for logic | New `test-discipline.md.template` (path-scoped); recency-block addition | `enforce_test_first` (new); `stack_has_testing_framework` (derived) |
| 4 | Visual-first for UI | Already shipped | (existing) |
| 5 | Check / test pre-commit | `session-discipline.md.template` Verification section; recency-block addition | `check_cmd != "(none)" || test_cmd != "(none)"` |
| 6 | Defer abstraction | `session-discipline.md.template` new section; `principles.md` one-line cross-link | None — universal |

Total scope estimate if all six ship: ~150 lines across 4–5 files, plus one new template (`test-discipline.md.template`). Inside the 300-line feature-work cap.

## Recommended sequencing — pilot one first

Do not ship all six in one phase. Pilot one and watch for the failure mode it claims to address before adding the rest. Reasoning: this brief is itself the cache transfer from a meta-problem ("user can't evaluate") to a set of opinions; we don't know yet which opinions actually help and which add noise. The continuous-mode discipline that governs the rest of the skill applies here too — act on evidence, not on the bundle.

Recommended pilot order:

1. **Item 1 (Smallest deployable first).** Highest-conviction, lowest-cost, easiest to evaluate ("did the project deploy in week 1 or didn't it"). Run this on the next real project before the others.
2. **Item 5 (Check / test pre-commit).** Highest-frequency surface (every commit). Easy to spot when it does or doesn't catch a real failure.
3. **Item 2 (Vertical slice).** Visible in the project's git log — did phases finish end-to-end or fragment?
4. **Items 3, 6 (Test-first, abstraction-deferral).** Slowest feedback loop; ship last when the others have proven the brief's hypothesis.
5. **Item 4** is already shipped. Skip.

## Open questions for the deeper session

1. **Should phase scaffolding live in `ROADMAP.md.template` or a new `BUILD_GUIDE.md.template`?** ROADMAP is the user's project-management surface; encoding opinions there might feel intrusive. A separate guide file keeps the opinions visible but separates them from the user's own roadmap planning.
2. **Should test-discipline be its own rule file or a section in `session-discipline.md`?** Path-scoping argues for a separate file (tests apply only when logic files are touched). File-count argues for keeping `session-discipline.md` as the umbrella.
3. **Does the rule-of-three deferral apply to rule files and docs, or only product code?** Brief proposes "product code only" — rule files have their own continuous-mode discipline that already governs this. But it's worth confirming.
4. **How prescriptive should Phase 1 be in `ROADMAP.md.template`?** A full filled-in phase ("git init; configure GitHub; deploy hello-world; tag commit") vs a one-line guide ("Phase 1 = ship hello-world to production"). The first is hand-holdy; the second trusts the agent to fill in. Lean is the first, per the user's stated need.
5. **What's the override path for opinions a specific project doesn't want?** Intake-time (new question per opinion) or in-project (the project's own ROADMAP can drop a phase)? Lean is intake-time for opinions that are universal-ish (3, maybe 6) and in-project override for opinions that are clearly stack-shape-dependent (1, 2).
6. **Should the brief itself ship as a rule the skill emits, so future scaffolded projects inherit the philosophy doc?** Probably yes — emit as `docs/build-philosophy.md` or similar, with the opinions stated and citations preserved.

## Cross-references

- The verify-vs-prompt-vs-hook discussion that informed item 5: this conversation's chapter "Session C: act on 4 promoted items" → follow-up on verification gates (2026-05-10).
- The forcing-function principle that justifies baking opinions in via templates rather than relying on rules-only: [`skills/context-engineering/principles.md`](../skills/context-engineering/principles.md) "Hooks defaults are a forcing function" section.
- Continuous-mode discipline (acts on evidence; pilot before bundle): [`BACKLOG.md`](../BACKLOG.md) "Format" section and [`docs/retros/`](retros/) history.
- HTML brief as the structural model: [`docs/html-over-markdown-brief.md`](html-over-markdown-brief.md).
- The two real audits that revealed the meta-problem (skills produce context but not procedure): `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`, `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md`.

## Status

- **Not started — brief only.** Implementation deferred to the next session.
- **Parallel-eligible** with the HTML-over-Markdown investigation. Independent.
- **Branch policy:** direct on `main`. The pilot (item 1) is a single template + ROADMAP scaffold update; no overlap with parallel work.

## Suggested first prompt for the implementation session

```
Read docs/build-defaults-brief.md. Then:

1. For each of the six opinions, state your position: ship as proposed, ship with modification, defer, or reject. For "ship with modification" or "defer," name the specific change or the trigger condition.

2. For the opinions you accept: rank by pilot order. Confirm or change the brief's recommendation (1 → 5 → 2 → 3, 6).

3. Resolve the open questions you have an opinion on; flag the ones you don't.

4. Pick the pilot opinion (likely item 1). Outline the edits: which template, which intake question (if any), what the Phase 1 scaffold says for each deploy_target. Scope estimate.

Do not write any code yet. End with a written go/no-go on the pilot.
```
