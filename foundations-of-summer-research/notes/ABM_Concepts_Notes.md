This document holds all of my notes on the basics of ABM, microbes, and any other foundational information. I added some extra information I thought was interesting or helpful to me.

### Microbes & Biology

- microbe: a type of tiny microorganism too small to be seen by the naked eye.
    - types of microbes: bacteria, archaea, fungi, viruses, protozoa, algae, prions
- Microbes are found throughout the human body, often working symbiotically
    - gut microbiome: aka microbiota; group of microbes that live in the gut
- The gut microbiome is critical for:
    - metabolism & digestion
    - vitamin production
    - pathogen protection
    - immune regulation
- Dysbiosis: imbalance in the microbes. Can cause variety of things like:
    - SIBO/gut issues
    - neurological issues (Parkinsons, autism, Alzheimer's, depression)
    - obesity and diabetes (specifically from shifts in ratio of Bacteroidetes and Firmicutes)
- Types of microbe behaviors:
    - competition
    - mutualism
    - parasitism
    - amensalism
    - commensalism
- Gut microbiota types:
    - Dominant types are: Firmicutes, Bacteroidetes, Actinobacteria, Proteobacteria, Fusobacteria, and Verrucomicroba
        - 90 percent are Firmicutes and Bacteroides

### ABM

- ABM: agent based modeling; form of generative science (generating patterns from collected data) used to map complex, large scale patterns from interactions between agents
    - agent: independent heterogenous individual
- ABM synthesizes components to determine novel behaviors
- Each agent has a state (eg.  being sick or healthy) and a set of rules that dictates behavior (eg. “if sick, stay home”)
- Agents can have actions:
    - action from environment
    - action on environment
    - action from other agent(s)
    - action on other agent(s)
    - action on self
- Python ABM Libraries (AgentPy vs Mesa for now):
    - Mesa:
        - older, but more widely used
        - more verbose
        - manual parameter sweeps (running the model across many parameter combos to test sensitivity; eg. how does changing predator energy threshold affect population stability in a predator prey model)
        - Datacollector Pandas integration
        - Separate visual setup
    - AgentPy:
        - newer, but less community resources
        - more concise
        - built in parameter sweeps
        - native pandas integration
        - cleaner built in visual setup
    - Other libraries of note:
        - matplotlib: primary plotting library; for plotting graphs and animations in both/creating the simulation with Mesa
        - numpy: numerical computing; used for grid calculations, spatial data, and any vectorized operations on agent populations in ABM
        - seaborn: built on matplotib to make statistical plots easier and prettier; useful for visualizing simulation output distributions, heatmaps, or comparing runs
        - pandas: data manipulation (see above on how AgentPy and Mesa use it)
        - random: Python’s built in randomness; core for any stochastic ABM
- Netlogo: software for creating ABM
    - limitations:
        - uses its own proprietary language (doesn’t integrate easily with standard pipelines which use Python or R)
        - struggles with large agent counts or complex environments
        - importing/exporting data to work with external datasets is difficult/not as direct as Python based tools
        - good for quick demos but hard to customize
        - less suited for statistical analysis