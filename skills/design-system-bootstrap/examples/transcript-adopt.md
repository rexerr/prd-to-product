# Example: adopt mode, Claude Design bundle

A worked example of the design-system-bootstrap skill in **adopt mode**. The product repo already contains a Claude Design handoff bundle; the skill detects it, copies the rendered design and tokens in, and emits the import rule. No interview runs — adopt copies, it does not ask for token values. Demonstrates the adopt fork through the generator.

Project: **the-council** — a product whose design was mocked in Claude Design and exported as a handoff bundle sitting at `claude-design/` in the repo.

This fixture deliberately shows the **interview branch and the emitted rule only**, not a full copied-bundle output tree. The `cp` of `design/reference/` and the token values is a mechanical filesystem operation with no PARAMETERIZE substitution to dry-run; the only regression-worthy artifact adopt emits is the import rule (below), so that is what this fixture pins.

## Cluster 0 — bundle detection (the adopt fork)

> Generator scans the working directory before asking anything. It finds `claude-design/README.md`, greps it, and the README declares itself a handoff bundle for a coding agent.

> Generator: "There's a Claude Design handoff bundle at `claude-design/`. Adopt it — copy the rendered design and tokens into the repo and wire an import rule so later page-builds stay faithful — or bootstrap a fresh token system from it instead?"

> Adopt it.

**Captured:** `mode = adopt`, `adopt_bundle_path = claude-design/`. Clusters 2–7 (the token interview) are skipped — adopt copies token values, it does not interview for them.

## Cluster 1 — paths

> **Q1a–c.** Project name? Where should `design/reference/` and the copied tokens live?

> the-council. Defaults are fine — reference at `design/reference/`, tokens copied into `app/styles/tokens.css`.

**Captured:** project=the-council, reference dir=`design/reference/` (the template default), token destination=`app/styles/tokens.css`.

## Cluster 8 — confirmation

> **Q8.** Before writing, the generator previews the three adopt writes:

> ```
> design/reference/                 (cp from claude-design/ — pages + component source, verbatim)
> app/styles/tokens.css             (cp of the bundle :root values, verbatim — bundle structure kept)
> .claude/rules/design-adoption.md  (emitted import rule)
> ```
> Tokens are copied as-is, NOT routed through the scale-first tokens.css template (that is the D-008 fidelity trap). The bundle stays the design source of record.

> Go.

## Generator writes the three adopt artifacts

Steps 1–2 are `cp` operations (verbatim copies). Step 3 emits `.claude/rules/design-adoption.md` from `templates/design-adoption.md.template`, default emission (`reference_dir = design/reference/`):

```markdown
---
description: Adopt the Claude Design bundle's components; never rebuild a covered surface
paths: ["app/**", "components/**", "src/**"]
---
# Design adoption — import, don't rebuild

The rendered design of record lives in `design/reference/` (the bundle's pages + component source, re-snapshotted on each Claude Design export).

- **Import the bundle's components; never rebuild a surface they already cover.** Rebuilding inline requires a cited reason in the commit.
  **Failure it prevents:** components got rebuilt inline instead of imported → every page diverged in composition (~100% drift, the-council 2026-06).
- **Diff every new surface against its `design/reference/` page before commit.** No reference for a surface → add one before building it.
  **Failure it prevents:** design fidelity enforced by nothing drifts every time; token compliance alone does not hold composition.
- **A surface diffed against a stale reference is flagged, not trusted.** Re-snapshot `design/reference/` whenever the Claude Design export changes.
  **Failure it prevents:** enforcing fidelity to a design that no longer exists.
```

The emitted rule's default paths and three failure-mode bullets match the source-of-record fence in `docs/design-handoff-adoption.md` verbatim. Output summary follows (adopt variant): what was copied, the bundle stays source of record, and the deferred-enforcement note (intra-app-consistency + staleness are prose in v1; the mechanical hook is deferred to v2).
