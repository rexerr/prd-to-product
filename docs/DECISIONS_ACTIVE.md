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

## Cross-references

- Full append-only log with rationale: [`docs/DECISIONS.md`](DECISIONS.md).
- Decisions-log discipline: [`CLAUDE.md`](../CLAUDE.md) "Decisions log".
