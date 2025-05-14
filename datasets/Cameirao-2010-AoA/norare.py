def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.42.2.474/MediaObjects/13428_2010_Article_420200474_MOESM1_ESM.zip',
        '13428_2010_Article_420200474_MOESM1_ESM.zip',
        'Cameirao-BRM-2010/AOA 1749 Portuguese Words.xls',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Cameirao-BRM-2010/AOA 1749 Portuguese Words.xls',
        concepticon,
        mappings,
        gloss='PORTUGUESE',
        language='pt',
        pos=True,
        pos_mapper = {
            'no': 'Person/Thing',
            'aj': 'Property',
            'vb': 'Action/Process',
            'av': 'Other'},
        pos_name = "PORTUGUESE_POS"
    )
