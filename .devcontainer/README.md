# DevContainer — Jekyll Development Environment

This devcontainer provides a ready-to-use environment for building and previewing the Agentic InfraOps MicroHack documentation site.

## What's Included

- **Ruby** (via Jekyll devcontainer image) — for Jekyll site generation
- **Node.js LTS** — for markdownlint-cli2
- **VS Code extensions** — Markdown linting, YAML support, Mermaid preview, Liquid syntax

## Getting Started

### 1. Open in DevContainer

In VS Code: **Ctrl+Shift+P** → `Dev Containers: Reopen in Container`

### 2. Start the Jekyll Dev Server

```bash
cd docs
bundle install
bundle exec jekyll serve
```

### 3. Preview the Site

Open [http://localhost:4000/microhack-agentic-infraops/](http://localhost:4000/microhack-agentic-infraops/) in your browser (port 4000 is auto-forwarded).

## Useful Commands

| Command | Purpose |
|---|---|
| `cd docs && bundle exec jekyll serve` | Start dev server with live reload |
| `cd docs && bundle exec jekyll build` | Build site without serving |
| `markdownlint-cli2 "docs/**/*.md"` | Lint all markdown files |
| `cd docs && bundle exec htmlproofer _site/` | Check for broken links |
