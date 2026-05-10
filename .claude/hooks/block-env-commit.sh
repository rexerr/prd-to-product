#!/usr/bin/env bash
# Hook: Block staging or committing of env files.
# Reason: env files contain secrets. Staging them risks committing secrets to
# version control, which is irreversible once pushed. This is a guarantee, not
# a guideline.

echo "BLOCKED: Do not stage or commit env files. This repo has no env files; .env* in any form should not be committed." >&2
exit 2
