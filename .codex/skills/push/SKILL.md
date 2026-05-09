---
name: push
description:
  Push current branch changes to origin and create or update the corresponding
  pull request; use when asked to push, publish updates, or create a pull
  request.
---

# Push

## Prerequisites

- `gh` CLI is installed and authenticated (via `GH_TOKEN` env var or
  `gh auth status`).
- `git` is configured with a working credential helper for `origin`.

## Goals

- Push current branch changes to `origin` safely.
- Create a PR if none exists for the branch, otherwise update the existing PR.
- Ensure PR has the `symphony` label.
- Keep branch history clean when remote has moved.

## Related Skills

- `pull`: use when push is rejected for a non-fast-forward / sync reason.
- `commit`: use to create the commit before pushing.

## Steps

1. Identify the current branch and confirm remote state.
2. Run local validation before pushing. For this repo the standard check is
   `uvx pytest -v` if `test_*.py` or `*_test.py` files exist; otherwise no
   tests are required.
3. Push branch to `origin` with upstream tracking if needed, using whatever
   remote URL is already configured. Do not switch protocols (HTTPS↔SSH) as a
   workaround for auth errors.
4. If push is not clean/rejected:
   - If the failure is a non-fast-forward or sync problem, run the `pull`
     skill to merge `origin/main`, resolve conflicts, and rerun validation.
   - Push again; use `--force-with-lease` only when history was rewritten.
   - If the failure is due to auth, permissions, or workflow restrictions,
     stop and surface the exact error rather than rewriting remotes.
5. Ensure a PR exists for the branch:
   - If no PR exists, create one with `gh pr create`.
   - If an open PR exists, update it.
   - If branch is tied to a closed/merged PR, create a new branch + PR.
   - Write a clear PR title that summarizes the shipped change.
   - On branch updates, reconsider whether the existing title still matches
     scope and edit if not.
6. Write/update the PR body:
   - If `.github/pull_request_template.md` exists, follow its sections; fill
     each one with concrete content; replace placeholder comments
     (`<!-- ... -->`).
   - If no template exists, use the default body template below.
   - For branch updates, refresh the body to reflect total PR scope (not just
     the newest commit). Do not reuse stale text from earlier iterations.
7. Ensure the PR has the `symphony` label. If the label does not exist on the
   repo, create it before applying.
8. Reply with the PR URL from `gh pr view`.

## Commands

```sh
# Identify branch
branch=$(git branch --show-current)

# Validation (only if a test suite exists in this repo)
if ls -1 test_*.py *_test.py tests/ 2>/dev/null | grep -q .; then
  uvx pytest -v
fi

# Push (will use the credential helper / GH_TOKEN configured by Symphony)
git push -u origin HEAD

# If the push failed because the remote moved, run the `pull` skill, rerun
# validation, then retry the same command.

# Only if history was rewritten locally:
# git push --force-with-lease origin HEAD

# Ensure PR exists
pr_state=$(gh pr view --json state -q .state 2>/dev/null || true)
if [ "$pr_state" = "MERGED" ] || [ "$pr_state" = "CLOSED" ]; then
  echo "Branch is tied to a closed PR; create a new branch + PR." >&2
  exit 1
fi

pr_title="<clear PR title written for this change>"
pr_body_file=$(mktemp)
# Build $pr_body_file from .github/pull_request_template.md if present,
# otherwise from the default template below.

if [ -z "$pr_state" ]; then
  gh pr create --title "$pr_title" --body-file "$pr_body_file"
else
  gh pr edit --title "$pr_title" --body-file "$pr_body_file"
fi
rm -f "$pr_body_file"

# Ensure `symphony` label exists, then apply it
gh label list --json name -q '.[].name' | grep -qx symphony \
  || gh label create symphony --color 5319e7 --description "Symphony orchestration"
gh pr edit --add-label symphony

# Show PR URL
gh pr view --json url -q .url
```

## Default PR body template

Use this when `.github/pull_request_template.md` is absent:

```md
## Summary
- <one bullet per logical change>

## Validation
- <command(s) run, results>

## Related
- Linear: <ticket identifier>
```

## Notes

- Do not use `git push --force`; only `--force-with-lease` as a last resort.
- Distinguish sync problems from auth/permission problems:
  - Use the `pull` skill for non-fast-forward issues.
  - Surface auth/permission errors directly; do not rewrite remotes.
