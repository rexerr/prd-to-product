# Generator output summary

The post-generation report. Run after every file in the inclusion table has been written.

## Format

Output a single message to the user with three sections.

### 1. Files generated

A tree of every file written, grouped by location:

```
<repo_local_path>/
├── AGENTS.md
├── CLAUDE.md
├── ROADMAP.md
├── .claude/
│   ├── commands/
│   │   └── session-start.md
│   └── rules/
│       ├── git-and-deploy.md
│       ├── session-discipline.md
│       └── ...
└── docs/
    ├── PRD.md
    ├── ARCHITECTURE.md
    ├── DECISIONS.md
    ├── retros/
    │   └── README.md
    └── ...
```

Mark files that are intentionally empty placeholders with `(empty placeholder)` after the filename. Mark files that contain user-supplied content from the intake with no annotation.

### 2. What you should review before starting work

A checklist of high-leverage things to verify. The user should be able to scan and confirm in under five minutes.

- **Vocabulary lock.** If the project has domain vocabulary, confirm the canonical list and the forbidden list are complete. Easy to forget an old name in the forbidden list.
- **AI surface paths.** If AI surfaces were specified, confirm the implementation file paths and API route paths in the `paths:` frontmatter of each `ai-<surface>.md` file actually point at real files in the repo.
- **Where-to-look table.** Read the table at the bottom of `AGENTS.md` (or `CLAUDE.md` for flat shape) and confirm every doc named exists or will exist soon.
- **Recency safeguard.** Read the "Before you respond" block at the bottom of `AGENTS.md`. Confirm every item is genuinely load-bearing and that you can defend each one.
- **Workflows.** If multiple workflows were named, confirm each is a real distinct surface, not a rename of the same thing.
- **Tech stack note.** AGENTS.md says "Next.js (App Router) on Vercel" plus the `additional_stack_summary` you provided. If you missed an integration (Inngest, an analytics tool, an email provider), add it to ARCHITECTURE.md "External integrations" before starting work.

### 3. What's next

A suggested next-step sequence:

1. Read `AGENTS.md` end-to-end. This is the file the agent reads every session.
2. Fill in any sections of `docs/PRD.md` and `docs/ARCHITECTURE.md` that are still placeholder. The generator scaffolded structure; the content is yours.
3. Run the `/session-start` slash command to confirm the orientation flow works before doing any code work.
4. Make the first decision and log it in `docs/DECISIONS.md` to validate the format. Promote it to `DECISIONS_ACTIVE.md` if it imposes a binding constraint.
5. Start the first session. Write a retro at the end.

## Flags to surface in the summary

If any of these are true, surface them in a "things to address before starting work" sub-section under "What you should review":

- Any `<!-- PARAMETERIZE: ... -->` marker remained unfilled in the output. Surface the marker name and the file. This is a generator bug; the user should not see unfilled markers.
- The `path_scoped_rule_list` resolved to zero rules but the AGENTS.md "Path-scoped rules" section was emitted anyway.
- A canonical workflow doc was named but no template was emitted for it. The user has to write that doc by hand; flag the filename.
- The vocabulary lock was filled with a canonical list but the forbidden list is empty. This is allowed but worth flagging — the forbidden list is what makes the rule work.

## Tone

Direct. No celebration. The generator wrote files; the user has work to do. Match the project's house style: sentence-case headers, no em dashes, no Oxford commas.
