Close out the session cleanly. Follow the session-discipline rules and the retro convention (`docs/retros/README.md`).

1. **Restate** in one short block: what was done, what was **verified** — concrete evidence (test/check output, or visual confirmation for a UI change), not "the code looks correct" — and what remains.

2. **Update the docs the work changed.** Tick completed Build-plan tasks in `BACKLOG.md` (mark a phase done only when its "done-when" is met) and update its In-progress / Backlog lists (resolved items move to a retro, not back into the file). Log any significant decision in `docs/DECISIONS.md`.

3. **Retro — only if the session was non-trivial** (skip one-line tweaks; avoid retro-spam). Get the time with `date "+%Y-%m-%d %H:%M %Z"`, then write `docs/retros/YYYY-MM-DD-topic.md` with a timestamped, session-numbered H1 (`# Retro — YYYY-MM-DD HH:MM TZ — [topic]   (Nth session of the day)`). Be honest about misses, deviations, and what verification did and did not cover.

4. **Commit + push as ONE commit.** Stage code + retro + doc updates together and push once — never push the code, then push the retro as a second commit (that double-push is the waste the retro exists to prevent). Paste the resulting commit URL: `https://github.com/jordan-d/simple-form/commit/<sha>`.
   - **Commit gate.** If the change touches a UI/visual surface and Jordan has not confirmed it in a running dev server, do **not** commit. Stop, say exactly what to check and on which page, and commit only after sign-off.

5. **Hand off.** List anything still gated on Jordan and the single next thing to pick up.
