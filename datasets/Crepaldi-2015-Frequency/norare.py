def download(dataset):
    dataset.download_file('http://crr.ugent.be/subtlex-it/subtlex-it.csv')


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'subtlex-it.csv',
        concepticon,
        mappings,
        gloss='ITALIAN',
        language='it',
        pos=True,
        pos_mapper = {
            'NOM': 'Person/Thing',
            'ADJ': 'Property',
            'VER': 'Action/Process',
            'ADV': 'Other',
            'CON': 'Other',
            'ABR': 'Other',
            'DET': "Other",
            'FW': "Other",
            'PRE': 'Other',
            "NPR": "Other",
            "PRO": "Other",
            "SENT": "Other",
            "SYM": "Other",
            "NUM": "Number",
            "INT": "Other",
            "PON": "Other"},
        pos_name = "ITALIAN_POS"
    )
