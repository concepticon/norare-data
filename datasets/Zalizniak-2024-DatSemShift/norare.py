import collections
from pyconcepticon import models
from csvw.dsv import reader
import json

def download(dataset):
    pass


def map(dataset, concepticon, mappings):
    # Load the Zalizniak-2024-4583 concept list from the raw folder inside the downloaded zip
    zalizniak = concepticon.conceptlists["Zalizniak-2024-4583"]
    
    # Initialize relationship dictionaries
    target_concepts = {concept.id: [] for concept in zalizniak.concepts.values()}
    linked_concepts = {concept.id: [] for concept in zalizniak.concepts.values()}

    for concept in zalizniak.concepts.values():
        tc = concept.attributes.get("target_concepts", "[]")
        lc = concept.attributes.get("linked_concepts", "[]")
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
            ('TARGET_CONCEPTS', target_concepts[concept.id]),
            ('LINKED_CONCEPTS', linked_concepts[concept.id]),
            ('DEGREE', concept.attributes.get('degree', '')),
            ('WEIGHTED_DEGREE', concept.attributes.get('weighted_degree', '')),
            ('RANK', concept.attributes.get('rank', '')),
        ])
        table.append(row)

    # Write to output
    dataset.table.write(table)