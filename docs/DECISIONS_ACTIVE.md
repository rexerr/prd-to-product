<!-- Reconciled against DECISIONS.md through D-034 · 2026-06-18. If DECISIONS.md carries higher-numbered decisions not yet evaluated for this view, this marker is stale — re-reconcile and bump it. Curated subset, NOT a completeness claim: not every D-NNN ≤ D-034 appears here (many are deliberately skipped as visible-by-reading; D-031/D-032/D-033 evaluated, not mirrored — visible by reading the furnace-plan/prd-creator skill files; D-034 mirrored below). Bump this line whenever a new decision is evaluated for mirroring, mirrored or not. -->

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

### D-008 — No adopt-automation for Claude Design bundles

The kit builds **no** adopt-skill, **no** DSB adopt-mode, and **no** token-adopt command for Claude Design handoff bundles. Bundles stay authoritative (recreate per their own README); to land tokens in a real product, do a one-time manual **`cp`** of token values into *that product's* repo — a product-side action, not a kit change. Knowledge is recorded in [`design-handoff-adoption.md`](design-handoff-adoption.md) (observation log + bundle ledger, not a tool). If an adopt path is ever built it defaults to CSS-vars, never Tailwind. Revisit only on a **2nd real bundle** (Rule of Two). Full entry: [`DECISIONS.md`](DECISIONS.md) D-008.

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

## Cross-references

- Full append-only log with rationale: [`docs/DECISIONS.md`](DECISIONS.md).
- Decisions-log discipline: [`CLAUDE.md`](../CLAUDE.md) "Decisions log".
