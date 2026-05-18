paper: https://link.springer.com/chapter/10.1007/978-3-032-09802-3_8

model: https://zenodo.org/records/14635432

Summary (what I got from the paper)

Paper is on modeling email and text interactions between individuals with temporal models. While the paper is based on a retrospective analysis of past events, this type of analysis can be applied to forensic analysis of criminal activity to predict/detect it before it occurs in the future. The first data set was had no criminal findings, but was analyzing inappropriate interactions between employees at a company (looked for keywords like party, beer, etc.). The second data set was from the Purdue’s Cyber Security Lab and included messages from previously identified offenders of drug related offenses. The modeling was used to identify keywords— specifically from the list of the DEA’s codeword list for the second set— and extrapolate behaviors by defining the interactions as “good” or “bad”.

Terms/definitions:

- Temporal Network: a dynamic map of relationships between entities, using nodes and edges
    - Nodes: individual entities on the network
    - Edges: interactions (ie email sent)
    - Motifs: smallest unit in a temporal network
        - Event motif: network comprising edges that connect nodes involved in a common event
    - Snapshot: “static picture” of patterns in a temporal network during a specified time frame
- Benefits of temporal networks:
    - data exploration and analysis
    - dynamic data and time based patterns
    - flexible and supports fast querying
    - sequential ordering
- NLP: natural language processing; specifically used in forensics to analyze things like social media, text, email, etc. for criminal activity by searching for keywords (including specific codewords)
- Static models visually shows clusters, which represents the individuals with a higher number of contacts (though this does not necessarily designate the contact as “bad”)
- Similarities between ABM and Temporal Networks:
    - mapping/graphing w/software to analyze data and extract behaviors/patterns
    - both represent individual entities and their attributes
        - ABM: agents (which are dynamic)
        - Temporal Networks: nodes (which are static)
    - both use interaction rules
    - both are built “bottom up” from individual relationships (which behaviors are later inferred from)
- Processes: 2 step construction process for static temporal network
    1. NLP extracts event motifs from timestamps
    2. Querying/reasoning
- Static model is a simplification which makes the dynamic network queryable