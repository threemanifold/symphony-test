#!/usr/bin/env bash
# Run the project's test suite and print a terse, deterministic result.
# On pass: prints one summary line ("OK: ...") and exits 0.
# On fail: prints "FAIL" + the last 20 lines of output and exits non-zero.
set -uo pipefail

OUT=$(uvx pytest -v 2>&1)
EC=$?

if [ "$EC" -eq 0 ]; then
  SUMMARY=$(printf '%s\n' "$OUT" | tail -1)
  echo "OK: $SUMMARY"
  exit 0
fi

echo "FAIL (exit $EC)"
printf '%s\n' "$OUT" | tail -20
exit "$EC"
