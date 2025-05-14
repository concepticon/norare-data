def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0494-7/MediaObjects/13428_2014_494_MOESM1_ESM.xlsx',
        '13428_2014_494_MOESM1_ESM.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2014_494_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de',
        pos=True,
        pos_mapper = {
            'noun': 'Person/Thing',
            'adjective': 'Property',
            'verb': 'Action/Process'},
        pos_name = "GERMAN_POS"
    )
