def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-017-0944-0/MediaObjects/13428_2017_944_MOESM1_ESM.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '13428_2017_944_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )
