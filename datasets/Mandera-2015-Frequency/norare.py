def download(dataset):
    dataset.download_file(
        'http://crr.ugent.be/subtlex-pl/subtlex-pl-cd-3.csv',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv('subtlex-pl-cd-3.csv', '\t', dicts=True),
        concepticon,
        mappings,
        gloss='POLISH',
        language='pl',
        pos=True,
        pos_mapper = {
            'subst': 'Person/Thing',
            'adj': 'Property',
            'verb': 'Action/Process',
            'adv': 'Other',
            'qub': 'Other',
            'conj': 'Other',
            'ign': "Other",
            'interp': "Other",
            'pred': 'Other',
            "tnum": "Other",
            "tsym": "Other",
            "prep": "Other",
            "To": "Other",
            "num": "Number",
            "pron": "Other",
            "xxx": "Other"},
        pos_name = "POLISH_POS"
    )
