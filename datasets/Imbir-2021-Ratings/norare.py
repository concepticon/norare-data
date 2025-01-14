def download(dataset):
    dataset.download_file(
        'https://ndownloader.figstatic.com/files/30470925',
        'data sheet 1.xlsx',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'data sheet 1.xlsx',
        concepticon,
        mappings,
        pos_mapper = {
            'N': 'Person/Thing',
            'A': 'Property',
            'V': 'Action/Process',
            'pron': 'Other',
            'adv': 'Other',
            'I': 'Action/Process',
            'pred': "Person/Thing",
            'ign': "Other",
            'num': 'Number',
            "prep": "Other",
            "qub": "Other"},
        pos_name = "POLISH_POS",
        gloss='POLISH',
        language='pl'
    )
