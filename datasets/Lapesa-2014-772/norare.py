"""
ID>-----NUMBER>-ENGLISH>POS>----CONCEPTICON_ID>-CONCEPTICON_GLOSS>------

IDS_IN_SOURCE>--
LINKS>--
POLYSEMY_CLASS>-
FREQUENCY_CLASS>
DEGREE_CLASS>---
RELATION_TYPE>--
FORWARD_SCORES>-
BACKWARD_SCORES

Lapesa-2014-772-7>------
7>------
accessibility>--
noun>---
>-------
>-------

592:accessibility-inaccessibility:0 593:accessibility-availability:0 594:accessibility-approachability:0>-------
→343 →51 →38>---
poli2 poli2 poli2>------
freqMax freqMax freqMax>
NOT HIGH LOW>---
SYN SYN SYN>----
0 4.1 3.2>------
0 3.5 3.8

"""
import json
import collections

from csvw import Column

SCHEMA = {
    "type": "object",
    "patternProperties": {
        ".+": {
            "type": "object",
            "required": [
                "RELATION_TYPE", 
                "FORWARD_SCORE", 
                "BACKWARD_SCORE", 
                "POLYSEMY_CLASS",
                "FREQUENCY_CLASS",
                "DEGREE_CLASS",
            ],
            "properties": {
                "RELATION_TYPE": {
                    "type": "string", 
                    "enum": ["ANT", "HYP", "SYN"],
                    "description": "The targeted relation between a word pair: antonym (ANT), hyponym (HYP), synonym (SYN).",
                },
                "FORWARD_SCORE": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 5,
                    "description": "The mean of similarity judgments to word pairs on a 5-point scale (forward calculation).",
                },
                "BACKWARD_SCORE": {
                    "type": "number",
                    "minimum": 0,
                    "maximum": 5,
                    "description": "The mean of similarity judgments to word pairs on a 5-point scale (backward calculation).",
                },
                "POLYSEMY_CLASS": {
                    "type": "string", 
                    "enum": ["poli1", "poli2", "poli3"],
                    "description": "The degree of polysemy (1-3).",
                },
                "FREQUENCY_CLASS": {
                    "type": "string", 
                    "enum": ["freqMin", "freqMed", "freqMax"],
                    "description": "The degree of frequency.",
                },
                "DEGREE_CLASS": {"type": "string", "enum": ["NOT", "HIGH", "LOW"]},
            }
        }
    }
}


def compute_scored_relations(row):
    row['SCORED_RELATIONS'] = {}
    for name, reltype, fscore, bscore, pcls, fcls, dcls in zip(row['IDS_IN_SOURCE'], row['RELATION_TYPE'], row['FORWARD_SCORES'], row['BACKWARD_SCORES'], row['POLYSEMY_CLASS'], row['FREQUENCY_CLASS'], row['DEGREE_CLASS']):
        row['SCORED_RELATIONS'][name.split(':')[1]] = {
            'RELATION_TYPE': reltype,
            'FORWARD_SCORE': fscore,
            'BACKWARD_SCORE': bscore,
            'POLYSEMY_CLASS': pcls,
            'FREQUENCY_CLASS': fcls,
            'DEGREE_CLASS': dcls,
        }
    return row


def map(dataset, concepticon, mappings):
    tg = concepticon.conceptlists[dataset.id].tg
    items = [compute_scored_relations(row) for row in tg.tables[0]]
    tg.tables[0].tableSchema.columns.append(Column.fromvalue(dict(
        name="SCORED_RELATIONS",
        datatype={"base": "json", "format": json.dumps(SCHEMA)})))
    tg.write(dataset.norare_dsdir / dataset.csvwmdpath.name, **{dataset.id + '.tsv': items})

