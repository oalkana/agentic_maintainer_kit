# Example Release Packet

## Draft release notes

### Added

- New issue triage template for read-only maintainer workflows.
- Template validator for required safety and evidence sections.

### Fixed

- Clarified that generated reviews do not authorize merge or deployment.

### Internal

- Added unit tests for template hygiene.

## Verification

- `python scripts/validate_templates.py`
- `python -m unittest discover -s tests`

## Known issues

- The validator checks headings only; it does not validate semantic correctness.

## Status

`RELEASE_DRAFT_READY`

## No-authority statement

This draft does not authorize publishing, tagging, deployment, or package release.

