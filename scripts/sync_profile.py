#!/usr/bin/env python3
"""Recompute article-count stats in the profile README.

Usage:
    python scripts/sync_profile.py [--ai-thoughts DIR] [--history DIR] [--readme FILE]

Safe to run locally or in CI. Only rewrites README.md when the computed
counts differ from what is currently in the file; exits 0 either way so the
workflow can decide whether to commit.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path


def count_docs(root: Path) -> int:
    if not root.is_dir():
        return 0
    docs = root / "docs"
    if not docs.is_dir():
        return 0
    return len(list(docs.glob("*.md")))


def count_indexed(root: Path) -> int:
    """Count articles indexed in the ai-thoughts manifest (articles.yaml)."""
    manifest = root / "articles.yaml"
    if manifest.is_file():
        text = manifest.read_text(encoding="utf-8")
        return len(re.findall(r'path:\s*"docs/[^"]+\.md"', text))
    return count_docs(root)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ai-thoughts", type=Path, default=Path("ai-thoughts"))
    ap.add_argument("--history", type=Path, default=Path("history"))
    ap.add_argument("--readme", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    ai = count_indexed(args.ai_thoughts)
    hist = count_docs(args.history)
    total = ai + hist
    print(f"ai-thoughts indexed: {ai}, history docs: {hist}, total: {total}")

    if ai == 0 and not (args.ai_thoughts / "articles.yaml").is_file():
        print(f"error: no articles found under {args.ai_thoughts}/articles.yaml — aborting",
              file=sys.stderr)
        return 1

    readme = Path(args.readme)
    text = readme.read_text(encoding="utf-8")
    orig = text
    edits: list[str] = []

    def sub(pattern: str, repl: str, desc: str) -> None:
        nonlocal text
        new, n = re.subn(pattern, repl, text)
        if n:
            text = new
            edits.append(desc)

    sub(r"\|\s*\d+\s*technical articles\s*\|",
        f"| {total} technical articles |", "portfolio stats line")
    sub(r"(\[`ai-thoughts`\]\(https://github\.com/negtivspace/ai-thoughts\)[^\n]*?\| )\d+( docs \|)",
        lambda m: f"{m.group(1)}{ai}{m.group(2)}", "ai-thoughts docs row")
    sub(r"(\*\*`history`\*\*[^\n]*?\| )\d+( docs \|)",
        lambda m: f"{m.group(1)}{hist}{m.group(2)}", "history docs row")
    sub(r"(— )\d+( articles on AI, privacy, and entrepreneurship)",
        lambda m: f"{m.group(1)}{ai}{m.group(2)}", "quick links article count")
    sub(r"(See all )\d+( articles at)",
        lambda m: f"{m.group(1)}{ai}{m.group(2)}", "latest-articles count")

    if edits:
        today = _dt.date.today()
        date_str = f"{today:%B} {today.day}, {today.year}"
        sub(r"(\*\*Last Updated:\*\* )[^|]+( \| Tracking: 8 active repos, )\d+( articles,)",
            lambda m: f"{m.group(1)}{date_str}{m.group(2)}{total}{m.group(3)}",
            "last-updated line")

    if text == orig:
        print("README.md up to date — no changes")
        return 0

    readme.write_text(text, encoding="utf-8")
    print("README.md updated:")
    for e in edits:
        print(f"  - {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
