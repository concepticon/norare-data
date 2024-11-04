def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-013-0426-y/MediaObjects/13428_2013_426_MOESM1_ESM.xlsx',
        '13428_2013_426_MOESM1_ESM.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        '13428_2013_426_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de',
        pos=True,
        pos_mapper = {
            'S': 'Person/Thing',
            'A': 'Property',
            'V': 'Action/Process'},
        pos_name = "GERMAN_POS"
    )