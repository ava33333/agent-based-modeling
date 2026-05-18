These are my notes on the SIRD model AgentPy setup, including the thinking and rules behind the model. This is an exploratory example to learn AgentPy basics.

The corresponding code is in the parent folder titled agentPy_SIRD_model.py.

**Model Rules & Design Decisions**

- An SIRD (suceptible, infected, recovered, dead) model maps out the effects of an epidemic. The agents include the affected population, typically human, though other organisms can apply to this model. Just like in real life, there is chance at play to who might get sick or die from getting a virus.
- Agents are human population
    - States: healthStatus = “sick”, “healthy”, “dead”, or “recovered”
- Rules:
    - All agents start off healthy except for 1 infected agent
    - An infected agent within the neighborhood (or same cell) as a healthy agent can infect them
    - There is a random chance that an agent who has come in contact with an infected agent will actually get sick
    - There is a random chance that a sick agent will die within the sickness period
    - Once an agent dies they can no longer move nor take actions on/from other agents (aka they can't infect other agents)
    - If an agent is sick for 5 days without dying, they will be recovered
    - If there are no more carriers (ie all of the sick agents die and/or are recovered) the simulation will end
- Parameters for model:
    - infectionRadius: neighboring cells on all 8 sides (upper left diagonal, lower left diagonal, upper right diagonal, lower right diagonal, up, down, left, right)
    - infectionProbability: 50% chance of infection (*bumped up to account for graph density)
    - mortalityProbability: 5% chance of death once infected (*bumped up so that it shows up at least a few times)
    - recovered: if the individual was sick but no longer is. This occurs after they are sick and do not die for 5 days (so on day 6 they would be recovered)
    - gridSize: size of grid (area for individuals to be in)
- This is different in a few ways from my predator prey model. Here are the new things I learned from building this:
    - The first thing that was vastly different from the model was that, rather than having different agents, my one agent had various different states (”sick”, “healthy”, “dead”, “recovered”). The best way to access these different states is through the .select() method (as shown below)
        
        ```python
        self.record('Sick', len(self.agents.select(self.agents.healthStatus == "sick")))
        ```
        
    - I had to figure out how to change the colors of the agents dynamically, rather than just setting it at the beginning of the simulation statically
    - I cleaned up the way that the simulation ended (realized there was a more concise/easier way to do it with the built in AgentPy methods)
    - manual vs AgentPy run loop— this was in my predator prey model but I forgot to note this. Because I introduced manual stepping (rather than an automatic loop which is built in to AgentPy) with a button, I had to handle termination myself in the next_step() function
    - looked more into AgentPy methods like setup, step, update, and end and how/when they fire automatically vs manually
    - visualization with ListedColormap rather than the color dictionary (allows custom colors)