# Security Review Packet

## Mode

Read-only security review unless the maintainer separately authorizes fixes.

## Scope

- Repository:
- Commit, branch, PR, or path:
- Threat model focus:
- Explicit exclusions:

## Agent instructions

- Identify plausible exploit paths, not theoretical style issues.
- Validate source-to-sink reasoning.
- Cite exact evidence.
- Do not publish vulnerabilities.
- Do not create exploit artifacts beyond minimal proof reasoning.
- Do not change code without authorization.

## Evidence chain

- Files inspected:
- Inputs and trust boundaries:
- Sinks reviewed:
- Existing mitigations:

## Required output

- Finding title.
- Severity and confidence.
- Attack path.
- Evidence.
- Impact.
- Recommended fix.
- Residual uncertainty.
- Status: `NO_FINDINGS`, `FINDINGS_NEED_MAINTAINER_REVIEW`, or `BLOCKED`.

## No-authority statement

This review does not authorize disclosure, release blocking, or production deployment decisions.

