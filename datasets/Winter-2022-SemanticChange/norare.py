import collections
from pyconcepticon import models
from csvw.dsv import reader
import json

def download(dataset):
    pass


def map(dataset, concepticon, mappings):
    # Load the Winter-2022-98 concept list from the raw folder inside the downloaded zip
    winter = concepticon.conceptlists["Winter-2022-98"]
    
    # Prepare dictionaries to hold related concepts by ID
    target_concepts = {concept.id: [] for concept in winter.concepts.values()}
    source_concepts = {concept.id: [] for concept in winter.concepts.values()}
    linked_concepts = {concept.id: [] for concept in winter.concepts.values()}

    # For each concept, fill the relationships
    for concept in winter.concepts.values():
        # Parse the fields from the original TSV attributes
        tc = concept.attributes.get("target_concepts", "[]")
        sc = concept.attributes.get("source_concepts", "[]")
        lc = concept.attributes.get("linked_concepts", "[]")
        
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
