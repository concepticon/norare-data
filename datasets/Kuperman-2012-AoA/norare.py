def download(dataset):
    dataset.download_zip(
        'http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip',
        'kuperman_aoa.zip',
        filename='AoA_ratings_Kuperman_et_al_BRM.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'AoA_ratings_Kuperman_et_al_BRM.xlsx',
        concepticon,
        mappings, 
        gloss='ENGLISH',
        language='en'
    )
