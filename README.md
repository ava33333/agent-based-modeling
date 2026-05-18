```markdown
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

#### `notes/`
- `ABM_Concepts_Notes.md` — general notes on ABM concepts, tools, and libraries
- `AgentPy_Predator_Prey_Notes.md` — observations from working through the predator-prey model
- `AgentPy_SIRD_Notes.md` — observations from working through the SIRD model
- `Ghosh_Temporal_Networks_Notes.md` — notes on Ghosh et al. temporal network paper
- `SCNIC_Notes.md` — notes on SCNIC paper and tool

#### Models
- `agentPY_Pred_Prey_model.py` — agents move on a toroidal grid, consuming resources 
  and reproducing based on energy thresholds. Demonstrates core ABM concepts: 
  agent state, emergent population dynamics, and environment interaction.
- `agentPy_SIRD_model.py` — SIRD epidemiological model (Susceptible, Infected, 
  Recovered, Deceased) implemented in AgentPy.
- `mesa_ex.py` — introductory Mesa example for library comparison.

*More examples added as research progresses.*

## Dependencies

- Python 3.11.9
- agentpy
- mesa
- matplotlib

Install with:
```bash
pip install agentpy mesa matplotlib
```

## Context

These examples were built as foundational work alongside undergraduate ML 
research at CofC exploring agent-based approaches to modeling biological 
systems. The research is ongoing and unpublished — this repo reflects my 
learning process, not research outputs.
```