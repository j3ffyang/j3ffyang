# AGENTS.md

## Project

`negtivSpace` is the repository behind the GitHub profile pages for two
**user accounts** — `j3ffyang` and `negtivspace`. The root `README.md` is
rendered as the profile page for both accounts (mirrored to
`j3ffyang/j3ffyang` and `negtivspace/negtivspace`). The repo also hosts
nested projects (`ai-thoughts`, `ai-custom-skills`, ...) and the `history/`
archive.

## Working rules

- **Get approval before any change.** Present the plan and wait for the
  user's explicit go-ahead before editing files, generating output, or
  running state-changing commands. If anything is unclear, ask rather than
  assume.
- **Commit only when asked.** Never commit, amend, or push unless the user
  explicitly requests it. When committing, stage only intended files.
- **Push to both remotes** on `main`: `j3ffyang` and `negtivspace`.

## Profile README sync

The root `README.md` is the GitHub profile page for both accounts — keep it in
sync whenever anything underneath this repo changes.

**Trigger conditions** (any of these):
- Articles added or removed in `ai-thoughts/` or `history/`
- Submodule pointers updated (`ai-thoughts`, `ai-custom-skills`, ...)
- New repos or tools published
- Stats in the README no longer match reality

**Refresh checklist:**
1. Article counts: `ls ai-thoughts/docs/*.md | wc -l` and
   `ls history/docs/*.md | wc -l`
2. Update: portfolio stats line, Writing & Documentation table, Quick Links,
   Latest Articles list, Activity Timeline, and the "Last Updated" date.
3. Commit `README.md` and push to **both** remotes (`j3ffyang`,
   `negtivspace`).

**Automation (`.github/workflows/profile-sync.yml`):**
- Runs on every push to `main`: clones `ai-thoughts` and `history`, recomputes
  the article counts via `scripts/sync_profile.py`, and commits the refreshed
  `README.md` back. Counts come from `ai-thoughts/articles.yaml` (indexed
  articles) + `history/docs/*.md`; drafts not yet in the manifest are excluded.
- To also auto-sync the **other** account's profile repo, set a
  `PROFILE_SYNC_TOKEN` repository secret (a PAT with write access to both
  `j3ffyang/j3ffyang` and `negtivspace/negtivspace`) in **both** repos. Without
  it, the action only updates the repo that ran it — push to both remotes
  manually as above.

**Gotchas:**
- After renaming the `j3ffyang` repo to match the username, the README did not
  auto-render on the profile — the **Share to profile** toggle in the repo's
  right sidebar (About) had to be clicked first. Even a post-July-2020 repo can
  need this after a rename. If the README doesn't show on the profile, check
  that toggle.

## Repository layout

- Root `README.md` — profile page for both accounts (hand-edited; see "Profile
  README sync").
- `ai-thoughts/` — separate git repo (submodule), AI/tech articles.
- `history/` — separate git repo (submodule), archived literary articles.
- Other nested repos (`ai-custom-skills`, `sum2chn`, `twitterBookmarkSum`,
  `twitter2md`) — separate git repos with their own remotes; only their
  gitlink pointers are recorded here.
