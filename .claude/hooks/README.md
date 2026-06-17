# `.claude/hooks/`

Hooks turn load-bearing rules from `AGENTS.md`/`CLAUDE.md` into actual enforcement. Prose in a context file is a request the agent tries to follow; a hook is a guarantee from the harness.

## Why this directory exists

The "Evaluating AGENTS.md" study (2025) found that even well-written context files are interpreted as guidelines, not constraints. For rules that must hold every time — never commit `.env`, never run a destructive deploy CLI, never create a worktree that breaks visual confirmation — the right enforcement layer is a hook, not a prose rule.

This directory holds the hooks that the context-engineering skill emitted for this project. Each script is short and single-purpose: it prints a reason and exits with code 2, which Claude Code surfaces back to the agent and blocks the tool call.

## Hooks in this project

| Hook | Matcher | What the script blocks |
|---|---|---|
| `block-env-commit.sh` | `Bash` | Staging env files — the script inspects the command and blocks only `git add/stage … .env*` (always emitted). |
| `validate-skills.sh` | `Bash` | A `git commit` when any `skills/*/SKILL.md` has malformed frontmatter (missing/empty `name`/`description`, no opening/closing `---` fence, leading tabs, `key:value` with no space) or a duplicate `name`. Structural + cheap-syntactic (not full YAML); **fails open** if no `SKILL.md` is found. Crib C-27 / D-017. |

### Scoping: the matcher selects the tool, the script decides

The `settings.json` entry uses a bare `"Bash"` matcher; the script reads the JSON payload on stdin and exits 2 only when the actual command stages an env file. **Do not scope hooks with the inner `if` filter**: it was observed misfiring on complex compound commands (2026-06-08, 2026-06-12) — so the script must scope itself regardless — and a stale `if` after a script-pattern change silently disarms the guard. Consequence of the bare matcher: the script runs on every Bash call, so its exit-0 path is the common path.

Two hooks the skill normally emits are **not** emitted here:

- `block-deploy-cli.sh` — suppressed because `deploy_target = none` (no CLI conflict to guard against).
- `block-worktree.sh` — suppressed because `uses_visual_confirmation_gate = false` (no UI, no single-dev-server constraint that worktrees would break).

If either condition changes, regenerate by re-running the `context-engineering` skill rather than hand-editing.

## How hooks integrate with `CLAUDE.md`

The prose rules in `CLAUDE.md`/`AGENTS.md` describe the workflow for humans reading the context. The hooks here enforce the load-bearing subset. They are deliberately redundant: the prose explains *why*, the hook guarantees *that*. Removing the prose without removing the hook breaks orientation; removing the hook without removing the prose breaks enforcement.

If you add a new rule to `CLAUDE.md` that must hold every time, consider whether it belongs as a hook here too.

## Editing or disabling

Each hook is a plain shell script. To disable one without removing it, comment out its block in `.claude/settings.json` (use `// disabled` keys; JSON does not support real comments, but Claude Code ignores keys starting with `//`).

To add a new hook:

1. Write the script in `.claude/hooks/<name>.sh`. Make it executable: `chmod +x`.
2. Read tool input from stdin as JSON. Use `jq` to parse (e.g., `jq -r '.tool_input.command // empty'`), and fall back to matching the raw payload when jq is unavailable — a blocking guard must never silently disarm because of a missing dependency (see `block-env-commit.sh` for the pattern).
3. Anchor command matching at command-word position (line start or after `|` `&` `;`) so prose or data mentioning the pattern doesn't block.
4. To block, exit 2 and write the reason to stderr — including what to do instead. To allow with no action, exit 0.
5. Register the hook in `.claude/settings.json` under `hooks.PreToolUse` (or the relevant event) with a bare tool matcher; no `if` filter.

Reference: <https://code.claude.com/docs/en/hooks>.
