# Skill internal notes

Notes for whoever maintains this skill. Not part of the user-facing flow.

## Regression test definition (Phase 1 success criterion 3)

The PRD requires the generator to produce usable output for three project shapes (small, medium, large). The Large shape uses feed (`epost-intelligence-feed`) as its reference.

**Important:** the test is not "the generator reproduces feed exactly." Findings.md flagged feed's structure as the less-evolved of the two ePost repos in two specific places. The generator should produce feed's structure with these corrections applied:

1. **AGENTS canonical, not CLAUDE canonical.** Feed has the right direction already (`CLAUDE.md` is `@AGENTS.md`). The skill default agrees. No action needed for the Large case, but for any project the test is "AGENTS canonical."
2. **DECISIONS.md plus DECISIONS_ACTIVE.md split.** Feed has only `decisions-history.md` and pushes binding constraints into `.claude/rules/`. The skill default uses the assessment shape (full log + curated active view). Generator output for the Large case should include `docs/DECISIONS_ACTIVE.md`, not push everything into rule files.

**Other deltas from feed that are intentional, not corrections:**

- Modular `.claude/rules/` directory: keep as-is for Large.
- Multiple AI surface rules: keep as-is for Large (Large case has 3 AI surfaces).
- `BACKLOG.md` with a `Later / V2` section: keep as-is for Large (`backlog_include_v2 == true`).
- `.codex/config.toml` and `.agents/skills/`: include for Large since Codex is in active use.

**On flat-vs-modular for assessment-shaped projects:** earlier framing said "assessment is canonical flat shape." Removed after the `epost-assessment` retrospective validation revealed assessment's own PRD describes a token-system-with-linter design, which crosses the modular threshold. The criterion in `decisions.md` correctly reads from the PRD's claims, so a project whose PRD describes a token system will land modular even if the current code doesn't have one yet. That's the right behavior — the PRD is forward-looking, the rules describe the target state.

The two corrections (AGENTS canonical, `DECISIONS_ACTIVE.md` present) remain the load-bearing regression test. Flat-vs-modular is a function of the PRD's claims, not a fixed expectation per project.

## Parked ideas

### `/session-end` slash command

Considered during Pass 1, pulled back. The PRD names `session-start` only. The close-out routine is already specified inside `session-discipline.md.template` (the "When the visual confirmer says 'end session', run the close-out" paragraph), so the behavior exists without the slash command. Adding `/session-end` is a Phase 2 speculation. If it earns its keep through real use, the content would be roughly:

```
Run the close-out for this session in order:

1. Check off completed Build-plan tasks in BACKLOG.md; update its In progress / Backlog lists (resolved items move to a retro).
2. Write a retro to docs/retros/YYYY-MM-DD-topic.md following the template in docs/retros/README.md.
3. Run `npm run check`. Fix any errors before committing.
4. Stage doc updates explicitly. Commit with a clear message.
5. Do not push unless I asked you to push earlier in the session.

When done, paste the commit SHA and summarize what was completed and what is next.
```

Add it as a template if and when the slash-command shortcut shows real value over the natural-language "end session" trigger.

### Flat template missing vocabulary lock

Noticed during Pass 1.6: `claude-rules-flat-CLAUDE.md.template` has no vocabulary lock section. The recency block stops at item 6 (AI client-component) with no item 7. A project running flat shape that has domain vocabulary (assessment-shape with Pardot field names, market keys) currently has nowhere to put a vocabulary lock. The modular AGENTS template handles this via the conditional `vocabulary_lock_section`. Add the same section to the flat template, plus item 7 in the recency block, when the project has vocabulary lock content.

Park for now because the validation case (the-council) ran modular and didn't surface this. Surface again on the next flat-shape validation run.

### Future skill: design-system-bootstrap (parked)

Validation runs (the-council, epost-assessment retrospective) both surfaced the same agent behavior: when a brand book or design spec is provided as source material, the agent improvises a `tokens.css` file. This is out of scope for context engineering and now explicitly prohibited in `decisions.md` "What the generator never writes."

The capability itself is useful, just not here. Spec for the future skill:

