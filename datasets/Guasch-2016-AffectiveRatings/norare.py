def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-015-0684-y/MediaObjects/13428_2015_684_MOESM1_ESM.xlsx',
        '13428_2015_684_MOESM1_ESM.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        '13428_2015_684_MOESM1_ESM.xlsx',
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es',
        pos=True,
        pos_mapper = {
            'N': 'Person/Thing',
            'A': 'Property',
            'V': 'Action/Process'},
        pos_name = "SPANISH_POS"
    )         