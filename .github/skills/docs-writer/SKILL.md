# Docs Writer Skill

## Purpose

Keep workshop documentation consistent, accurate, and fresh.

## When to Use

- Writing or editing challenge guides, setup instructions, or reference pages
- Ensuring terminology matches the glossary
- Updating cross-references after structural changes

## Guidelines

- Use Starlight admonitions (`:::tip`, `:::caution`, `:::note`, `:::danger`) for callouts
- Challenge files must include frontmatter with `title`, `description`, `sidebar.order`, and `sidebar.badge`
- Collapsible sections use `<details><summary>Title</summary>` HTML syntax
- Keep language concise and scannable — workshop participants are under time pressure
- Preserve scoring consistency with `facilitator/scoring-rubric.md`

## Constraints

- Do not reveal facilitator-only content (solutions, scoring details) in participant-facing docs
- Do not change challenge timings or points without updating all canonical references
- Use relative links without `.md` extension for internal navigation
