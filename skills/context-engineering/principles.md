# Context engineering principles

The structural conventions this skill scaffolds, and the rationale behind them. Read this when you want to understand why a template is shaped the way it is, or when you hit an edge case the templates do not cover. Do not read it on every skill invocation.

## What this skill is for

A new AI-assisted coding project starts in a state where the agent does not know what the project is, what conventions apply, what is canonical when docs disagree, or what rules are non-negotiable. Every session re-derives this from scratch. The fix is a small set of files at known paths that the agent reads at session start and on touch. This skill scaffolds those files. It does not write product content. It writes the shape that holds the content.

## What this skill bets on

Two pieces of empirical context for anyone reading this:

The "Evaluating AGENTS.md" arXiv study (2025) found LLM-generated context files reduce autonomous-task success by 0.5–2% and increase cost 20–23%. Human-written files improved success by 4% on average — but did not help Claude Code specifically. The study was Python-only and measured single-shot SWE-bench-style resolution, with substantial overlap between context files and existing README/docs.

This skill optimizes for a different target: human-in-the-loop project workflow where the dominant failure mode is the agent claiming false success. The session-discipline rules (scope check, visual confirmation, retro) are not optimizing for benchmark resolution rate; they are optimizing against hallucinated done-ness. That is a legitimate divergence from the paper's metric, but it is a divergence — restate it when re-evaluating.

The one finding from that paper this skill follows directly: explicit tool commands get used reliably and almost never get used when absent. That is why the AGENTS.md template carries an explicit Commands section. The redundancy guards in the generator (drop "What this project is" when PRD.md exists; pointer to ARCHITECTURE.md instead of restating layout) are also paper-aligned: they prevent the duplication that the paper showed accounts for most of the negative cost finding.

### Relationship to Claude Code's auto memory

Claude Code (v2.1.59+) has a separate auto-memory system that runs alongside whatever this skill scaffolds. It stores agent-discovered notes (build commands, debugging insights, corrections) at `~/.claude/projects/<project>/memory/`, machine-local, on by default. The two systems are complementary: this skill produces the human-written, version-controlled side (CLAUDE.md, AGENTS.md, `.claude/rules/`); auto memory captures what Claude learns by doing.

The practical implication: do not put learned-correction-style content into CLAUDE.md. Things like "this codebase uses pnpm not npm" or "the test runner needs a local Redis instance" belong in auto memory — Claude will write them itself when they come up. CLAUDE.md is for instructions the user *decides in advance* the agent should follow; auto memory is for things discovered mid-session. Mixing the two bloats CLAUDE.md and weakens the signal.

Auto memory is per-machine and per-git-repo (shared across worktrees of the same repo). It is not in scope for this skill to manage; the user does not need to scaffold or configure anything. See `https://code.claude.com/docs/en/memory` for the upstream reference.

### Progressive disclosure

The skill, the templates, and the projects scaffolded from them all follow the same loading discipline. At session start, only the smallest set of orientation files load: `AGENTS.md`, `ROADMAP.md`, the most recent retro, and (if present) `PARKING_LOT.md`. Path-scoped rules under `.claude/rules/` load only when matching files are touched. Reference docs (`PRD.md`, `ARCHITECTURE.md`, canonical workflow docs) load when the agent is about to act in their domain. This skill's `principles.md` follows the same rule: `SKILL.md` defers it to "when asked why a pattern exists or you hit an edge case." Up-front context stays small. Detail loads on demand.

### Position-aware placement

The U-shaped attention curve penalizes information placed in the middle of long context. Critical constraints belong at the beginning *and* the end of any file the agent reads cold. `AGENTS.md` carries a brief "primary constraints" anchor near the top (right after the project description) and the full "Before you respond" recency block at the bottom. Both ends; the middle is structure and orientation.

