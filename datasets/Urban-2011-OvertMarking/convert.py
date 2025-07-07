import pathlib
import collections
import os

from csvw.dsv import reader
from pyconcepticon import models
from pyconcepticon.util import ConceptlistWithNetworksWriter

# Set your conceptlist ID and output filename
conceptlist_id = "Urban-2011-160"
output_filename = conceptlist_id

# Set base directory and force working directory to script folder
base_dir = pathlib.Path(__file__).parent.resolve()
os.chdir(base_dir)

# Load conceptlist
urban = models.Conceptlist.from_file("raw/Urban-2011-160.tsv")
concept2id = {concept.english: concept.id for concept in urban.concepts.values()}

# Load Indo-Aryan shift data with typo normalization
reps = {
    "mirrow": "mirror",
    "straw/hay": "straw",
    "cheeck": "cheek"
}
iashifts = collections.defaultdict(dict)
for row in reader("raw/indo-aryan-shifts.tsv", delimiter="\t", dicts=True):
    source = reps.get(row["Source"], row["Source"])
    target = reps.get(row["Target"], row["Target"])
    iashifts[source][target] = row["ID"]

# Initialize containers
linked_concepts = {concept.id: [] for concept in urban.concepts.values()}
targeted_concepts = {concept.id: [] for concept in urban.concepts.values()}

# Build relationships
for concept in urban.concepts.values():
    targets, links = [], []

    # Indo-Aryan shifts only (no semantic_change)
    if concept.english in iashifts and not concept.attributes["semantic_change"]:
        for target, idx in iashifts[concept.english].items():
            if target not in concept2id:
                continue
            targeted_concepts[concept.id].append({
                "ID": concept2id[target],
                "NAME": target,
                "OvertMarking": 0,
                "IndoAryanShift": 1,
                "ShiftID": idx
            })

    # Semantic change shifts
    if concept.attributes["semantic_change"]:
        for entry in concept.attributes["semantic_change"].split("; "):
            try:
                data_a, data_b = entry.split("» (")
                number = data_a.split(" ")[0][1:-1]
                source = data_a.split(">")[0].split("«")[1][:-2]
                target = data_a.split(">")[1].strip()[1:]
                polysemies = int(data_b.split(" ")[0])
                overt = int(data_b.split(", ")[1].split(" ")[0])
                target = reps.get(target, target)

                if target not in concept2id:
                    continue

                attested_shift = 0
                if concept.english in iashifts and target in iashifts[concept.english]:
                    attested_shift = 1

                shift_id = int(number) + 1

                targeted_concepts[concept.id].append({
                    "ID": concept2id[target],
                    "NAME": target,
                    "OvertMarking": overt,
                    "IndoAryanShift": attested_shift,
                    "ShiftID": shift_id
                })

                linked_concepts[concept.id].append({
                    "ID": concept2id[target],
                    "NAME": target,
                    "Polysemy": polysemies,
                    "ShiftID": shift_id
                })

                linked_concepts[concept2id[target]].append({
                    "ID": concept.id,
                    "NAME": concept.english,
                    "Polysemy": polysemies,
                    "ShiftID": shift_id
                })

            except Exception as e:
                print(f"Skipping malformed entry: '{entry}' due to error: {e}")

# Write output
with ConceptlistWithNetworksWriter(output_filename) as table:
    for concept in urban.concepts.values():
        row = collections.OrderedDict([
            ('NUMBER', concept.number),
            ('ENGLISH', concept.english),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('SEMANTIC_CLASS_ID', concept.attributes.get("semantic_class_id", '')),
            ('CATEGORY', concept.attributes.get("category", '')),
            ('TARGET_CONCEPTS', targeted_concepts[concept.id]),
            ('LINKED_CONCEPTS', linked_concepts[concept.id])
        ])
        table.append(row)
