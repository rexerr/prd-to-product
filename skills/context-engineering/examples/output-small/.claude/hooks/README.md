# `.claude/hooks/`

Hooks turn load-bearing rules from `CLAUDE.md` into actual enforcement. Prose in a context file is a request the agent tries to follow; a hook is a guarantee from the harness.

## Hooks in this project

| Hook | Fires on | What it blocks |
|---|---|---|
| `block-env-commit.sh` | `Bash(git add .env*)` | Staging env files. |
| `block-deploy-cli.sh` | `Bash(vercel *)` | Vercel CLI commands (this project auto-deploys via GitHub integration). |
| `block-worktree.sh` | `Bash(git worktree *)`, `EnterWorktree` | Worktree creation (worktrees break the visual-confirmation commit gate). |

## How hooks integrate with `CLAUDE.md`

The prose rules in `CLAUDE.md` describe the workflow for humans reading the context. The hooks here enforce the load-bearing subset. They are deliberately redundant: the prose explains *why*, the hook guarantees *that*.

## Editing or disabling

Each hook is a plain shell script. To disable one without removing it, comment out its block in `.claude/settings.json` using a `// disabled` key (Claude Code ignores keys starting with `//`).

To add a new hook:

1. Write the script in `.claude/hooks/<name>.sh`. `chmod +x`.
2. Read tool input from stdin as JSON (`jq -r '.tool_input.command'`).
3. To block, exit 2 and write the reason to stderr.
4. Register in `.claude/settings.json` under `hooks.PreToolUse`.

Reference: <https://code.claude.com/docs/en/hooks>.
