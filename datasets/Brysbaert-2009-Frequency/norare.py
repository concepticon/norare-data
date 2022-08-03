def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.4.977/MediaObjects/Brysbaert-BRM-2009.zip',
        'brysbaert_freq.zip',
        'Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )

