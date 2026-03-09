---
layout: default
title: Setup Guide
parent: Getting Started
nav_order: 1
description: "Complete environment setup: Azure subscription, GitHub Codespace, VS Code extensions, and verification"
---

<!-- markdownlint-disable MD033 -->

> Mandatory requirements and setup steps for Agentic InfraOps

## 📑 Table of Contents

- [Readiness Gate](#readiness-gate)
- [Who This Is For](#who-this-is-for)
- [What to Expect](#what-to-expect)
- [Prerequisites](#prerequisites)
- [Handling Secrets Safely](#handling-secrets-safely)
- [🐳 Dev Container](#dev-container)
- [Setup Steps](#setup-steps)
- [⚖️ Azure Quota Requirements](#azure-quota-requirements)
- [Post-Event Cleanup](#post-event-cleanup)
- [Pre-Event Checklist](#pre-event-checklist)
- [First 10 Minutes on Event Day](#first-10-minutes-on-event-day)
- [Troubleshooting Quick Fixes](#troubleshooting-quick-fixes)
- [Next Steps](#next-steps)

---

## Readiness Gate

> Run through this quick checklist to confirm you can participate. **Every item marked "Blocks participation" must pass before the event starts.** Items marked "Optional" enhance the experience but won't stop you.\n{: .important }

| # | Check | How to verify | Blocks participation? |
|---|---|---|---|
| 1 | **Copilot Pro+ or Enterprise** license | [github.com/settings/copilot](https://github.com/settings/copilot) → confirms Pro+ or Enterprise | **Yes** — custom agents require this tier |
| 2 | **Azure subscription** with Owner access | `az login && az account show` → shows your subscription | **Yes** — you cannot deploy without it |
| 3 | **One subscription per team** confirmed | Ask your facilitator | **Yes** — shared subscriptions are not supported |
| 4 | **Azure quota** in swedencentral | `az vm list-usage -l swedencentral -o table` → sufficient vCPUs | **Yes** — insufficient quota blocks deployment |
| 5 | **Dev Container builds** successfully | F1 → "Reopen in Container" → tools load | **Yes** — all challenge work happens inside the container |
| 6 | **Custom agents visible** in Copilot Chat | Ctrl+Alt+I → agent dropdown shows InfraOps Conductor | **Yes** — challenges depend on custom agents |
| 7 | **Azure CLI authenticated** inside container | `az account show` inside Dev Container terminal | **Yes** — deployment requires authentication |
| 8 | **Repository created from template** | Your repo exists at `github.com/<your-org>/<your-repo>` (not a clone of this docs repo) | **Yes** — you need your own working repo |
| 9 | Docker Desktop running | `docker --version` | **Yes** — required for Dev Container |
| 10 | Network access to Azure and GitHub | Can reach `portal.azure.com` and `github.com` | **Yes** — required throughout |

> If any "Blocks participation" item fails, resolve it before the event or contact your facilitator immediately. Do not wait until event day.
{: .warning }

---

## Who This Is For

- **Microhack participants**: Complete the setup checklist and read "What to Expect"
  before event day.
- **Self-guided learners**: Follow the same steps to explore the agentic workflow
  at your own pace.

> **Important**: Your working repository is created from the [azure-agentic-infraops-accelerator template](https://github.com/jonathan-vella/azure-agentic-infraops-accelerator), not from this documentation repository. If you cloned this repo directly, you have the wrong starting point.
{: .warning }

---

## What to Expect

> **TL;DR**: 8 challenges in one day. You use AI agents to capture requirements, design architecture, generate Bicep, deploy to Azure, and present your solution. A DR curveball hits midway through.
{: .tip }

### The Microhack in 60 Seconds

Your team will build real Azure infrastructure — from business requirements through
deployed resources — using AI agents instead of manual coding. You'll use GitHub Copilot
custom agents that understand Azure best practices, the Well-Architected Framework, and
Bicep Infrastructure as Code.

**The flow**: Requirements → Architecture → Bicep Code → Deploy → Documentation

**The twist**: Midway through, facilitators announce a curveball requirement
(multi-region disaster recovery) that forces you to adapt your architecture.

### What You'll Actually Do

| Block                   | You Will...                                                 |
| ----------------------- | ----------------------------------------------------------- |
| Intro (30 min)          | Meet your team, verify setup, learn the workflow            |
| Challenges 1-2 (60 min) | Capture requirements and design architecture with AI agents |
| Challenge 3 (45 min)    | Generate and deploy Bicep templates                         |
| Challenge 4 (45 min)    | Adapt to new DR requirements (the curveball!)               |
| Challenges 5-7 (50 min) | Load test, document, and diagnose                           |
| Challenge 8 (60 min)    | Present your solution to the group                          |

> See the full schedule in [AGENDA.md](../about/agenda.md).
{: .tip }

### Mindset Tips

1. **Let the agents drive** — Resist the urge to write Bicep manually.
2. **Be specific in your prompts** — "Create a hub-spoke network in swedencentral
   with Application Gateway" beats "Create some infrastructure."
3. **Iterate, don't restart** — Refine in the same conversation rather than starting over.
4. **Read the artifacts** — Review `agent-output/{project}/` before the next challenge.
5. **Rotate roles** — Each team member should drive at least one challenge.

---

## Prerequisites

> All items in this section are **mandatory**. The microhack cannot proceed without every
> prerequisite in place. Complete the [Pre-Event Day Checklist](#pre-event-checklist) to confirm
> readiness before the event.
{: .warning }

### Pre-Event Checklist

> Complete every item below **before the event day**. Arrive ready — there is no setup
> time built into the agenda.
{: .important }

- [ ] **Docker Desktop** installed and running
- [ ] **VS Code** 1.100+ with Dev Containers and GitHub Copilot Chat extensions
- [ ] **Azure CLI** 2.50+ installed (`az version`)
- [ ] **PowerShell 7** installed (`pwsh --version`)
- [ ] **Git** installed (2.40+)
- [ ] **GitHub account** with Copilot Pro+ or Enterprise
- [ ] **Azure subscription** with Owner access
- [ ] **Repository cloned** locally
- [ ] **Dev Container image pulled and built** (F1 → Reopen in Container)
- [ ] **Azure CLI authenticated** (`az login` successful)
- [ ] **Custom agents enabled** (VS Code setting)
- [ ] **Network access** verified (no proxy issues)
- [ ] **Quota verified** for Sweden Central

<details markdown="1">
<summary><strong>Software Requirements</strong></summary>

#### Docker Desktop

GitHub Copilot custom agents run inside a Dev Container. You need Docker.

<details markdown="1">
<summary><strong>Installation Instructions</strong></summary>

**Install:**

- **Windows/Mac**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Linux**: [Docker Engine](https://docs.docker.com/engine/install/)

**Verify:**

```bash
docker --version
# Expected: Docker version 24.x or newer
```

**Alternatives** (if Docker Desktop licensing is an issue):

- [Rancher Desktop](https://rancherdesktop.io/)
- [Podman Desktop](https://podman-desktop.io/)
- [Colima](https://github.com/abiosoft/colima) (macOS/Linux)

</details>

#### Visual Studio Code

**Install:** [VS Code](https://code.visualstudio.com/) (version 1.100+)

The Dev Container auto-installs most extensions when it starts. You only need to install
the following on your **host machine** before opening the container:

| Extension           | ID                                   | Why host-only?                                                                    |
| ------------------- | ------------------------------------ | --------------------------------------------------------------------------------- |
| Dev Containers      | `ms-vscode-remote.remote-containers` | Required to open any Dev Container at all                                         |
| GitHub Copilot Chat | `github.copilot-chat`                | Licensing and sign-in happen on the host; automatically installs `github.copilot` |

**Install all at once:**

```bash
code --install-extension ms-vscode-remote.remote-containers
code --install-extension github.copilot-chat
```

> Extensions such as Bicep, Azure CLI Tools, PowerShell, and Azure Resource Groups are
> declared in `.devcontainer/devcontainer.json` and are installed automatically when the
> Dev Container image is built. No manual action needed for those.
{: .note }

#### Azure CLI

Required for authenticating to Azure, managing resources, running quota checks, and
executing deployment scripts throughout the microhack.

<details markdown="1">
<summary><strong>Installation Instructions</strong></summary>

**Install:**

- **Windows**: [Azure CLI installer](https://learn.microsoft.com/cli/azure/install-azure-cli-windows)
- **Mac**: `brew install azure-cli`
- **Linux**: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`

**Verify:**

```bash
az version
# Expected: azure-cli 2.50.0 or newer
```

> The Dev Container ships with the latest Azure CLI pre-installed.
> Install it locally only if you plan to use the CLI outside the container.
{: .note }

</details>

#### PowerShell 7

Required for deployment scripts, the prerequisite check script, and microhack cleanup.
PowerShell 7 (pwsh) is distinct from Windows PowerShell 5.1 and must be installed separately.

<details markdown="1">
<summary><strong>Installation Instructions</strong></summary>

**Install:**

- **Windows**: [PowerShell 7 installer](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows)
- **Mac**: `brew install --cask powershell`
- **Linux**: `sudo apt-get install -y powershell`
  (see [Linux install docs](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux))

**Verify:**

```bash
pwsh --version
# Expected: PowerShell 7.4 or newer
```

> The Dev Container ships with PowerShell 7 pre-installed. Install it locally only if
> you plan to run scripts outside the container.
{: .note }

</details>

#### Git

<details markdown="1">
<summary><strong>Installation Instructions</strong></summary>

**Install:**

- **Windows**: [Git for Windows](https://gitforwindows.org/)
- **Mac**: `brew install git` or Xcode Command Line Tools
- **Linux**: `sudo apt install git` or equivalent

**Verify:**

```bash
git --version
# Expected: git version 2.40 or newer
```

</details>

</details>

<details markdown="1">
<summary><strong>Account Requirements</strong></summary>

#### GitHub with Copilot Pro+ or Enterprise

> This microhack requires **GitHub Copilot Pro+** or **GitHub Copilot Enterprise**.
> Custom agents are **NOT available** on Copilot Free, Copilot Pro, or Copilot Business.
{: .warning }

| Plan                   | Custom Agents | Compatible |
| ---------------------- | ------------- | ---------- |
| Copilot Free           | No            | No         |
| Copilot Pro            | No            | No         |
| Copilot Business       | No            | No         |
| **Copilot Pro+**       | **Yes**       | **Yes**    |
| **Copilot Enterprise** | **Yes**       | **Yes**    |

Compare plans: [GitHub Copilot Plans](https://github.com/features/copilot/plans)

> GitHub Copilot can be billed directly through your Azure subscription.
> See [Copilot Azure billing][copilot-azure-billing] for setup instructions.
{: .tip }

**Verify:**

1. Go to [github.com/settings/copilot](https://github.com/settings/copilot)
2. Confirm your subscription shows **Pro+** or **Enterprise**
3. Ensure "Copilot Chat in the IDE" is enabled

Setup guide: [VS Code Copilot Setup](https://code.visualstudio.com/docs/copilot/setup)

#### Azure Subscription

> This is a **Bring-Your-Own-Subscription** event. No Azure subscriptions
> will be provided.
{: .warning }

**Compatible subscription types:**

| Subscription Type                     | Compatible |
| ------------------------------------- | ---------- |
| Azure in CSP                          | Yes        |
| Enterprise Agreement (EA)             | Yes        |
| Pay As You Go                         | Yes        |
| Visual Studio subscription            | Yes        |
| Azure Free Account (with Credit Card) | Yes        |
| **Azure Pass**                        | **No**     |

**Requirements:**

- **One Azure subscription per team** — this is the only supported model. Shared subscriptions cause naming collisions, RBAC confusion, and accidental cross-team interference. Do not share a subscription across teams.
- **Owner** role on the subscription is required so that facilitators can deploy Azure Policy assignments for the governance challenges. If your organisation restricts Owner, the minimum alternative is **Contributor** plus **Resource Policy Contributor** — but Owner is strongly recommended.
- Sufficient quota — see [Azure Quota Requirements](#azure-quota-requirements) below

**Verify:**

```bash
az login
az account list --output table
```

</details>

---

## Post-Event Cleanup

> **The team lead is responsible for cleanup.** Before leaving the event, the team lead must delete all team resources and confirm cleanup is complete. Do not leave resources running overnight.
{: .warning }

**Cleanup steps:**

1. Delete all resource groups created during the microhack:

   ```bash
   az group delete -n rg-freshconnect-dev-swc --yes --no-wait
   # Repeat for any additional resource groups (e.g., secondary region)
   az group delete -n rg-freshconnect-dev-gwc --yes --no-wait
   ```

2. Ask your facilitator to remove governance policies (or, if you have Owner access):

   ```powershell
   pwsh -File scripts/Remove-GovernancePolicies.ps1 -Subscription "<subscription-name-or-id>"
   ```

3. Verify cleanup is complete:

   ```bash
   az group list --query "[?starts_with(name, 'rg-freshconnect')]" -o table
   # Expected: empty result
   ```

**Deadline**: Cleanup must be confirmed before the team leaves the event venue.

---

## Handling Secrets Safely

> Throughout the microhack you will work with Azure credentials, connection strings, and API keys. Follow these rules to prevent accidental leakage.
{: .warning }

- **Never paste** real passwords, connection strings, access keys, or tokens into Copilot Chat prompts.
- **Never commit** secrets to your repository. Use placeholders like `<your-connection-string>` in code and documentation.
- **Use environment variables or Key Vault** for any values your deployment scripts need at runtime.
- **If you accidentally expose a secret**: rotate it immediately (`az keyvault secret set`, regenerate storage keys, etc.) and notify your facilitator.
- **Review agent output** before committing — agents may echo sensitive values from your terminal session.

---

## Dev Container

> **Pull and build the Dev Container image before the event day.** The first build
> downloads ~1–2 GB of layers and takes 3–5 minutes. Doing this on-site wastes time
> and strains shared Wi-Fi. Complete [Setup Steps](#setup-steps) in advance.
{: .important }

The repo includes a Dev Container with all tools pre-installed. It works with
**VS Code Dev Containers** (local Docker) and **GitHub Codespaces** (cloud).

<details markdown="1">
<summary><strong>Tools Included</strong></summary>

| Tool              | Version | Purpose                        |
| ----------------- | ------- | ------------------------------ |
| Azure CLI (`az`)  | Latest  | Azure resource management      |
| Bicep CLI         | Latest  | Infrastructure as Code         |
| GitHub CLI (`gh`) | Latest  | Repository and PR management   |
| Node.js + npm     | 20.x    | Linting, validation scripts    |
| Python 3 + pip    | 3.12+   | Diagram generation, MCP server |
| PowerShell        | 7.x     | Microhack scripts, deployment  |
| Git               | Latest  | Version control                |

</details>

<details markdown="1">
<summary><strong>Configuration Files</strong></summary>

| File                              | Purpose                                   |
| --------------------------------- | ----------------------------------------- |
| `.devcontainer/devcontainer.json` | Container definition and VS Code settings |
| `.vscode/extensions.json`         | Recommended VS Code extensions            |

</details>

<details markdown="1">
<summary><strong>Customization</strong></summary>

**Add a VS Code extension** — append to `.vscode/extensions.json`:

```jsonc
{
  "recommendations": ["your-publisher.your-extension"],
}
```

**Install additional tools** — add to `postCreateCommand` in `devcontainer.json`:

```jsonc
{
  "postCreateCommand": "npm install && pip install -r requirements.txt",
}
```

**Pass environment variables:**

```jsonc
{
  "remoteEnv": {
    "AZURE_SUBSCRIPTION_ID": "${localEnv:AZURE_SUBSCRIPTION_ID}",
  },
}
```

</details>

<details markdown="1">
<summary><strong>GitHub Codespaces</strong></summary>

1. Create your own repository from the [azure-agentic-infraops-accelerator template](https://github.com/jonathan-vella/azure-agentic-infraops-accelerator)
2. Open your new repository on GitHub
3. Click **Code** → **Codespaces** → **Create codespace on main**
4. Wait for the container to build (first time takes 2-3 minutes)

</details>

---

## Setup Steps

> Complete **all steps below before the event day**. Steps 1 and 2 pull and build the
> Dev Container image (~1–2 GB download). Do not leave this for the morning of the event.
{: .important }

<details markdown="1">
<summary><strong>1. Create Your Repo and Open It</strong></summary>

1. Go to the [azure-agentic-infraops-accelerator template](https://github.com/jonathan-vella/azure-agentic-infraops-accelerator)
2. Click **Use this template** → **Create a new repository**
3. Clone your new repository and open it in VS Code:

```bash
git clone https://github.com/<your-org-or-user>/<your-new-repo>.git
cd <your-new-repo>
code .
```

1. If the repository still contains template placeholders, run `npm run init:template` from the repo root. If you do not have Node.js locally, run it after reopening in the dev container.

When VS Code opens, accept the **"Reopen in Container"** prompt.

</details>

<details markdown="1">
<summary><strong>2. Pull and Build the Dev Container</strong></summary>

> **Do this before the event.** The initial image pull and build takes 3–5 minutes and
> requires a reliable internet connection. On the event day, skip straight to step 3.
{: .warning }

1. Press `F1` → type "Dev Containers: Reopen in Container"
2. Wait for the container to build (watch progress in the terminal)
3. Once complete, verify tools:

```bash
az version        # Expected: 2.50+
bicep --version   # Expected: 0.20+
pwsh --version    # Expected: 7+
```

</details>

<details markdown="1">
<summary><strong>3. Authenticate with Azure</strong></summary>

```bash
az login
az account set --subscription "<your-subscription-id>"
az account show --query "{Name:name, SubscriptionId:id, TenantId:tenantId}" -o table
```

</details>

<details markdown="1">
<summary><strong>4. Enable Custom Agents</strong></summary>

Open VS Code Settings (`Ctrl+,`) and add:

```json
{
  "github.copilot.chat": {
    "customAgentInSubagent": {
      "enabled": true
    }
  }
}
```

</details>

<details markdown="1">
<summary><strong>5. Verify Prerequisites - skip this step</strong></summary>

Verify the core tools manually:

```powershell
az version
bicep --version
node --version
npm --version
gh --version
```

</details>

<details markdown="1">
<summary><strong>6. Start the Workflow</strong></summary>

Open Copilot Chat (`Ctrl+Shift+I`) and select **InfraOps Conductor**:

```text
Describe the Azure infrastructure project you want to build.
```

The Conductor guides you through all 7 steps with approval gates:

1. **Requirements** — capture what you need
2. **Architecture** — WAF assessment and cost estimate
3. **Design** — diagrams and ADRs (optional)
4. **Planning** — Bicep implementation plan with governance
5. **Code** — AVM-first Bicep templates
6. **Deploy** — Azure provisioning with what-if preview
7. **Documentation** — as-built suite

Explore complete sample artifacts in the `agent-output/_sample/` directory (created during the workshop).

<details markdown="1">
<summary><strong>Network Requirements</strong></summary>

Ensure your network allows outbound HTTPS to:

| Service        | Domains                                                       |
| -------------- | ------------------------------------------------------------- |
| GitHub         | `github.com`, `api.github.com`                                |
| GitHub Copilot | `copilot.github.com`, `*.githubusercontent.com`               |
| Azure          | `*.azure.com`, `*.microsoft.com`, `login.microsoftonline.com` |
| Docker         | `docker.io`, `registry-1.docker.io`                           |

</details>

</details>

---

## Azure Quota Requirements

> **Verify your subscription has sufficient quota BEFORE the microhack.**
{: .warning }

<details markdown="1">
<summary><strong>Per-Team Resource Requirements</strong></summary>

| Resource Type           | Quantity | SKU/Tier     | Region         |
| ----------------------- | -------- | ------------ | -------------- |
| Resource Groups         | 1-2      | N/A          | Sweden Central |
| App Service Plans       | 1        | P1v4 or S1   | Sweden Central |
| App Services (Web Apps) | 1-2      | N/A          | Sweden Central |
| Azure SQL Server        | 1        | N/A          | Sweden Central |
| Azure SQL Database      | 1        | S0 or Basic  | Sweden Central |
| Storage Accounts        | 1-2      | Standard_LRS | Sweden Central |
| Key Vault               | 1        | Standard     | Sweden Central |
| Application Insights    | 1        | N/A          | Sweden Central |
| Log Analytics Workspace | 1        | Per-GB       | Sweden Central |

</details>

<details markdown="1">
<summary><strong>Optional Advanced Resources</strong></summary>

| Resource Type                  | Quantity | SKU/Tier              | Region         |
| ------------------------------ | -------- | --------------------- | -------------- |
| Azure Front Door               | 1        | Standard or Premium   | Global         |
| Application Gateway            | 1        | Standard_v2 or WAF_v2 | Sweden Central |
| Web Application Firewall (WAF) | 1        | N/A (part of AppGW)   | Sweden Central |
| Traffic Manager                | 1        | N/A                   | Global         |
| Azure Container Registry       | 1        | Basic or Standard     | Sweden Central |

</details>

<details markdown="1">
<summary><strong>Challenge 4 — DR Additional Resources</strong></summary>

| Resource Type                | Quantity | SKU/Tier     | Region               |
| ---------------------------- | -------- | ------------ | -------------------- |
| Resource Groups              | 1        | N/A          | Germany West Central |
| App Service Plans            | 1        | P1v4 or S1   | Germany West Central |
| App Services (Web Apps)      | 1        | N/A          | Germany West Central |
| Azure SQL Database (replica) | 1        | S0 or Basic  | Germany West Central |
| Storage Accounts (GRS)       | 1        | Standard_GRS | Sweden Central       |

</details>

<details markdown="1">
<summary><strong>Multi-Team Shared Subscription (4 teams)</strong></summary>

| Resource Type            | Total |
| ------------------------ | ----- |
| Resource Groups          | 8-12  |
| App Service Plans        | 8     |
| App Services (Web Apps)  | 8-12  |
| Azure SQL Servers        | 4     |
| Azure SQL Databases      | 8     |
| Storage Accounts         | 8-12  |
| Key Vaults               | 4     |
| Application Insights     | 4     |
| Log Analytics Workspaces | 4     |

</details>

<details markdown="1">
<summary><strong>Checking and Increasing Quotas</strong></summary>

**Azure Portal**: Search "Quotas" → filter by region → review per resource type.

**Azure CLI:**

```bash
az vm list-usage --location swedencentral --output table
az storage account list --query "length(@)"
```

**Common issues:**

| Issue                         | Solution                                         |
| ----------------------------- | ------------------------------------------------ |
| "Subscription not registered" | `az provider register --namespace Microsoft.Web` |
| "Quota exceeded"              | Request increase via Azure Portal → Quotas       |
| "Region not available"        | Use alternative region or request access         |
| "SKU not available in region" | Try a different SKU tier                         |

> **Request quota increases at least 1 week before the microhack** to ensure approval.
{: .warning }

</details>

<details markdown="1">
<summary><strong>Estimated Event Costs</strong></summary>

| Configuration         | Estimated Cost (~8 hours) |
| --------------------- | ------------------------- |
| Single team (basic)   | €5-10                     |
| Single team (with DR) | €10-20                    |
| 4 teams (shared sub)  | €30-50                    |

> Delete all resources immediately after the microhack.
> Delete the resource groups created for the event, or use your own cleanup automation if your workshop fork includes it.
{: .important }

</details>

<details markdown="1">
<summary><strong>Pre-Microhack Verification</strong></summary>

```powershell
az login
az account set --subscription "<your-subscription-id>"
az group create --name rg-quota-test --location swedencentral
az group delete --name rg-quota-test --yes --no-wait
```

</details>

---

## First 10 Minutes on Event Day

1. Open VS Code → Reopen in Container (if not already running)
2. Verify Azure auth: `az account show`
3. Open Copilot Chat (`Ctrl+Alt+I`) → confirm agents appear in the dropdown
4. Read the [Workshop Prep](workshop-prep.md) to understand the scenario and team roles
5. Assign team roles using the role cards in [Workshop Prep](workshop-prep.md)

---

## Troubleshooting Quick Fixes

| Problem                   | Fix                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------- |
| Docker won't start        | **Windows**: ensure WSL 2 is enabled. **Mac**: check virtualization. Restart Docker.  |
| Copilot not working       | Sign out and back in with the correct GitHub account. Reload VS Code.                 |
| Azure CLI login fails     | Use device code flow: `az login --use-device-code`                                    |
| Dev Container build fails | `F1` → "Dev Containers: Rebuild Container Without Cache". Check Docker has 4 GB+ RAM. |
| Agents not in dropdown    | Verify `customAgentInSubagent` is enabled. Reload VS Code window.                     |

See [Troubleshooting](../reference/troubleshooting.md) for a complete reference.

---

## Next Steps

- [Copilot Guide](../guides/copilot-guide.md) — agents, skills, and prompting best practices
- [Workshop Prep](workshop-prep.md) — scenario brief and team role cards
- [Hints & Tips](../guides/hints-and-tips.md) — challenge-specific guidance
- [Troubleshooting](../reference/troubleshooting.md) — common issues and fixes

[copilot-azure-billing]: https://docs.github.com/en/copilot/reference/copilot-billing/azure-billing
