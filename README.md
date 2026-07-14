# J3ffyang's Portfolio

Building **AI-powered automation skills**, **productivity tools**, and **knowledge systems** for individual developers and AI-native workflows.

---

## 🎯 What I Do

I build and deploy **AI-powered automation skills** that ship to production across multiple platforms.

**Current Portfolio:** 21 published skills | 8 active repos | 59 technical articles | Deployed on OpenClaw, Hermes, Claude Code

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
| **[`ai-custom-skills`](https://github.com/negtivspace/ai-custom-skills)** | Production-ready skills for multiple platforms (Claude Code, Hermes, OpenClaw). Covers content creation, data export, workflow automation. | `add new skill and tidy up the repo` (Jul 2026) | 🔄 Active |
| **[`hermes-custom-skills`](https://github.com/negtivspace/hermes-custom-skills)** | Specialized skills for [Hermes Agent](https://hermes.ai) — autonomous workflows, content generation, task orchestration. | `docs: add README and CONTRIBUTING` (Jul 2026) | 🔄 Active |
| **[`openclaw-custom-skills`](https://github.com/negtivspace/openclaw-custom-skills)** | Production skills for [OpenClaw](https://openclaw.ai) published to ClawHub. Multilingual blog publishing, media generation. | `add chinese edition` (Jul 2026) | 🔄 Active |
| **[`claude-custom-skills`](https://github.com/negtivspace/claude-custom-skills)** | Automation skills for [Claude Code](https://claude.ai) — productivity hacks, data export, content workflows. | `add i18n support to README` (Jul 2026) | ✨ Stable |

### Tools & Extensions

| Repo | Purpose | Type | Latest |
|------|---------|------|--------|
| **[`sum2chn`](https://github.com/negtivspace/sum2chn)** | Chrome extension: translate & summarize English web pages → Simplified Chinese Markdown | Chrome Ext | `Initial release` (Jul 2026) |
| **[`twitter2md`](https://github.com/negtivspace/twitter2md)** | Extract Twitter/X posts as Markdown (Chrome Extension + Node.js CLI) | Chrome Ext + CLI | `Initial release` (May 2026) |
| **[`twitterBookmarkSum`](https://github.com/negtivspace/twitterBookmarkSum)** | Chrome extension: summarize tweets on-demand via GPT-4o, save as Markdown | Chrome Ext | `Update README` (Jun 2024) |

### Writing & Documentation

| Repo | Purpose | Articles | Latest |
|------|---------|----------|--------|
| **[`ai-thoughts`](https://github.com/negtivspace/ai-thoughts)** | Articles & essays: AI platforms (OpenClaw, Hermes), solo entrepreneurship, privacy, technical deep-dives. Bilingual: English + Traditional Chinese | 59 docs | `docs: add Brave browser privacy analysis` (Jul 2026) |

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
**Repo:** `sum2chn` | **Language:** JavaScript | **Purpose:** Translate & summarize web pages using Claude Sonnet

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
- **Jul 14:** Added Brave browser privacy analysis (bilingual) to `ai-thoughts`
- **Jul 14:** Polished and committed two blog posts with bilingual README updates
- **Early Jul:** Releasing v1 of `sum2chn` Chrome extension (translation + summarization)

**Current Focus:**
- Expanding Hermes Agent skill library
- Building bilingual content automation pipelines
- Documenting OpenClaw security patterns

### Q2 2026
- **Jun:** Completed `twitter2md` Chrome extension and Node.js CLI tool
- **Jun:** Refactored `twitterBookmarkSum` to use popup-triggered summarization
- **May:** Released `twitter2md` for X post extraction as Markdown

### Q1 2026
- **Apr:** Published first Hermes Agent articles and tutorials in `ai-thoughts`
- **Mar:** Established `openclaw-custom-skills` repo on ClawHub
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
- **[@negtivspace](https://github.com/negtivspace)** — Published skills & tools (organizational account)
- **[@j3ffyang](https://github.com/j3ffyang)** — Personal portfolio, articles, experiments

**Resources:**
- **Blog:** [`ai-thoughts`](https://github.com/negtivspace/ai-thoughts) — 59 articles on AI, privacy, and entrepreneurship
- **Gists:** [Personal experiments](https://gist.github.com/j3ffyang)

---

## 📝 Latest Articles

From `ai-thoughts` (recent posts):

1. **"Why I Switched to Brave"** (Jul 2026) — Deep analysis of Brave vs Firefox: local keychain, WebRTC control, Tor integration
2. **"Brave Browser Privacy Analysis"** (Jul 2026) — Bilingual breakdown of privacy features + real-world tracking prevention
3. **"AI Usage & Combination: From Doubao User to AI Power User"** (Jul 2026) — Complete guide to OpenRouter + OpenCode + Skills for multi-provider AI workflows
4. **"OpenClaw Security Audit"** — Real incidents, vulnerabilities, hardening checklist for self-hosters
5. **"Hermes Agent Setup Guides"** — Connect to free models, backup data, configure personality (SOUL.md)

👉 See all 59 articles at **[ai-thoughts/docs](https://github.com/negtivspace/ai-thoughts/tree/main/docs)**

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
# Twitter to Markdown
git clone https://github.com/negtivspace/twitter2md
cd twitter2md
npm install
npm run build  # or load extension manually in Chrome

# Web page translator
git clone https://github.com/negtivspace/sum2chn
# Follow SETUP.md to load as Chrome extension
```

### Read Articles
```bash
git clone https://github.com/negtivspace/ai-thoughts
cd docs
# 59 articles: AI platforms, privacy, solo entrepreneurship, technical deep-dives
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

**Last Updated:** July 14, 2026 | Tracking: 8 active repos, 59 articles, 10+ published skills
