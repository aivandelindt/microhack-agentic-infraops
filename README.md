# Agentic InfraOps MicroHack

> **6-Hour Challenge**: Transform business requirements into deployed Azure infrastructure using AI agents and GitHub Copilot.

## Overview

Teams use GitHub Copilot custom agents to design, plan, implement, and deploy Azure infrastructure — all guided by AI and aligned with the [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/).

**What you'll experience:**

- AI-assisted requirements gathering and architecture design
- Automated Bicep code generation from natural language
- Cost estimation using Azure Pricing MCP
- Real deployment to your Azure subscription
- A mid-event "curveball" that tests your adaptability

## Learning Objectives

1. **Understand agentic workflows** for Infrastructure as Code
2. **Generate production-ready Bicep** using AI agents
3. **Apply WAF principles** (Reliability, Security, Cost, Operations, Performance)

## The Scenario: Nordic Fresh Foods

A Stockholm-based farm-to-table delivery company needs cloud infrastructure. Your team will capture requirements, design a WAF-aligned architecture, generate and deploy Bicep templates, and adapt to a surprise multi-region DR requirement mid-event.

## Schedule (6 Hours)

| Time        | Block           | Duration | Activity                          |
| ----------- | --------------- | -------- | --------------------------------- |
| 10:00–10:30 | Intro           | 30 min   | Welcome, setup, team formation    |
| 10:30–11:00 | Challenge 1     | 30 min   | Requirements Capture              |
| 11:00–11:30 | Challenge 2     | 30 min   | Architecture Design               |
| 11:30–12:00 | Lunch           | 30 min   | Break                             |
| 12:00–12:45 | Challenge 3     | 45 min   | Bicep Implementation & Deployment |
| 12:45–13:30 | Challenge 4     | 45 min   | DR Curveball & Deployment         |
| 13:30–13:45 | Break           | 15 min   | Rest & recharge                   |
| 13:45–14:15 | Challenge 5     | 30 min   | Load Testing                      |
| 14:15–14:30 | Challenge 6     | 15 min   | Documentation                     |
| 14:30–14:35 | Challenge 7     | 5 min    | Diagnostics                       |
| 14:35–14:50 | Prep            | 15 min   | Presentation Preparation          |
| 14:50–15:50 | Challenge 8     | 60 min   | Partner Showcase                  |
| 15:50–16:00 | Wrap-up         | 10 min   | Leaderboard, cleanup, close       |

## Repository Structure

```text
docs/                   # GitHub Pages site (just-the-docs theme)
facilitator/            # Facilitator guide, scoring rubric, solution reference
scripts/                # Governance & scoring PowerShell scripts
```

## Getting Started

1. **Open in Dev Container** — This repo includes a dev container with all prerequisites.
2. **Read** [Getting Started](docs/getting-started/setup.md) for setup and Azure quota requirements.
3. **Review** [Workshop Prep](docs/getting-started/workshop-prep.md) for the scenario brief and team roles.
4. **Follow** the challenges in order starting from [Challenge 1](docs/challenges/challenge-1-requirements.md).

## Quick Links

| Resource | Description |
| --- | --- |
| [Agenda](docs/about/agenda.md) | Full schedule with timing |
| [Copilot Guide](docs/guides/copilot-guide.md) | Agents, skills, and prompting tips |
| [Quick Reference Card](docs/guides/quick-reference-card.md) | Printable one-page cheat sheet |
| [Scoring Rubric](facilitator/scoring-rubric.md) | WAF-aligned evaluation criteria |
| [Troubleshooting](docs/reference/troubleshooting.md) | Common issues and fixes |

## Contributing

See [Contributing Guide](https://github.com/jonathan-vella/microhack-agentic-infraops/blob/main/CONTRIBUTING.md) for Git workflow, commit conventions, and versioning.

## License

This project is provided for educational and workshop use. See the repository for license details.
