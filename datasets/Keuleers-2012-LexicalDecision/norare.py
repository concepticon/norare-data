def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0118-4/MediaObjects/13428_2011_118_MOESM1_ESM.zip',
        'keuleers_bld.zip',
        '13428_2011_118_MOESM1_ESM/blp-items.xls',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2011_118_MOESM1_ESM/blp-items.xls',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
