# Context engineering principles

The structural conventions this skill scaffolds, and the rationale behind them. Read this when you want to understand why a template is shaped the way it is, or when you hit an edge case the templates do not cover. Do not read it on every skill invocation.

## What this skill is for

A new AI-assisted coding project starts in a state where the agent does not know what the project is, what conventions apply, what is canonical when docs disagree, or what rules are non-negotiable. Every session re-derives this from scratch. The fix is a small set of files at known paths that the agent reads at session start and on touch. This skill scaffolds those files. It does not write product content. It writes the shape that holds the content.

### Progressive disclosure

The skill, the templates, and the projects scaffolded from them all follow the same loading discipline. At session start, only the smallest set of orientation files load: `AGENTS.md`, `ROADMAP.md`, the most recent retro, and (if present) `PARKING_LOT.md`. Path-scoped rules under `.claude/rules/` load only when matching files are touched. Reference docs (`PRD.md`, `ARCHITECTURE.md`, canonical workflow docs) load when the agent is about to act in their domain. This skill's `principles.md` follows the same rule: `SKILL.md` defers it to "when asked why a pattern exists or you hit an edge case." Up-front context stays small. Detail loads on demand.

### Position-aware placement

The U-shaped attention curve penalizes information placed in the middle of long context. Critical constraints belong at the beginning *and* the end of any file the agent reads cold. `AGENTS.md` carries a brief "primary constraints" anchor near the top (right after the project description) and the full "Before you respond" recency block at the bottom. Both ends; the middle is structure and orientation.

## The core structure

Four patterns hold up the rest. If a project skips any of them, the rest of the structure leaks.

### Thin-pointer pair

`AGENTS.md` is the canonical entry-point file. `CLAUDE.md` is a one-line file that imports it: `@AGENTS.md`. Codex and other agent tools read `AGENTS.md` directly. Claude Code reads it via `CLAUDE.md`. One file is the source of truth. The other is a pointer plus, at most, one tool-specific override paragraph.

The default direction is AGENTS canonical because AGENTS is the agent-agnostic name. The other direction works but adds friction when adding a second tool to the workflow.

### Always-on vs path-scoped split

Rules that apply to every session live in `AGENTS.md` directly or in always-on files under `.claude/rules/` (no `paths:` frontmatter). Rules that apply only when certain files are touched live in path-scoped files under `.claude/rules/` with `paths:` frontmatter. Claude Code honors `paths:` automatically. Codex does not. The AGENTS.md "Path-scoped rules" section names this and tells Codex to read every rule file at session start and mentally check matches.

Use the modular split when the rule set is large enough that a flat `CLAUDE.md` becomes hard to scan. Use the flat shape (everything in `CLAUDE.md`) when the project is small enough to fit in one file without losing structure.

### Canonical-source-of-truth on conflict

Documentation drifts. When two docs disagree, the agent needs a rule that picks the winner without escalating to a human. The two working forms:

- **Single named tiebreaker doc.** Useful when one doc covers a single domain (workflow behavior, scoring engine, etc.) that drives the rest. Name it explicitly in `AGENTS.md`: "If documents conflict on behavior, follow `docs/X.md` as source of truth."
- **Touched-area table.** Useful when the project has several distinct domains. A small table in `AGENTS.md` mapping "touching X" to "conflict source of truth Y."

Both forms are valid. The skill defaults to the table because it scales.

### Docs vs rules separation

`docs/` describes the project for the agent and for humans. `.claude/rules/` (or rule sections of `CLAUDE.md`) tell the agent what to do and not do. Docs answer "what is this." Rules answer "how do I behave." Mixing the two produces 800-line CLAUDE.md files that nobody reads.

## The always-on patterns

Each pattern below has a short rule. The corresponding template carries the full text.

- **Hard scope limits.** Bug fix or small tweak ≤ 3 files and ≤ 50 lines. Feature work ≤ 300 lines per session. File size ≤ 500 lines before extraction. Why: makes "you went over scope" checkable, not a vibes call.
- **Scope check before coding.** State files, intended changes, scope estimate. Wait for confirmation if the plan touches more than two files.
- **Verification before claiming done.** UI changes need a running dev server and human visual confirmation. Logic changes need shown output. "The code looks correct" is not enough.
- **Commit gate.** Do not commit until the human confirms the change visually for UI work, or confirms the verification output for logic work.
- **Push protocol.** Paste the commit URL, say "waiting for deploy," wait for human production confirmation. Do not declare done on Vercel "Ready" alone. CDN and browser cache delay visible-on-production by a minute or two.
- **Reproduce before fixing.** For any bug, write the failing reproduction first. Then the fix. Then verify.
- **Server-only AI calls.** Never call the AI layer from a client component. Always route through an API route. Why: keeps API keys server-side and centralizes prompt logic.
- **Session retros.** End every non-trivial session with `docs/retros/YYYY-MM-DD-topic.md`. Read the most recent retro before starting a new session.
- **Session-start command.** A `.claude/commands/session-start.md` slash command that reads the entry-point file, the roadmap, and the most recent retro and reports orientation. Replaces re-explaining context every session.
- **Direct-on-main, no branches, no worktrees.** Single-developer pre-launch projects do not benefit from branch overhead. Worktrees break visual confirmation because the dev server cannot see them.
- **No deploy CLI.** Pushes to `main` deploy automatically via the deploy target's GitHub integration. Do not run the CLI. It creates parallel deployment paths.

