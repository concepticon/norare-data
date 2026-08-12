from csvw.dsv import UnicodeDictReader
import collections
import json


def download(dataset):
    dataset.download(
        'https://github.com/lexibank/datsemshift/raw/main/cldf/parameters.csv',
        'parameters.csv',
    )

def map(dataset, concepticon, mappings):

    dss = concepticon.conceptlists["Zalizniak-2024-4583"]

    concept_by_id = {c.id: c for c in dss.concepts.values()}

    # load TSV once
    with UnicodeDictReader(dataset.raw_dir / "parameters.csv", delimiter=",") as reader:
        data = {}
        for row in reader:
            data[row["ID"]] = row

    num2id = {concept.number: concept.id for concept in dss.concepts.values()}
    num2name = {concept.number: concept.english for concept in dss.concepts.values()}

    table = []

    for cid, row in data.items():

        concept = concept_by_id.get(cid)
        if not concept:
            continue

        def parse_json(field):
            val = row.get(field, "")
            if not val or val == "[]":
                return []
            try:
                return json.loads(val)
            except Exception:
                return []

        linked = parse_json("Linked_Concepts")
        targets = parse_json("Target_Concepts")

        table.append(collections.OrderedDict([
            ("ID", cid),
            ("NUMBER", concept.number),
            ("CONCEPTICON_ID", concept.concepticon_id),
            ("CONCEPTICON_GLOSS", concept.concepticon_gloss),
            ("ENGLISH", concept.english),

            ("GLOSS_IN_SOURCE", row.get("Gloss_in_Source", "")),

            ("LINKED_CONCEPTS", linked),
            ("TARGET_CONCEPTS", targets),

            ("SHIFTS", row.get("Shifts", "").split()),

            ("DOMAIN", row.get("Domain", "")),
            ("ALIAS", row.get("Alias", "")),
            ("DEFINITION", row.get("Definition", "")),
        ]))

    dataset.table.write(table)