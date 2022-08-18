def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.2.546/MediaObjects/Desrochers-BRM-2009.zip',
        'desrochers_freq_fr.zip',
        'Desrochers-Thompson_2009_Ratings.xls'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Desrochers-Thompson_2009_Ratings.xls',
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr'
    )
