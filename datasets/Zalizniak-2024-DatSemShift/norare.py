import collections
from pyconcepticon import models
from csvw.dsv import reader
import json

def download(dataset):
    dataset.download_zip(
        'https://github.com/concepticon/concepticon-data/archive/refs/heads/master.zip',
        'concepticon-data-master.zip',
        'concepticon-data-master/concepticondata/conceptlists/Zalizniak-2024-4583.tsv'
    )

def map(dataset, concepticon, mappings):
    # Load the CLDF-formatted Zalizniak file from the downloaded zip
    zalizniak = models.Conceptlist.from_file(
        dataset.raw_dir / "concepticon-data-master" / "concepticondata" / "conceptlists" / "Zalizniak-2024-4583.tsv"
    )
    
    # Initialize relationship dictionaries
    target_concepts = {concept.id: [] for concept in zalizniak.concepts.values()}
    linked_concepts = {concept.id: [] for concept in zalizniak.concepts.values()}

    # JSON parsing helper
    def parse_json_field(field):
        try:
            return json.loads(field) if field else []
        except json.JSONDecodeError:
            return []

    # Populate relationship data
    for concept in zalizniak.concepts.values():
        tc = parse_json_field(concept.attributes.get("target_concepts", "[]"))
        lc = parse_json_field(concept.attributes.get("linked_concepts", "[]"))
        target_concepts[concept.id] = tc
        linked_concepts[concept.id] = lc

    # Construct output table
    table = []
    for concept in zalizniak.concepts.values():
        row = collections.OrderedDict([
            ('ID', concept.id),
            ('NUMBER', concept.number),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('ENGLISH', concept.english),
            ('GLOSS_IN_SOURCE', concept.attributes.get('gloss_in_source', '')),
            ('TARGET_CONCEPTS', target_concepts[concept.id]),
            ('LINKED_CONCEPTS', linked_concepts[concept.id]),
            ('SHIFTS', concept.attributes.get('shifts', '')),
            ('DOMAIN', concept.attributes.get('domain', '')),
            ('ALIAS', concept.attributes.get('alias', '')),
            ('DEFINITION', concept.attributes.get('definition', '')),
        ])
        table.append(row)

    # Write to output
    dataset.table.write(table)
