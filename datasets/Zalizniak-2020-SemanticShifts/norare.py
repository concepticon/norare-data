from csvw.dsv import UnicodeDictReader
import collections


def download(dataset):

    pass


def map(dataset, concepticon, mappings):

    dss = concepticon.conceptlists[dataset.concepticon]

    with UnicodeDictReader(dataset.raw_dir / "data.tsv", delimiter="\t") as reader:
        data = {}
        for row in reader:
            data[row["ID"]] = row


    num2id = {concept.number: concept.id for concept in dss.concepts.values()}
    num2name = {concept.number: concept.english for concept in dss.concepts.values()}

    table = []

    for concept in dss.concepts.values():
        links = data[concept.id]["LINKS"].split()
        dirs = data[concept.id]["DIRECTIONS"].split()
        shifts = data[concept.id]["URLS"].split()
        weights = data[concept.id]["WEIGHTS"].split()
    
        polysemy, sources, targets = [], [], []
        for link, direction, shift, weight in zip(links, dirs, shifts, weights):
            if direction in ['—', '↔']:
                polysemy += [{
                    "ID": num2id[link],
                    "NAME": num2name[link],
                    "Weight": weight,
                }]
            elif direction == "→":
                targets += [{
                    "ID": num2id[link],
                    "NAME": num2name[link],
                    "Weight": weight,
                }]
        table.append(collections.OrderedDict([
            ("ID", concept.id),
            ("CONCEPT_ID", concept.id),
            ('NUMBER', concept.number),
            ('ENGLISH', concept.english),
            ('CONCEPTICON_ID', concept.concepticon_id),
            ('CONCEPTICON_GLOSS', concept.concepticon_gloss),
            ('RANK', concept.attributes["rank"]),
            ('DEGREE', concept.attributes["degree"]),
            ('WEIGHTED_DEGREE', concept.attributes["weighted_degree"]),
            ('LINKED_CONCEPTS', polysemy),
            ('TARGET_CONCEPTS', targets),
        ]))
    dataset.table.write(table)
