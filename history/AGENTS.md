# AGENTS.md

## Project

Bilingual (English · 中文) repository of historical and literary articles —
Five Dynasties & Ten Kingdoms, silk, *Dream of the Red Chamber*, and Chinese
classical literature. All articles are written in Chinese.

## Working rules

- **Get approval before any change.** Present the plan and wait for the
  user's explicit go-ahead before editing files, generating output, or
  running state-changing commands. If anything is unclear, ask rather than
  assume.
- **Commit only when asked.** Never commit, amend, or push unless the user
  explicitly requests it. When committing, stage only intended files.

## Repository layout

- `docs/` — article Markdown files (follow the `YYMMDD-slug` naming).
- `imgs/` — article images, same `YYMMDD-slug` prefix as the article they
  belong to.
- `README.md` — bilingual index, edited by hand. Keep it in sync whenever
  articles are added, moved, or removed.

## Conventions

- Articles reference images with a relative path (`../imgs/<file>`); keep
  `docs/` and `imgs/` as sibling directories so those links stay valid.
- Chinese articles use Simplified Chinese by default; Traditional Chinese
  only when the article was originally written that way.
- This directory is part of the parent `negtivSpace` repo (no separate git
  history). Do not create a nested `.git` here.
