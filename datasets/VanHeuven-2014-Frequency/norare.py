def download(dataset):
    dataset.download_file('http://crr.ugent.be/papers/SUBTLEX-UK.xlsx')


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SUBTLEX-UK.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=True,
        pos_mapper = {
            'noun': 'Person/Thing',
            'adjective': 'Property',
            'verb': 'Action/Process',
            'adverb': 'Other',
            'conjunction': 'Other',
            'pronoun': 'Other',
            'determiner': "Other",
            'unclassified': "Other",
            "preposition": "Other",
            "name": "Other",
            "number": "Number",
            "interjection": "Other",
            "marker": "Other"},
        pos_name = "ENGLISH_POS"
    )

