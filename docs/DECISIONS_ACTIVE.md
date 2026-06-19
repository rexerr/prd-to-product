<!-- Reconciled against DECISIONS.md through D-044 · 2026-06-19. If DECISIONS.md carries higher-numbered decisions not yet evaluated for this view, this marker is stale — re-reconcile and bump it. Curated subset, NOT a completeness claim: not every D-NNN ≤ D-044 appears here (many are deliberately skipped as visible-by-reading; D-031/D-032/D-033/D-035 and D-036/D-037/D-038/D-039/D-040/D-041 evaluated, not mirrored — visible by reading the furnace-plan/prd-creator/context-engineering/CLAUDE.md files; D-034, D-042, D-043, and D-044 mirrored below). Bump this line whenever a new decision is evaluated for mirroring, mirrored or not. -->

# Active decisions

Curated view of currently-binding decisions whose constraints are not obvious from reading code alone. IDs mirror the full append-only history in [`docs/DECISIONS.md`](DECISIONS.md). Read the full entry there for rationale and context.

A decision belongs here if **all** are true:

- It imposes a rule the agent must follow now.
- That rule is not enforced or visible by reading the code itself.
- It has not been superseded by a later decision.

When a new decision lands in `DECISIONS.md` that meets these criteria, mirror it here as a one-liner.

---

### D-001 — Skills stay markdown-only

All skills in this repo produce markdown output until the HTML-over-Markdown investigation in [`docs/html-over-markdown-brief.md`](html-over-markdown-brief.md) explicitly authorizes a change. Do not introduce HTML output paths in any skill without that decision being recorded.

### D-002 — Direct-on-main for skill-refinement phases

Skill-refinement work commits direct on `main`. Branches only for genuinely parallel work (e.g., HTML investigation if it touches overlapping skill files).

### D-003 — Recency-block visual confirmation is conditional

In `context-engineering`, the recency-block item "Visual confirmation gates the commit" is gated on `uses_visual_confirmation_gate == true`. Same gate drops body Commit gate, Verification UI bullet, Codex override, and the "No worktrees" suffix. Do not hardcode UI assumptions back into the templates.

### D-005 — Generators are non-destructive by default

All three skills must not overwrite an existing file without explicit consent: before writing, check if the target exists; if it does and is not an unfilled scaffold (no `<!-- PARAMETERIZE:` markers), show a diff and ask overwrite/skip (default skip). Merge only where defined (DSB rule file + tailwind config + `globals.css`), and **the agent performs those merges itself with a diff-confirm — never a snippet for the user to apply** (interactive-only; headless skips per the D-006 ceiling — see D-007); whole-file artifacts are overwrite-or-skip. The prose remains the backstop; **enforcement is now provided by the write-guard hook — see D-006.** Full entry: [`DECISIONS.md`](DECISIONS.md) D-005; merge mechanism: D-007.

### D-006 — Write guard is hook-enforced (interactive-`ask` / headless-`deny`)

A global PreToolUse hook ([`hooks/write-guard.sh`](../hooks/write-guard.sh), matcher `Write|Edit|MultiEdit`) enforces D-005 while a generator run is armed. Each skill arms at run start / disarms at run end via Bash (`: > ~/.claude/state/write-guard/$CLAUDE_CODE_SESSION_ID.sentinel`). A write to a file that **existed before the run** is gated: interactive → non-forgeable `ask` dialog; headless / `bypassPermissions` → `deny` (default-skip, never clobbers/hangs). Run-created files are auto-tracked (run-owned) and stay editable; a missing owned-set fails safe. **Install is the operator's `~/.claude/settings.json` (manual, gated) and the hook must be `chmod +x`.** Honest ceiling: bypassable by `--dangerously-skip-permissions`; headless runs are *update-incapable* on pre-existing files (greenfield only), which clears the `/idea-to-product` gate for the clobber-safety class only. Full entry + verification: [`DECISIONS.md`](DECISIONS.md) D-006. Reference: [`hooks/README.md`](../hooks/README.md).

### D-008 — No adopt-automation for Claude Design bundles *(narrowed by D-044)*

**Partly superseded by [D-044](DECISIONS.md):** DSB now **has** an adopt mode (see below). What still binds from D-008: bundles stay authoritative and the **design source of record**; the schema-mismatch reasoning holds, so an adopt path **copies, never transforms** (no routing bundle tokens through the scale-first template); it defaults to CSS-vars, **never Tailwind**; and the **Rule-of-Two** revisit trigger (re-evaluate on a 2nd real bundle) is unchanged — still N=1. Knowledge + the import-rule source of record live in [`design-handoff-adoption.md`](design-handoff-adoption.md). Full entry: [`DECISIONS.md`](DECISIONS.md) D-008.

