def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1099-3/MediaObjects/13428_2018_1099_MOESM2_ESM.csv',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2018_1099_MOESM2_ESM.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )

