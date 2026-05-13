
import agentpy as ap
import random

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

'''
This is an ABM predator-prey model.
'''

class Predator(ap.Agent):
    '''
    Predator and prey move randomly, losing energy with each step.
    If a predator lands on prey, it eats it, gains energy.
    Any predator or prey above the energy threshold reproduces one offspring.
    All offspring get half of the parent's energy.
    Any predator or prey at 0 energy dies.
    '''
    def setup(self):
        self.alive = True #start off as alive. if it dies midstep, this will catch it
        self.energy = random.randint(3, 10) #randomly places the predator
    
    def move(self):
        x, y = self.model.environment.positions[self]
        dx, dy = random.choice([(i,j) for i in [-1,0,1] for j in [-1,0,1] if (i,j) != (0,0)])
        new_position = ((x+dx) % self.model.p.size, (y+dy) % self.model.p.size)
        self.model.environment.move_to(self, new_position)
        self.energy -= 1
        if self.energy <= 0:
            self.alive = False

    def eat(self, prey):
        self.energy += prey.energy
        prey.energy = 0
        prey.alive = False

    def reproduce(self):
        if self.energy >= 6:
            self.energy = 3     # each child gets half energy
            new_agent = ap.AgentList(self.model, 1, Predator)   # create new child
            new_agent[0].energy = 3     # give it 3 energy too
            pos = self.model.environment.positions[self]    # getting parent's position (offspring spawns in same cell)
            self.model.environment.add_agents(new_agent, positions=[pos])   # add to grid
            self.model.predators += new_agent   # increase number of predators
            
    def die(self):
        self.model.environment.remove_agents([self])    # remove from list of agents
        self.model.predators.remove(self)               # remove actual agent from grid

class Prey(ap.Agent):
    '''
    Predator and prey move randomly, losing energy with each step.
    If a prey lands on a grass patch, it eats it, gains energy, and the grass cell becomes empty.
    Any predator or prey above the energy threshold reproduces one offspring.
    All offspring offspring get half of the parent's energy.
    Any predator or prey at 0 energy dies. For prey, if a predator eats it, it will die.
    '''
    def setup(self):
        self.alive = True #start off as alive. if it dies midstep, this will catch it
        self.energy = random.randint(3, 10)
    
    def move(self):
        x, y = self.model.environment.positions[self]
        dx, dy = random.choice([(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)])
        new_position = ((x+dx) % self.model.p.size, (y+dy) % self.model.p.size)
        self.model.environment.move_to(self, new_position)
        self.energy -= 1
        if self.energy <= 0:
            self.alive = False

    def eat(self, grass):
        grass.hasGrass = False
        self.energy += 1

    def reproduce(self): # see comments in other reproduce function (for predator)
        if self.energy >= 6:
            self.energy = 3
            new_agent = ap.AgentList(self.model, 1, Prey)
            new_agent[0].energy = 3
            pos = self.model.environment.positions[self]
            self.model.environment.add_agents(new_agent, positions=[pos])
            self.model.prey += new_agent
    def die(self):
        # if the energy = 0
        self.model.environment.remove_agents([self])    # remove from list of agents
        self.model.prey.remove(self)                    # remove actual agent from grid

class EnvironmentModel(ap.Model):
    '''
    The environment is populated randomly with grass patches for the prey to eat.
    Each grass patch has 1 energy and the cell becomes empty when the prey eats it.
    '''
    def setup(self):
        # create grass
        n_grass = int(self.p['Grass density'] * (self.p.size**2))
        self.grass = ap.AgentList(self, n_grass, ap.Agent)
        self.grass.hasGrass = True

        #create predators and prey
        self.predators = ap.AgentList(self, self.p.n_predators, Predator)
        self.prey = ap.AgentList(self, self.p.n_prey, Prey)

        #create grid (torus for when agents go to the edge they can loop back around)
        self.environment = ap.Grid(self, [self.p.size]*2, track_empty=True, torus=True)
        self.environment.add_agents(self.grass, random=True, empty=True)
        self.environment.add_agents(self.predators, random=True, empty=True)
        self.environment.add_agents(self.prey, random=True, empty=True)

    def grass_regrowth(self):
        # regrows each step. more realistic than regrowing each time grass is eaten
        for grass in self.grass:
            if grass.hasGrass == False:
                if random.random() < self.p.grass_regrowth_rate:
                    grass.hasGrass = True

    def step(self):
   
        self.predators.move()

        dead_predators = [pd for pd in self.predators if not pd.alive]
        for pd in dead_predators:
            pd.die()

        for pd in self.predators:
            position = self.environment.positions[pd]
            prey_here = [a for a in self.environment.agents if (isinstance(a, Prey)) and (a.alive) and (self.environment.positions[a] == position)]
         
            if prey_here:
                pd.eat(prey_here[0])
            pd.reproduce()

        self.prey.move()

        dead_prey = [py for py in self.prey if not py.alive]
        for py in dead_prey:
            py.die()

        for py in self.prey:
            position = self.environment.positions[py]
            grass_here = [a for a in self.environment.agents 
                          if (self.environment.positions[a] == position) 
                          and hasattr(a, 'hasGrass') and a.hasGrass]
         
            if grass_here:
                py.eat(grass_here[0])
            py.reproduce()

        self.grass_regrowth()
    
    # collect data for plot at end of simulation
    def update(self):
        self.record('Predators', len(self.predators))
        self.record('Prey', len(self.prey))

parameters = {
    'size': 20,
    'n_predators': 10,
    'n_prey': 20,
    'Grass density': 0.4,
    'grass_regrowth_rate': 0.3,
}

def animation_plot(model, ax):
    import numpy as np
    grid_data = np.zeros((model.p.size, model.p.size))

    for g in model.grass:
        if g.hasGrass:
            x, y = model.environment.positions[g]
            grid_data[x][y] = 1
    for p in model.prey:
        x, y = model.environment.positions[p]
        grid_data[x][y] = 2
    for p in model.predators:
        x, y = model.environment.positions[p]
        grid_data[x][y] = 3
        
    color_dict = {0: '#ffffff', 1: '#7FC97F', 2: '#4444ff', 3: '#d62c2c', None: '#ffffff'}
    ap.gridplot(grid_data, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"t={model.t}  Predators={len(model.predators)}  Prey={len(model.prey)}")

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

model = EnvironmentModel(parameters)
model.setup()
animation_plot(model, ax)

# record population counts at each step
pred_history = [] 
prey_history = []

def next_step(event):
    model.t += 1 # step counter
    model.step()
    pred_history.append(len(model.predators))
    prey_history.append(len(model.prey))

    animation_plot(model, ax)
    fig.canvas.draw()

    if len(model.predators) == 0 or len(model.prey) == 0:
        plt.close()
        plt.plot(pred_history, label='Predators', color='red')
        plt.plot(prey_history, label='Prey', color='blue')
        plt.xlabel('Step')
        plt.legend()
        plt.show()

ax_button = plt.axes([0.4, 0.05, 0.2, 0.08])
button = Button(ax_button, 'Next Step')
button.on_clicked(next_step)

plt.show()

"""
Prey are blue
Predators are red
Multiple agents can be in the same cell, 
    so you might not see the number of predators/prey 
    that actually are there because they are "stacked"
"""

