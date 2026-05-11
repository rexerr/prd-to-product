# Working brief: Anti-Generic Machine

A single-page web tool: paste content (headline, brand brief, homepage copy, design rationale, About page), get scored on "AI-generic" feel, see exactly which phrases tripped the rubric, get 2–3 reframings per offender.

## What it is

A diagnostic tool, not a rewriter. You bring writing that's already done. The tool tells you where it's wearing the AI uniform — em dash overuse, "It's not just X, it's Y" constructions, rule-of-three pile-ups, glossy verbs (seamless / streamlined / robust / leverage), tidy parallelisms, vague attributions ("many experts agree"), the whole catalog. Each offender is highlighted with the pattern named and 2–3 sharper alternatives offered.

## Who it's for

Marketers reviewing copy before launch. Designers reviewing brand statements. Founders reviewing their About page. Copywriters reviewing client deliverables. Anyone whose work is about to ship and who has the gnawing feeling that it sounds like every other AI-assisted thing on the internet.

## The core problem

AI-generated content has a uniform that's unmistakable once you know the tells. Once you see it, every brand starts to look the same. The current remedy is "have good taste and rewrite by hand," which doesn't scale and which most people can't do in 10 minutes before a Tuesday launch. There's no fast diagnostic.

## Rough shape of the experience

- Paste content.
- Get a score (0–100, where 0 is fully human and 100 is fully uniformed).
- Below the score, the original text with offending phrases highlighted; click a highlight to see the pattern name and reframing options.
- Optional "before / after" side-by-side using the user's preferred reframings.
- Export the revised text.

## What this is NOT

- Not an end-to-end rewriter. The user makes every call.
- Not "humanize my AI text" (humanizer skill already exists for that — anti-generic is upstream *diagnosis*, not downstream *rewriting*).
- Not plagiarism detection — different problem.
- Not voice-matching to a brand. That's a separate tool.
- Not for visual content in V1 (logos, designs); text-only.

## Open questions for the interview

- **The rubric.** Wikipedia's "Signs of AI writing" is a starting corpus. What else? Do we maintain it manually, or learn from user feedback over time?
- **Calibration.** False positives on writing that legitimately uses em dashes (lots of good writers do) are the failure mode that kills trust. How tight is the scoring? Confidence thresholds?
- **Reframing quality.** Generic "make it sharper" suggestions are themselves AI-generic. The reframings have to feel like an editor wrote them, not a model. How? Maybe seed with examples from writers known for sharp prose.
- **Free tier vs paid.** Single-page tool with no auth screams "free, virally shareable." But the LLM calls cost something.
- **Decay.** AI tells shift as model behavior shifts. How do we keep the rubric current?
- **Visual extension.** "Anti-generic for logos / brand directions" is a natural sibling but a much harder build. V2 at earliest.
- **Stack.** Single-page Next.js + Vercel. The backend is one API route that calls Claude with the rubric. Smallest deployable surface of the three candidate projects.

## Source

This conversation, 2026-05-11. Related skill that already exists: anthropic-skills:humanizer (rewriting). Anti-generic is the diagnostic step before rewriting; the two could compose.
