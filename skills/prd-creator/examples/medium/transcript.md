# Medium example: Standup Digest

Abbreviated transcript. A SaaS-style tool with a real AI surface and a small but real brand-voice section. Brand content lands inline (three items). Decisions list is medium length.

---

**User:** Build me a PRD for "Standup Digest." It reads my Slack channels overnight and writes my morning standup update for me.

**Skill:** Running the PRD interview. Cluster 0 first.

> Source material question.

**User:** I have a notes doc. [Pastes 200-word note covering: target user is engineering managers, bored writing standups, want a draft they can ship in 30 seconds, monetization is later.]

**Skill:** Read it. Note covers user, problem, and monetization stance. Does not cover workflow, stack, or success criteria. Asking those clusters anyway, not pre-filling.

> Cluster 1 questions.

**User:** Engineering managers and senior engineers on teams that run async standup. They're tired of the writing tax and they currently either skip days or paste yesterday's update with the date changed.

**Skill:** Cluster 1 summary captured. Moving to workflow.

> Cluster 2.

**User:** [Five-step workflow: nightly Slack scrape → AI summarizes activity per user → user opens app at 9am → reviews and edits the draft → posts back to standup channel with one click.]

**Skill:** Captured. Open question swept: "What's the cutoff time for 'overnight' if a user is in a different timezone." Captured.

> Cluster 3.

**User:** V1: one Slack workspace per user, AI draft generation, edit-and-post flow, basic auth. Cuts: multi-workspace, team analytics, custom prompt tuning, integrations beyond Slack. Deferred: GitHub PR activity in the digest, Linear issue activity, weekly retrospective rollup.

**Skill:** Captured. D-001 candidate, "V1 supports one Slack workspace per user."

> Cluster 4.

**User:** Next.js on Vercel. Supabase for auth and Postgres. Slack OAuth. Anthropic API for the summarization. Inngest for the overnight job.

**Skill:** Captured as D-002. Open question: "Whether Inngest scales to per-user nightly jobs at the cost we want." Asked about AI surface specifics.

**User:** One AI call per user per night. Server-side. Claude Haiku for cost. Prompt is templated.

**Skill:** Captured as D-003 and D-004. Open question: "Whether Haiku's quality on summarization-of-Slack is sufficient." Captured.

> Cluster 5 read-back.

[Six decisions confirmed: workspace-per-user, full stack, AI server-only, Haiku for cost, no custom prompts in V1, free tier with usage cap.]

> Cluster 6, brand and voice.

**User:** Audience is engineering managers, terse and time-pressed. Three tone attributes: terse, useful, never cute. Vocabulary lock: it's a "digest," not a "summary," not a "report." That's it for brand.

**Skill:** Three items captured (audience plus three tone attributes counts as one tone-attributes block plus one audience plus one vocabulary item, total three). Inline appendix per the placement rule.

> Cluster 7.

**User:** Hundred users post a digest within their first three days. Drafts are accepted (posted with no edits) at least 30% of the time. Mean edit time under 60 seconds. No support tickets about "the AI hallucinated activity that didn't happen."

**Skill:** Captured. Last criterion is a watch-not, kept as success criterion (checkable: count tickets matching that complaint).

> Outline confirmed. Writing PRD.

[PRD emits 11 sections plus inline brand-and-voice appendix. Six decisions, four open questions, four success criteria.]

> Output summary.

PRD generated at docs/PRD.md.

Sections that emitted: 12 (including inline Brand and voice appendix).

Sections that were skipped:
- Supporting documents. Reason: no sibling file, no external sources named.

Decisions captured: 6. Top three by criticality:
- D-002 Stack is Next.js on Vercel, Supabase for auth and Postgres, Slack OAuth, Anthropic for AI, Inngest for jobs.
- D-003 AI calls are server-only via API route.
- D-001 V1 supports one Slack workspace per user.

Open questions: 4. Top blockers for V1:
- Whether Haiku's quality on Slack-summarization is sufficient.
- Whether Inngest scales to per-user nightly jobs at target cost.
- Cutoff time for "overnight" across timezones.

Brand and voice placement: inline appendix.

Files written:
- docs/PRD.md

Next step:
Run the context-engineering skill against this PRD.
