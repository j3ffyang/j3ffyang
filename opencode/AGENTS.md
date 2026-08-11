# AGENTS.md — global rules

Universal working rules that apply to every opencode session, across all `negtivSpace` repos and submodules. Loaded together with each project's local `AGENTS.md`. This file is the git-managed source of truth for `~/.config/opencode/AGENTS.md` (symlinked).

## Working rules

- **Get approval before any change.** Present the plan and wait for the user's explicit go-ahead before editing files, generating output, or running state-changing commands. If anything is unclear, ask rather than assume.
- **Commit only when asked.** Never commit, amend, or push unless the user explicitly requests it. When committing, stage only intended files and follow the repo's `type: subject` commit style (e.g. `docs: ...`, `ci: ...`).
- **Push to both remotes** on `main` for repos under `negtivSpace`: `j3ffyang` and `negtivspace`. `negtivspace` is a normal GitHub **user account** (a second personal account, "Negative Space 留白"), not an org — editing `negtivspace/*` via `gh`/API requires that account's own token.
- **Give HONEST answers.** Do not assume, do not guess. If you don't know or aren't sure, say so and verify before claiming.
- **Find ground truth when possible.** Verify claims against the actual source of truth — installed system state, files on disk, upstream docs/wiki/source code — instead of relying on memory or inference. When verification isn't possible, say so explicitly.
- **Ensure all changes can be rolled back.** If the change is wrong, there must be a clear way to revert it.

## Writing conventions

- **OpenCode capitalization.** Use `OpenCode` (capital O/C) when referring to the product, company, or brand; keep `opencode` all-lowercase for the command/binary and in code and config.
- **Brand glyph icons.** Hermes Agent → `⚕` (U+2695), but the `hermes` command gets no glyph; OpenClaw → `🦞` (U+1F99E); OpenCode → `◧` (U+25E7, temporary), but the `opencode` command gets no glyph; Arch Linux → `` (U+F303, `nf-linux-archlinux`).
- **Prose wrapping is per-repo.** Follow each repo's AGENTS.md — `ai-thoughts` requires no hard-wrap (one paragraph per line, verified with its `scripts/unwrap_md.py`), `history` auto-wraps. Never assume a global wrapping rule.

## OpenCode permissions

Permission rules live in `~/.config/opencode/opencode.jsonc` (a symlink to `negtivSpace/opencode/opencode.jsonc`, single source of truth): read-only shell/git/gh commands are pre-approved and run silently, destructive/state-changing commands prompt (`ask`), and everything else falls through to OpenCode's permissive defaults — it runs without prompting. `edit` prompts. The TUI's "Accept always" only lasts for the current session — permanent rules go in that config file. Config changes require an opencode restart.
