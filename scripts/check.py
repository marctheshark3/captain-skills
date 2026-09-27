#!/usr/bin/env python3
"""Fail closed on skill shape and on strings that must not ship public."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = ("navigator", "captain-order", "make-grade", "make-pass", "miss-check", "cut-bloat", "miss-hunt")
BANNED = (
    "northrop",
    "spark-adb4",
    "tailscale",
    "jenna",
    "zhc.local",
    "wiki-hub",
    ":9093",
    "gabby",
    "neuralyogi",
)

def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise SystemExit("SKILL.md must start with ---")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise SystemExit("frontmatter did not close")
    block = text[4:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        key, _, value = line.partition(":")
        out[key.strip()] = value.strip().strip('"')
    return out


def main() -> int:
    names = sorted(p.name for p in SKILLS.iterdir() if p.is_dir())
    if names != sorted(REQUIRED):
        raise SystemExit(f"skill set drift: {names}")
    blob_parts: list[str] = []
    for name in REQUIRED:
        path = SKILLS / name / "SKILL.md"
        text = path.read_text()
        blob_parts.append(text)
        fm = frontmatter(text)
        if fm.get("name") != name:
            raise SystemExit(f"{name}: name mismatch {fm.get('name')}")
        desc = fm.get("description", "")
        if not desc.startswith("This skill should be used when"):
            raise SystemExit(f"{name}: description is not a trigger")
        if len(desc) > 1024:
            raise SystemExit(f"{name}: description {len(desc)} > 1024")
        if "Do not" not in text and "do not" not in text:
            raise SystemExit(f"{name}: missing a refusal")
    blob = "\n".join(blob_parts).lower()
    readme = (ROOT / "README.md").read_text().lower()
    guide = (ROOT / "docs" / "guide.md").read_text()
    if guide.count("```mermaid") < 4:
        raise SystemExit("docs/guide.md needs the four voyage diagrams")
    blob = blob + "\n" + readme + "\n" + guide.lower()
    for word in BANNED:
        if word in blob:
            raise SystemExit(f"banned string present: {word}")
    if not (ROOT / "templates" / "ORDERS.md").is_file():
        raise SystemExit("missing templates/ORDERS.md")
    print("ok", len(REQUIRED), "skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
