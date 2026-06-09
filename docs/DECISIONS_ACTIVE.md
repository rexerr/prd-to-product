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

## Cross-references

- Full append-only log with rationale: [`docs/DECISIONS.md`](DECISIONS.md).
- Decisions-log discipline: [`CLAUDE.md`](../CLAUDE.md) "Decisions log".
