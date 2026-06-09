# Small example: Morning Intent

Full transcript of a prd-creator run for a single-purpose daily tool. The user is the developer building it for themselves. No brand work, no AI surface, tight V1.

---

**User:** I want to build a morning intent tracker. Just for me. Use the prd-creator skill.

**Skill:** Running the PRD interview. First, let me check whether you have anything for me to read.

Before we start, do you have a working brief, research dump, transcript, message thread, or notes you want me to read first. Paste, link, or tell me there's none.

**User:** None. It's just an idea.

**Skill:** Acknowledged. Let's start with the pitch.

In one paragraph, what is this product. Lead with what it does, then who it is for, then why it exists.

**User:** A tiny tool I open every morning. I type three intents for the day. At 6pm it texts me a check-in: did I do them. That's it. It's for me, because I keep telling myself I'll do focused work and then drift, and writing intents on paper doesn't follow me into the afternoon.

**Skill:** Got it. Two more on the same theme.

Who specifically is the V1 user. You said "for me," confirming that V1 ships single-user and the only user is you.

**User:** Yes. Single-user. Me.

**Skill:** What are you currently doing instead.

**User:** Writing intents in a notebook every morning. Forgetting the notebook by 11am. Sometimes I open Notes on my phone but I never look at it again.

**Skill:** Captured. Quick recap: Morning Intent is a personal daily tool that captures three intents each morning and texts a check-in at 6pm. V1 is single-user (you). The current workaround is paper notebooks and the Notes app, both of which you abandon mid-day.

Anything you do not yet know about the product, user, or problem that would change the build.

**User:** No. It's clear.

**Skill:** Confirmed. Next, the main workflow.

Walk me through the V1 happy path. What does the user do, step by step, the first time the product works for them.

**User:** I open the URL on my phone in the morning. I type three intents. I close the tab. At 6pm I get an SMS with my three intents and a yes/no for each. I tap yes or no and that's it. Maybe it shows me a streak.

**Skill:** Five steps, clean. Captured.

Anything you do not yet know about the workflow.

**User:** Whether the SMS check-in should be 6pm fixed or configurable. Probably fixed for V1.

**Skill:** Noting that as a decision to confirm later: check-in time is 6pm fixed in V1. Recap: five-step happy path from morning capture through evening SMS check-in plus optional streak display.

Next, scope.

What is V1. Bullet list of capabilities, each one checkable.

**User:** Authless single-page app at a URL only I know. Three text inputs that save to a database. A scheduled job at 6pm that sends an SMS with my intents and yes/no buttons. Tap yes or no, it saves. Streak counter that resets if I miss a day.

**Skill:** Captured.

What did you consider for V1 and explicitly cut.

**User:** Multi-user accounts. AI suggestions for intents. Calendar integration. Anything beyond yes/no on the check-in. Configurable check-in time.

**Skill:** Captured.

What is V2 or later.

**User:** Maybe AI nudges based on patterns. Maybe a weekly review. Honestly I don't know if there's a V2.

**Skill:** Capturing "AI nudges based on patterns" and "weekly review" as deferred. Noted that V2 is uncertain.

Anything you do not yet know about scope.

**User:** No.

**Skill:** Recap: V1 is single-page authless app with three intent inputs, scheduled SMS at 6pm, yes/no response, streak counter. Cuts include multi-user, AI suggestions, calendar integration, anything beyond yes/no. Deferred items noted.

Next, architecture and stack.

What is the stack.

**User:** Next.js on Vercel. Postgres on Neon. Twilio for SMS. That's it.

**Skill:** Captured, and noted as a decision to confirm later: stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS.

What integrations does V1 require.

**User:** Twilio for the SMS. That's the only external thing.

**Skill:** Captured.

What is the AI surface, if any.

**User:** None in V1.

**Skill:** Captured, and noted as a decision to confirm later: no AI surface in V1.

Anything you do not yet know about architecture.

**User:** How to schedule the 6pm job. Vercel cron probably but I haven't checked.

**Skill:** Capturing "How to schedule the 6pm job. Vercel cron is the lean candidate" as an open question. Recap: Next.js on Vercel, Postgres on Neon, Twilio SMS, no AI in V1. One open question on the scheduler.

Now let me read back the decisions you've locked in.

Here's what I captured. Confirm, edit, or drop each.

- D-001: Check-in time is 6pm fixed in V1. Rationale: simplifies V1, configuration adds settings UI you do not want yet.
- D-002: Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS. Rationale: matches your existing tooling.
- D-003: No AI surface in V1. Rationale: the value of V1 is friction-free capture, not AI features.

**User:** All three confirmed. Add: D-004, no auth in V1. Just an obscure URL.

**Skill:** Added.

- D-004: No auth in V1, access via obscure URL only. Rationale: single-user product, auth is overhead with no benefit.

Four decisions locked. Next, brand and voice.

**User:** Skip. It's just for me, no copy to write.

**Skill:** Skipping brand and voice. Last, success criteria.

What does V1 success look like.

**User:** I use it every morning for two weeks straight without dropping a day. The 6pm SMS arrives reliably and I tap yes or no without thinking about it. Streak counter is accurate.

**Skill:** Captured three criteria. Anything you do not yet know about success.

**User:** No.

**Skill:** Recap: success is two weeks of daily use, reliable SMS, accurate streak.

All clusters complete. Proposed PRD outline:

Sections that will emit:
- Product summary
- Target users
- Core problem
- Main workflow
- Version 1 scope
- Out of scope
- Deferred capabilities
- Architecture and stack
- Decisions already made (four entries)
- Open questions (one entry)
- Success criteria

Sections that will be skipped:
- Brand and voice. Reason: not run, no user-facing copy.
- Supporting documents. Reason: no sibling file emitted, no external sources named.

Path: `docs/PRD.md`. Confirm to write.

**User:** Confirm.

**Skill:** Writing. [PRD.md is shown at `examples/small/PRD.md`.]

PRD generated at docs/PRD.md.

Sections that emitted:
- Product summary
- Target users
- Core problem
- Main workflow
- Version 1 scope
- Out of scope
- Deferred capabilities
- Architecture and stack
- Decisions already made
- Open questions
- Success criteria

Sections that were skipped:
- Brand and voice. Reason: not run, no user-facing copy.
- Supporting documents. Reason: no sibling file, no external sources.

Decisions captured: 4. All:
- D-001 Check-in time is 6pm fixed in V1.
- D-002 Stack is Next.js on Vercel, Postgres on Neon, Twilio for SMS.
- D-003 No AI surface in V1.
- D-004 No auth in V1, access via obscure URL only.

Open questions: 1.
- How to schedule the 6pm job. Vercel cron is the lean candidate.

Brand and voice placement: not run.

Files written:
- docs/PRD.md

Next step:
Run the context-engineering skill against this PRD to scaffold AGENTS.md, CLAUDE.md, .claude/rules/, and docs/. The PRD's decisions and architecture sections feed that skill directly; you will not be asked to restate them.
