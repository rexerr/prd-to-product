---
slug: skill-injection-by-project-type
status: blocked
title: Skill injection by project type — domain-layer companion
---

# Skill injection by project type

Domain-layer companion to the agent-process work. Where that is the *process* layer (always-on, stack-independent), this is the *domain* layer: teach `context-engineering` to map a new project's **stack + primary output** → a curated skill shortlist, install a tiny **active** set into `.claude/skills/`, **park** the rest in `docs/references/staged-skills/`, and **promote per phase** via ROADMAP notes. Generalizes what Séance did by hand.

## Current state

Capability is greenfield on top of one existing hook: Q27a `external_skill_references` ([intake.md:215](../skills/context-engineering/generator/intake.md)) only cross-links *already-installed* global skills — there is no stack→skill map, no manifest, no active/parked/promote concept. Source reference: `/Users/rexc/Sites/seance/docs/references/skill-injection-by-project-type.md` (reviewed 2026-06-08; its `staged-skills/README.md` + per-phase ROADMAP promotion notes are the working reference implementation).

## Blocking design question (resolve before building)

The doc's promote-mechanic assumes you **vendor** repo files (`cp -R` into `.claude/skills/`), but most candidates now arrive as **marketplace plugins** (~70 plugin descriptions load every session — the exact context-cost the doc warns about, observed live 2026-06-08). For plugin-sourced skills "active vs parked" is enable/disable, not a filesystem move, and may not be per-project controllable at all. The manifest schema anticipates this with a `source` field (`plugin | marketplace | repo-vendored | url`) but the §4 flow only solves the vendored case. **Don't build until the source-dependent promotion mechanic is designed** — otherwise it ships solving one source.

## Scope when it lands

Large (>300-line feature gate) + new generated-artifact type (architecture decision) — needs explicit scope confirmation and likely phasing. For *this* repo the domain layer is a near-no-op (skill-building project → active `skill-creator`, parked `mcp-builder`, both already present as plugins). Defer the long tail to `find-skills`.

## Why (pointers)

Connects to [agent-teams-scaffold-guidance](agent-teams-scaffold-guidance.md) (same domain-layer surface). Source doc above.
