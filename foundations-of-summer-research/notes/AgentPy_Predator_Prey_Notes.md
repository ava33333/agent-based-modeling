# Predator Prey Model Notes & Setup

These are my notes on the predator prey model AgentPy setup, including the thinking and rules behind the model. This is an exploratory example to learn AgentPy basics

The corresponding code is in the parent folder titled agentPy_Pred_Prey.py.

### Model Rules & Design Decisions

- The goal of a predator prey model is to map out energy flow within an environment. The predator eats the prey and the prey eats the grass. In a functional ecosystem, it is necessary to have a proper balance of all these factors to ensure population sizes do not get too low or high for any organism.
- State: energy level (death=0)
- Agents: predator and prey
- Rules for model:
    1. all agents move randomly with each step
    2. predator lands on prey —> eats it, gains all energy from prey, prey dies
    3. prey lands on grass cell —> eats it, gains energy from grass (energy always is n = 1 for grass), grass cell becomes empty
    4. empty grass cells regrow with the same probability each step
    5. any agent at or above the energy threshold (n≥6) reproduces by splitting into two instances, both starting at energy level n=3
        - I chose n=3 so, no matter what the parent’s energy was, the offspring do not start off with a very high energy level to prevent skewed population distributions
    6. any agent at 0 energy dies and is removed from the grid
    7. each step results in one energy loss
- Torus grid was chosen to allow for agents to wrap around edges without hitting a boundary, maintaining a continuous space
- Both agents have the same functions (setup, move, eat, reproduce, and die) with some discrepancies between how specific functions are set up to handle the above rules
- The resulting model portrayed allows the user to step through the simulation until one, or both, of the populations are at n=0
- After one, or both, populations die, a graph is displayed, mapping out the population sizes of the agents at each step