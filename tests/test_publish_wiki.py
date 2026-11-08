#!/usr/bin/env python3
"""Regression tests for Wiki URL rewriting."""
import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("publish_wiki", ROOT / "scripts" / "publish_wiki.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class WikiLinkTests(unittest.TestCase):
    def test_percent_encoded_image_filename_is_not_double_encoded(self):
        origin = ROOT / "docs" / "wiki" / "getting-oriented.md"
        source = "![System breakdown](../assets/branding/Open%20MABEL%20Safety%20System%20Breakdown-2.png)"
        rendered = module.rewrite(source, origin)
        self.assertIn("Open%20MABEL%20Safety%20System%20Breakdown-2.png", rendered)
        self.assertNotIn("%2520", rendered)
        self.assertIn("raw.githubusercontent.com", rendered)

    def test_angle_bracket_image_with_spaces(self):
        origin = ROOT / "docs" / "wiki" / "safety-architecture.md"
        rendered = module.rewrite("![Architecture](<../assets/branding/Open MABEL Safety Architecture-1.png>)", origin)
        self.assertIn("Open%20MABEL%20Safety%20Architecture-1.png", rendered)

    def test_wiki_page_link(self):
        origin = ROOT / "docs" / "wiki" / "getting-oriented.md"
        rendered = module.rewrite("[Home](README.md)", origin)
        self.assertEqual(rendered, "[Home](https://github.com/TomcoGame/Open-MABEL-Safety-Edition/wiki/Home)")

if __name__ == "__main__":
    unittest.main()
