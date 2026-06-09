# HTML over Markdown — investigation brief

## Why this exists

Thariq Shihipar (Anthropic, Claude Code team) has been publishing a position: HTML is a strictly better output format than Markdown for many of the artifacts agents produce, and he has stopped using Markdown for most things. The thesis affects how `prd-creator` and `design-system-bootstrap` ship their outputs, but does NOT affect `context-engineering` (Claude Code parses `CLAUDE.md`/`AGENTS.md` as markdown — those must stay markdown).

This brief is the entry point for a future session that investigates the case in depth and decides what (if anything) to change. It deliberately does not pre-decide the answer.

## The thesis (Thariq's argument, summarized)

- **Information density.** HTML can carry tables, SVG diagrams, color, code with syntax highlighting, interactive controls, mobile-responsive layout, and absolute-positioned spatial data. Markdown cannot.
- **Visual clarity.** Markdown files over ~100 lines stop being read. HTML files of the same content remain navigable because of structural cues (tabs, illustrations, links).
- **Sharing.** HTML files open in any browser; you can upload to S3 and share a link. Markdown attaches as a file.
- **Two-way interaction.** HTML supports sliders, knobs, draggable cards, copy-as-prompt buttons. Markdown is read-only. Thariq's "playgrounds" pattern: build a throwaway HTML editor for the exact thing being designed, with an export button that produces text to paste back into Claude Code.
- **Data ingestion.** Claude Code can ingest filesystem, MCP, web, git history, etc., and assemble all that context into one HTML report. Hard to do well in markdown.
- **Joy.** Thariq names this directly. Making HTML feels more involved and invested. Worth flagging because the user has already mentioned similar feelings about over-automated outputs.

## What changes if we adopt this

### `prd-creator` (Business Process Automation skill)

Current: emits `PRD.md`. Reviewer reads markdown.

Possible: emit `PRD.html` with embedded SVG flow diagrams, tabbed sections (overview / users / architecture / open questions / decisions), maybe a sticky table-of-contents. Or emit BOTH — `PRD.md` for Claude Code to read at session start, `PRD.html` for humans.

Open questions to answer in the deeper session:

- What's the cost of emitting both? (Generator complexity, drift between the two.)
- If we emit only HTML, how does `context-engineering` reference it from `AGENTS.md`'s "Where to look" table? Claude Code can read HTML but Markdown is the default expectation.
- What does the rendered HTML actually look like in the wild? (Inspect Thariq's gallery.)

### `design-system-bootstrap` (Code Scaffolding skill)

Current: emits CSS tokens, three React components, a markdown design-system doc.

Possible: emit an HTML design-system reference (token swatches with live colors, component previews, typography scale rendered, motion samples). Thariq specifically mentions design as a strong HTML use case — "Claude Design is based on HTML because HTML is incredibly expressive at design."

Open questions:

- Does this replace the markdown doc, or supplement it?
- Does the HTML design system become the canonical source-of-truth Claude refers to during UI work, or is it just a human-facing artifact?

### `context-engineering` (NOT changing)

`CLAUDE.md` and `AGENTS.md` must stay markdown. Claude Code parses them as markdown at session start. This is non-negotiable.

The only tangential question for this skill: should the `docs/PRD.md` and `docs/ARCHITECTURE.md` it scaffolds *also* emit HTML versions, or stay markdown? Probably stays markdown — the skill's own principles say agents need to read these at session start, and markdown is what the agent expects.

## Sources to inspect in the next session

- Thariq's article: search for "Lessons from Building Claude Code: The Unreasonable Effectiveness of HTML" (already collected — see prior session's `Thariq Articles.rtfd` if available).
- Thariq's example gallery: <https://thariqs.github.io/html-effectiveness>
- Thariq's GitHub: the user mentioned having Thariq's GitHub where he explores the HTML concept in more detail. Pull that explicitly at session start.
- Thariq's playgrounds post: <https://x.com/trq212/status/2017024445244924382> (referenced in his article — confirm URL works).

## Failure modes to watch for

- **Adopting HTML for everything because it's cool.** Same drift risk we named for the skill itself. Each switch should answer "what mistake does this prevent?" Likely answer for `prd-creator` and `design-system-bootstrap`: humans don't read 200-line markdown docs but do read HTML. Real failure mode.
- **Emitting both formats and letting them drift.** If we emit `PRD.md` and `PRD.html`, one will be canonical and the other will rot. Pick which is canonical and treat the other as derived (regenerate, don't hand-edit).
- **Ignoring version control.** Thariq names this himself: HTML diffs are noisy. If we emit HTML to a repo, the diffs will be hard to review. Possible mitigations: emit HTML to a separate `dist/` or `artifacts/` location that's gitignored; or upload to S3 and reference the link.
- **Losing the agent's ability to read the file.** If the canonical is HTML and Claude is supposed to read it, confirm Claude Code parses HTML as gracefully as markdown. (It should — HTML is text — but the model may not be as fluent in extracting structure from it.)

## Out of scope for this brief

- Implementing HTML output for any skill. This is investigation only; the next session decides direction.
- Editing `context-engineering` to emit HTML versions of `CLAUDE.md`/`AGENTS.md`. Those stay markdown.
- General Markdown vs HTML debates outside the user's specific skills. Stay scoped to the skills that exist.

## Suggested first prompt for the investigation session

```
Read docs/html-over-markdown-brief.md as cluster-0 source material. Then:
1. Read Thariq's HTML example gallery at https://thariqs.github.io/html-effectiveness and his GitHub repo (I'll paste the URL).
2. For each of `prd-creator` and `design-system-bootstrap`, draft a recommendation: stay markdown, switch to HTML, or emit both. Tie each recommendation to a specific failure mode it prevents.
3. If the recommendation is "switch to HTML" or "emit both", outline what the skill change actually looks like — new templates, new intake questions, what's gitignored, what's canonical.
4. Surface the open questions you can't answer without the user's input.

Don't make any code changes yet. End with a written recommendation memo I can review before we touch anything.
```

## Status

- **Investigated 2026-06-09. Recommendation written; decision pending Rex.** Output memo: [`html-over-markdown-recommendation.md`](html-over-markdown-recommendation.md). Bottom line: DSB descriptive-doc HTML *supplement* is ripe and low-risk (canonical stays the CSS token file); `prd-creator` stays markdown canonical; `context-engineering` untouched. Nothing proceeds without a `D-NNN` per D-001.
- **Parallel-eligible.** Can run in its own session at any time. Independent of skill-refinement phases A–E.
- **Branch policy:** branch only if the investigation produces edits that overlap with main-branch work in `skills/context-engineering/`. Otherwise commit on `main` from a separate session.
