#!/usr/bin/env python3
"""Build GitHub Wiki pages from version-controlled docs/wiki source.

Run: python3 scripts/publish_wiki.py --output /tmp/mabel-wiki-pages
Images stay in the main repository and are linked via raw.githubusercontent.com.
"""
import argparse
import pathlib
import re
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "wiki"
REPO = "TomcoGame/Open-MABEL-Safety-Edition"
WIKI = f"https://github.com/{REPO}/wiki"
BLOB = f"https://github.com/{REPO}/blob/main"
RAW = f"https://raw.githubusercontent.com/{REPO}/main"
PAGE_NAMES = {
    "README.md": "Home",
    "getting-oriented.md": "Getting-Oriented",
    "risk-assessment.md": "Risk-Assessment",
    "safety-architecture.md": "Safety-Architecture",
    "safety-requirements.md": "Safety-Requirements",
    "verification-evidence.md": "Verification-and-Evidence",
    "visual-authoring-guide.md": "Visual-Authoring-Guide",
}
LINK = re.compile(r"(!?\[[^\]]*\])\((<[^>]*>|[^)]*)\)")

def rewrite(text, origin):
    def replace(match):
        label, target = match.groups()
        target = target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if target.startswith(("https://", "http://", "#", "mailto:")):
            return match.group(0)
        anchor = ""
        if "#" in target:
            target, fragment = target.split("#", 1)
            anchor = "#" + fragment
        resolved = (origin.parent / target).resolve() if target else origin
        if not resolved.is_relative_to(ROOT):
            raise ValueError(f"Link escapes repository: {origin} -> {target}")
        if resolved.parent == SOURCE and resolved.name in PAGE_NAMES:
            url = f"{WIKI}/{PAGE_NAMES[resolved.name]}{anchor}"
        else:
            rel = resolved.relative_to(ROOT).as_posix()
            url = f"{RAW if label.startswith('!') else BLOB}/{quote(rel, safe='/')}{anchor}"
        return f"{label}({url})"
    return LINK.sub(replace, text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    dest = pathlib.Path(args.output)
    dest.mkdir(parents=True, exist_ok=True)
    for filename, slug in PAGE_NAMES.items():
        source = SOURCE / filename
        if not source.is_file():
            raise FileNotFoundError(source)
        text = rewrite(source.read_text(encoding="utf-8"), source)
        (dest / (slug + ".md")).write_text(text, encoding="utf-8")
    sidebar = """### Open MABEL Safety Edition

- [Home](Home)
- [Getting oriented](Getting-Oriented)
- [Risk assessment](Risk-Assessment)
- [Safety requirements](Safety-Requirements)
- [Safety architecture](Safety-Architecture)
- [Verification & evidence](Verification-and-Evidence)
- [Visual authoring guide](Visual-Authoring-Guide)

---

[Source repository](https://github.com/TomcoGame/Open-MABEL-Safety-Edition)
"""
    (dest / "_Sidebar.md").write_text(sidebar, encoding="utf-8")
    footer = "[Open MABEL Safety Edition](https://github.com/TomcoGame/Open-MABEL-Safety-Edition) · Safety-Enabled Robotics · [Documentation source](https://github.com/TomcoGame/Open-MABEL-Safety-Edition/tree/main/docs/wiki)\n"
    (dest / "_Footer.md").write_text(footer, encoding="utf-8")
    print(f"Prepared {len(PAGE_NAMES)} pages and wiki navigation in {dest}")

if __name__ == "__main__":
    main()
