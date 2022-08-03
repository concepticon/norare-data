def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.40.3.791/MediaObjects/Cortese-BRM-2008.zip',
        'Cortese-BRM-2008.zip',
        'Cortese-BRM-2008/Cortese B377 norms.xls',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Cortese-BRM-2008/Cortese B377 norms.xls',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
