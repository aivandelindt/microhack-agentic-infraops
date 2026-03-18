#!/usr/bin/env python3
"""Convert MkDocs Material Markdown files to Astro Starlight format.

Handles:
- Admonitions (!!! type "title" → :::type[title])
- Collapsibles (??? type "title" → <details><summary>title</summary>)
- Material icons (:material-xxx: → Unicode emoji)
- Attribute lists ({ .md-button } → stripped)
- Relative .md links → remove extension
- <div class="..." markdown> → stripped
- YAML frontmatter augmentation (sidebar order, badges, prev/next)
"""

import os
import re
import shutil
import sys
import yaml

# ── Source / destination paths ──────────────────────────────────────────────
SRC = os.path.join(os.path.dirname(__file__), "..", "docs")
DST = os.path.join(os.path.dirname(__file__), "..",
                   "site", "src", "content", "docs")

# ── Material icon → emoji mapping ──────────────────────────────────────────
ICON_MAP = {
    ":material-clock-outline:": "⏱️",
    ":material-trophy-outline:": "🏆",
    ":material-trophy:": "🏆",
    ":material-robot-outline:": "🤖",
    ":material-robot:": "🤖",
    ":material-file-document-outline:": "📄",
    ":material-file-document:": "📄",
    ":material-rocket-launch:": "🚀",
    ":material-book-open-variant:": "📖",
    ":material-bookshelf:": "📚",
    ":material-information:": "ℹ️",
    ":material-brightness-7:": "☀️",
    ":material-brightness-4:": "🌙",
    ":material-check-circle:": "✅",
    ":material-alert:": "⚠️",
    ":material-close-circle:": "❌",
    ":octicons-arrow-right-24:": "→",
    ":octicons-arrow-right-16:": "→",
}

# ── Admonition type mapping (MkDocs Material → Starlight) ─────────────────
# Starlight supports: note, tip, caution, danger
ADMONITION_MAP = {
    "note": "note",
    "abstract": "note",
    "summary": "note",
    "info": "note",
    "todo": "note",
    "tip": "tip",
    "hint": "tip",
    "important": "tip",
    "success": "tip",
    "check": "tip",
    "done": "tip",
    "question": "note",
    "help": "note",
    "faq": "note",
    "warning": "caution",
    "caution": "caution",
    "attention": "caution",
    "failure": "danger",
    "fail": "danger",
    "missing": "danger",
    "danger": "danger",
    "error": "danger",
    "bug": "danger",
    "example": "note",
    "snippet": "note",
    "quote": "note",
    "cite": "note",
}

# ── Sidebar ordering per directory ─────────────────────────────────────────
SIDEBAR_ORDER = {
    "getting-started/index.md": {"order": 0, "hidden": True},
    "getting-started/setup.md": {"order": 1},
    "getting-started/workshop-prep.md": {"order": 2},
    "getting-started/learning-resources.md": {"order": 3},
    "challenges/index.md": {"order": 0},
    "challenges/challenge-1-requirements.md": {"order": 1, "badge": {"text": "30 min", "variant": "note"}},
    "challenges/challenge-2-architecture.md": {"order": 2, "badge": {"text": "30 min", "variant": "note"}},
    "challenges/challenge-3-implementation.md": {"order": 3, "badge": {"text": "45 min", "variant": "success"}},
    "challenges/challenge-4-dr-curveball.md": {"order": 4, "badge": {"text": "45 min", "variant": "caution"}},
    "challenges/challenge-5-load-testing.md": {"order": 5, "badge": {"text": "30 min", "variant": "note"}},
    "challenges/challenge-6-documentation.md": {"order": 6, "badge": {"text": "15 min", "variant": "note"}},
    "challenges/challenge-7-diagnostics.md": {"order": 7, "badge": {"text": "5 min", "variant": "note"}},
    "challenges/challenge-8-partner-showcase.md": {"order": 8, "badge": {"text": "60 min", "variant": "tip"}},
    "guides/index.md": {"order": 0, "hidden": True},
    "guides/copilot-guide.md": {"order": 1},
    "guides/hints-and-tips.md": {"order": 2},
    "guides/quick-reference-card.md": {"order": 3},
    "reference/index.md": {"order": 0, "hidden": True},
    "reference/glossary.md": {"order": 1},
    "reference/governance-scripts.md": {"order": 2},
    "reference/troubleshooting.md": {"order": 3},
    "about/index.md": {"order": 0, "hidden": True},
    "about/agenda.md": {"order": 1},
    "about/invitation.md": {"order": 2},
    "about/feedback.md": {"order": 3},
}

