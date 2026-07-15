import igraph
import networkx as nx
from lingpy.convert.graph import igraph2networkx
import collections


def download(dataset):
    dataset.download_zip(
            "https://github.com/clics/clics2/raw/refs/heads/master/output/graphs/infomap-3-families.gml.zip",
            "infomap-3-families.gml.zip",
            "infomap-3-families.gml"
            )



def map(dataset, concepticon, mappings):
    concepts = {c.english: c for c in
                   concepticon.conceptlists[dataset.concepticon].concepts.values()}
    
    
    graph = igraph.read(dataset.raw_dir / "infomap-3-families.gml")
    for node in graph.vs:
        node['name'] = node['Gloss']
    # convert graph to networkx graph for convenience
    graph = igraph2networkx(graph)
    
    deg = dict(nx.degree(graph))
    fdeg = nx.degree(graph, weight='FamilyWeight')
    ldeg = nx.degree(graph, weight='LanguageWeight')


    # calculate the json links
    links = {concept: [] for concept in concepts}

    # iterate over concepts / nodes and compute links per node
    for gloss, concept in concepts.items():
        idx = concept.id
        if gloss in graph:
            for neighbor, weights in graph[gloss].items():
                if neighbor in concepts:
                    nidx = concepts[neighbor].id
                    links[gloss] += [{
                        "ID": nidx,
                        "NAME": neighbor,
                        "WordWeight": int(weights["WordWeight"]),
                        "LanguageWeight": int(weights["LanguageWeight"]),
                        "FamilyWeight": int(weights["FamilyWeight"])
                        }]
                else:
                    raise ValueError("neighbor must be present in concepts")
        else:
            raise ValueError("gloss must be present in graph")


    ranks = {gloss: i + 1 for i, gloss in enumerate(sorted(concepts, key=lambda x:
                                                       deg.get(x, 0)))}

    # iterate over all concepts again, insert degree and the like
    table = []
    for gloss, concept in concepts.items():
        if gloss in deg:
            d, f, l = deg[gloss], fdeg[gloss], ldeg[gloss]
        else:
            d, f, l = 0, 0, 0
        # get community from graph
        community, central_concept = "", ""
        community = graph.nodes[gloss]["infomap"]
        central_concept = graph.nodes[gloss]["CentralConcept"]
        ff = graph.nodes[gloss]["FamilyFrequency"]
        lf = graph.nodes[gloss]["LanguageFrequency"]
        wf = graph.nodes[gloss]["WordFrequency"]


        table += [collections.OrderedDict({
            "ID": concept.id,
            "CONCEPTICON_ID": concept.concepticon_id,
            "CONCEPTICON_GLOSS": concept.concepticon_gloss,
            "ENGLISH": gloss,
            "FAMILY_FREQUENCY": int(ff),
            "LANGUAGE_FREQUENCY": int(lf),
            "WORD_FREQUENCY": int(wf),
            "RANK": ranks[gloss],
            "COMMUNITY": community,
            "CENTRAL_CONCEPT": central_concept,
            "DEGREE": int(deg[gloss]),
            "WEIGHTED_FAMILY_DEGREE": int(fdeg[gloss]),
            "WEIGHTED_LANGUAGE_DEGREE": int(ldeg[gloss]),
            "LINKED_CONCEPTS": links[gloss]
            })]
    
    dataset.table.write(table)