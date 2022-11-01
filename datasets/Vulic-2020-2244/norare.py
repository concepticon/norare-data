import collections

from csvw import Column

LANGS = [
    'ENGLISH',
    'ARABIC',
    'CHINESE',
    'WELSH',
    'ESTONIAN',
    'FINNISH',
    'FRENCH',
    'HEBREW',
    'POLISH',
    'RUSSIAN',
    'SPANISH',
    'CANTONESE',
]
SCHEMA = '{"type":"object","patternProperties":{".+": {"type": "object", "required":["Score","Concepticon_ID"],"properties":{"Score":{"type":"number"},"Concepticon_ID":"oneOf":[{"type":"number"},{"type":"null"}]}}}}'


def compute_scored_relations(row, linked):
    for lang in sorted(LANGS):
        sims = {}
        if not row['{}_IN_SOURCE'.format(lang)]:
            # One translation in Estonian is missing!
            assert row['NUMBER'] == '111' and lang == 'ESTONIAN'
            continue
        for i, link in enumerate(row['LINKS']):
            sims['{}:{}'.format(
                row['{}_IN_SOURCE'.format(lang)][i], 
                linked[link][lang]
            )] = {
                'Score': row['{}_SCORE'.format(lang)][i],
                'Concepticon_ID': linked[link]['CONCEPTICON_ID'],
            }
        row['{}_SIMILARITY'.format(lang)] = sims
    return row


def map(dataset, concepticon, mappings):
    tg = concepticon.conceptlists[dataset.id].tg
    linked = {r['NUMBER']: r for r in tg.tables[0]}
    items = [compute_scored_relations(row, linked) for row in tg.tables[0]]
    for lang in sorted(LANGS):
        tg.tables[0].tableSchema.columns.append(Column.fromvalue(dict(
            name="{}_SIMILARITY".format(lang), 
            datatype={"base": "json", "format": SCHEMA})))

    tg.write(dataset.norare_dsdir / dataset.csvwmdpath.name, **{dataset.id + '.tsv': items})

