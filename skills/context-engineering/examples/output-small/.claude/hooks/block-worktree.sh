#!/usr/bin/env bash
# Hook: Block worktree creation.
# Reason: worktrees create isolated working copies. The dev server points at
# the main checkout, not the worktree, so changes "made" in the worktree are
# not what `npm run dev` is rendering. Visual confirmation breaks silently.
# Worktrees are not bad in general — they are incompatible with this project's
# specific commit gate. Only emitted when uses_visual_confirmation_gate == true.

echo "BLOCKED: Worktrees break the visual-confirmation commit gate in this project. The dev server points at the main checkout. Work directly in /Users/jordan/Sites/simple-form." >&2
exit 2
