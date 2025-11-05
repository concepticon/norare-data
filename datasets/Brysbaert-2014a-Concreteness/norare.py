def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-013-0403-5/MediaObjects/13428_2013_403_MOESM1_ESM.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2013_403_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )

