import collections
import igraph
import enum
import functools


class Graphs(enum.Enum):  # We read data from three different CLICS graphs.
    Full = 1
    Affix = 2
    Overlap = 3


def node_dict(type_):  # The skeleton for a concept node.
    res = {'ID': '', 'NAME': ''}
    if type_ == 'LINKED':
        res.update({'{}{}'.format(Graphs.Full.name, s): 0 for s in ['Vars', 'Lngs', 'Fams']})
        res.update({'{}{}'.format(Graphs.Overlap.name, s): 0 for s in ['Vars', 'Lngs', 'Fams']})
    else:
        res.update({'{}{}'.format(Graphs.Affix.name, s): 0 for s in ['Vars', 'Lngs', 'Fams']})
    return res


def download(dataset):

    dataset.download_zip(
            "https://github.com/lingpy/pacs/raw/main/examples/colexifications-graphs.zip",
            target="graphs.zip",
            filename="colexification-affix.gml"
            )
    dataset.download_zip(
            "https://github.com/lingpy/pacs/raw/main/examples/colexifications-graphs.zip",
            target="graphs.zip",
            filename="colexification-full.gml"
            )
    dataset.download_zip(
            "https://github.com/lingpy/pacs/raw/main/examples/colexifications-graphs.zip",
            target="graphs.zip",
            filename="colexification-overlap.gml"
            )


def map(dataset, concepticon, mappings):

    listdata = concepticon.conceptlists[dataset.concepticon]
    c2i = {c.gloss: c.id for c in concepticon.conceptsets.values()}
    g2i = {c.concepticon_gloss: c.id for c in listdata.concepts.values()}

    # iterate over graphs and read them with igraph
    concepts = {}
    for g in Graphs:
        print(f"Reading Graph {g.name}")
        graph = igraph.read(
                dataset.raw_dir / f"colexification-{g.name.lower()}.gml")
        for i, node in enumerate(graph.vs):
            data = node.attributes()
            concepts[data["label"]] = collections.OrderedDict([
                ('variety_count', int(data["variety_count"])),
                ('language_count', int(data["language_count"])),
                ('family_count', int(data["family_count"])),
                ('linked_concepts', collections.defaultdict(functools.partial(node_dict, 'LINKED'))),
                ('target_concepts', collections.defaultdict(functools.partial(node_dict, 'TARGET')))
            ])
        for edge in graph.es:
            if ((g != Graphs.Overlap and int(edge["family_count"]) > 1)
                    or (g == Graphs.Overlap and int(edge["family_count"]) > 4)):
                sname, tname = graph.vs[edge.source]["label"], graph.vs[edge.target]["label"]
                jds = concepts[sname]['target_concepts' if g == Graphs.Affix else 'linked_concepts']
                target_idx = g2i[tname]
                jds[target_idx]["ID"] = target_idx
                jds[target_idx]["NAME"] = tname
                jds[target_idx][g.name + "Vars"] = int(edge["variety_count"])
                jds[target_idx][g.name + "Lngs"] = int(edge["language_count"])
                jds[target_idx][g.name + "Fams"] = int(edge["family_count"])
                if g != Graphs.Affix:
                    jds = concepts[tname]['linked_concepts']
                    target_idx = g2i[sname]
                    jds[target_idx]["ID"] = target_idx
                    jds[target_idx]["NAME"] = sname
                    jds[target_idx][g.name + "Vars"] = int(edge["variety_count"])
                    jds[target_idx][g.name + "Lngs"] = int(edge["language_count"])
                    jds[target_idx][g.name + "Fams"] = int(edge["family_count"])
    table = []
    for concept in listdata.concepts.values():
        row = collections.OrderedDict([
            ('ID', concept.id),
            ('NUMBER', concept.number),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('ENGLISH', concept.english),
            (
                'FAMILY_COUNT', 
                concepts[concept.concepticon_gloss]["family_count"]
                ),
            (
                'LANGUAGE_COUNT', 
                concepts[concept.concepticon_gloss]["language_count"]
                ),
            (
                'VARIETY_COUNT', 
                concepts[concept.concepticon_gloss]["variety_count"]
                ),
            (
                'LINKED_CONCEPTS', 
                concepts[concept.concepticon_gloss]["linked_concepts"]
                ),
            (
                'TARGET_CONCEPTS', 
                concepts[concept.concepticon_gloss]["target_concepts"]
                ),
        ])
        table.append(row)

    # Write to output
    dataset.table.write(table)
