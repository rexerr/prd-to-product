# HTML over Markdown — recommendation memo

**Status: investigated, recommendation pending Rex's decision. No code/template work authorized.**
Companion to [`html-over-markdown-brief.md`](html-over-markdown-brief.md) (the entry point). This is the brief's requested "written recommendation memo to review before we touch anything." Date of investigation: 2026-06-09.

---

## What was investigated

Three primary sources, plus the rebuttal for the opposing case:

- Thariq's gallery — <https://thariqs.github.io/html-effectiveness> — 20 self-contained HTML artifacts.
- Thariq's repo — <https://github.com/ThariqS/html-effectiveness> — same 20 examples; README is demo-only (*"Not maintained and not accepting contributions"*).
- Thariq's Anthropic article — <https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html>.
- Rebuttal (opposing case) — <https://kurtis-redux.medium.com/the-unreasonable-ineffectiveness-of-html-5bd01ae1e879>.

## What the evidence actually shows

1. **The thesis is strongest for spatial/interactive content.** The gallery's wins are all 2-D or interactive: annotated diffs, call-graphs, design systems with live swatches, animation sandboxes with sliders. The honest framing line: *"diffs and call-graphs are spatial information; markdown flattens them."*
2. **The article's real driver is human attention, not correctness.** Thariq's stated motive is feeling *"in the loop"* / reading plans he'd otherwise skim. That is a human-review-moment benefit, not an agent-correctness one — which matters because it tells us *who* the HTML is for.
3. **Thariq's material is silent on repo discipline.** Neither the gallery nor the repo gives guidance on canonical-vs-derived, version-control/diff handling, or when *not* to use HTML. The burden of those decisions is entirely ours.
4. **The rebuttal names the costs that bite our skills specifically:** raw HTML source is hostile to read; HTML diffs are noisy → review collapses; markdown pastes natively into GitHub/Slack/Notion while HTML needs hosting.

## The crux for *our* skills

Our outputs are **repo artifacts that the agent reads at session start AND humans review.** That dual role is exactly where the rebuttal's failure modes land hardest. The decision therefore splits by *which artifact is canonical* (machine-read source of truth) vs *human-facing*.

---

## Recommendations

### `context-engineering` — no change (not in scope)
`CLAUDE.md` / `AGENTS.md` are parsed as markdown at session start. Non-negotiable, stays markdown. The scaffolded `docs/PRD.md` / `docs/ARCHITECTURE.md` also stay markdown — the agent reads them every session.

### `prd-creator` — stay markdown canonical; HTML only as an optional *derived* export
- **Why.** `PRD.md` is named in the scaffolded "Where to look" table as the source of truth the *agent* reads each session. Making HTML canonical breaks agent-readability and turns every PRD edit into a noisy, unreviewable diff — in a repo whose entire discipline is diff-review.
- **Failure HTML would prevent:** humans don't read 200-line markdown PRDs.
- **Failure HTML-as-canonical would cause:** agent loses its session-start source of truth; PRD diffs become unreviewable.
- **Verdict.** Markdown stays canonical. An optional rendered `PRD.html` is a low-priority "nice-to-have" — if ever built, it is explicitly **derived** (regenerate, never hand-edit) and gitignored. Not recommended as next work.

### `design-system-bootstrap` — HTML *supplement* is genuinely justified (the clean case)
- **Why it's clean.** DSB's canonical source of truth is already the **CSS token file** (machine-read) — not the markdown doc. The markdown design-system *doc* is purely descriptive/human-facing. Rendering that doc as HTML (live swatches, rendered type scale, component previews) hits the gallery's single strongest category *without touching the canonical agent-read artifact* — so the agent-readability and which-is-canonical objections do not apply.
- **Precedent.** Claude Design ships as HTML for exactly this reason.
- **Failure it prevents:** a markdown design doc nobody opens while a live swatch sheet would actually get used.
- **Residual cost:** diff-noise on the generated doc — mitigated by treating it as a generated artifact (regenerate, don't hand-edit), and deciding gitignore-vs-commit at build time.

---

## If we proceed — documented plan (NOT yet authorized)

### DSB HTML-supplement (the recommended-to-act item)
- New template: an HTML design-system reference alongside the existing markdown doc (or replacing it), rendering token swatches with live color, the type scale, spacing, and the three seed components.
- Canonical stays the CSS token file; the HTML is **derived/descriptive**, never the source of truth Claude reads during UI work.
- Decide at build: commit the HTML, or gitignore it and treat as a local artifact (diff-noise tradeoff).
- Likely a new intake question (emit HTML doc / markdown doc / both) gated like other optional surfaces.
- Must respect D-005/D-006 (non-destructive write guard) like every other generated artifact.

### prd-creator optional HTML export (low priority, only if asked)
- A derived `PRD.html` regenerated from the canonical `PRD.md`; gitignored; never hand-edited.
- Only worth building if the "humans don't read the markdown" failure is observed on a real project.

---

## Gating before any of this becomes action

- **D-001 requires a recorded decision.** No skill may emit HTML until a `D-NNN` entry authorizes it. This memo is the input to that decision, not the decision.
- **D-009 council threshold.** Changing the markdown-only invariant is explicitly named as a costly-and-hard-to-reverse fork. The narrow DSB-*doc*-supplement case (canonical stays CSS) may be reversible enough to skip a council; a broader `prd-creator` flip would not. Recommend a council if the scope grows beyond the DSB descriptive-doc.

## Open questions for Rex (deferred, not answered here)

1. For the DSB HTML doc: **commit it or gitignore it?** (diff-noise vs. shareability)
2. Does the DSB HTML doc **replace** the markdown doc or **supplement** it?
3. Is even the narrow DSB case worth a council under D-009, or is "canonical stays CSS" reversible enough to proceed on a solo `D-NNN`?

## Bottom line

Of the two skills in scope, only the **DSB descriptive-doc supplement** is ripe and low-risk. `prd-creator` stays markdown. `context-engineering` is untouched. Nothing proceeds without a `D-NNN` per D-001.
