def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0059-y/MediaObjects/13428_2011_59_MOESM1_ESM.xls',
    )


def map(dataset, concepticon, mappings):    
    for m in list(mappings['de']):
        if m.lower() not in mappings['de']:
            mappings['de'][m.lower()] = mappings['de'][m]

    dataset.extract_data(
        '13428_2011_59_MOESM1_ESM.xls',
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de'
    )
