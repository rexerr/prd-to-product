# Claude skills for product work

Three composable Claude Code skills that take a product from rough idea to a real codebase scaffold. Each skill does one thing and hands off to the next.

## The three skills

1. **[prd-creator](skills/prd-creator/)** — interview-driven PRD generation. Takes a rough idea, working brief, or research dump and produces a structured `PRD.md` plus an optional `BRAND.md` for voice and tone.
2. **[context-engineering](skills/context-engineering/)** — context scaffolding for AI-assisted coding projects. Takes a PRD and produces `AGENTS.md`, `CLAUDE.md`, `.claude/rules/`, and the `docs/` structure.
3. **[design-system-bootstrap](skills/design-system-bootstrap/)** — token-based design system generation. Takes brand assets or direct input and produces `tokens.css`, three seed React components, and a `DESIGN_SYSTEM.md`.

## How they compose

The output of each skill is the input to the next. You can run them in sequence on a fresh project, or run any one standalone if the upstream context already exists.

```
rough idea
   ↓
prd-creator
   ↓ produces docs/PRD.md and optional docs/BRAND.md
   ↓
context-engineering
   ↓ produces AGENTS.md, CLAUDE.md, .claude/rules/, docs/
   ↓
design-system-bootstrap
   ↓ produces app/styles/tokens.css, three seed components, docs/DESIGN_SYSTEM.md
   ↓
ready to build
```

The skills know about each other. Context-engineering reads the PRD without making you restate it. Design-system-bootstrap detects context-engineering's design-system rule and updates rather than overwriting it.

## Install

Clone the repo and symlink each skill into `~/.claude/skills/`. Symlinking (over copying) means edits to the repo land in your active skills without re-installing.

```bash
git clone https://github.com/<your-handle>/<repo-name>.git
cd <repo-name>
for skill in skills/*/; do
  ln -s "$(pwd)/$skill" "$HOME/.claude/skills/$(basename "$skill")"
done
```

If you prefer to copy instead of symlink (skills do not auto-update on `git pull`):

```bash
cp -r skills/* ~/.claude/skills/
```

Verify the install:

```bash
ls -la ~/.claude/skills/ | grep -E "prd-creator|context-engineering|design-system-bootstrap"
```

You should see all three.

## How to use

In any Claude Code session, trigger a skill by name or by phrase.

- `use the prd-creator skill` or `draft a PRD for <idea>`
- `use the context-engineering skill` or `scaffold context for a new project`
- `use the design-system-bootstrap skill` or `bootstrap design system from brand book`

Each skill runs an interview, summarizes what it captured, asks for confirmation before writing files, and prints a post-generation report at the end.

For a fresh project, run them in order in an empty directory:

```bash
mkdir ~/Code/my-new-project
cd ~/Code/my-new-project
claude
```

Then in the session: `use the prd-creator skill` followed by `use the context-engineering skill` followed by `use the design-system-bootstrap skill`.

## Conventions

The three skills share a few opinions, captured here so you can decide whether they fit your project before adopting them.

- **Single-developer, direct-on-main, Vercel + Next.js.** V1 hardcodes this stack. Multi-developer and other stacks are parked for Phase 2.
- **Sentence-case headers, no em dashes, no Oxford commas.** Applied to all generated docs.
- **Skills do not write product code.** They scaffold context, structure, and tokens. The product itself is your job.
- **Per-decision explicit asks.** When promoting decisions to a binding active list, the skills ask one at a time with criteria stated, not in bulk.
- **Position-aware placement.** Generated files put load-bearing constraints at the top and bottom, structure in the middle.

For the full rationale, read each skill's `principles.md`.

## How the skills were built

Each skill follows a five-piece architecture: `SKILL.md` (trigger and procedure), `principles.md` (rationale, deferred-loaded), `templates/` (annotated stubs), `generator/` (intake, decisions, output-summary), `examples/` (three runs at small, medium, large scale), `NOTES.md` (regression tests and parked ideas).

Session-by-session build history lives in [`docs/retros/`](docs/retros/). For active investigations that govern the skills' shape, see [`docs/build-defaults-brief.md`](docs/build-defaults-brief.md) and [`docs/html-over-markdown-brief.md`](docs/html-over-markdown-brief.md).

## License

[MIT](LICENSE).
