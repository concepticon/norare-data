import enum
import functools
import collections

import igraph
from pynorare.util import NetworksWriter



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
    for suff in ["full", "overlap", "affix"]:
        dataset.download_zip(
            "https://github.com/lingpy/pacs/raw/main/examples/colexifications-graphs.zip",
            "colexification-graphs.zip",
            f"colexification-{suff}.gml",
        )


def map(dataset, concepticon, mappings):

    concepts, label2id = {}, {}
    for g in Graphs:
        dataset.log.info('reading graph {}'.format(g.name))
        graph = igraph.read(dataset.raw_dir / "colexification-{}.gml".format(g.name.lower()))
        if g == Graphs.Full:  # Initialize the concepts.
            c2i = {c.gloss: c.id for c in concepticon.conceptsets.values()}
            for i, node in enumerate(graph.vs):
                data = node.attributes()
                label2id[data["label"]] = str(i + 1)
                concepts[label2id[data["label"]]] = collections.OrderedDict([
                    ("ID", dataset.id + "-" + label2id[data["label"]]),
                    ('NUMBER', label2id[data["label"]]),
                    ('ENGLISH', data["label"]),
                    ('CONCEPTICON_ID', c2i[data["label"]]),
                    ('CONCEPTICON_GLOSS', data["label"]),
                    ('VARIETY_COUNT', int(data["variety_count"])),
                    ('LANGUAGE_COUNT', int(data["language_count"])),
                    ('FAMILY_COUNT', int(data["family_count"])),
                    ('LINKED_CONCEPTS', collections.defaultdict(functools.partial(node_dict, 'LINKED'))),
                    ('TARGET_CONCEPTS', collections.defaultdict(functools.partial(node_dict, 'TARGET')))
                ])
    
        for edge in graph.es:  # Collect the data for the network columns.
            if ((g != Graphs.Overlap and int(edge["family_count"]) > 1)
                    or (g == Graphs.Overlap and int(edge["family_count"]) > 4)):  # Apply thresholds.
                sname, tname = graph.vs[edge.source]["label"], graph.vs[edge.target]["label"]
                sidx, tidx = label2id[sname], label2id[tname]
                jds = concepts[sidx]['TARGET_CONCEPTS' if g == Graphs.Affix else 'LINKED_CONCEPTS']
                target_idx = dataset.id + "-" + tidx
                jds[target_idx]["ID"] = target_idx
                jds[target_idx]["NAME"] = tname
                jds[target_idx][g.name + "Vars"] = int(edge["variety_count"]) 
                jds[target_idx][g.name + "Lngs"] = int(edge["language_count"]) 
                jds[target_idx][g.name + "Fams"] = int(edge["family_count"])
                if g != Graphs.Affix:  # For non-Affix edges, we also add the reversed edge.
                    jds = concepts[tidx]['LINKED_CONCEPTS']
                    target_idx = dataset.id + "-" + sidx
                    jds[target_idx]["ID"] = target_idx
                    jds[target_idx]["NAME"] = sname
                    jds[target_idx][g.name + "Vars"] = int(edge["variety_count"]) 
                    jds[target_idx][g.name + "Lngs"] = int(edge["language_count"]) 
                    jds[target_idx][g.name + "Fams"] = int(edge["family_count"])
    table = []
    for rid, row in sorted(concepts.items(), key=lambda x: int(x[1]['NUMBER'])):
        for type_ in ['TARGET', 'LINKED']:
            row[type_ + '_CONCEPTS'] = sorted(
                row[type_ + '_CONCEPTS'].values(),
                key=lambda x: int(x["ID"].split('-')[-1]))
        table.append(row)
    dataset.table.write(table)
