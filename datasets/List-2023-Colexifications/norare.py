from urllib.request import urlretrieve
import zipfile
import collections
from pyconcepticon import models
import json
import pathlib

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
    print(listdata)
    input()
    base_dir = pathlib.Path(__file__).parent.resolve()
    new_tsv_path = base_dir / "List-2023-1308.tsv"  # change this if your file has a different name

    listdata = models.Conceptlist.from_file(new_tsv_path)

    # Initialize relationship dictionaries
    target_concepts = {concept.id: [] for concept in listdata.concepts.values()}
    linked_concepts = {concept.id: [] for concept in listdata.concepts.values()}

    # JSON parsing helper
    def parse_json_field(field):
        try:
            return json.loads(field) if field else []
        except json.JSONDecodeError:
            return []

    # Populate relationship data
    for concept in listdata.concepts.values():
        tc = parse_json_field(concept.attributes.get("target_concepts", "[]"))
        lc = parse_json_field(concept.attributes.get("linked_concepts", "[]"))
        target_concepts[concept.id] = tc
        linked_concepts[concept.id] = lc

    # Construct output table
    table = []
    for concept in listdata.concepts.values():
        row = collections.OrderedDict([
            ('ID', concept.id),
            ('NUMBER', concept.number),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('ENGLISH', concept.english),
            ('FAMILY_COUNT', concept.attributes.get('family_count', '')),
            ('LANGUAGE_COUNT', concept.attributes.get('language_count', '')),
            ('VARIETY_COUNT', concept.attributes.get('variety_count', '')),
            ('LINKED_CONCEPTS', linked_concepts[concept.id]),
            ('TARGET_CONCEPTS', target_concepts[concept.id]),
        ])
        table.append(row)

    # Write to output
    dataset.table.write(table)
