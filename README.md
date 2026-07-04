
# Agentic Maintainer Kit

Small, reusable workflow templates for open-source maintainers who use coding agents for issue triage, pull-request review, security review, release preparation, and cross-agent handoff.

The kit is intentionally conservative. It helps agents produce evidence-backed maintenance reports without taking unsafe actions, changing project authority, or hiding uncertainty.

## Why this exists

Open-source maintainers often lose time restating context for every issue, review, or release. Agentic tools can help, but only when the task packet is scoped, the evidence chain is explicit, and the output avoids pretending that a review is an approval.

This repository provides:

- task templates for common maintainer workflows;
- evidence-first report formats;
- no-run and read-only modes for sensitive reviews;
- a lightweight validator that checks template hygiene;
- example packets that can be adapted for real repositories.

## Workflows

- Pull request review
- Issue triage
- Security review handoff
- Release notes preparation
- Evidence memo
- Agent handoff

## Quickstart

Copy a template from `templates/`, fill in the scope, and give it to Codex or another coding agent.

Run the validator:

```powershell
python scripts/validate_templates.py
```

Run tests:

```powershell
python -m unittest discover -s tests
```

## Safety posture

The templates default to narrow, reversible maintenance work:

- no production deployment;
- no secret access unless explicitly authorized;
- no destructive cleanup;
- no broad scans when an exact path is provided;
- no commit, push, or release unless the maintainer explicitly asks;
- findings must cite files, lines, commands, or reports.

## Project status

Early public-ready scaffold for OSS maintainer workflow experimentation.




