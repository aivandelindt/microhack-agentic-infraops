---
title: Challenges
description: Orientation page for the full challenge sequence, artifact chain, and
  optional deep-dive references.
sidebar:
  order: 0
---

Eight challenges take you from problem framing to stakeholder defense. Treat this
page as the map for the whole workshop: skim the chain here, then open only the
challenge you are working on.

:::tip

The workshop is now reference-driven by design. Each challenge page tells you what
to do now, what artifact to produce, what decisions matter, and what the next
challenge needs. Use the shared guides only for optional depth or when you hit a
decision you cannot resolve quickly.

:::

## Fast Orientation

1. Start by finding your current challenge in the pipeline below.
2. Check the input artifact and required output before you open the page.
3. Use [Quick Reference Card](../guides/quick-reference-card/) for commands,
   naming, security baselines, Mermaid conventions, and handoff rules.
4. Use [Hints & Tips](../guides/hints-and-tips/) only when you need deeper prompt
   patterns, WAF prompts, governance help, DR guidance, or load-test ideas.

## Challenge Pipeline

```mermaid
%%{init: {'theme':'neutral'}}%%
graph LR
    C1[C1 Requirements] --> C2[C2 Architecture]
    C2 --> C3[C3 Implementation]
    C3 --> CB[Curveball]
    CB --> C4[C4 DR]
    C4 --> C5[C5 Load Test]
    C5 --> C6[C6 Docs]
    C6 --> C7[C7 Diagnostics]
    C7 --> C8[C8 Showcase]

    style CB fill:#d83b01,color:#fff
    style C8 fill:#0078d4,color:#fff
```

<details>
<summary>Text alternative: challenge pipeline</summary>

C1 Requirements -> C2 Architecture -> C3 Implementation -> Curveball -> C4 DR ->
C5 Load Test -> C6 Documentation -> C7 Diagnostics -> C8 Showcase

</details>

:::note

Challenge 4 is announced as a surprise midway through the event. If your Challenge 3
deployment did not complete, you still continue by documenting the DR design as a
paper exercise and carrying that design evidence into later challenges.

:::

## Challenge Chain

<div class="challenge-chain-table-wrap">
  <table class="challenge-chain-table">
    <colgroup>
      <col style="width: 18%" />
      <col style="width: 8%" />
      <col style="width: 6%" />
      <col style="width: 18%" />
      <col style="width: 22%" />
      <col style="width: 28%" />
    </colgroup>
    <thead>
      <tr>
        <th>Challenge</th>
        <th>Duration</th>
        <th>Points</th>
        <th>Input</th>
        <th>Output</th>
        <th>What the next step consumes</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><a href="challenge-1-requirements/">C1 Requirements</a></td>
        <td>30 min</td>
        <td>20</td>
        <td>Scenario brief</td>
        <td><code>agent-output/freshconnect/01-requirements.md</code></td>
        <td>C2 uses the agreed business, operational, and compliance requirements</td>
      </tr>
      <tr>
        <td><a href="challenge-2-architecture/">C2 Architecture</a></td>
        <td>30 min</td>
        <td>25</td>
        <td><code>01-requirements.md</code></td>
        <td><code>02-architecture-assessment.md</code>, <code>03-des-architecture-diagram.md</code></td>
        <td>C3 uses the chosen services, constraints, and architecture diagram</td>
      </tr>
      <tr>
        <td><a href="challenge-3-implementation/">C3 Implementation</a></td>
        <td>45 min</td>
        <td>25</td>
        <td>Architecture assessment and diagram</td>
        <td>IaC folder, <code>04-implementation-plan.md</code>, workflow diagram, deployment evidence</td>
        <td>C4 uses your templates, deployment outcome, and explanation of how the platform is delivered</td>
      </tr>
      <tr>
        <td><a href="challenge-4-dr-curveball/">C4 DR Curveball</a></td>
        <td>45 min</td>
        <td>10</td>
        <td>C3 templates and deployment outcome</td>
        <td><code>04-adr-ha-dr-strategy.md</code>, updated diagram, updated IaC or paper design</td>
        <td>C5 uses the revised platform or, if blocked, your documented intended target</td>
      </tr>
      <tr>
        <td><a href="challenge-5-load-testing/">C5 Load Testing</a></td>
        <td>30 min</td>
        <td>5</td>
        <td>Deployed endpoint or documented fallback plan</td>
        <td><code>05-load-test-results.md</code></td>
        <td>C6 uses the measured results and recommendations</td>
      </tr>
      <tr>
        <td><a href="challenge-6-documentation/">C6 Documentation</a></td>
        <td>15 min</td>
        <td>5</td>
        <td>All prior artifacts</td>
        <td><code>07-ab-operations-guide.md</code> plus at least one additional doc</td>
        <td>C7 distills the broader docs into a one-page triage aid</td>
      </tr>
      <tr>
        <td><a href="challenge-7-diagnostics/">C7 Diagnostics</a></td>
        <td>5 min</td>
        <td>5</td>
        <td>Platform knowledge, docs, and architecture</td>
        <td><code>07-diagnostics-quick-card.md</code></td>
        <td>C8 uses the diagnostics card as evidence of operational maturity</td>
      </tr>
      <tr>
        <td><a href="challenge-8-partner-showcase/">C8 Team Showcase</a></td>
        <td>60 min</td>
        <td>10</td>
        <td>All artifacts from C1-C7</td>
        <td>Live presentation and Q&amp;A</td>
        <td>Workshop wrap-up</td>
      </tr>
    </tbody>
  </table>
</div>

**Total:** 105 base points + up to 25 bonus points

## Optional Deep Guidance

| Need | Go here |
| --- | --- |
| Commands, naming rules, security baseline, budget guardrails, artifact handoff rules, Mermaid and ADR conventions | [Quick Reference Card](../guides/quick-reference-card/) |
| Prompt patterns, WAF decision prompts, security/compliance questions, governance policy pitfalls, DR thinking, load-test guidance, documentation prompts | [Hints & Tips](../guides/hints-and-tips/) |
| Broken deployment, policy denial, agent issues, or environment problems | [Troubleshooting](../reference/troubleshooting/) |

## Read This Way

Keep the challenge page as your execution surface.

- Read the fast block at the top of the challenge page first.
- Do the required tasks before opening any collapsed hint section.
- Open the shared guides only when you need extra depth, not as required reading.
- Preserve your output artifact names and paths exactly so later challenges can find them.
