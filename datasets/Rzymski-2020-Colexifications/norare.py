import igraph
import networkx as nx
import collections
from lingpy.convert.graph import igraph2networkx

def download(dataset):
    dataset.download_zip(
        "https://github.com/clics/clics3/raw/refs/tags/v1.1/clics3-infomap.gml.zip",
        "clics3-infomap.gml.zip",
        "graphs/infomap-3-families.gml"
        )

def map(dataset, concepticon, mappings):

    lookup = {c.id: c.gloss for c in
                concepticon.conceptsets.values()}

    
    graph = igraph.read(dataset.raw_dir / "graphs" / "infomap-3-families.gml")
    count = 0
    visited = set()
    for node in graph.vs:
        node['name'] = node['label']
        visited.add(node['label'])
    # convert graph to networkx graph for convenience
    graph = igraph2networkx(graph)
    
    deg = dict(nx.degree(graph))
    fdeg = nx.degree(graph, weight='FamilyWeight')
    ldeg = nx.degree(graph, weight='LanguageWeight')

    concepts = {lookup[c]: c for c in visited}
    concept_ids = {cid: f"Rzymski-2020-{i + 1}" for i, cid in
                   enumerate(sorted(visited))}
    # calculate the json links
    links = {concept: [] for concept in concepts}


    # iterate over concepts / nodes and compute links per node
    for gloss, idx in concepts.items():
        for neighbor, weights in graph[idx].items():
            nidx = concept_ids[neighbor]
            links[gloss] += [{
                "ID": nidx,
                "NAME": lookup[neighbor],
                "WordWeight": int(weights["WordWeight"]),
                "LanguageWeight": int(weights["LanguageWeight"]),
                "FamilyWeight": int(weights["FamilyWeight"])
                }]

    ranks = {gloss: i + 1 for i, gloss in enumerate(sorted(concepts, key=lambda x:
                                                       deg.get(concepts[x], 0)))}
    # iterate over all concepts again, insert degree and the like
    table = []
    for gloss, idx in concepts.items():
        # get community from graph
        community, central_concept = "", ""
        community = graph.nodes[idx]["infomap"]
        central_concept = graph.nodes[idx]["CentralConcept"]
        ff = graph.nodes[idx]["FamilyFrequency"]
        lf = graph.nodes[idx]["LanguageFrequency"]
        wf = graph.nodes[idx]["WordFrequency"]

        table += [collections.OrderedDict({
            "ID": concept_ids[idx],
            "NUMBER": concept_ids[idx].split("-")[-1],
            "CONCEPTICON_ID": idx,
            "CONCEPTICON_GLOSS": gloss,
            "ENGLISH": gloss,
            "FAMILY_FREQUENCY": int(ff),
            "LANGUAGE_FREQUENCY": int(lf),
            "WORD_FREQUENCY": int(wf),
            "RANK": ranks[gloss],
            "COMMUNITY": community,
            "CENTRAL_CONCEPT": central_concept,
            "DEGREE": int(deg[idx]),
            "WEIGHTED_FAMILY_DEGREE": int(fdeg[idx]),
            "WEIGHTED_LANGUAGE_DEGREE": int(fdeg[idx]),
            "LINKED_CONCEPTS": links[gloss]
            })]
    
    dataset.table.write(table)