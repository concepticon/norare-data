from scipy.stats import kendalltau
from collections import defaultdict
from pyconcepticon import Concepticon
from itertools import combinations
from tabulate import tabulate
from statistics import mean
from scipy.stats import spearmanr, pearsonr
# for convenience of parsing
import igraph

concepticon = Concepticon()

# load list 2014, for mapping to concepticon
clics1 = {}
for concept in concepticon.conceptlists['List-2014-1280'].concepts.values():
    clics1[concept.english] = concept.concepticon_id

# load clics2 and clics1 to see which concepts we have for pairs, we could also
# separate and make individual comparisons with concepts in clics1 vs. msl and
# clics2 vs. msl and Rzymsky/clics3, but we do the intersection here
clics1_concepts = {concept.concepticon_id for concept in
                   concepticon.conceptlists['List-2014-1280'].concepts.values()}
clics2_concepts = {concept.concepticon_id for concept in
                   concepticon.conceptlists["List-2018-1105"].concepts.values()}
clics3_concepts = {concept.concepticon_id for concept in
                   concepticon.conceptlists["Rzymski-2020-1624"].concepts.values()}
covered_concepts = clics1_concepts.intersection(clics2_concepts, clics3_concepts)

# igraph requires some specific reading, so we convert this already to a
# source-target pairs list for concepticon keys
# this is the graph clics2 (do we have list et al. 2018 online?)
# in all cases, you can also use other weights, like LanguageWeight, etc.!
G2 = igraph.read('infomap-1-families.gml')
graph_lookup2 = {}
for edge in G2.es:
    nA, nB = G2.vs[edge.source].attributes()["label"], G2.vs[edge.target].attributes()["label"]
    graph_lookup2[nA, nB] = edge.attributes()["FamilyWeight"]

# igraph for clics1
G1 = igraph.read('clics.gml')  # clics1 graph
graph_lookup1 = {}
for edge in G1.es:
    nA, nB = G1.vs[edge.source].attributes()["label"], G1.vs[edge.target].attributes()["label"]
    graph_lookup1[clics1[nA], clics1[nB]] = edge.attributes()["families"]

# igraph for clics3
G3 = igraph.read('network-3-families.gml')
graph_lookup3 = {}
for edge in G3.es:
    nA, nB = G3.vs[edge.source].attributes()["label"], G3.vs[edge.target].attributes()["label"]
    graph_lookup3[nA, nB] = edge.attributes()["FamilyWeight"]

# load multisimlex, this is a bit more complex, since we have to get the
# information on the pairings
languages = ["english", "russian", "chinese", "cantonese", "arabic",
             "spanish", "polish", "french", "estonian", "finnish"]
msl = {}
cl = {
    concept.number: concept for concept in concepticon.conceptlists[
        "Vulic-2020-2244"].concepts.values()}
msl = {}
for concept in cl.values():
    # retrieve all specific values, they are already formatted as a list here
    values = [concept.attributes[attribute] for attribute in
              ["simlex_ids"] + [language + "_score" for language in languages]]
    # zipping values, means, we tackle them in their order
    for i in range(len(values[0])):
        msl[values[0][i]] = (
            concept.concepticon_id or "",
            concept.concepticon_gloss or "", [
                values[j][i] for j in range(1, len(values))])

pairs = {language: [] for language in languages}
pairs['clics1'] = []
pairs['clics2'] = []
pairs['clics3'] = []
for i in range(1, 1889):
    (cidA, cglB, scoresA), (cidB, cglB, scoresB) = msl[str(i) + ':1'], msl[str(i) + ':2']
    if cidA in covered_concepts and cidB in covered_concepts:
        for j, language in enumerate(languages):
            assert scoresA[j] == scoresB[j]
            pairs[language] += [scoresA[j]]
        # we convert to integer, since the metadata.json does not assign this
        # yet as integer, since it is not yet in norare
        # this can be varied by adding, e.g., weighted_degree as well!
        try:
            pairs["clics1"] += [
                graph_lookup1[cidA, cidB]
            ]
        except KeyError:
            pairs["clics1"] += [0]

        try:
            pairs["clics2"] += [
                graph_lookup2[cidA, cidB]
            ]
        except KeyError:
            pairs["clics2"] += [0]

        try:
            pairs["clics3"] += [
                graph_lookup3[cidA, cidB]
            ]
        except KeyError:
            pairs["clics3"] += [0]

print("found {0} pairs in common".format(len(pairs["clics1"])))

# average correlations
msl_scores, table = [], []
for langA, langB in combinations(languages, r=2):
    t, s = pearsonr(pairs[langA], pairs[langB])
    table += [[langA, langB, t, s]]
    msl_scores += [t]

# correlate against clics1
clics_scores = []
for lang in languages:
    t, s = pearsonr(pairs[lang], pairs["clics1"])
    clics_scores += [t]
    table += [[lang, "clics1", t, s]]

# correlate against clics2
clics2_scores = []
for lang in languages:
    t, s = pearsonr(pairs[lang], pairs["clics2"])
    clics2_scores += [t]
    table += [[lang, "clics2", t, s]]

# correlate against clics3
clics3_scores = []
for lang in languages:
    t, s = pearsonr(pairs[lang], pairs["clics3"])
    clics3_scores += [t]
    table += [[lang, "clics3", t, s]]

table += [["MSL (average)", mean(msl_scores), '']]
table += [["CLICS (average)", mean(clics_scores), '']]
table += [["CLICS2 (average)", mean(clics2_scores), '']]
table += [["CLICS3 (average)", mean(clics3_scores), '']]

print(tabulate(table, headers="firstrow", floatfmt=".2f"))
