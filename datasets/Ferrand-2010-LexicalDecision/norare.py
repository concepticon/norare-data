def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.42.2.488/MediaObjects/Ferrand-BRM-2010.zip',
        'ferrand_fld.zip',
        'Ferrand-BRM-2010/FLP-words.xls',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Ferrand-BRM-2010/FLP-words.xls',
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr'
    )
