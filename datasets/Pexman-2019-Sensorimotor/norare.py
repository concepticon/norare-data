def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1171-z/MediaObjects/13428_2018_1171_MOESM1_ESM.csv',
        '13428_2018_1171_MOESM1_ESM.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        '13428_2018_1171_MOESM1_ESM.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )          