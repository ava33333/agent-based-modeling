These are the notes on the Microbial Association Network Construction Tutorial. I included notes on the attached slides.

link: http://msysbiology.com/microbialnetworks/index.php

### Slides

- microbial relationship examples:
    - dental plaque formation
    - cross-feeding between bacterial symbionts of a marine worm (one is a sulfur oxidizer, the other is a sulfate reducer)
    - human skin bacteria
    - Amoeba proteus feeding on algae
    - bacteriophages infecting bacterium
    - competition between 2 species of a paramecium
    - algae bloom killing other organisms
- co-occurence: presence, absence, or shared abundance patterns of microbial taxa in specific environments or datasets
- checkerboard-like co-occurence: competition between species is shown between presences and absences across habitats
    - if two species compete they will rarely be seen in the same habitat— they alternate
- reasons for co-occurence
    - niche overlap (more competition pressure)
    - ecological relationships:
    
    | Relationship Type | ( A / B) | Co-occurence Indication |
    | --- | --- | --- |
    | mutualism | (+ / +) | positive (likely to be found in same habitat) |
    | commensalism | (+ / 0) | positive (likely to be found in same habitat) |
    | predator/parasite | (+ / -) | positive (likely to be found in same habitat) |
    | competition | (- / -) | negative (unlikely to be found in same habitat) |
    | amensalism | (- / 0) | negative (unlikely to be found in same habitat) |
    | prey/host | (- / +) | positive (likely to be found in same habitat) |
- 16s profiling used to profile communities (review: 16s profiling is a way to sequencing DNA to find specific rRNA segments that help identify different microbial taxa)
    - other ways of profiling: organism counting techniques (flow cytometry, flowcam, zooscan), phylogenetic microarrays (array with DNA probes that match known taxonomic groups)
- network inference: process of figuring out what edges should be for a model
    - ABM would use data from the network inference to dynamically map out those interactions over time
- significant co presence indicates niche overlap, mutualism, commensalism, etc.
- significant mutual exclusion indicates alternative niche preference, competitive amensalism, etc.
- there are some compositionality issues with correlation measures (similar to SCNIC notes on this)
    - compositionality means microbial abundance data is relative and if one taxon increases, others appear to decrease even if nothing actually changed (SparCC designed to handle this issue)
- regression based network inference solves some compositionality issues, but runs into various issues when large number of taxa are present
    - large taxa counts largely increases number of parameters which leads to more parameters than samples
- tools for this:
    - SparCC (sparse correlations for compositional data): works on relative abundance data directly by assuming true underlying network is sparse to aid in compositionality problem
        - limitation: sparsity assumption breaks if network is actually dense
    - MENA (molecular ecological network analysis pipeline)
        - RMT (random matrix theory) approach: way of distinguishing real biological signal in a correlation matrix from noise
    - LSA (local similarity analysis): captures time lagged associations
    - CoNet: ensemble based network— means combines multiple methods and only keeps edges that show up consistently  across methods (more reliable)