# Challenge prev/next navigation
CHALLENGE_NAV = {
    "challenges/challenge-1-requirements.md": {
        "prev": {"link": "../", "label": "Challenges Overview"},
        "next": {"link": "../challenge-2-architecture/", "label": "C2: Architecture"},
    },
    "challenges/challenge-2-architecture.md": {
        "prev": {"link": "../challenge-1-requirements/", "label": "C1: Requirements"},
        "next": {"link": "../challenge-3-implementation/", "label": "C3: Implementation"},
    },
    "challenges/challenge-3-implementation.md": {
        "prev": {"link": "../challenge-2-architecture/", "label": "C2: Architecture"},
        "next": {"link": "../challenge-4-dr-curveball/", "label": "C4: DR Curveball"},
    },
    "challenges/challenge-4-dr-curveball.md": {
        "prev": {"link": "../challenge-3-implementation/", "label": "C3: Implementation"},
        "next": {"link": "../challenge-5-load-testing/", "label": "C5: Load Testing"},
    },
    "challenges/challenge-5-load-testing.md": {
        "prev": {"link": "../challenge-4-dr-curveball/", "label": "C4: DR Curveball"},
        "next": {"link": "../challenge-6-documentation/", "label": "C6: Documentation"},
    },
    "challenges/challenge-6-documentation.md": {
        "prev": {"link": "../challenge-5-load-testing/", "label": "C5: Load Testing"},
        "next": {"link": "../challenge-7-diagnostics/", "label": "C7: Diagnostics"},
    },
    "challenges/challenge-7-diagnostics.md": {
        "prev": {"link": "../challenge-6-documentation/", "label": "C6: Documentation"},
        "next": {"link": "../challenge-8-partner-showcase/", "label": "C8: Partner Showcase"},
    },
    "challenges/challenge-8-partner-showcase.md": {
        "prev": {"link": "../challenge-7-diagnostics/", "label": "C7: Diagnostics"},
    },
}


def replace_icons(text: str) -> str:
    """Replace Material/Octicon icon shortcodes with Unicode emoji."""
    for icon, emoji in ICON_MAP.items():
        text = text.replace(icon, emoji)
    # Catch any remaining :material-*: or :octicons-*: patterns
    text = re.sub(r":material-[a-z0-9-]+:", "", text)
    text = re.sub(r":octicons-[a-z0-9-]+:", "", text)
    return text


def strip_attr_lists(text: str) -> str:
    """Remove MkDocs attr_list syntax like { .md-button .md-button--primary }."""
    return re.sub(r"\{[^}]*\.md-button[^}]*\}", "", text)


def strip_div_markdown(text: str) -> str:
    """Remove <div ... markdown> and </div> wrappers."""
    text = re.sub(r'<div[^>]*markdown[^>]*>', '', text)
    text = re.sub(r'</div>', '', text)
    return text


def convert_md_links(text: str) -> str:
    """Convert relative .md links to extensionless paths for Astro routing.
    e.g., [text](../foo/bar.md) → [text](../foo/bar/)
          [text](foo.md#anchor) → [text](foo/#anchor)
    """
    def _repl(m):
        prefix = m.group(1)
        path = m.group(2)
        anchor = m.group(3) or ""
        # Don't touch external URLs or absolute paths
        if path.startswith("http") or path.startswith("/"):
            return m.group(0)
        # Remove .md extension and add trailing slash
        path = re.sub(r'\.md$', '/', path)
        # Ensure single trailing slash (avoid //)
        if not path.endswith('/'):
            path += '/'
        return f"{prefix}{path}{anchor})"
    return re.sub(r'(\[[^\]]*\]\()([^)#]+?\.md)(#[^)]*)?(\))', lambda m: _repl(m), text)


def convert_admonitions(text: str) -> str:
    """Convert MkDocs Material admonitions to Starlight asides.

    !!! type "title"        → :::type[title]
        content               content
                              :::

    !!! type                → :::type
        content               content
                              :::
    """
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        # Match !!! type or !!! type "title"
        m = re.match(r'^(!{3})\s+(\w+)(?:\s+"([^"]*)")?\s*$', lines[i])
        if m:
            admon_type = m.group(2).lower()
            title = m.group(3)
            sl_type = ADMONITION_MAP.get(admon_type, "note")

            if title:
                result.append(f":::{sl_type}[{title}]")
            else:
                result.append(f":::{sl_type}")

            i += 1
            # Collect indented content (4 spaces)
            while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                if lines[i].strip() == '':
                    result.append('')
                else:
                    result.append(lines[i][4:])  # Remove 4-space indent
                i += 1
            result.append(':::')
            result.append('')
            continue

        result.append(lines[i])
        i += 1

    return '\n'.join(result)


