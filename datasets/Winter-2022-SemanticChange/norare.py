import collections
from pyconcepticon import models
from csvw.dsv import UnicodeDictReader
import json

def download(dataset):
    dataset.download_file(
        "https://github.com/bodowinter/asymmetry/raw/master/data/asymmetry.csv",
        "asymmetry.csv"
        )


def map(dataset, concepticon, mappings):
    # Load the Winter-2022-98 concept list from the raw folder inside the downloaded zip
    winter = concepticon.conceptlists[dataset.concepticon]

    # must correct for error in data
    correct = {
        "soil": "soil/earth",
        "Milky Way": "milky way",
        "river": "river/stream",
        "fog": "fog/mist",
        "(molar) tooth": "tooth",
        "stomach": "belly/stomach"
    }
    
    map_concepts = {
        "pupil": ["1658", "PUPIL"],
        "straw/hay": ["2299", "STRAW"],
        "spring": ["849", "SPRING (OF WATER)"],
        "meteoroid": ["2288", "METEOROID (SHOOTING OR SHINING STAR)"],
        "road/street/way": ["2457", "PATH OR ROAD"],
    }


    # read in data
    data = collections.defaultdict(list)
    with UnicodeDictReader(dataset.raw_dir / "asymmetry.csv") as reader:
        for row in reader:
            concept = correct.get(row["ConceptComplete"], row["ConceptComplete"])
            if row["ID"] == "65" and row["Word"] == "river":
                concept = "river/stream"
            data[concept].append(row)

    row2idx = {concept: idx for idx, (concept, _) in enumerate(data.items(), start=1)}

    graph = collections.defaultdict(lambda: {"sources": [], "targets": [], "linked": []})
    for concept, rows in data.items():
        for row in rows:
            if row["PairName"] == "day~noon":
                oma, omar, polysemy = 3, 20, 0
            else:
                oma, omar, polysemy = (
                    int(row["OvertMarking"]), int(row["OvertMarkingReverse"]), int(row["Polysemy"]))
            _s, _t = row["PairName"].split("~")
            source, target = correct.get(_s, _s), correct.get(_t, _t)

            source_id, target_id = (
                    "{}-{}".format(dataset.id, row2idx[source]),
                    "{}-{}".format(dataset.id, row2idx[target]))

            source_json = {"NAME": source, "ID": source_id, "OvertMarking": oma}
            target_json = {"NAME": target, "ID": target_id, "OvertMarking": oma}
            if concept == source:
                links_json = {"NAME": target, "ID": target_id, "Polysemy": polysemy}
            elif concept == target:
                links_json = {"NAME": source, "ID": source_id, "Polysemy": polysemy}
            if concept == source:
                graph[concept]["targets"] += [target_json]
                graph[concept]["sources"] += [{
                    k: omar if k == "OvertMarking" else v for k, v in target_json.items()}]
            else:
                graph[concept]["sources"] += [source_json]
                graph[concept]["targets"] += [{
                    k: omar if k == "OvertMarking" else v for k, v in source_json.items()}]
            graph[concept]["linked"] += [links_json]
            
     # Build the output table with all fields required
    table = []
    for concept in winter.concepts.values():
        row = collections.OrderedDict([
            ('ID', concept.id),
            ('NUMBER', concept.number),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('ENGLISH', concept.english),
            ('TARGET_CONCEPTS', graph[concept.english]['sources']),
            ('SOURCE_CONCEPTS', graph[concept.english]['targets']),
            ('LINKED_CONCEPTS', graph[concept.english]['linked']),
        ])
        table.append(row)

    # Write the table back into the dataset
    dataset.table.write(table)
