# Large example: Founder OS

Abbreviated transcript. A multi-surface personal product with substantive brand work. Sibling `BRAND.md` emits because cluster 6 produced more than three items. Decisions list is longer. Demonstrates the multi-cluster decision running tally, the cluster 5 review, and the sibling-file path.

---

**User:** Use the prd-creator skill. I want to PRD a thing called Founder OS. Personal CRM, decision log, and weekly review for solo founders.

**Skill:** Running the PRD interview. Cluster 0 first.

> Source material question.

**User:** [Pastes a 600-word working brief covering target user, three core surfaces, and a strong opinion on advice tone.]

**Skill:** Read it. Brief covers user, surfaces, and tone stance. Does not cover stack, decisions, or success criteria. Asking those clusters anyway.

> Cluster 1 (paraphrased).

**User:** Solo founders 0-2 years in. They're losing track of conversations, decisions, and weekly cycles. Currently they use Notion plus Apple Notes plus a CRM trial they let expire. They want one surface, opinionated, that pushes back when they drift.

**Skill:** Captured. Cluster 1 summary confirmed.

> Cluster 2.

**User:** Three workflows: (1) log a conversation, AI extracts the contact and summarizes; (2) log a decision with reasoning, get a weekly review of decisions made; (3) Sunday morning review surface that asks five questions and stores the answers.

**Skill:** Three workflows captured. Open question swept: "Whether the three workflows share state or live as separate surfaces."

> Cluster 3.

**User:** V1: contact log with AI extraction, decision log with weekly review email, Sunday review surface. Cuts: team accounts, mobile native app, integrations beyond email, AI advice or recommendations. Deferred: pattern recognition across decisions, founder-specific prompt tuning, calendar integration.

**Skill:** Captured. Multiple decisions building.

> Cluster 4.

**User:** Next.js on Vercel. Supabase for auth and Postgres. Resend for the weekly email. Anthropic for AI extraction and summarization. Posthog for analytics.

**Skill:** Captured. AI surface follow-up.

**User:** Three AI surfaces: contact extraction from conversation log, decision summarization for weekly review, the Sunday review questions are pre-written but the responses get summarized for the next week's email. All server-side. Sonnet for extraction, Haiku for summarization.

**Skill:** Captured as D-005, D-006, D-007. Open question: "Whether Sonnet for extraction is overkill if the conversation logs are short."

> Cluster 5 read-back.

[Eight decisions presented as D-001 through D-008. User edits one (changes Posthog to Vercel Analytics for V1), confirms the rest.]

Renumbered: D-001 through D-008. Final list confirmed.

> Cluster 6, brand and voice.

**User:** Audience is solo founders 0-2 years in, plus their advisors who occasionally see the weekly emails. Tone attributes: opinionated (the product takes positions), terse (founders don't have time), warm-but-not-cheery (no cheerleading), specific (cite the decision, not "great progress"), grounded (no founder-mythology language). Vocabulary: it's "decisions" not "choices," "review" not "retrospective," "conversations" not "meetings." Do-not list: never use "journey," "intentional," "let's unpack," anything from a LinkedIn thread.

**Skill:** Counting items: one audience block, five tone attributes, three vocabulary terms (canonical plus alternates), one do-not pattern. Total nine items. Sibling file per the placement rule.

> Cluster 7.

**User:** Hundred founders complete at least three Sunday reviews in their first month. Decision log entries are read at the next week's review at least 60% of the time. AI extraction accuracy on contacts is over 90% as judged by user accept rate. Founders self-report that the weekly email "made them think about something they would have skipped" at least once a month.

**Skill:** Last criterion captured as a survey-driven measure with explicit phrasing. Open question: "Whether self-report quarterly is checkable enough or needs an in-product question."

> Outline confirmed. Writing files.

[PRD.md emits 12 sections plus a Supporting documents pointer to BRAND.md. BRAND.md emits with audience, five tone attributes, vocabulary block, do-not list, and three on/off voice examples generated from the user's stated tone.]

> Output summary.

PRD generated at docs/PRD.md. BRAND.md generated at docs/BRAND.md.

Sections that emitted: 12 in PRD plus the BRAND.md sibling.

Sections that were skipped: none.

Decisions captured: 8. Top three by criticality:
- D-002 Stack is Next.js on Vercel, Supabase for auth and Postgres, Resend for email, Anthropic for AI, Vercel Analytics.
- D-005 All AI calls server-side via API routes.
- D-007 Sonnet for contact extraction, Haiku for summarization. (See open question on Sonnet's necessity.)

Open questions: 5. Top blockers for V1:
- Whether the three workflows share state or live as separate surfaces.
- Whether Sonnet for extraction is overkill given short conversation logs.
- Whether self-report on the "made me think" criterion needs an in-product question.

Brand and voice placement: sibling file at docs/BRAND.md.

Files written:
- docs/PRD.md
- docs/BRAND.md

Next step:
Run the context-engineering skill against this PRD. The PRD's decisions and architecture sections become cluster 0 input. The BRAND.md will trigger context-engineering's voice-and-tone rule pattern, which scaffolds a path-scoped rule under .claude/rules/.
