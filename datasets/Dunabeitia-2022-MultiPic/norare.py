from collections import defaultdict, OrderedDict

def download(dataset):
    dataset.download_zip(
        'https://figshare.com/ndownloader/articles/19328939/versions/8',
        'MultiPic.zip',
        'MultiPic Dataset Open Materials.csv',
    )


def map(dataset, concepticon, mappings):
    mapping = {}
    for concept in concepticon.conceptlists["Dunabeitia-2022-500"].concepts.values():
        mapping[concept.attributes["picture_code"]] = (
            concept.concepticon_id,
            concept.concepticon_gloss,
            concept.english
            )
    data = dataset.get_csv(
        "MultiPic Dataset Open Materials.csv",
        delimiter=";")

    # define languages we want to keep
    languages = OrderedDict({
            "Czech": "CZECH", 
            "Finnish": "FINNISH",
            "Italian": "ITALIAN",
            })
    responses = {
            language : {} for language in languages
            }
    # organize the data per code
    for row in data:
        if row["Language"] in languages:
            responses[row["Language"]][row["Code"]] = row["Modal Response"]
    
    # fill the table
    table = []
    for code, (cid, cgl, eng) in mapping.items():
        row = [cid, cgl, eng, code]
        for language in languages:
            row += [responses[language][code]]
        table += [row]
    dataset.table.write(table)
    # dataset.extract_data(
    #     'SpanishAoA.xlsx',
    #     concepticon,
    #     mappings,
    #     pos_mapper = {
    #         'NOUN': 'Person/Thing',
    #         'ADJECTIVE': 'Property',
    #         'VERB': 'Action/Process',
    #         'ADPOSITION': 'Other',
    #         'ADVERB': 'Other',
    #         'CONJUNCTION': 'Other',
    #         'DATE': "Person/Thing",
    #         'DETERMINER': "Other",
    #         'INTERJECTION': 'Other',
    #         "PRONOUN": "Other",
    #         " ": "Other"},
    #     pos_name = "SPANISH_POS",
    #     gloss='SPANISH',
    #     language='es'
    # )
