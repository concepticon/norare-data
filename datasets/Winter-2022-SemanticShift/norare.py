import collections
from pyconcepticon import models
from csvw.dsv import reader

def download(dataset):
    dataset.download_zip(
        'https://github.com/concepticon/concepticon-data/archive/refs/heads/master.zip',
        'concepticon-data-master.zip',
        'concepticon-data-master/concepticondata/conceptlists/Winter-2022-98.tsv'
    )


def map(dataset, concepticon, mappings):
    # get data path raw folder

    # get concept to concepticon ID to have all data at hand
    # this part should later be replaced by the original concept list frm
    # concepticon
    # concepticon.conceptlists[...]
    urban = models.Conceptlist.from_file(
            dataset.raw_dir / "Winter-2022-98.tsv"
            )
    # we turn concepts to identifiers, as we need to write them in the network
    concept2id = {concept.english: concept.id for concept in winter.concepts.values()}
    
    table = []

    # here is the routine to create a network (potentially a bit complicated)
    linked_concepts = {concept.id: [] for concept in winter.concepts.values()}
    targeted_concepts = {concept.id: [] for concept in winter.concepts.values()}

    
    for concept in winter.concepts.values():
        row = collections.OrderedDict([
            ('ID', f"Urban-2011-160-{concept.number}"),
            ('NUMBER', concept.number),
            ('ENGLISH', concept.english),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('SEMANTIC_CLASS_ID', concept.attributes["semantic_class_id"]),
            ('CATEGORY', concept.attributes["category"]),
        ])
                
        row['TARGET_CONCEPTS'] = targeted_concepts[concept.id]
        row['LINKED_CONCEPTS'] = linked_concepts[concept.id]
        table.append(row)
    dataset.table.write(table)