---
layout: default
title: Challenges
nav_order: 3
has_children: true
description: "8 challenges taking you from requirements to partner showcase"
---

# Challenges

Eight challenges guide you through the full Infrastructure-as-Code lifecycle — from gathering requirements with an AI agent to presenting your solution in a partner showcase.

## Challenge Overview

| # | Challenge | Duration | Points |
|---|---|---|---|
| 1 | Requirements Capture | 30 min | 20 |
| 2 | Architecture Design | 30 min | 25 |
| 3 | Bicep Implementation & Deploy | 45 min | 25 |
| 4 | DR Curveball & Deploy | 45 min | 10 |
| 5 | Load Testing | 30 min | 5 |
| 6 | Workload Documentation | 15 min | 5 |
| 7 | Troubleshooting & Diagnostics | 5 min | 5 |
| 8 | Partner Showcase | 60 min | 10 |

**Total:** 105 base points + up to 25 bonus points

## Challenge Flow

```mermaid
%%{init: {'theme':'neutral'}}%%
graph LR
    C1[C1: Requirements] --> C2[C2: Architecture]
    C2 --> C3[C3: Bicep]
    C3 --> CB[⚡ CURVEBALL ⚡]
    CB --> C4[C4: DR]
    C4 --> C5[C5: Load Test]
    C5 --> C6[C6: Docs]
    C6 --> C7[C7: Diagnose]
    C7 --> C8[C8: Showcase]

    style CB fill:#ff6b6b,color:#fff
    style C8 fill:#0078d4,color:#fff
```

> Challenge 4 is announced as a surprise midway through the event — simulating real-world requirement changes.
{: .note }
