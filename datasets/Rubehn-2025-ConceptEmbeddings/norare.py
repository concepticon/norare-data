import collections
import json


modes = {
    "fullfams": "EMBEDDINGS_FULL",
    "full-affix": "EMBEDDINGS_FULL_AFFIX",
    "full-affix-overlap": "EMBEDDINGS_FULL_AFFIX_OVERLAP"
}

def download(dataset):
    for mode in modes:
        dataset.download_file(f"https://raw.githubusercontent.com/calc-project/concept-embeddings/refs/tags/v.1.0/embeddings/{mode}/prone.json", f"{mode}.json")

def map(dataset, concepticon, mappings):
    embedding_data = {}

    for mode in modes:
        with open(dataset.raw_dir / f"{mode}.json") as f:
            embedding_data[mode] = json.load(f)["embeddings"]

    concepts = set()
    for mode in modes:
        concepts.update(embedding_data[mode].keys())

    # map concepticon gloss to id
    concepticon_gloss_to_id = {c.gloss: c.id for c in concepticon.conceptsets.values()
                               if c.gloss in concepts}

    table = []
    for i, (concepticon_gloss, concepticon_id) in enumerate(concepticon_gloss_to_id.items()):
        row = collections.OrderedDict([
            ("ID", f"Rubehn-2025-{len(concepticon_gloss_to_id)}-{i + 1}"), # TODO where the ID's should actually come from?
            ("CONCEPTICON_ID", concepticon_id),
            ("CONCEPTICON_GLOSS", concepticon_gloss)
        ])

        for mode, col_name in modes.items():
            row[col_name] = embedding_data[mode].get(concepticon_gloss)

        table.append(row)

    # Write to output
    dataset.table.write(table)