### D-009 — Recommend a council at genuine forks (never auto-run); reconcile bundle vs interview PRD by KIND

The LLM Council is **not** a wired-in primitive. A *recommend-don't-auto-run* note lives in this repo's [`CLAUDE.md`](../CLAUDE.md), in `context-engineering`'s scaffolded session-discipline (flat + modular + example), and as a `prd-creator` principle — firing only when a decision is **both costly to get wrong and hard to reverse**, phrased tool-agnostically in scaffolded output. To reconcile a Claude Design bundle PRD against an interview PRD: build nothing structural (per D-008) — **human diff-and-adjudicate, section-keyed, with deltas routed by KIND**: pure additions are presumptively safe; anything re-expanding a deliberately-cut scope is held as a **scope-gate** ("the bundle re-introduces something you decided to cut"). Full entry + council: [`DECISIONS.md`](DECISIONS.md) D-009, [`council-report-2026-06-09-reconcile.html`](council/council-report-2026-06-09-reconcile.html).

### D-010 — prd-creator drafts-and-presents from source material, never asks cold for what a brief covers

When cluster-0 source material substantively covers a later cluster, prd-creator **drafts that cluster's answer from the material and presents it for confirm/edit** (draft-and-present), and asks cold only where the material is thin. Silent absorption stays banned; this is the third behavior between it and ask-cold. Cluster 0 still runs first and still asks the source-material question. User-facing copy carries **no internal scaffolding**: no "cluster N", no mid-capture "D-NNN candidate" narration, no "(from cluster N)" provenance tags (`D-NNN` is legitimate only at the cluster-5 read-back and in the written PRD); and the skill makes **no temporal/provenance claims** about source material. Full entry: [`DECISIONS.md`](DECISIONS.md) D-010.

### D-013 — `/audit-context` skill declined; fix brownfield drift by hand

Do **not** build an `/audit-context` (drift-audit) skill. Brownfield context drift is handled by hand from the three pilot audit docs ([`docs/audits/`](audits/)); once a project is brought current, it's current. **Revisit only if** a change must sweep across *all* current projects at once *and* by-hand propagation becomes impractical — and even then scope a *targeted-propagation* tool to that need, not this drift auditor. Full entry: [`DECISIONS.md`](DECISIONS.md) D-013.

### D-017 — skill-frontmatter validation hook (commit-time gate)

`.claude/hooks/validate-skills.sh` — a PreToolUse `Bash` hook in `.claude/settings.json`, sibling to `block-env-commit` — blocks `git commit` when any `skills/*/SKILL.md` has malformed frontmatter (missing/empty `name`/`description`, no opening/closing `---` fence, leading tabs, `key:value` with no space) or a duplicate `name`. v1 is structural + cheap-syntactic (not a full YAML parse), **fails open** when no `SKILL.md` is found, validates the working tree, and gates the agent's commits only. First adopted crib of the hooks-as-gates direction. Full entry: [`DECISIONS.md`](DECISIONS.md) D-017.

### D-018 — Outside agents: no product writes, one measurement-ledger carve-out

