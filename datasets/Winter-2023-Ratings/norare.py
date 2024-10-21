def download(dataset):
    dataset.download_file(
        'https://osf.io/download/ex37k/',
        'iconicity_ratings_cleaned.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'iconicity_ratings_cleaned.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )    