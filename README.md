# J3ffyang's Portfolio

Building **AI-powered automation skills**, **productivity tools**, and **knowledge systems** for individual developers and AI-native workflows.

---

## 🎯 What I Do

I build and deploy **AI-powered automation skills** that ship to production across multiple platforms.

**Current Portfolio:** 23 published skills | 7 active repos | 69 technical articles | Deployed on OpenClaw, Hermes, Claude Code

I focus on:
- **Skill-based AI orchestration** — turning workflows into reusable, composable skills
- **Multilingual content automation** — English ↔ Chinese/Traditional Chinese
- **Developer productivity tools** — Chrome extensions, CLI utilities, API integrations
- **AI platform experimentation** — deeply hands-on with OpenClaw, Hermes, Claude, and OpenRouter

All code prioritizes **clarity over cleverness**: simple, readable, portable, and easy to fork.

---

## 📑 Table of Contents

- [What I Do](#-what-i-do)
- [Main Repositories](#-main-repositories)
- [Code Highlights](#-code-highlights)
- [Activity Timeline](#-activity-timeline)
- [Tech Stack](#-tech-stack)
- [Design Philosophy](#-design-philosophy)
- [Why This Approach](#-why-this-approach)
- [Getting Started](#-getting-started)
- [Quick Links](#-quick-links)

---

## 📦 Main Repositories

### Core AI Skills & Automation

| Repo | Purpose | Latest | Status |
|------|---------|--------|--------|
| **[`ai-custom-skills`](https://github.com/negtivspace/ai-custom-skills)** | Production-ready skills for [Claude Code](https://claude.ai/code), [Hermes](https://hermes.ai), and [OpenClaw](https://openclaw.ai) — content creation, data export, workflow automation, task orchestration (3 + 13 + 7 skills). | `tidy repo: fix README indexes and links, drop duplicate five-dynasties skill and stale draft` (Aug 2026) | 🔄 Active |

> **Legacy (merged into `ai-custom-skills`):** [`hermes-custom-skills`](https://github.com/negtivspace/hermes-custom-skills) · [`openclaw-custom-skills`](https://github.com/negtivspace/openclaw-custom-skills) · [`claude-custom-skills`](https://github.com/negtivspace/claude-custom-skills)

### Tools & Extensions

| Repo | Purpose | Type | Latest |
|------|---------|------|--------|
| **[`chrome-extensions`](https://github.com/negtivspace/chrome-extensions)** | Monorepo of Chrome extensions: [`sum2chn`](https://github.com/negtivspace/chrome-extensions/tree/main/sum2chn) (translate & summarize web pages → Simplified Chinese MD) · [`twitter2md`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter2md) (X post → Markdown, ext + Node CLI) · [`twitter-bookmark-summarizer`](https://github.com/negtivspace/chrome-extensions/tree/main/twitter-bookmark-summarizer) (summarize tweets via GPT-4o) | Chrome Ext + CLI | `docs: add top-level README and MIT license` (Aug 2026) |

### Writing & Documentation

| Repo | Purpose | Articles | Latest |
|------|---------|----------|--------|
| **[`ai-thoughts`](https://github.com/negtivspace/ai-thoughts)** | Articles & essays: AI platforms (OpenClaw, Hermes), solo entrepreneurship, privacy, technical deep-dives. Bilingual: English + Traditional Chinese | 63 docs | `docs: add opencode-is-best essay, ollama-to-llamacpp draft, and astro-sync skill` (Aug 2026) |
| **[`history`](https://github.com/negtivspace/history)** | Archived bilingual literary articles — Five Dynasties & Ten Kingdoms, silk, *Dream of the Red Chamber*, Zhiyanzhai | 6 docs | Aug 2026 |

### Books, Handbooks & Reference

| Repo | Purpose | Language | Latest |
|------|---------|----------|--------|
| **[`langchain_project_book`](https://github.com/j3ffyang/langchain_project_book)** | Handbook on orchestrating large language models with LangChain | JavaScript | Aug 2025 |
| **[`opensource_devops`](https://github.com/j3ffyang/opensource_devops)** | DevOps handbook & technical guide — conceptual best practices + hands-on guides. Bilingual: English + Simplified Chinese | Ruby | Apr 2026 |
| **[`astro_journal`](https://github.com/j3ffyang/astro_journal)** | Personal blog built on Astro | Astro | Aug 2026 |

---

## 🔍 Code Highlights

### Example: Twitter Bookmarks to Markdown Exporter
**Repo:** `ai-custom-skills` | **Language:** Python | **Purpose:** Parse Twitter bookmarks → individual Markdown files

```python
#!/usr/bin/env python3
"""
Twitter Bookmarks to Markdown Exporter
Parses bookmarks.json (X GraphQL or legacy v1 format) into individual .md files.
"""

import json
import re
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent.parent  # project root
OUT_DIR = SCRIPT_DIR / "output" / "bookmarks"
BOOKMARKS_FILE = SCRIPT_DIR / "bookmarks.json"
```

**Why it matters:** Demonstrates ability to parse complex data structures, handle multiple input formats, and produce clean, organized output.

---

### Example: Claude API Integration for Translation
**Repo:** `chrome-extensions/sum2chn` | **Language:** JavaScript | **Purpose:** Translate & summarize web pages using Claude Sonnet

```javascript
const CLAUDE_API_URL = 'https://api.anthropic.com/v1/messages';
const CLAUDE_MODEL = 'claude-sonnet-4-6';

const TRANSLATION_SYSTEM_PROMPT = `You are a professional translator and technical writer specializing in Simplified Chinese (简体中文).

Process the provided English web page content and produce a high-quality Chinese document by following these steps:

1. TRANSLATION: Translate all English content faithfully and accurately into Simplified Chinese.
2. GRAMMAR & STYLE: Improve the Chinese text for natural fluency.
3. REORGANIZATION: Improve readability and logical flow.
4. SUMMARIZATION: Condense repetitive content without losing key information.
5. MARKDOWN FORMAT: Output in standard Markdown format with proper headings and code blocks.
```

**Why it matters:** Shows hands-on experience with Claude API, prompt engineering, and production-level system prompts.

---

## 📈 Activity Timeline

### Q3 2026 (Current)
- **Aug 4:** Merged the three Chrome extensions (`sum2chn`, `twitter2md`, `twitter-bookmark-summarizer`) into a single `chrome-extensions` monorepo
- **Aug 3:** Published "OpenCode is Best for Me" and added the Ollama → llama.cpp draft to `ai-thoughts`; tidied `ai-custom-skills` (fixed README indexes/links, dropped a duplicate skill)
- **Aug 2:** Archived 4 literary articles into `history/`; normalized `YYMMDD-slug` naming across `ai-thoughts` docs & images
- **Jul 22:** Published "Unknown Unknowns" on the four types of knowledge
- **Jul 21:** Published "Build Your Own AI-Powered Wiki" (Obsidian + Karpathy LLM Wiki + Ollama)
- **Jul 6:** Added Brave browser privacy analysis (bilingual) to `ai-thoughts`

**Current Focus:**
- Expanding Hermes Agent skill library
- Building bilingual content automation pipelines
- Documenting OpenClaw security patterns

### Q2 2026
- **Jun:** Published DCS joystick-tuning guide and "immutable OS strategy" essay; wrote the "2nd Brain" design doc
- **May:** Hermes tutorials in `ai-thoughts` — SOUL.md, free-model connection, skill install workflow, backup guide
- **Apr:** Published first Hermes Agent articles and tutorials in `ai-thoughts`

### Q1 2026
- **Mar 10:** Released v1 of `sum2chn` Chrome extension (translation + summarization)
- **Mar:** Established `openclaw-custom-skills` repo on ClawHub
- **Feb 24:** Released `twitter2md` for X post extraction as Markdown (Chrome extension + Node CLI)
- **Feb 20:** Refactored `twitterBookmarkSum` to popup-triggered summarization
- **Feb:** Began deep-dive experimentation with OpenClaw and Hermes platforms

---

## 🛠️ Tech Stack

**Programming:** Python, JavaScript, TypeScript, Bash

**AI Platforms:** [OpenClaw](https://openclaw.ai), [Hermes Agent](https://hermes.ai), [Claude Code](https://claude.ai/code), [OpenRouter](https://openrouter.ai)

**APIs & Services:** Anthropic Claude (Sonnet, Opus), OpenAI GPT-4o, Twitter/X API v2, Chrome Extension APIs, Web scraping & DOM manipulation

**DevOps:** Git + GitHub, Node.js + npm, Python 3.10+, Markdown-first documentation

---

## 💡 Design Philosophy

1. **Skills > Projects** — I think in workflows. Every tool becomes a reusable skill.
2. **Multilingual by default** — English + Chinese (Simplified + Traditional)
3. **Code clarity wins** — Readable Python/JS beats clever one-liners. Always.
4. **Composition over bloat** — Small, focused repos that work well together.
5. **Learn in public** — Detailed articles about what works (and what doesn't).

---

## 🎓 Why This Approach

I've found that **skill-based thinking** scales better than project-based thinking:

- **Skills are composable** — combine multiple skills to solve new problems
- **Platforms evolve** — Claude Code, OpenClaw, and Hermes are all 2025-2026 products; shipping skills across all three future-proofs my work
- **Multilingual content** — 40%+ of my audience is Chinese-speaking; this isn't optional, it's essential
- **Learn in public** — writing about the journey attracts collaborators and opportunities

---

## 🔗 Quick Links

**GitHub Accounts:**
- **[@negtivspace](https://github.com/negtivspace)** — Published skills & tools
- **[@j3ffyang](https://github.com/j3ffyang)** — Personal portfolio, articles, experiments

**Resources:**
- **Blog:** [`ai-thoughts`](https://github.com/negtivspace/ai-thoughts) — 63 articles on AI, privacy, and entrepreneurship (+4 literary articles archived in [`history`](https://github.com/negtivspace/history))
- **References:** [`langchain_project_book`](https://github.com/j3ffyang/langchain_project_book) (LangChain handbook) · [`opensource_devops`](https://github.com/j3ffyang/opensource_devops) (DevOps handbook) · [`astro_journal`](https://github.com/j3ffyang/astro_journal) (personal blog)
- **Gists:** [Personal experiments](https://gist.github.com/j3ffyang)

---

## 📝 Latest Articles

From `ai-thoughts` (recent posts):

1. **"Arch Linux + Hyprland on GPD Win4 with iGPU + eGPU"** (Aug 2026) — Arch Linux + Hyprland on GPD Win4 with dual AMD GPUs — iGPU + eGPU (RX 7600M XT via OCuLink) rendering offload, verification commands, and stable DRM symlinks
2. **"OpenCode is Best for Me"** (Aug 2026) — Personal essay on why OpenCode is the best AI agent setup for me — vendor freedom, the big-pickle model, enforced conventions, and unified billing via OpenRouter
3. **"Clean Up Bloated Skills & Plugins in Hermes ⚚"** (Jul 2026) — Guide to cleaning up bloated skills & plugins in Hermes Agent — list enabled skills, opt out of bundled skills, and revert anytime
4. **"Unknown Unknowns"** (Jul 2026) — Personal essay on the four types of knowledge — known knowns, known unknowns, unknown knowns, and the unknown unknowns that shape our lives
5. **"Build Your Own AI-Powered Wiki with Obsidian + Karpathy LLM Wiki + Ollama"** (Jul 2026) — Build your own AI-powered wiki with Obsidian + Karpathy LLM Wiki + Ollama — query your personal vault with a local LLM

👉 See all 63 articles at **[ai-thoughts/docs](https://github.com/negtivspace/ai-thoughts/tree/main/docs)**

---

## 🚀 Getting Started

### Clone a Skill Repo
```bash
git clone https://github.com/negtivspace/ai-custom-skills
cd ai-custom-skills
# Follow README for your specific platform (Claude Code / Hermes / OpenClaw)
```

### Try a Tool
```bash
# Chrome extensions monorepo (twitter2md, sum2chn, twitter-bookmark-summarizer)
git clone https://github.com/negtivspace/chrome-extensions
cd chrome-extensions/twitter2md
npm install
npm run build  # or load the extension manually in Chrome
```

### Read Articles
```bash
git clone https://github.com/negtivspace/ai-thoughts
cd docs
# 63 articles: AI platforms, privacy, solo entrepreneurship, technical deep-dives
```

---

## 💬 Let's Connect

- **Collaborate on skills?** Open an issue in any repo
- **Need a custom skill?** Check the individual repo's CONTRIBUTING.md
- **Have feedback?** File an issue or ping me on GitHub

**Current availability:** Available for OpenClaw/Hermes/Claude Code skill requests

---

## 📄 License

Most repos are **MIT License** — see individual repos for details.

---

**Last Updated:** August 8, 2026 | Tracking: 7 active repos, 69 articles, 23 published skills
