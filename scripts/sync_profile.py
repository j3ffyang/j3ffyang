#!/usr/bin/env python3
"""Recompute the profile README so its numbers never drift.

Derived from the single sources of truth in the nested repos:

  * article count   — ai-thoughts/articles.yaml (+ history/docs/*.md)
  * skill count     — platform dirs under ai-custom-skills
  * active repos    — repo rows in the README's "Main Repositories" tables
  * latest articles — top 5 published (non-draft) English articles, titles
                      read from each doc's first H1, descriptions from yaml

Usage:
    python scripts/sync_profile.py [--ai-thoughts DIR] [--history DIR]
        [--ai-custom-skills DIR] [--readme FILE]

Exits 1 if any expected README pattern fails to match, so CI alerts on drift
instead of silently going stale. Exits 0 otherwise, whether or not the README
was rewritten.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
import sys
from pathlib import Path

MONTHS = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
]


# --------------------------------------------------------------------------- #
# Counts
# --------------------------------------------------------------------------- #

def count_docs(root: Path) -> int:
    """Number of *.md files under <root>/docs (history-style repos)."""
    if not root.is_dir():
        return 0
    docs = root / "docs"
    if not docs.is_dir():
        return 0
    return len(list(docs.glob("*.md")))


def count_indexed(root: Path) -> int:
    """Number of rows in the ai-thoughts manifest (articles.yaml)."""
    manifest = root / "articles.yaml"
    if manifest.is_file():
        text = manifest.read_text(encoding="utf-8")
        return len(re.findall(r'path:\s*"docs/[^"]+\.md"', text))
    return count_docs(root)


def count_skills(root: Path) -> int:
    """Number of skill dirs across the ai-custom-skills platform folders."""
    if not root.is_dir():
        return 0
    total = 0
    for platform in ("claude-code", "openclaw", "hermes"):
        total += sum(1 for d in (root / platform).glob("*") if d.is_dir())
    return total


def count_repos(text: str) -> int:
    """Number of repo rows in the 'Main Repositories' section of the README."""
    m = re.search(r"## 📦 Main Repositories(.*?)## 🔍 Code Highlights", text, re.S)
    if not m:
        return 0
    return len(re.findall(r"^\|\s+\*\*\[", m.group(1), re.M))


# --------------------------------------------------------------------------- #
# Latest articles
# --------------------------------------------------------------------------- #

def _extract_articles(manifest: Path) -> list[dict]:
    """Parse articles.yaml into published-EN article rows.

    Returns dicts with keys: path, title_fallback, desc, date (yyyymmdd int
    or 0), year, month.
    """
    text = manifest.read_text(encoding="utf-8")
    rows: list[dict] = []

    for block in re.split(r"\n(?=  - section:)", text):
        sec = re.search(r"^\s*- section: (\w+)", block, re.M)
        st = re.search(r"^\s*status: (\w+)", block, re.M)
        if not sec or not st:
            continue
        if sec.group(1) == "drafts" or st.group(1) != "published":
            continue

        en = re.findall(r'path: "docs/([^"]+\.md)", lang: en', block)
        if not en:
            continue

        desc_m = re.search(r'desc_en: "((?:[^"\\]|\\.)*)"', block)
        path = en[0]
        label = re.search(r'label: "([^"]*)"', block)
        rows.append({
            "path": path,
            "label": label.group(1) if label else "",
            "desc": desc_m.group(1).replace(r"\"", '"') if desc_m else "",
            "date": _date_key(path),
        })
    return rows


def _date_key(path: str) -> int:
    m = re.match(r"(\d{6})-", path)
    return int(m.group(1)) if m else 0


def _title_for(doc: Path, fallback: str) -> str:
    """First H1 heading of the article, else the yaml label."""
    try:
        for line in doc.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^#\s+(.+?)\s*$", line)
            if m:
                return m.group(1).strip()
    except OSError:
        pass
    return fallback


def latest_articles(ai_thoughts: Path, limit: int = 5) -> list[str]:
    """Render the top-5 newest published English articles as list lines."""
    manifest = ai_thoughts / "articles.yaml"
    if not manifest.is_file():
        print(f"error: {manifest} not found — aborting", file=sys.stderr)
        return []

    rows = sorted(_extract_articles(manifest), key=lambda r: r["date"], reverse=True)
    lines = []
    for i, row in enumerate(rows[:limit], start=1):
        date = row["date"]
        if date:
            year = 2000 + date // 10000
            month = MONTHS[(date // 100) % 100 - 1]
            when = f"({month} {year})"
        else:
            when = "(date unknown)"

        title = _title_for(ai_thoughts / "docs" / row["path"], row["label"])
        desc = f" — {row['desc']}" if row["desc"] else ""
        lines.append(f'{i}. **"{title}"** {when}{desc}')
    return lines


# --------------------------------------------------------------------------- #
# README rewriting
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ai-thoughts", type=Path, default=Path("ai-thoughts"))
    ap.add_argument("--history", type=Path, default=Path("history"))
    ap.add_argument("--ai-custom-skills", type=Path, default=Path("ai-custom-skills"))
    ap.add_argument("--readme", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    ai = count_indexed(args.ai_thoughts)
    hist = count_docs(args.history)
    total = ai + hist
    skills = count_skills(args.ai_custom_skills)
    print(f"ai-thoughts indexed: {ai}, history docs: {hist}, total: {total}, "
          f"skills: {skills}")

    if not (args.ai_thoughts / "articles.yaml").is_file():
        print(f"error: no articles found under {args.ai_thoughts}/articles.yaml — aborting",
              file=sys.stderr)
        return 1

    readme = Path(args.readme)
    text = readme.read_text(encoding="utf-8")
    orig = text
    repos = count_repos(text)
    if repos == 0:
        print("error: could not find 'Main Repositories' section in README — aborting",
              file=sys.stderr)
        return 1

    subs: list[tuple[str, str, str]] = [
        # banner
        (r"(\*\*Current Portfolio:\*\* )\d+( published skills \| )",
         lambda m: f"{m.group(1)}{skills}{m.group(2)}", "banner skills count"),
        (r"(published skills \| )\d+( active repos \| )",
         lambda m: f"{m.group(1)}{repos}{m.group(2)}", "banner repos count"),
        (r"(active repos \| )\d+( technical articles \| )",
         lambda m: f"{m.group(1)}{total}{m.group(2)}", "banner article count"),
        # repo tables
        (r"(\[`ai-thoughts`\]\(https://github\.com/negtivspace/ai-thoughts\)[^\n]*?\| )\d+( docs \|)",
         lambda m: f"{m.group(1)}{ai}{m.group(2)}", "ai-thoughts docs row"),
        (r"(\[`history`\]\(https://github\.com/negtivspace/history\)[^\n]*?\| )\d+( docs \|)",
         lambda m: f"{m.group(1)}{hist}{m.group(2)}", "history docs row"),
        # quick links + latest-articles count
        (r"(— )\d+( articles on AI, privacy, and entrepreneurship)",
         lambda m: f"{m.group(1)}{ai}{m.group(2)}", "quick links article count"),
        (r"(See all )\d+( articles at)",
         lambda m: f"{m.group(1)}{ai}{m.group(2)}", "latest-articles count"),
        # getting started
        (r"(cd docs\n# )\d+( articles:)",
         lambda m: f"{m.group(1)}{ai}{m.group(2)}", "getting-started article count"),
        # footer counts
        (r"(Tracking: )\d+( active repos, )",
         lambda m: f"{m.group(1)}{repos}{m.group(2)}", "footer repos count"),
        (r"(active repos, )\d+( articles, )",
         lambda m: f"{m.group(1)}{total}{m.group(2)}", "footer article count"),
        (r"(articles, )\d+\+?( published skills)",
         lambda m: f"{m.group(1)}{skills}{m.group(2)}", "footer skills count"),
    ]

    edits: list[str] = []
    failures: list[str] = []

    def apply(pattern: str, repl: str, desc: str, flags: int = 0) -> None:
        nonlocal text
        new, n = re.subn(pattern, repl, text, flags=flags)
        if n:
            text = new
            edits.append(desc)
        else:
            failures.append(desc)

    for pattern, repl, desc in subs:
        apply(pattern, repl, desc)

    # Regenerate the Latest Articles list (kept from drifting, never hand-edited).
    articles = latest_articles(args.ai_thoughts)
    if articles:
        items = "\n".join(articles) + "\n"
        apply(
            r"(From `ai-thoughts` \(recent posts\):\n\n).*?(?=\n👉 See all)",
            lambda m: m.group(1) + items,
            "latest-articles list",
            flags=re.DOTALL,
        )
    else:
        failures.append("latest-articles list (no published English articles found)")

    # Only bump "Last Updated" when something actually changed.
    if edits:
        today = _dt.date.today()
        apply(
            r"(\*\*Last Updated:\*\* )[^|]+(\| Tracking:)",
            lambda m: f"{m.group(1)}{today:%B} {today.day}, {today.year} {m.group(2)}",
            "last-updated date",
        )

    if failures:
        print("error: the following README sections could not be matched:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        print("Refusing to rewrite a README with mismatched sections.", file=sys.stderr)
        return 1

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
