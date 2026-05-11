# Audit procedure

The full procedure for auditing a project's AI-context structure against the `context-engineering` standard. Modeled on the two reference audits at `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md` and `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md`. The output structure the audits converged on is in [`templates/output-skeleton.md`](templates/output-skeleton.md); read that when you're about to write the report.

## 1. Reading order

Read in this exact order. The order matters: principles → standard → examples → project → prior audits.

1. **`/Users/rexc/Sites/prd-to-product/skills/context-engineering/SKILL.md`** — what the skill does, when it triggers, what shape it produces.
2. **`/Users/rexc/Sites/prd-to-product/skills/context-engineering/principles.md`** — the standards behind every template choice. Each rule cites the failure mode it prevents. This is the principal source-of-truth for "what should this project look like."
3. **`/Users/rexc/Sites/prd-to-product/skills/context-engineering/generator/decisions.md`** — the decision logic. Tells you which optional sections exist for which project shapes, what the per-decision DECISIONS_ACTIVE criterion is, and when the modular vs flat shape applies.
4. **`/Users/rexc/Sites/prd-to-product/skills/context-engineering/examples/output-small/`** — a complete worked example for the flat shape. Useful as a concrete reference; not every project should match this shape, but every project's shape should be derivable from the same decision logic.
5. **The audited project** — `CLAUDE.md`, `AGENTS.md`, `.claude/` (every file, including `settings.json`, `hooks/`, `commands/`, `rules/`), `docs/` (every file). Plus enough of the source tree (top-level layout, `package.json` if it exists, framework-config files) to infer the stack and project shape.
6. **The most recent prior audit in this project, if one exists** — `docs/context-audit-*.md`. Drives the §7 comparison closing if present.

If any of files 1–4 are unavailable (e.g., `prd-to-product` is not on disk), halt and ask the user how to proceed rather than running a partial audit against unknown standards.

## 2. Output structure

Six mandatory sections plus an optional seventh:

1. Inferred intake answers (table).
2. Missing files (load-bearing / cosmetic / correctly-omitted).
3. Present but drifted (intentional / accidental / borderline, with judgment).
4. Present and correct.
5. Open questions for the post-audit discussion.
6. Notes on what was *not* checked.
7. Comparison to prior audit — watch items (conditional, only if a prior audit exists).

Use the section headings verbatim. Fill the report by copying [`templates/output-skeleton.md`](templates/output-skeleton.md) into the audited project's `docs/` and replacing the placeholders. Do not reshape the sub-buckets or the table columns — the convergent structure across two real audits is the load-bearing part.

## 3. What to check explicitly

Beyond the section-by-section walk, the audit checks three watch items that emerged from the first two real audits. Both `the-council` and `field-society-demo` showed the same patterns; absent intervention these will keep recurring. Check each by name:

1. **`session-discipline.md` canonical-section coverage.** Does the project's `.claude/rules/session-discipline.md` carry all three of: **Read before you write**, **Checkpoint between phases of multi-step work**, **Session management** (`/rewind`, `/compact`, new sessions)? Both audited projects missed all three. If this project also misses them, name in §3 as drift; if it carries them, name in §4 as correct. Either way, check by name.
2. **AGENTS.md "Before you respond" recency-block dilution.** Does the recency block contain items duplicating body content — specifically direct-on-main, no deploy CLI, or reproduce-before-fixing? Both audited projects drifted the same three items into the recency block. If this project does the same, flag in §3 with judgment on intentional-vs-pattern-propagation; if not, name in §4.
3. **Hooks-layer presence vs prose-only.** Does the project have `.claude/settings.json` and `.claude/hooks/` matching the failure modes its prose cites? Both audited projects documented env-commit / deploy-CLI / worktree failures in `git-and-deploy.md` and shipped zero hooks. If this project does the same, flag in §2 (load-bearing missing files) with the prose-cites-failure evidence; if it has hooks, name in §4.

These three are table-stakes. If a fourth real audit surfaces a new universal watch-item, add it to this list rather than letting it live only in audit prose.

## 4. Source-of-truth precedence

When the project's files contradict what the skill would emit, the project wins for that project. The audit's job is to *flag the divergence so the user sees it*, not to recommend overwriting. Apply this principle throughout §3 — the judgment column always considers "this might be intentional and right for this project" before concluding "this is accidental drift."

If a project deliberately overrides a skill principle and the override is well-reasoned, name it in §3 as intentional and document the reasoning. That's a positive divergence, not a failure.

Drift only flows one direction at audit time: project-side findings are reported. Skill-side changes (e.g., "this drift pattern is now appearing in three projects; the skill principle should change") are out of scope for the audit. Those are continuous-mode triggers in `prd-to-product`, not audit findings in the audited project.

## 5. Read-only contract

The audit writes one file: the drift report. It does not edit `.claude/`, `AGENTS.md`, `CLAUDE.md`, anything else in `docs/`, or any source code. Fixes happen in a follow-up session, sized and decided after the audit lands.

If the user asks to "just fix it while you're in there," decline and capture the requested fix as an open question in §5. This keeps audit-and-act phases separable.

## 6. Output location

Save to `<audited-project>/docs/context-audit-YYYY-MM-DD.md` using today's ISO date. If the project has no `docs/` directory, save to project root with the same filename and flag in §2 that a `docs/` set is itself a missing canonical pattern.

Do not overwrite an existing audit file. If today already has an audit at the target path, suffix `-rerun-N` to the filename; for separate-day re-audits, the §7 comparison section replaces the function of overwriting.

## 7. After the report lands

The procedure ends at "report saved." Anything after — discussion of findings, deciding what to act on, opening follow-up sessions — is the user's call. Surface in §5 the questions that would unblock those decisions, but do not propose specific fixes or roadmaps. That separation is the read-only contract restated.

## Cross-references

- The skill this audit checks against: [`/Users/rexc/Sites/prd-to-product/skills/context-engineering/`](../context-engineering/).
- Output skeleton: [`templates/output-skeleton.md`](templates/output-skeleton.md).
- Reference audits that shaped this procedure: `/Users/rexc/Sites/the-council/docs/context-audit-2026-05-10.md`, `/Users/rexc/Sites/field-society-demo/docs/context-audit-2026-05-10.md` (external repos).
- Where audit findings drive skill changes: continuous-mode discipline in [`/Users/rexc/Sites/prd-to-product/ROADMAP.md`](../../ROADMAP.md) "Continuous mode after Phase 4."
- Heavy-validator option as future work: [`NOTES.md`](NOTES.md).
