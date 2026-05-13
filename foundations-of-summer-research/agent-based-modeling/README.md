# Agent-Based Modeling

A growing collection of ABM examples built during undergraduate ML research 
at the College of Charleston. This repo documents my learning process through 
annotated code and notes — it will expand over time as the research progresses.

## What is ABM?

Agent-based modeling is a form of generative science used to map complex, 
large-scale patterns from interactions between individual agents. Rather than 
modeling a system top-down, you define simple agent behaviors and let 
emergent structure arise from their interactions. Agents are independent individuals 
in a population, each defined by their own state and behavioral rules.


## Contents

### `foundations-of-summer-research/`
Foundational ABM examples and concepts built at the start of the research process.

**`notes/`** — General notes on ABM concepts, tools, and libraries built up over the course of the research.

**Examples** follow this structure:
- `model.py` — working implementation
- `notes.md` — observations and questions from working through the model

#### Examples
- `predator-prey/` — agents move on a toroidal grid, consuming resources 
  and reproducing based on energy thresholds. Demonstrates core ABM concepts: 
  agent state, emergent population dynamics, and environment interaction.

*More examples added as research progresses.*

## Dependencies

- Python [VERSION]
- agentpy
- matplotlib

Install with:
```bash
pip install agentpy matplotlib
```

## Context

These examples were built as foundational work alongside undergraduate ML 
research at CofC exploring agent-based approaches to modeling biological 
systems. The research is ongoing and unpublished — this repo reflects my 
learning process, not research outputs.
