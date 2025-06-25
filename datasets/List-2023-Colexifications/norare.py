import collections
from pyconcepticon import models
import json

def download(dataset):
    dataset.download_zip(
        'https://github.com/concepticon/concepticon-data/archive/refs/heads/master.zip',
        'concepticon-data-master.zip',
        'concepticon-data-master/concepticondata/conceptlists/List-2023-1308.tsv'
    )


def map(dataset, concepticon, mappings):
    listdata = models.Conceptlist.from_file(
        dataset.raw_dir / "concepticon-data-master" / "concepticondata" / "conceptlists" / "List-2023-1308.tsv"
    )

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
