def download(dataset):
    dataset.download_file(
        'https://osf.io/download/g4dms',
        'Kannada Age-of-Acquisition Word List.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'Kannada Age-of-Acquisition Word List.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=True,
        pos_mapper = {
            'verb': 'Action/Process',
            'noun': 'Person/Thing',
            'adjective': 'Property',
            'pronoun': 'Other',
            'adjective': 'Other'},
        pos_name = "KANNADA_POS"
    )  