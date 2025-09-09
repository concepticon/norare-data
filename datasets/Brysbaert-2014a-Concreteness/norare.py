def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-013-0403-5/MediaObjects/13428_2013_403_MOESM1_ESM.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2013_403_MOESM1_ESM.xlsx',
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