The recency block is intentionally short — two always-on items (hard scope limits; visual confirmation gates the commit), plus optional items 3 and 4 for AI-surface and vocabulary-lock projects. Items belong here only if violating them would damage product, lose work, or burn a stakeholder. Other rules (direct-on-main, no deploy CLI, reproduce-before-fixing) live in the body of the file and are not duplicated in the recency block. Duplication dilutes the signal.

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
- **Read before you write.** Read the file's exports, immediate callers, and obvious shared utilities before adding code. Why: prevents the failure mode where a new function lands next to an existing identical function nobody read, and import-order silently picks a winner.
- **Scope check before coding.** State files, intended changes, scope estimate. Wait for confirmation if the plan touches more than two files.
- **Checkpoint between phases of multi-step work.** For any task with more than one distinct phase, pause between phases and restate what was done, what was verified, what remains. Why: prevents phase 4 of a 6-step refactor going wrong while phases 5 and 6 land on top of the broken state. Different from session retros: retros capture learning at the end, checkpoints prevent compounding broken state mid-session.
- **Verification before claiming done.** UI changes need a running dev server and human visual confirmation. Logic changes need shown output. "The code looks correct" is not enough.
- **Commit gate.** Do not commit until the human confirms the change visually for UI work, or confirms the verification output for logic work.
- **Push protocol.** Paste the commit URL, say "waiting for deploy," wait for human production confirmation. Do not declare done on the deploy provider's "Ready" signal alone. CDN and browser cache delay visible-on-production by a minute or two.
- **Reproduce before fixing.** For any bug, write the failing reproduction first. Then the fix. Then verify.
- **Server-only AI calls.** Never call the AI layer from a client component. Always route through an API route. Why: keeps API keys server-side and centralizes prompt logic. Only emitted for stacks with a client/server split.
- **Session retros.** End every non-trivial session with `docs/retros/YYYY-MM-DD-topic.md`. Read the most recent retro before starting a new session.
- **Session-start command.** A `.claude/commands/session-start.md` slash command that reads the entry-point file, the roadmap, and the most recent retro and reports orientation. Replaces re-explaining context every session.
- **Direct-on-main, no branches.** Single-developer pre-launch projects do not benefit from branch overhead.
- **No worktrees when visual confirmation gates commits.** Conditional. `git worktree` is a legitimate Git feature — Claude Code itself uses it for parallel agent work. The constraint only applies when the workflow ties commits to visual confirmation in a single dev server: the dev server points at the main checkout, the worktree has its own working copy, and changes "made" in the worktree are not what `npm run dev` is rendering. For projects without a UI (CLI tools, backend services, Python projects) or with separate dev servers per worktree, this rule does not apply and is not emitted.
- **No deploy CLI.** Only emitted when the deploy target uses a CLI that conflicts with auto-deploy. Pushes to `main` deploy automatically via the deploy target's GitHub integration. Running the CLI creates parallel deployment paths.

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
- **Stack.** Framework + runtime. Drives default commands and which rules are emitted (e.g., the server-only AI call rule is only relevant for stacks with a client/server split). Options include `nextjs`, `react-vite`, `node-cli`, `python`, `other`. Defaults are inferred per stack but can be overridden.
- **Deploy target.** Vercel, Netlify, Cloudflare Pages, Fly, Railway, manual, or none. Drives the "no deploy CLI" rule (only emitted when the target's CLI conflicts with auto-deploy via GitHub integration), the push-protocol "waiting for deploy" wording, and `env_pattern` defaults.
- **Commands.** `install_cmd`, `dev_cmd`, `check_cmd`, `test_cmd`, `build_cmd`, `env_pattern`. Defaults inferred from stack (e.g., `npm run dev` for Next.js, `pnpm dev` if the user prefers pnpm). The actual commands a session needs — the paper's strongest empirical positive on context files.
- AI surface count (zero, one, or several). The server-only AI call rule is only emitted for stacks with a client/server split.
- Whether the project has a design system with a token file.
- Whether the project produces user-facing copy that needs a voice-and-tone rule.
- Whether Codex sessions are part of the workflow.
- Whether `PARKING_LOT.md`, `DECISIONS_ACTIVE.md`, and `FUTURE.md` should be included.
- Domain vocabulary, if any, for the vocabulary lock pattern.

What it does not ask about: branch policy (direct-on-main, no worktrees), retro location (`docs/retros/`), session-start command location (`.claude/commands/session-start.md`). These are hardcoded.