## The conditional patterns

Use these when the project's shape calls for them.

- **Modular `.claude/rules/`.** Use when the rule set is large enough that a flat `CLAUDE.md` is hard to scan, or when path-scoped loading would meaningfully reduce always-loaded context.
- **`docs/PARKING_LOT.md`.** A place for items deferred mid-session. Read at session start alongside the most recent retro.
- **`docs/DECISIONS_ACTIVE.md`.** A curated subset of `docs/DECISIONS.md` listing only currently-binding constraints not visible from reading code alone. Promotion criteria stated at the top of the file.
- **Voice-and-tone rule.** Use when the project produces user-facing copy, especially AI-generated copy. Path-scoped to AI generation files and UI files.
- **Design system rule.** Use when the project has a token file (CSS custom properties or equivalent) and a "no hardcoded values" enforcement target.
- **Design heuristics rule.** Use when the project applies named UX laws (Fitts, Hick, Miller, Nielsen) to specific in-app decisions.
- **`.codex/config.toml` and `.agents/skills/`.** Use when Codex sessions are part of the workflow and per-repo skills are worth maintaining.
- **`FUTURE.md`.** Use for V2-and-beyond items that would otherwise pollute `ROADMAP.md`.

## The recency safeguard

The bottom of `AGENTS.md` carries a "Before you respond" block listing the load-bearing constraints that must not be lost mid-session. Long sessions push the top of the file out of attention. The safeguard pulls the most important rules to the bottom on purpose, so the last thing the agent reads before responding is what it cannot violate.

The block is short. Five to seven imperatives. Each one has a one-line rationale or a pointer to the rule file that owns it. Items belong here only if violating them would damage product, lose work, or burn a stakeholder.

## The vocabulary lock pattern

When a project uses domain-specific names (output types, indicator types, field names) that have evolved, list both the canonical names and the old values that must not be used. Pattern:

> Canonical: `INTERNAL`, `NEWSLETTER`, `BLOG`, `LINK`, `ALERT`. Do not use old values: `internal-brief`, `customer-newsletter`, `weekly-news-roundup`, `news-update`, `breaking-alert`.

The forbidden list is what makes the rule work. Without it, the agent has no signal that the alternatives are wrong, only that the canonical names are right.

## Conventions for writing rules

Rules in `.claude/rules/` and in `AGENTS.md` should follow these conventions.

- **Every paragraph earns its tokens.** Before keeping a sentence in a rule file, ask: does the agent actually need this, or am I writing for a human reader who has never seen the project? Cut anything the agent already knows or can derive. Rule files are not documentation; they are constraints. If a paragraph does not change behavior, it is bloat.
- **Imperatives, not principles.** "Never use Sonnet in background jobs" is a rule. "Be thoughtful about model choice" is not. If the rule cannot be checked, rewrite it until it can.
- **Specific, not generic.** "≤ 3 files, ≤ 50 lines for bug fixes" beats "keep changes small."
- **Cite the failure mode.** Every rule should be defensible against "why does this exist." Carry the answer in the file or in a separate why-block.
- **Cross-reference at the bottom.** Every rule and canonical doc ends with a list of related files. Without this, the rule graph fragments silently as the project grows.
- **One rule per concern.** Do not write a rule that does two things. Split.

## What the generator parameterizes on

The generator asks the user about these. Defaults exist for a few; most must be answered.

- Project name and GitHub repo URL.
- Visual confirmer name (the human who confirms UI changes).
- AI surface count (zero, one, or several).
- Whether the project has a design system with a token file.
- Whether the project produces user-facing copy that needs a voice-and-tone rule.
- Whether Codex sessions are part of the workflow.
- Whether `PARKING_LOT.md`, `DECISIONS_ACTIVE.md`, and `FUTURE.md` should be included.
- Domain vocabulary, if any, for the vocabulary lock pattern.

What it does not ask about: deploy target (Vercel), framework (Next.js App Router), branch policy (direct-on-main), retro location (`docs/retros/`). These are hardcoded in V1.
