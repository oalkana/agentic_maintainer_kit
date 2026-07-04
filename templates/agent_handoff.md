# Agent Handoff Packet

## Mode

## Scope

- Define the current state and boundaries of the handoff.
- List files, reports, and resources that may be referenced.
- Specify any constraints or prohibited actions.


Context transfer only.

## Current objective

- Goal:
- Current status:
- Last completed step:
- Next safe step:

## Workspace map

- Canonical files:
- Generated reports:
- Tests:
- Files not to touch:

## Evidence chain

- Decisions:
- Reports:
- Hashes:
- Open blockers:

## Agent instructions

- Continue from the current state; do not restart blindly.
- Verify existing work before modifying it.
- Preserve unrelated user changes.
- Ask the maintainer before broad scans, cleanup, commits, or releases.

## Required output

- What was resumed.
- What was changed.
- What was verified.
- What remains.
- Status: `HANDOFF_READY`, `CONTINUED`, `BLOCKED`, or `COMPLETE`.

## No-authority statement

This handoff does not authorize deployment, release, merge, or production changes.

