def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-020-01455-8/MediaObjects/13428_2020_1455_MOESM1_ESM.xlsx',
        '13428_2020_1455_MOESM1_ESM.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        '13428_2020_1455_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )    