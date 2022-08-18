def download(dataset):
    dataset.download_file(
        'http://crr.ugent.be/papers/Concreteness_ratings_Brysbaert_et_al_BRM.txt',
        'brysbaert_concreteness.tsv'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'brysbaert_concreteness.tsv',
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            'Noun': 'Person/Thing',
            'Adjective': 'Property',
            'Verb': 'Action/Process',
            'Adverb': 'Other',
            'Article': 'Other',
            'Conjunction': 'Other',
            'Determiner': "Other",
            'Ex': "Other",
            '#N/A': 'Other',
            "Interjection": "Other",
            "Name": "Person/Thing",
            "Preposition": "Other",
            "To": "Other",
            "Number": "Number",
            "Pronoun": "Other",
            "Not": "Other"},
        pos_name = "ENGLISH_POS"
    )

