#!/usr/bin/env bash
# Open a PR for the current branch with the "symphony" label.
# Usage: open-pr.sh ["<title>"] ["<linear-issue-id>"]
# Defaults: title = latest commit subject, body references the Linear issue if provided.
# If a PR already exists for the branch, prints its URL and exits 0.
set -euo pipefail

TITLE="${1:-$(git log -1 --pretty=%s)}"
ISSUE="${2:-}"

BODY="Automated PR from Symphony orchestration."
if [ -n "$ISSUE" ]; then
  BODY+=$'\n\nLinear: '"$ISSUE"
fi

gh label create symphony --description "Created by Symphony orchestration" --color FF6B35 >/dev/null 2>&1 || true

if URL=$(gh pr view --json url -q .url 2>/dev/null); then
  gh pr edit --add-label symphony >/dev/null 2>&1 || true
  echo "$URL"
  exit 0
fi

URL=$(gh pr create --title "$TITLE" --body "$BODY" --label symphony 2>&1 | tail -1)
echo "$URL"
