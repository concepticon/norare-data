import collections
from pyconcepticon import models
from csvw.dsv import reader
import json

def download(dataset):
    dataset.download_zip(
        'https://github.com/concepticon/concepticon-data/archive/refs/heads/master.zip',
        'concepticon-data-master.zip',
        'concepticon-data-master/concepticondata/conceptlists/Winter-2022-98.tsv'
    )


def map(dataset, concepticon, mappings):
    # Load the Winter-2022-98 concept list from the raw folder inside the downloaded zip
    winter = models.Conceptlist.from_file(
        dataset.raw_dir / "concepticon-data-master" / "concepticondata" / "conceptlists" / "Winter-2022-98.tsv"
    )
    
    # Prepare dictionaries to hold related concepts by ID
    target_concepts = {concept.id: [] for concept in winter.concepts.values()}
    source_concepts = {concept.id: [] for concept in winter.concepts.values()}
    linked_concepts = {concept.id: [] for concept in winter.concepts.values()}

    # Helper to parse the JSON-like strings in the TSV fields, fallback to empty list
    def parse_json_field(field):
        try:
            return json.loads(field) if field else []
        except json.JSONDecodeError:
            return []

    # For each concept, fill the relationships
    for concept in winter.concepts.values():
        # Parse the fields from the original TSV attributes
        tc = parse_json_field(concept.attributes.get("target_concepts", "[]"))
        sc = parse_json_field(concept.attributes.get("source_concepts", "[]"))
        lc = parse_json_field(concept.attributes.get("linked_concepts", "[]"))
        
        target_concepts[concept.id] = tc
        source_concepts[concept.id] = sc
        linked_concepts[concept.id] = lc

    # Build the output table with all fields required
    table = []
    for concept in winter.concepts.values():
        row = collections.OrderedDict([
            ('ID', concept.id),
            ('NUMBER', concept.number),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('ENGLISH', concept.english),
            ('TARGET_CONCEPTS', target_concepts[concept.id]),
            ('SOURCE_CONCEPTS', source_concepts[concept.id]),
            ('LINKED_CONCEPTS', linked_concepts[concept.id]),
        ])
        table.append(row)

    # Write the table back into the dataset
    dataset.table.write(table)