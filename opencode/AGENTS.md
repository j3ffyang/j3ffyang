# AGENTS.md — global rules

Universal working rules that apply to every opencode session, across all `negtivSpace` repos and submodules. Loaded together with each project's local `AGENTS.md`. This file is the git-managed source of truth for `~/.config/opencode/AGENTS.md` (symlinked).

## Working rules

- **Get approval before any change.** Present the plan and wait for the user's explicit go-ahead before editing files, generating output, or running state-changing commands. If anything is unclear, ask rather than assume.
- **Commit only when asked.** Never commit, amend, or push unless the user explicitly requests it. When committing, stage only intended files and follow the repo's `type: subject` commit style (e.g. `docs: ...`, `ci: ...`).
- **NEVER commit secrets or API keys.** Before staging, scan for hardcoded credentials (`sk-*`, `sk-or-v1-*`, `AIza*`, `gh*_*`, `github_pat_*`, `Bearer <token>`) and never stage `.env`, `.pem`, `.key`, or credential files. Use repo/CI secrets (`${{ secrets.X }}`) instead of literals. If a real key is ever found already committed to a public repo, say so immediately and suggest rotation.
- **NEVER poison a working tree with scratch artifacts.** Throwaway clones, test checkouts, and any temporary git artifact belong in `/tmp/opencode/` — NEVER inside `~/pool/git/**` or any managed repo. A stray nested repo corrupts `git status`, breaks project-root detection, and litters the workspace (this already happened once: a profile-sync clone left behind in `negtivSpace/` on 2026-08-17). If one exists, remove it before finishing the task; if the task needs a working copy of another repo, clone it to `/tmp/opencode/` and delete it when done.
- **Push to both remotes** on `main` for repos under `negtivSpace`: `j3ffyang` and `negtivspace`. `negtivspace` is a normal GitHub **user account** (a second personal account, "Negative Space 留白"), not an org — editing `negtivspace/*` via `gh`/API requires that account's own token.
- **Give HONEST answers.** Do not assume, do not guess. If you don't know or aren't sure, say so and verify before claiming.
- **Find ground truth when possible.** Verify claims against the actual source of truth — installed system state, files on disk, upstream docs/wiki/source code — instead of relying on memory or inference. When verification isn't possible, say so explicitly.
- **Ensure all changes can be rolled back.** If the change is wrong, there must be a clear way to revert it.

## Collaboration model — the thought-flow loop

We collaborate through an 8-stage loop. Keep it in mind for every task: INTENT → CONSTRAINTS → PROPOSE → PRESS → PRACTICE → INVESTIGATE → CODIFY → BOUNDARY-CHECK. The loop is not a rigid process — it is an architecture of thought-flow, a loop that converges. The `thought-flow` skill lives in `ai-thoughts/.opencode/skills/` and loads only in `ai-thoughts` sessions (skills are visible only up to their git worktree root); here it is summarized as the eight rules below.

- **Intent (1) and Constraints (2) are the most expensive stages.** State them plainly up front; a precise description beats a better model. Spending ten minutes stating constraints saves an hour of rework.
- **Propose (3) with options + a recommendation.** A plan with only one path is a demand, not a proposal. Include the tradeoffs so the user can disagree meaningfully.
- **Press (4) is negotiation, not conflict.** When the user pushes back, do not just argue and do not just agree — look for a third option that respects the real constraints. The best outcomes are neither the agent's first idea nor the user's, but a compromise that holds.
- **Practice (5) is where the loop is honest.** Approve, build, run, observe. Real failures live here.
- **Investigate (6) before blaming.** When something looks broken, verify against the real system first — read the upstream source, call the API, check the live state — before concluding the tool or workflow is wrong. An error message is a clue, not a conclusion.
- **Codify (7) what works.** A procedure that works twice becomes a candidate for a SKILL.md. A rule true for a whole repo becomes an AGENTS.md entry. Skill for the procedure, AGENTS.md for the constitution.
- **Boundary-check (8) is the meta-skill.** Where knowledge lives — which repo, which worktree, which file — determines whether it is specific enough to be useful and small enough to be maintained. OpenCode loads skills only up to the git worktree root: a parent-level skill is invisible inside a sub-repo session. Put knowledge where the work happens.
- **Prefer `gh` and the API for verification.** `gh run watch`, `gh run view --log`, `gh api`, and `curl` against live endpoints beat clicking around the UI. The API is the primary way to verify; the registry's own report can be wrong.

## Writing conventions

- **OpenCode capitalization.** Use `OpenCode` (capital O/C) when referring to the product, company, or brand; keep `opencode` all-lowercase for the command/binary and in code and config.
- **Brand glyph icons.** Hermes Agent → `⚕` (U+2695), but the `hermes` command gets no glyph; OpenClaw → `🦞` (U+1F99E); OpenCode → `◧` (U+25E7, temporary), but the `opencode` command gets no glyph; Arch Linux → `` (U+F303, `nf-linux-archlinux`).
- **Prose wrapping is per-repo.** Follow each repo's AGENTS.md — `ai-thoughts` requires no hard-wrap (one paragraph per line, verified with its `scripts/unwrap_md.py`), `history` auto-wraps. Never assume a global wrapping rule.

## OpenCode permissions

Permission rules live in `~/.config/opencode/opencode.jsonc` (a symlink to `negtivSpace/opencode/opencode.jsonc`, single source of truth): read-only shell/git/gh commands are pre-approved and run silently, destructive/state-changing commands prompt (`ask`), and everything else falls through to OpenCode's permissive defaults — it runs without prompting. `edit` prompts. The TUI's "Accept always" only lasts for the current session — permanent rules go in that config file. Config changes require an opencode restart.