- **Name:** `design-system-bootstrap` (working title).
- **Inputs:** brand book PDF, color palette image, typography spec, or similar design assets.
- **Outputs:** `tokens.css` (or equivalent), seed component examples (Button, Card, Input), updates to an existing `design-system.md` rule to reflect what was generated.
- **Trigger:** "bootstrap design system from brand book," "generate tokens from brand assets."
- **Integration:** runs after `context-engineering` on a new project (which scaffolds the rule that references the token file path), or standalone on an existing project that doesn't have a token system yet.
- **Scope discipline:** writes only files under `app/design-system/` (or wherever the design rule names), not arbitrary product code.

**Build order:** `context-engineering` (current, in real use) → `prd-creator` (next, parked separately) → `design-system-bootstrap` (after prd-creator). Don't start until both upstream skills have shipped and been validated.

## PRD template gap surfaced by prd-creator hand-off

PRD-creator (shipped 2026-05-09) emits a PRD with eleven sections: product summary, target users, core problem, main workflow, version 1 scope, out of scope, deferred capabilities, architecture and stack, decisions already made, open questions, success criteria (plus optional brand and voice and supporting documents). This skill's PRD template carries seven of those.

During the field-society-demo validation run, the skill correctly detected the collision and asked the user before overwriting, then proposed preserving the prd-creator output verbatim with a four-line cross-references append. Right call. But the long-term fix is to update this skill's PRD template to the eleven-section shape so the collision does not recur on future runs.

The cluster 6 extraction logic in `generator/intake.md` already pulls from "version 1 scope," "decisions already made," "open questions," and "success criteria" if the source PRD has them. The template just needs to match. Phase 2 patch.

## Open questions for Phase 2

These came up during Phase 1 build. Park them; do not address until Phase 1 ships and is used on a real project.

- **Frontmatter schema for `.claude/rules/*.md`.** Currently just `paths:`. Could grow (last_reviewed, supersedes, etc.). Hold until pain shows up.
- **Multi-developer / branch-policy patterns.** V1 hardcodes single-developer direct-on-main. Real-world projects with collaborators need different rules. Phase 2 if validation demands.
- **Stack diversification.** V1 hardcodes Next.js + Vercel. Other stacks (Remix, plain Node, Python) would need their own templates. Phase 2.
- **Resume logic for the generator.** Currently single-shot. If users abandon partway, they start over. Phase 2 if it turns out to be needed.
- **Audience-tagged docs.** D-038 in assessment names the agent-doc vs human-doc distinction. The skill doesn't enforce it at the filesystem level. Hold for Phase 2.

## Style notes for any update to this skill

- Sentence-case headers, H1/H2/H3 only.
- No em dashes.
- No Oxford commas.
- Imperatives, not principles, in rule content.
- AP style, Strunk and White.
- No colons in titles.

## Templates quick reference

```
templates/
├── AGENTS.md.template                    Entry-point file, modular shape (default)
├── CLAUDE.md.template                    Thin pointer (one line: @AGENTS.md)
├── claude-rules-flat-AGENTS.md.template  Alternative for small projects, AGENTS canonical (rules inline + Codex section)
├── claude-rules-flat-CLAUDE.md.template  Pairs with the flat AGENTS; thin pointer (one line: @AGENTS.md)
├── codex-config.toml.template            Optional, when uses_codex == true
├── agents-skills-README.md.template      Optional, when uses_codex && has_repo_skills
├── claude-rules-modular/
│   ├── git-and-deploy.md.template        Always-on
│   ├── session-discipline.md.template    Always-on
│   ├── product-rules.md.template         Always-on, optional
│   ├── voice-and-tone.md.template        Path-scoped, optional
│   ├── design-system.md.template         Path-scoped, optional
│   ├── design-heuristics.md.template     Path-scoped, optional
│   ├── ai-shared.md.template             Path-scoped, conditional on AI surfaces
│   └── ai-surface-stub.md.template       Instantiated once per AI surface the user names
├── docs/
│   ├── PRD.md.template                   Required
│   ├── ARCHITECTURE.md.template          Required
│   ├── BACKLOG.md.template               Required (build plan + in-progress + backlog + open decisions; optional Later/V2 section)
│   ├── DECISIONS.md.template             Required
│   ├── DECISIONS_ACTIVE.md.template      Optional (recommended)
│   └── retros/README.md.template         Required
└── claude-commands/
    └── session-start.md.template         Required
```
