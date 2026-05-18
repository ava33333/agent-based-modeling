https://onlinelibrary.wiley.com/doi/epdf/10.1111/1755-0998.13704

https://github.com/lozuponelab/SCNIC

Look into later:

- Lauder et al. 2016 in *Microbiome* has a readable methods overview
- The QIIME2 documentation (qiime2.org) has a plain-language explanation of the whole workflow
- Knight et al. 2018 "Best practices for analysing microbiomes" in *Nature Reviews Microbiology* — worth adding to your reading list generally

### Overview:

This paper talks about the software SCNIC, which stands for sparse cooccurrence network investigation for compositional data. Though this software was initially developed for microbial data, it can also be applied to other multi-omic* data sets (the author however noted in the discussion that it is optimized for microbial data sets). It works by generating correlation networks and can detect and summarize modules* of highly correlated features. This is important for downstream statistical analysis and increases statistical power through feature reduction. Feature reduction allows researchers to look at fewer features, which reduces the amount of false positives between microbes. SCNIC was used on data sets from previous studies (HIV and Great Lakes) which further confirmed previous findings, and improved statistical power by identifying more associate taxa. 

### Comparison to ABM

- SCNIC is an inference tool which takes data and works backwards to figure out which microbes are correlated and groups them
    - determined network structure but doesn’t simulate anything
- ABM simulates network structure and runs it to see what behaviors emerge
- SCNIC gives static snapshot (like temporal network) and ABM provides dynamic layer
- The correlation network from SCNIC could be used to define ABM rules and further map out microbe interactions

### Notes/definitions:

- Multi-omic data: combines multiple (2+) types of omic data
    - Omic: large scale biological data types (ex: genomics (DNA), transcripomics (RNA), metabolomics (metabolism)
- LMM and SMD: algorithms for grouping nodes in a network into clusters (modules)
    - Louvain Modularity Maximization (LMM): “greedy optimization”; repeatedly merges pairs of groups that most improve overall network modularity until merging no longer helps
    - Shared Minimum Distance (SMD): only groups microbes together if every pair in the group is correlated above your threshold
        - stricter than LMM
- (review) RNA types:
    - mRNA: messenger RNA (carries genetic instructions)
    - tRNA: transfer RNA (brings amino acids during protein building)
    - rRNA: ribosomal RNA (structural/functional component of ribosomes)
        - ribosomes: cellular machines that build proteins
- 16S rRNA sequencing: extract DNA from sample, amplify the specific genetic region on every bacteria in the sample with the 16S rRNA, sequence it, use variation to identify which species are there
    - 16S rRNA: subunit of ribosome found in bacteria + archaea useful for identifying microbes\
- Feature reduction: decreasing the number of things you’re testing simultaneously, which reduces the false positive rate
    - Feature: specific thing being measured
- OTU: operational taxonomic unit; “bins” of sequences that are similar
- Modular partitions: how the network gets divided into modules
- Modules: clusters of microbes
    - SCNIC summarizes modules by summing counts, which preserves total sample counts (why it is compatible with tools like ANCOM & why it has advantage over WGCNA)
- Sparsity: most entries are 0 (sparse data set)
- Compositionality: data only tells relative abundancies, not absolute counts
- Statistical power: ability to detect a real effect
    - SCNIC does this by reducing the number of comparisons