# Working brief: AI Research Synthesizer

A web app for running the same research question against multiple AI providers in parallel, then synthesizing the outputs into a single set of insights — with the agreements, disagreements, and contradictions made visible.

## What it is

You type a question. The app fans out to Claude, Gemini, GPT-4, and Perplexity (or some subset) simultaneously. Each provider's answer renders in a column as it streams. When all are done, a "synthesize" button asks Claude to read across the columns and produce a unified output: what they agree on, where they contradict, what claims need human verification, what's missing.

## Who it's for

Knowledge workers doing landscape scans: product folks researching a market, founders sizing a problem, consultants briefing a topic, researchers triangulating a fact. Anyone whose default workflow is currently "ask ChatGPT, then double-check with Claude, then maybe Perplexity for sources, then reconcile by hand."

## The core problem

Each model has a distinct knowledge cutoff, training corpus, and inference bias. Asking only one gives you one slice of the answer. Asking all four manually means an hour of copy-paste-reconcile, and the reconciliation usually doesn't happen — you skim the second model's output and move on. The contradictions stay invisible.

## Rough shape of the experience

- Query box at top, provider selector underneath.
- Run → side-by-side columns stream in.
- Synthesize button → Claude reads all outputs, produces structured synthesis:
  - Points of agreement (high-confidence)
  - Contradictions (flagged for user attention)
  - Source-able claims (links if providers gave them)
  - Notable absences (something one model said the others missed)
- Save session for later. Export as markdown.

## What this is NOT

- Not real-time collaboration on research sessions.
- Not a research feed / public browsing of others' queries.
- Not training a custom model on user history.
- Not deep web scraping beyond what providers natively do.
- Not a chatbot — this is single-question fan-out, not multi-turn.

## Open questions for the interview

- **Auth and billing.** BYOK (each user supplies their own provider API keys) or service-managed (you pay all the bills and charge for it)? BYOK is dramatically simpler for V1 and dodges per-request cost risk.
- **Persistence.** Save sessions or stateless? If save, what shape — by-project, by-tag, by-date?
- **Provider set in V1.** Locking in choices that don't age well is a real risk. Claude + Gemini + GPT-4 is the safe minimum. Perplexity is differentiated (web access). Local models?
- **Synthesis prompt.** How do we keep Claude from just *averaging* the outputs and instead surface real disagreements? This is the hardest part of the product; the prompt matters more than the UI.
- **Output format.** Chat-style, document-style, structured-table, or all three?
- **Streaming.** Real-time stream is more impressive but harder; one-shot per provider is simpler.
- **Stack.** Next.js + Vercel works for the UI; the multi-provider fan-out is server-side and exercises the server-only-AI-calls rule.

## Source

This conversation, 2026-05-11. Adjacent: any of the "synthetic creative director / personal board of mentors" ideas could be specialized cases of this same engine (different prompt configurations).
