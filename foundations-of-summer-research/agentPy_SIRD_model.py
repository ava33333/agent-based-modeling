import agentpy as ap
import random

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.colors import ListedColormap

'''
This is an SIRD model (suceptible, infected, recovered, dead)
to model how a virus would move affect a population.
'''

class Human(ap.Agent):
    '''
    All agents start off healthy except for one infected 
    agent.
    An infected agent within the neighborhood (or same cell) 
    as a healthy agent can infect them (but may not).
    There is a random chance that an agent who has come into contact 
    with an infected agent will actually get sick.
    There is a random chance that the sick agent will die within the sickness 
    period (5 days).
    Once an agent dies they can no longer move nor take actions on/from other 
    agents.
    If an agent is sick for 5 days without dying, they will be recovered.
    If there are no more carriers (ie all the sick agents die and/or are recovered) 
    the simulation will end.
    '''
    def setup(self):
        # agents can be healthy, infected, recovered, or dead
        self.healthStatus = "healthy" # set starting agents to be healthy
        self.daysSick = 0
    
    def step(self):
        # if they are dead they can't move
        if self.healthStatus == "dead":
            return
        
        if self.sickPeriod() == True:
            return

        if self.healthStatus == "sick":
            self.daysSick += 1

        if self.healthStatus == "healthy":
            # check if they are near a sick person
            neighbors = self.model.environment.neighbors(self)
            near_sick = any(a.healthStatus == "sick" for a in neighbors)

            if near_sick:
                if self.sickProb():
                    return

        # anybody who gets this far moves (incl recovered agents)
        x, y = self.model.environment.positions[self]
        dx, dy = random.choice([[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)])
        new_pos = ((x+dx) % self.model.p.size, (y+dy) % self.model.p.size)
        self.model.environment.move_to(self, new_pos)

        # check if recovered before moving to next step
        self.recovered()

    def sickPeriod(self):
        dead = False
        # if they are in the sick period
        if 0 < self.daysSick < 6:
            if random.random() < 0.016:
                self.healthStatus = "dead"
                dead = True
        return dead
    def sickProb(self):
        sick = False
        if random.random() < 0.2:
            # set them to sick
            self.healthStatus = "sick"
            self.daysSick = 1
            sick = True
        return sick
    
    def recovered(self):
        # if they have been sick for more than 5 days
        # increments by 1 so would alway be at 6
        if self.daysSick == 6:
            # reset days sick
            self.daysSick = 0
            self.healthStatus = "recovered"



class Environment(ap.Model):
    '''
    Simulation should end when there are no more living and/or sick individuals.
    Everybody should get sick and recover or die.
    '''
    def setup(self):
        self.agents = ap.AgentList(self, self.p.population, Human)

        # infect exactly one agent after all are created
        patient_zero = self.agents.random() # or self.agents[0]
        patient_zero.healthStatus = "sick"
        patient_zero.daysSick = 1
        
        #create grid and add agents (torus for when agents go to the edge they can loop back around)
        self.environment = ap.Grid(self, [self.p.size]*2, track_empty=True, torus=True)
        self.environment.add_agents(self.agents, random=True, empty=True)
        
    def step(self):
        self.agents.step()

    def update(self):
        # update the number of SIRD for each by getting the subset of the lists
        self.record('Sick', len(self.agents.select(self.agents.healthStatus == "sick")))
        self.record('Healthy', len(self.agents.select(self.agents.healthStatus == "healthy")))
        self.record('Recovered', len(self.agents.select(self.agents.healthStatus == "recovered")))
        self.record('Dead', len(self.agents.select(self.agents.healthStatus == "dead")))

parameters = {
    'size': 20,
    'population': 50,
}

def animation_plot(model, ax):
    import numpy as np
    grid_data = np.zeros((model.p.size, model.p.size))

    for p in model.agents:
        x, y = model.environment.positions[p]
        
        if p.healthStatus == "healthy":
            grid_data[x, y] = 1
        elif p.healthStatus == "recovered":
            grid_data[x, y] = 2
        elif p.healthStatus == "sick":
            grid_data[x, y] = 3
        elif p.healthStatus == "dead":
            grid_data[x, y] = 4


    cmap = ListedColormap(['#ffffff', '#29F229', '#3BAEF5', '#FF3636', '#000000'])
    ap.gridplot(grid_data, ax=ax, cmap=cmap, vmin=0, vmax=4)    
    ax.set_title(f"Days={model.t} Population={(len(model.agents.select(model.agents.healthStatus == 'healthy'))) + (len(model.agents.select(model.agents.healthStatus == 'recovered'))) + (len(model.agents.select(model.agents.healthStatus == 'sick')))} Dead={len(model.agents.select(model.agents.healthStatus == 'dead'))}")

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

model = Environment(parameters)
model.setup()
animation_plot(model, ax)

sick_history = []
healthy_history = []
dead_history = []
recovered_history = []

def next_step(event):

    model.t += 1
    model.step()

    sick_history.append(len(model.agents.select(model.agents.healthStatus == "sick")))
    healthy_history.append(len(model.agents.select(model.agents.healthStatus == "healthy")))
    dead_history.append(len(model.agents.select(model.agents.healthStatus =="dead")))
    recovered_history.append(len(model.agents.select(model.agents.healthStatus == "recovered")))

    animation_plot(model, ax)
    fig.canvas.draw()

    # ending parameters for simulation
    # if there is no more sickness
    if len(model.agents.select(model.agents.healthStatus == "sick")) == 0:
        plt.close()
        plt.plot(sick_history, label='Sick', color='#FF3636')
        plt.plot(healthy_history, label='Healthy', color='#29F229')
        plt.plot(dead_history, label='Dead', color='#000000')
        plt.plot(recovered_history, label='Recovered', color='#3BAEF5')
        plt.xlabel('Day')
        plt.legend()
        plt.show()

ax_button = plt.axes([0.4, 0.05, 0.2, 0.08])
button = Button(ax_button, 'Next Step')
button.on_clicked(next_step)

plt.show()