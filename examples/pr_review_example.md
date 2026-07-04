# Example PR Review Output

## Findings

1. `src/auth.py:42` accepts an unsigned token path when `issuer` is blank.
   Severity: high. The branch bypasses signature verification for malformed input. Add a hard rejection before claims parsing.

2. `tests/test_auth.py` does not cover blank issuer or malformed token cases.
   Severity: medium. Add regression tests for rejected unsigned tokens.

## Open questions

- Should blank issuer be rejected at parsing time or validation time?

## Test gaps

- No negative test for unsigned token fallback.

## Status

`PATCH_RECOMMENDED`

## No-authority statement

This review does not approve merge, release, deployment, or production use.

