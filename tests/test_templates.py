from __future__ import annotations

import unittest

from scripts.validate_templates import validate_all


class TemplateValidationTest(unittest.TestCase):
    def test_templates_have_required_sections(self) -> None:
        self.assertEqual(validate_all(), [])


if __name__ == "__main__":
    unittest.main()

