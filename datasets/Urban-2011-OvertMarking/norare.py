import collections
from pyconcepticon import models
import csv
from csvw.dsv import UnicodeDictReader


def download(dataset):
    
    pass


def map(dataset, concepticon, mappings):

    # load the concept list that we downloaded
    urban = concepticon.conceptlists["Urban-2011-160"]
    
    # make dictionary to retrieve concepticon ID from the english values
    concept2id = {concept.english: concept.id for concept in urban.concepts.values()}

    # replacement dictionary corrects mismatches from the TSV file with
    # Concepticon
    reps = {"mirrow": "mirror", "straw/hay": "straw", "cheeck": "cheek"}
    
    # collect the shifts
    shifts = collections.defaultdict(dict)
    with UnicodeDictReader(
            dataset.raw_dir / "indo-aryan-shifts.tsv", delimiter="\t"
            ) as reader:
        for row in reader:
            # control for mismatches
            source = reps.get(row["Source"], row["Source"])
            target = reps.get(row["Target"], row["Target"])

            # populate shifts
            shifts[source][target] = row["ID"]

    # 
    linked_concepts = {concept.id: [] for concept in urban.concepts.values()}
    target_concepts = {concept.id: [] for concept in urban.concepts.values()}
    table = []
    for concept in urban.concepts.values():
        targets, links = [], []
        if concept.english in shifts and not concept.attributes["semantic_change"]:
            for target, idx in shifts[concept.english].items():
                target_concepts[concept.id] += [{
                    "ID": concept2id[target],
                    "NAME": target,
                    "OvertMarking": 0,
                    "IndoAryanShift": 1,
                    "ShiftID": idx}]
        if concept.attributes['semantic_change']:
            for text in concept.attributes["semantic_change"].split("; "):
                data_a, data_b = text.split("» (")
                number = data_a.split(" ")[0][1:-1]                
                source = data_a.split(">")[0].split("«")[1][:-2]
                target = data_a.split(">")[1].strip()[1:]
                target = reps.get(target, target)
                polysemies = data_b.split(" ")[0]
                overt = data_b.split(", ")[1].split(" ")[0]
                attested_shift = 0
                if concept.english in shifts:
                    if target in shifts[concept.english]:
                        attested_shift = 1
                target_concepts[concept.id] += [{
                    "ID": concept2id[target],
                    "NAME": target,
                    "OvertMarking": int(overt),
                    "IndoAryanShift": attested_shift,
                    "ShiftID": int(number) + 1}]
                linked_concepts[concept.id] += [{
                    "ID": concept2id[target],
                    "NAME": target,
                    "Polysemy": int(polysemies),
                    "ShiftID": int(number)+ 1}]
                linked_concepts[concept2id[target]] += [{
                    "ID": concept.id,
                    "NAME": concept.english,
                    "Polysemy": int(polysemies),
                    "ShiftID": int(number) + 1}]
        table.append({
            "ID": concept.id,
            "NUMBER": concept.number,
            "CONCEPTICON_ID": concept.concepticon_id,
            "CONCEPTICON_GLOSS": concept.concepticon_gloss,
            "ENGLISH": concept.english,
            "TARGET_CONCEPTS": target_concepts[concept.id],
            "LINKED_CONCEPTS": linked_concepts[concept.id],
            "SEMANTIC_CHANGE": concept.attributes["semantic_change"],
            "SEMANTIC_CLASS_ID": concept.attributes["semantic_class_id"],
            "CATEGORY": concept.attributes["category"]
            })
    dataset.table.write(table)