def convert_collapsibles(text: str) -> str:
    """Convert MkDocs collapsible admonitions to HTML details/summary.

    ??? type "title"    → <details>
        content           <summary>title</summary>
                          content
                          </details>
    """
    lines = text.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^\?{3}\+?\s+\w+\s+"([^"]*)"', lines[i])
        if m:
            title = m.group(1)
            result.append('<details>')
            result.append(f'<summary>{title}</summary>')
            result.append('')
            i += 1
            while i < len(lines) and (lines[i].startswith('    ') or lines[i].strip() == ''):
                if lines[i].strip() == '':
                    result.append('')
                else:
                    result.append(lines[i][4:])
                i += 1
            result.append('')
            result.append('</details>')
            result.append('')
            continue

        result.append(lines[i])
        i += 1

    return '\n'.join(result)


def strip_grid_cards(text: str) -> str:
    """Remove Material grid card containers (they'll be rebuilt in index.mdx)."""
    text = re.sub(r'<div[^>]*class="grid cards"[^>]*markdown[^>]*>', '', text)
    return text


def update_frontmatter(text: str, rel_path: str) -> str:
    """Update YAML frontmatter with Starlight-specific fields."""
    if not text.startswith('---'):
        # No frontmatter; create one
        text = "---\ntitle: Page\n---\n\n" + text

    parts = text.split('---', 2)
    if len(parts) < 3:
        return text

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return text

    # Add sidebar config
    sidebar_key = rel_path.replace('\\', '/')
    if sidebar_key in SIDEBAR_ORDER:
        cfg = SIDEBAR_ORDER[sidebar_key]
        sidebar = {}
        if "order" in cfg:
            sidebar["order"] = cfg["order"]
        if cfg.get("hidden"):
            sidebar["hidden"] = True
        if "badge" in cfg:
            sidebar["badge"] = cfg["badge"]
        fm["sidebar"] = sidebar

    # Add prev/next navigation
    if sidebar_key in CHALLENGE_NAV:
        nav = CHALLENGE_NAV[sidebar_key]
        if "prev" in nav:
            fm["prev"] = nav["prev"]
        if "next" in nav:
            fm["next"] = nav["next"]

    # Build new frontmatter
    new_fm = yaml.dump(fm, default_flow_style=False,
                       allow_unicode=True, sort_keys=False)
    return f"---\n{new_fm}---\n{parts[2]}"


def convert_file(src_path: str, dst_path: str, rel_path: str) -> None:
    """Convert a single Markdown file."""
    with open(src_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Skip index.md — it will be manually created as index.mdx
    if rel_path == "index.md":
        print(f"  SKIP {rel_path} (will be manually created as index.mdx)")
        return

    # Order matters: collapsibles before admonitions (??? before !!!)
    text = convert_collapsibles(text)
    text = convert_admonitions(text)
    text = replace_icons(text)
    text = strip_attr_lists(text)
    text = strip_div_markdown(text)
    text = strip_grid_cards(text)
    text = convert_md_links(text)
    text = update_frontmatter(text, rel_path)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"  OK   {rel_path}")


def copy_assets(src_dir: str, dst_dir: str) -> None:
    """Copy image assets."""
    src_assets = os.path.join(src_dir, "assets", "images")
    dst_assets = os.path.join(dst_dir, "..", "..", "assets", "images")

    if os.path.isdir(src_assets):
        os.makedirs(dst_assets, exist_ok=True)
        for item in os.listdir(src_assets):
            s = os.path.join(src_assets, item)
            d = os.path.join(dst_assets, item)
            if os.path.isfile(s) and not os.path.exists(d):
                shutil.copy2(s, d)
                print(f"  ASSET {item}")


def main():
    print(f"Converting MkDocs → Starlight")
    print(f"  Source: {SRC}")
    print(f"  Dest:   {DST}")
    print()

    if not os.path.isdir(SRC):
        print(f"ERROR: Source directory not found: {SRC}")
        sys.exit(1)

    os.makedirs(DST, exist_ok=True)

    count = 0
    for root, dirs, files in os.walk(SRC):
        # Skip assets directory (handled separately)
        if "assets" in dirs:
            dirs.remove("assets")

        for fname in sorted(files):
            if not fname.endswith('.md'):
                continue
            src_path = os.path.join(root, fname)
            rel_path = os.path.relpath(src_path, SRC)
            dst_path = os.path.join(DST, rel_path)
            convert_file(src_path, dst_path, rel_path)
            count += 1

    # Copy assets
    copy_assets(SRC, DST)

    print(f"\nConverted {count} files.")
    print("NOTE: index.md was skipped — create site/src/content/docs/index.mdx manually.")


if __name__ == "__main__":
    main()
