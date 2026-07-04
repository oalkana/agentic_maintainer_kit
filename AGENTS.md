# AGENTS.md

This repository contains maintainer workflow templates. Agents working here should preserve clarity, evidence, and maintainer authority.

## Default rules

- Prefer exact-path reads over broad scans.
- Do not access secrets, private data, production systems, or external services unless the maintainer explicitly authorizes it.
- Do not commit, push, publish, release, or delete files unless explicitly requested.
- Treat generated reports as decision support, not final maintainer approval.
- Lead reviews with findings and cite file paths, line numbers, command output, or report names.
- If evidence is missing, say so directly.

## Verification

Use:

```powershell
python scripts/validate_templates.py
python -m unittest discover -s tests
```

## Output standard

Every substantial task should include:

- scope;
- files read;
- files changed;
- evidence pointers;
- result status;
- residual risk;
- explicit no-authority statement when relevant.

