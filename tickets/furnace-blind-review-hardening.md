---
slug: furnace-blind-review-hardening
status: next
seq: 1
title: Harden furnace-plan blind review — fixed reviewer-prompt template + pinned model
---

The furnace-plan blind-review step is **structurally tainted by author improvisation**. The skill says the reviewer prompt contains ONLY (1) plan path, (2) acceptance criteria, (3) rubric pointer — *"Pass nothing else. Do not paste your reasoning."* But the prompt is assembled by the author each run, which is exactly where the author's "be helpful, tell the reviewer what to check" instinct leaks in. In the 2026-06-24 session it happened **twice** (escalating from a generic "verify the claims" to naming specific findings to confirm — `confirm prd-creator's scan at decisions.md:101–114, the (Q7c) occurrences…`), turning a blind review into a confirmation checklist. Compounded by an unpinned reviewer model (Explore defaulted to a weak model). Caught externally by Rex, not by the furnace — the preflight audits the *plan*, never *how the review was set up*.

**The fix is to remove the degree of freedom, not "try harder":**

1. **Fixed reviewer-prompt template in the skill.** Make the three-element prompt a verbatim template the author fills with only {plan-path} + {acceptance-criteria}, with the verification expectation living *inside the rubric the reviewer reads* (plan-review/SKILL.md), NOT in the author's prompt. Nothing for the author to "helpfully" add. Acceptance criteria must be phrased as task goals, never as "confirm that claim X is true."
2. **Pin the reviewer to a capable model.** The skill says "Explore type" but doesn't set a model; it defaulted to Haiku. A pre-filter reviewer given an answer key + a weak model is the worst case. Pin Opus/Sonnet (the trial-ledger already treats the cc-subagent as a same-model reviewer, so Opus matches design intent).

**Why it matters:** the clean Opus re-run (neutral prompt) on 2026-06-24 caught a real issue the tainted Haiku pass rubber-stamped — same plan, same reviewer type, only prompt-hygiene + model differed. That comparison is the evidence.

**Next:** `/furnace-plan` the SKILL.md self-edit (it's a shipped-product self-modification of agent config → scope-gated). Edit `skills/furnace-plan/SKILL.md` "The blind review" section: add the fixed prompt template + the `model:` pin. Verify by reading the section back; consider whether the verification-expectation belongs in `skills/plan-review/SKILL.md` (the rubric) instead of the furnace prompt.

**Open question:** can the furnace add a self-audit that the blind review was run per spec (model pinned, prompt unmodified)? Probably not mechanically (no runner) — but a one-line author checklist item ("reviewer prompt = template verbatim, model pinned") in the skill might help. Decide during the fix.

Reasoning + root cause: [retro 2026-06-24](../docs/retros/2026-06-24-no-jargon-leak-scan.md) ("Failure this session"); the [D-043](../docs/DECISIONS.md#d-043) blind-reviewer design; [D-035](../docs/DECISIONS.md#d-035) engineered-blindness rationale.
