from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates"

REQUIRED_HEADINGS = [
    "## Mode",
    "## Scope",
    "## Agent instructions",
    "## Evidence chain",
    "## Required output",
    "## No-authority statement",
]


def validate_template(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in text]
    return [f"{path.relative_to(ROOT)} missing {heading}" for heading in missing]


def validate_all() -> list[str]:
    errors: list[str] = []
    for path in sorted(TEMPLATE_DIR.glob("*.md")):
        errors.extend(validate_template(path))
    if not list(TEMPLATE_DIR.glob("*.md")):
        errors.append("templates directory has no markdown templates")
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("template validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

