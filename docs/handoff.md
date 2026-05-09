# Skill-build handoff

State of Rex's skill-building work. Pick up here in a fresh conversation by uploading this file plus the working brief for whichever skill is next.

## Where we are

**Context-engineering skill: shipped and validated.** Lives at `/Users/rexc/Sites/prd-to-product/context-engineering/`, symlinked into `~/.claude/skills/context-engineering/`. Validated through Pass 1.7 across two real-use runs (`the-council` forward test, `epost-assessment` retrospective), then through a third hand-off run against `prd-creator` output (`field-society-demo`, 2026-05-09). Stable. One Phase 2 patch surfaced and parked: PRD template needs to grow to eleven sections to match prd-creator output. See `context-engineering/NOTES.md` "PRD template gap" section.

**PRD-creator skill: shipped and validated.** Lives at `/Users/rexc/Sites/prd-to-product/prd-creator/`, symlinked into `~/.claude/skills/prd-creator/`. Built across two passes plus one Pass-2.1 patch. Validated end-to-end against `field-society-demo` (Field Society Parkway Planter), with hand-off to context-engineering also passing on the same project. Stable.

**Next scope: design-system-bootstrap skill.** Working brief at `/Users/rexc/Sites/prd-to-product/design-system-bootstrap-brief.md`. Build in a fresh session. Different discipline from the first two skills, more visual and asset-heavy.

## The three skills compose

The end-state workflow looks like this:

1. **PRD-creator** takes a working brief or rough idea, runs an interview-driven question flow, produces a structured PRD that downstream skills can consume.
2. **Context-engineering** takes the PRD plus answers a few workflow questions, produces the project's `AGENTS.md`, `.claude/rules/`, `docs/`, etc.
3. **Design-system-bootstrap** takes a brand book or design assets, produces token CSS plus seed components, integrates with the design rule context-engineering already scaffolded.

Each skill is single-purpose. Each skill's output is the next skill's input. Don't conflate them.

## Build environment

Claude Code, not Cowork. Reasons: multi-file work across templates, generators, examples; Rex is fluent in Claude Code; the skills themselves run in Claude Code. Cowork stays in scope only for the eventual "validate the skill on a fresh project" runs.

## Conventions for any skill we build

These held for context-engineering and should hold for PRD-creator and beyond.

- **Architecture:** SKILL.md (trigger + procedure) + principles.md (rationale, deferred-loaded) + templates/ (annotated stubs) + generator/ (intake.md, decisions.md, output-summary.md) + examples/ (transcripts plus output) + NOTES.md (internal regression tests, parked ideas).
- **Annotation conventions in templates:** `<!-- PARAMETERIZE: <field> -->`, `<!-- KEEP AS-IS: <reason> -->`, `<!-- OPTIONAL: <condition> -->`.
- **Question flow shape:** clustered (project basics, then domain-specific clusters), 2–4 options for branching questions, max 3 questions per call, summary after each cluster, explicit confirmation before writing files.
- **Cluster 0 always asks for source material first.** Don't silently absorb context.
- **Per-template inclusion table** in `decisions.md` driving which conditional templates emit.
- **Hard prohibition on writing product code.** Skills scaffold context, not product files. Reference paths in templates, never create files at those paths.
- **Examples must include three project shapes** (small as full output tree, medium and large as abbreviated transcripts).
- **Validation runs surface bugs, not paper validation.** Don't declare a skill done until it's run on a real project end-to-end.

## Style for any artifact we write

Rex's working style. Holds across all skills, briefs, plan files, retros.

- Sentence-case headers, H1/H2/H3 only.
- No em dashes.
- No Oxford commas.
- No colons in titles.
- AP style, Strunk and White.
- Imperatives, not principles. "Never use Sonnet in background jobs" is a rule. "Be thoughtful about model choice" is not.
- Every paragraph earns its tokens. If a sentence doesn't change behavior, cut it.
- Tone is direct but warm. Push back where you disagree with framing. Do not cheerlead.

## Three load-bearing patterns from context-engineering

Worth carrying as defaults to PRD-creator unless the new skill argues otherwise.

1. **Progressive disclosure.** SKILL.md stays small (under 500 words, readable in under a minute). principles.md loads only when the user asks why a pattern exists or the agent hits an edge case. Don't load the whole skill on every invocation.
2. **U-shape position-aware placement.** Critical constraints live at the beginning *and* the end of any file the agent reads cold. The middle is structure. Applies to AGENTS.md in scaffolded projects; should apply to PRD output too (executive summary at top, "what to do next" at bottom).
3. **Per-decision explicit ask, not bulk.** When the agent has multiple candidates that need a Y/N (which decisions promote to ACTIVE, which sections to include, etc.), ask one at a time with criteria stated. Don't batch. Don't decide silently and report.

## Files to read at session start

Everything is local under `/Users/rexc/Sites/prd-to-product/`. The new session reads them directly; nothing needs uploading. Tell the new session to read these files in order before doing anything else:

1. This handoff doc (`handoff.md`).
2. `design-system-bootstrap-brief.md` — the working brief that scopes the new skill.
3. `context-engineering/SKILL.md` and `prd-creator/SKILL.md` — architectural pattern references.
4. `context-engineering/principles.md` and `prd-creator/principles.md` — pattern references.

Optionally, if useful as raw input for validation:

- A real brand book PDF, Figma export, or palette image to test asset extraction against.
- `~/Sites/field-society-demo/docs/BRAND.md` (the voice file produced by prd-creator) as an example of voice content the design-system-bootstrap skill should NOT touch.

Do NOT read as Phase 0 audit: validation transcripts, the prd-creator templates folder (different discipline), this conversation's history. The brief and the SKILL/principles files name what to read; reading is in service of building, not analysis.

## What to skip in the new session

- Do not redesign the SKILL/principles/generator/examples architecture. It works across two skills now. Use it.
- Do not relitigate style conventions. Listed above.
- Do not start by auditing existing brand books or design specs as a Phase 0. The brief names what to read; reading is in service of building, not analysis.
- Do not generate product code. Like the first two skills, this one writes a small set of files at named paths and stops.
- Do not retrofit voice or brand-text content. That belongs to prd-creator's BRAND.md. This skill is visual only.

## What's parked across all the skills

- Multi-stack support beyond Vercel + Next.js (context-engineering Phase 2).
- Multi-developer / branch-policy patterns (context-engineering Phase 2).
- Frontmatter schema for `.claude/rules/*.md` (context-engineering Phase 2).
- Audience-tagged docs split (context-engineering Phase 2).
- Eval / test-harness rule file (context-engineering Phase 2).
- PRD template growth from seven to eleven sections (context-engineering Phase 2; surfaced by prd-creator hand-off).
- Resume logic for any generator (revisit if a real run gets abandoned partway).
- PRD-review or critique skill (parked from prd-creator; possible separate skill later).
