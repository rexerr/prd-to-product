## Retro — 2026-05-11 — Docs audit and validation-project setup

Second session of the day, after the build-defaults pilot item 1 ship that morning ([prior retro](2026-05-11-build-defaults-pilot-item-1.md)). This session ran a docs audit on the repo, collapsed four work-tracking surfaces into a single `BACKLOG.md`, archived seven historical design docs, and set up the Squirreled validation project — a real deployable web app whose build run will test the pilot, the new BACKLOG shape, and the prd-creator → context-engineering composition simultaneously.

## What landed

Five commits, all on `main`, all pushed.

| Commit | Change |
|---|---|
| [`afb2964`](https://github.com/rexerr/prd-to-product/commit/afb2964) | Docs audit: consolidate four work-tracking surfaces into `BACKLOG.md`. Deletes `ROADMAP.md`, `docs/PARKING_LOT.md`, `docs/FUTURE.md`, and the PRD's "Deferred capabilities" pointer. Also deletes seven historical design docs (`findings.md`, three `phase-*` files at root, `docs/handoff.md`, `docs/prd-creator-brief.md`, `docs/design-system-bootstrap-brief.md`). Patches references in `CLAUDE.md`, `README.md`, `ARCHITECTURE.md`, `PRD.md`, `DECISIONS.md`, `build-defaults-brief.md`, and the session-start slash command. Net: ~1,100 lines out, ~50 in. |
| [`01d7657`](https://github.com/rexerr/prd-to-product/commit/01d7657) | Four product briefs in `docs/product-briefs/`: `taste-builder.md` (the validation project), `ai-research-synthesizer.md`, `anti-generic-machine.md`, `design-process-recorder.md`. BACKLOG.md gains three entries: Squirreled as In progress validation, skill consolidation (gated on the retro), and a red-team sibling-skill backlog item. |
| [`8ed3caf`](https://github.com/rexerr/prd-to-product/commit/8ed3caf) | Taste Builder brief absorbs the client-work mining path and the Taste Journal naming candidate after user-shared assessment from another Claude conversation. Personal-mode vs client-mode friction mismatch added as a real risk. |
| [`25c312f`](https://github.com/rexerr/prd-to-product/commit/25c312f) | Naming shortlist gains Squirreled plus the *register-split* framing — personal-practice names (Journal, Squirreled, Reps) vs client-work names (Throughline, Atelier, Refinery). |
| [`1aa8199`](https://github.com/rexerr/prd-to-product/commit/1aa8199) | Adopts Squirreled as the working name for the validation project. Brief title and BACKLOG entry updated. Filename preserved as `taste-builder.md` since the product name may shift during the prd-creator interview. |

Total net diff: 5 files modified plus 6 new files, ~280 lines added, ~700 deleted, ~420 line reduction. All docs; zero code.

## What was rejected vs. what shipped

| Topic | Considered | Shipped | Why |
|---|---|---|---|
| Historical docs | Archive to `docs/archive/` | Delete outright | Git preserves history; `docs/archive/` clutters globs and consumes attention. User named token usage as a concern. |
| `ROADMAP.md` | Keep as stub pointer to BACKLOG | Delete entirely | A pointer file with no content is rule proliferation. CLAUDE.md "Where to look" gains a `BACKLOG.md` row instead. |
| Red-team capability | Feature inside prd-creator | Sibling skill | Capability is generic across documents. Each existing skill should stay single-purpose. Composes by invocation, not coupling. |
| Validation project shape | Another Claude skill | Deployable web app | A skill validation would skip Phase 1 deploy-shell entirely (same `stack=other, deploy_target=none` shape as this repo). Defeats the test purpose. |
| Taste Builder framing | "Better reference library" + tagging + search | Training loop + forced interpretation + taste profile + project boards | User shared an external assessment that reframed the product. Library is a side effect; the work is reflection. Storage-shaped V1 misses the differentiator. |
| Naming | Pick a winner mid-session | Defer to PRD interview, capture register split | Premature lock-in. Register split (personal-practice vs client-work) is the useful finding; the specific name should fall out of which positioning is load-bearing. |

## What surfaced

Things I didn't predict before starting.

1. **The repo's own dog-food experience is evidence the skill emits too many work-tracking surfaces.** The four-file split (ROADMAP / PARKING_LOT / FUTURE / PRD-deferred) wasn't malicious — each surface had a good local reason. But the bloat was structural: phased lifecycle artifacts that outlived their phase. The fix we just made *here* now belongs in the skill itself for scaffolded projects (captured in BACKLOG as the "skill consolidation" In progress entry, gated on Squirreled retro). The first real-instance evidence is *this session*, not a future one.

2. **The 20-idea brainstorm filter was inverted from what validation needs.** The other Claude ranked ideas by "easiest to prototype in Claude" — which means "easiest as a skill." That's the *opposite* of what the validation requires (a deployed web app exercising the deploy-shell pilot). Worth remembering: when external brainstorms hand back a "easiest" ranking, check what "easy" was optimizing for.

3. **The Taste Builder reframe was structural, not cosmetic.** The brief I wrote first had the *diagnosis* right ("saves become a graveyard, learning doesn't compound") but proposed a *storage-shaped solution* (auto-tag + library + search). The assessment caught that the diagnosis pointed at a different solution: a forcing function on the moment of capture (forced interpretation) that turns passive collection into active observation. The library is the side effect, not the product. This kind of reframe is exactly the work prd-creator's interview should do — and that reinforces that the brief is a *seed*, not a finished design.

4. **Client-work mining is the load-bearing differentiator for stickiness.** Personal-practice tools get abandoned in week 3 (self-improvement is hard to sustain). Tools that are useful on a Tuesday afternoon when you're starting a client kickoff don't. The dual positioning — personal corpus you build + client slices you mine — is what makes Squirreled potentially sticky for working designers. But it creates real UX tension (interpretation friction has to differ between modes), which is the right thing for prd-creator to pull on.

5. **Naming names split along two registers.** Personal-practice register (Journal, Squirreled, Reps — modest, behavior-honest) and client-work register (Throughline, Atelier, Refinery — professional, working-tool). Almost no name fits both registers cleanly. The framework is more useful than any individual name choice; it tells you the naming question is downstream of the positioning question.

## Scope

5 commits, ~420-line net reduction across the session, all docs. Each commit was atomic and reviewable. No code changes. No skill changes — the changes to the *skill* (scaffolding a `BACKLOG.md` in new projects, dropping `PARKING_LOT.md.template` and `FUTURE.md.template`) are queued in BACKLOG as the next In progress item, gated on Squirreled retro per continuous-mode discipline.

Inside scope limits throughout. No hard-limit violations.

## Verification

- After each docs-audit edit, grepped active docs (excluding `skills/` and `docs/retros/`) for refs to deleted files. Zero surviving refs after the final patch.
- All five commits cleanly land on `origin/main`. No force pushes.
- `BACKLOG.md` and `CLAUDE.md` session-start required-reading list cross-checked for consistency.
- The Taste Builder brief was reviewed against the external assessment at three points: original draft, post-reframe, post-client-work-angle. Each revision survives the next.
- Squirreled name lands consistently across the brief, the BACKLOG entry, and (by reference) the project directory the user will create next.

## Open questions to watch on the validation run

When the Squirreled project session kicks off, the things worth watching are:

- **Does the brief seed prd-creator well?** Are the open questions in the brief the right shape for the interview to pull on, or do they over-determine answers?
- **Does Phase 1 = deploy-shell get treated as real work?** Or does the agent improvise around it / skip ahead to feature code?
- **Does the scaffolded ROADMAP/BACKLOG split feel right?** Or does the new shape itself create friction?
- **Does the dual personal/client positioning survive the interview?** Or does one mode collapse the other under interview pressure?
- **What's the friction calibration that emerges for interpretation prompts?** Personal mode wants depth; client mode wants speed. The compromise design will be informative.

## Decisions worth noting (not big enough for D-005 yet)

- **One work-not-done surface per project, not four.** Validated in this repo; pending validation in scaffolded projects. Will become D-005 if the skill consolidation ships.
- **Red-team as sibling skill, not feature.** Architectural call captured in BACKLOG; not yet binding.
- **Working names are operational, not committed.** Squirreled is the project folder name; the final product name is a PRD-interview question.

Nothing promoted to `DECISIONS.md` this session. The work was cleanup and setup, not new policy.

## Next session

New session in `~/Sites/squirreled/` (or wherever the user creates the project folder).

1. Invoke `prd-creator` in the fresh project directory. Hand it the brief at `~/Sites/prd-to-product/docs/product-briefs/taste-builder.md` as cluster-0 source material.
2. Walk the interview. Resolve as many open questions as possible; defer the ones that aren't ready.
3. Produce `docs/PRD.md` in the Squirreled project.
4. Invoke `context-engineering` with the new PRD. Scaffold AGENTS, CLAUDE, .claude/rules, BACKLOG, ROADMAP. Phase 1 should be deploy-shell per the build-defaults pilot.
5. Start Phase 1 in the same session if there's room. Target a live URL by end of week 1.
6. Retro before any Phase 2 work.

That retro is the next evidence-input for promoting (or modifying) the skill consolidation item in BACKLOG. Don't ship skill changes before it lands.
