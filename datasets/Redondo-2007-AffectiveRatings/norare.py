def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBF03193031/MediaObjects/Redondo-BRM-2007.zip',
        'Redondo-BRM-2007',
        'Redondo-BRM-2007/Redondo(2007).xls'
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Redondo-BRM-2007/Redondo(2007).xls',
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