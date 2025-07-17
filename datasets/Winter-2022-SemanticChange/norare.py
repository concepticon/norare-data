import collections
import builtins


def download(dataset):
    dataset.download_file(
        "https://github.com/bodowinter/asymmetry/raw/master/data/asymmetry.csv",
        )


def map(dataset, concepticon, mappings):

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
    for row in dataset.get_csv("asymmetry.csv", delimiter=",", dicts=True):
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
            source, target = list(builtins.map(
                lambda x: correct.get(x, x), row["PairName"].split("~")))
            source_id, target_id = list(builtins.map(
                lambda x: "{}-{}".format(dataset.id, row2idx[x]),
                [source, target]))
    
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



    # Load the Winter-2022-98 concept list from the raw folder inside the downloaded zip
    # winter = concepticon.conceptlists["Winter-2022-98"] 
    winter = {concept.english: concept for concept in
              concepticon.conceptlists["Winter-2022-98"].concepts.values()
              }
    
    table = []
    for concept in graph:
        table.append(dict([
            ("ID", winter[concept].id),
            ('NUMBER', str(row2idx[concept])),
            ('ENGLISH', concept),
            ('CONCEPTICON_ID', winter[concept].concepticon_id),
            ('CONCEPTICON_GLOSS', winter[concept].concepticon_gloss),
            ('SOURCE_CONCEPTS', graph[concept]["sources"]),
            ('TARGET_CONCEPTS', graph[concept]["targets"]),
            ('LINKED_CONCEPTS', graph[concept]["linked"]),
            ]))

    # Write the table back into the dataset
    dataset.table.write(table)
