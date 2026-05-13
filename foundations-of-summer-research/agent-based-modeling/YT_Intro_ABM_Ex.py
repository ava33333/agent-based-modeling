import mesa
import matplotlib.pyplot as plt

import seaborn as sns
import numpy as np

import pandas as pd

print("You are using Mesa version: " + mesa.__version__)

def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.agents]
    n = sorted(agent_wealths)
    N = model.num_agents
    B = sum((i + 1) * xi for i, xi in enumerate(n)) / (N * sum(n))
    return 1 + (1 / N) - 2 * B

class MoneyAgent(mesa.Agent):
    """
    An agent with fixed initial wealth.
    This class represents an agent in our model
    """
    def __init__(self, model):
        #run parent class's setup. child agent gets attributes that parent provides
        super().__init__(model)

        self.wealth = 1 #each agent starts with wealth of 1

    def step(self):
        """
        Define the actions the agent takes in one step.
        Here, the agent will simply print its unique identifier.
        """
        self.move()

        if self.wealth > 0:
            self.give_money() #if agent has wealth, it gives money to another agent in the same cell

        print("Hi, I am agent " + str(self.unique_id) + ".")
    
    def move(self):
        #agent will move to any of the 8 directions (8 cells in neighborhood)
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, #agents current position
            moore=True, #Moore neighboorhood (incl diagonal)
            include_center=False #exclude the cell where `the agent is currently located`
        )

        new_position = self.random.choice(possible_steps) #choose a new position at random
        self.model.grid.move_agent(self, new_position) # move agent to the new position
    
    def give_money(self):
        # get all agents in the same cell as this agent
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if len(cellmates) > 1: # check that there is more than one agent in the cell
            other = self.random.choice(cellmates) #randomly select another agent in the same cell
            if other != self: #ensure the selected agent is not itself
                other.wealth += 1 #increase the other agent's wealth
                self.wealth -= 1 #decremement this agent's wealth
            

class MoneyModel(mesa.Model):
    """
    A model with some number of agents.
    This class represents the overall model/environment in which our agents operate.
    """

    def __init__(self, N, width, height):
        super().__init__()
        #initialize model with N agents
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, torus=True)
        #multigrid allows multiple agents in a cell. 'torus=True'makes the grid wrap around
        
        #create agents and add them to the model
        for i in range(self.num_agents): #iterate over the number of agents
            a = MoneyAgent(self)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y)) #place agent at our random coordinates

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, #collection function
            agent_reporters={"Wealth": "wealth"} #collecting an attribute
        )

        self.datacollector.collect(self)

    def step(self):
        """
        Advance the model by one step.
        Each step, every agent's 'step' methodd will be called.
        """
        self.agents.shuffle_do("step") #triggers all agents in random order to take a step
        self.datacollector.collect(self)
    
'''#create model instance w/10 agents
model = MoneyModel(10)

#advance model by one step    
for _ in range(10):
    model.step()

agent_wealth = [a.wealth for a in model.agents]
plt.hist(agent_wealth)
plt.show()
'''
'''
all_wealth = []

for j in range(100):
    model = MoneyModel(10)
    for i in range(10):
        model.step()
    
    for agent in model.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins=range(max(all_wealth) + 1))

plt.show()
'''
'''
model = MoneyModel(50, 10, 10) # 50 agents on a 10x10 grid

for i in range(20):
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell_content, (x, y) in model.grid.coord_iter():
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count

g = sns.heatmap(agent_counts, cmap="viridis", annot=True, cbar=False, square=True)
g.figure.set_size_inches(4, 4)
g.set(title="Number of agents on each cell of the grid")
plt.show()
'''
'''

model = MoneyModel(10, 10, 10)

for i in range(100):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()


gini.plot()
gini
plt.show()

'''
params = {
    "N": np.arange(10, 51, 10),
    "width": 10,
    "height": 10
}

param_run = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=1,
    max_steps=30,
    number_processes=1,
    data_collection_period=1,
    display_progress=True
)

param_run