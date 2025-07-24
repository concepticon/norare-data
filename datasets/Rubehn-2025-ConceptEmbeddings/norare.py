import collections
from pyconcepticon import models
from csvw.dsv import reader
import json

def download(dataset):
    dataset.download_file("https://raw.githubusercontent.com/calc-project/concept-embeddings/refs/heads/main/embeddings/full-affix-overlap/prone.json")

def map(dataset, concepticon, mappings):
    with open(dataset.raw_dir / "prone.json") as f:
        embedding_data = json.load(f)

    # map concepticon gloss to id
    concepticon_gloss_to_id = {c.gloss: c.id for c in concepticon.conceptsets.values()}

    table = []
    for i, (concepticon_gloss, embedding) in enumerate(embedding_data["embeddings"].items()):
        row = collections.OrderedDict([
            ("ID", f"Rubehn-2025-{len(embedding_data["embeddings"])}-{i+1}"), # TODO where the ID's should actually come from?
            ("CONCEPTICON_ID", concepticon_gloss_to_id[concepticon_gloss]),
            ("CONCEPTICON_GLOSS", concepticon_gloss),
            ("EMBEDDING", embedding)
        ])

        table.append(row)

    # Write to output
    dataset.table.write(table)
