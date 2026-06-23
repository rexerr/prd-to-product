# Brief — scaffold-port candidates + belt/suspenders scan

> **Status: executed 2026-06-23.** Both known gaps ported; belt+suspenders scan run over the process layer *and* the shipped skills; two evidenced suspenders adopted (prd-creator leak-grep, CE product-code allowlist), four deferred (n<2). Board row retired. Kept as the record of the scan method + the deferred candidates. See the 2026-06-23 retro.

**Read this when:** running the focused session that ports known process improvements into the `context-engineering` scaffold and scans for belt+suspenders gaps. Spawned 2026-06-23 from the CF-29/push-state session ([retro](../retros/2026-06-22-cf29-dsb-format.md)); governs work under the new CLAUDE.md rule "Port self-improvements back to the skill."

This repo's product *is* the skills it ships. Improvements to this repo's own process/config are often portable to the scaffold templates (`skills/context-engineering/templates/` + the `output-small` fixture) so new projects inherit them. This brief lists what's already known un-ported, plus a scan prompt to find more.

## Do first — two known generic gaps to port

Both are present in this repo's root `CLAUDE.md` but absent from the scaffold. Port each into the scaffold's autonomy/session-discipline surfaces (`templates/claude-rules-flat-AGENTS.md.template`, `templates/claude-rules-modular/session-discipline.md.template`) **and** the rendered `examples/output-small/AGENTS.md`, with generic wording (no this-repo vocabulary, per [D-013](../DECISIONS.md) / [D-019](../DECISIONS.md)), each citing its failure mode. Verify by dry-run diff against `output-small` (class T).

1. **Self-modification-of-config gate.** Source: root `CLAUDE.md` "Autonomy" (~line 54) — always-gated list includes "self-modification of agent config (`.claude/` commands, settings, CLAUDE.md startup behavior)." The scaffold's autonomy bullet gates "irreversible/outward-facing" but never names self-config-editing as a category. Add it: an agent should not auto-edit its own startup behavior / commands / settings without explicit user approval.
2. **Delegate-to-subagent + engineered-blindness verifier.** Source: root `CLAUDE.md` "Session management" (~line 88). Hand a verifier only the artifact + acceptance criteria, never your own reasoning/conclusion (a verifier shown the author's framing rubber-stamps); when no subagent is available, say "Self-verified — independent sub-task unavailable" rather than passing anchored self-review off as independent.

## Also consider (conditional — port only with the relevant feature)

- **Reload a co-edited file before writing** (root CLAUDE.md ~line 60) — generalizes to any multi-agent project; port the reload half, NOT the Cowork-specific measurement-artifact carve-out (D-018, this-repo).
- **DECISIONS_ACTIVE marker reconciliation** in end-session — only for scaffolds that enable a `DECISIONS_ACTIVE` curated subset.

## Correctly NOT ported (do not touch)

Cribs routing, the non-Claude-Code-agents rule, example-diff verification, hook live-firing, the "bad substitution" retro tag — all this-repo-specific machinery; the D-013/D-019 line governs.

## Then — belt + suspenders scan

A belt+suspenders setup pairs a prevention rule (belt) with an INDEPENDENT detection/correction check (suspenders) that fails for a different reason, so one slip doesn't cause the failure. Hunt for failure modes guarded by only ONE mechanism that depends on a human/agent *remembering*, with no deterministic check that catches the slip.

```
Scan this repo (prd-to-product) AND the skills it ships for belt+suspenders gaps.
1. Inventory prose rules/disciplines that rely on remembering: CLAUDE.md,
   .claude/commands/, docs/retros/README.md, docs/DECISIONS_ACTIVE.md, and the
   scaffold templates under skills/context-engineering/templates/.
2. Classify each: (a) belt-only (rule, no check), (b) suspenders-only (check, no
   rule), (c) both, (d) neither. Flag belt-only items whose failure is costly.
3. For each candidate name: the failure mode, why prose-alone is fragile (does it
   need remembering EVERY time?), and the cheapest INDEPENDENT check (hook,
   session-start/end-session step, grep in verification, git check). Prefer
   deterministic checks over "remember harder."
4. Cross-check the retro tag-log (docs/retros/) for evidence each failure recurred
   (n>=2). Adopt suspenders where there's evidence; don't accrete guards against
   failures that never happen (this repo's anti-guardrail stance).
Precedent: push/sync-state (belt = "never write push-state in a retro"; suspenders
= "session-start reads sync from git"), adopted 2026-06-23 at n=3 — see
docs/retros/README.md line 11 and docs/retros/2026-06-22-cf29-dsb-format.md.
Return a ranked table: failure mode | current guard(s) | proposed suspenders |
evidence (n=?) | port-to-scaffold? Recommend, then implement the evidenced ones.
```