Outside agent surfaces (Cowork, claude.ai, Codex, etc.) may not author or edit **product** — skills, code, docs, decisions — which go through the Claude-Code scope-gated workflow. **Exception:** a designated, append-only **measurement artifact** the agent owns may be written by that agent — currently only the furnace trial ledger (Cowork's `/plan-review` writes it). Category test: *product, or the agent's own measurement output?* Product banned, own-measurement-data permitted. Replaces the former blanket "agents are read-only here"; reverses the 2026-06-16 no-carve-out call. Full entry: [`DECISIONS.md`](DECISIONS.md) D-018.

### D-019 — `context-engineering-audit` not promoted to global; stays a design record

Do **not** symlink / promote the `context-engineering-audit` skill into `~/.claude/skills/`. It stays in-repo as the design record of the light-tier audit method (consistent with D-013's by-hand verdict) and lacks the pilots' field-0 "opted-into-the-standard?" gate. **If ever promoted, port that gate first** — without it an audit on a never-scaffolded project produces a harmful false-positive cascade. Full entry: [`DECISIONS.md`](DECISIONS.md) D-019.

### D-020 — `furnace-plan` hosted + versioned in this repo

`furnace-plan` lives at `skills/furnace-plan/`, symlinked into `~/.claude/skills/` like the chain skills (no longer a bare unbacked dir). Its `trial-ledger.md` is the durable cross-project furnace-learning ledger. D-018's category test partitions the two files: **`SKILL.md` = product** (edit only via the Claude-Code scope-gated workflow), **`trial-ledger.md` = measurement output** (the distinct reviewer may append; see D-018 for that write permission — not restated here). `SKILL.md` forces plan mode (`EnterPlanMode`) as its first action on invocation. Full entry: [`DECISIONS.md`](DECISIONS.md) D-020.

### D-034 — the two-load model governs `disable-model-invocation`

When authoring a skill, choose invocation mode by the two-load cut: a **model-invoked** skill's description sits in the context window every turn (context-load); a **user-invoked** skill (`disable-model-invocation: true`) costs nothing in-window but is findable only from the human's memory (cognitive-load). Set `disable-model-invocation: true` for narrow/heavyweight explicit-invoke tools whose always-in-window description would tax every turn (e.g. `furnace-plan`); leave it model-invoked when firing on trigger phrases without the user remembering the skill is the point (the chain skills). Full entry: [`DECISIONS.md`](DECISIONS.md) D-034.

### D-042 — `plan-review` hosted + versioned in this repo

The `plan-review` Cowork skill lives at `skills/plan-review/SKILL.md`, versioned in-repo (was unbacked-up, edited in place). Mirrors D-020's furnace-plan treatment with one difference: it's a **Cowork** skill, so it deploys by **ZIP-upload (Cowork → Settings → Skills)**, not a `~/.claude/skills/` symlink — and it is **not** symlinked onto the Claude Code surface (runs there only as a deliberately-spawned subagent, never inline). D-018 category test: **`SKILL.md` = product** (Claude-Code scope-gated edits only); it already writes the `trial-ledger.md` measurement file. The skill is host-agnostic (output returns to "the plan loop" by either path). Full entry: [`DECISIONS.md`](DECISIONS.md) D-042.

### D-043 — furnace-plan runs a blind in-session reviewer every pass; Cowork stays sole ledger writer

Every `/furnace-plan` pass, before `ExitPlanMode`, spawns **one read-only `Explore` subagent** that reviews the plan-mode plan file against the `plan-review` rubric (resolved via the skill's symlinked dir, `<real-dir>/../plan-review/SKILL.md`) under a **blind handoff** (prompt = plan path + acceptance criteria + rubric pointer only, never the author's reasoning), then the planner revises, appends a `## Subagent review log`, and verifies the repo tree is clean of product edits. Single pass; **reversible toggle** (a skipped pass = a calibration run). The `trial-ledger.md` gains a last-column `Reviewer` (`cowork` | `cc-subagent`; blank = `cowork`), a **per-reviewer** promotion rubric (read the furnace-preflight signal only from the raw-output reviewer, never Cowork's post-fix residual), and a pair-by-plan miss-rate tally. **Binding writer model: Cowork remains the sole ledger writer** — the cc-subagent never writes; Cowork transcribes its findings into `cc-subagent` rows. This **declines** D-042's flagged D-018 evolution (no "reviewer subagent may write"). Cowork is **not** replaced — still the authoritative reviewer + measurement oracle. Full entry: [`DECISIONS.md`](DECISIONS.md) D-043.

### D-044 — DSB adopt mode (copy, never transform); narrows D-008

`design-system-bootstrap` has an **adopt mode** alongside bootstrap. On a confirmed Claude Design bundle (cluster-0 detect, never silent) it makes three product-repo writes under the write guard: `cp` the rendered design into `design/reference/`, `cp` the bundle tokens into the product CSS **verbatim** (never through the scale-first `tokens.css` template — that is D-008's fidelity trap), and emit `.claude/rules/design-adoption.md` (import, don't rebuild). **Binding invariants:** adopt **copies, never authors** — it relocates the bundle's own components/tokens, never writing feature code; the bundle stays the design source of record; v1 enforces intra-app consistency + reference-staleness as **rule prose**, with the **mechanical hook deferred to v2**. Crosses DSB's "never feature components" line and rule 3's "context-engineering writes no design content" — sanctioned only by copy, logged here deliberately. Does not touch [D-009](DECISIONS.md)'s PRD-reconciliation stance. Full entry: [`DECISIONS.md`](DECISIONS.md) D-044.

## Cross-references

- Full append-only log with rationale: [`docs/DECISIONS.md`](DECISIONS.md).
- Decisions-log discipline: [`CLAUDE.md`](../CLAUDE.md) "Decisions log".
