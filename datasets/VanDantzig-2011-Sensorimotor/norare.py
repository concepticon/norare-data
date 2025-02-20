def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-010-0038-8/MediaObjects/13428_2010_38_MOESM1_ESM.xls',
        '13428_2010_38_MOESM1_ESM.xls',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2010_38_MOESM1_ESM.xls',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
