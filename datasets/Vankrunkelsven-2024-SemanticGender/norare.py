def download(dataset):
    dataset.download_file(
        'https://osf.io/download/wfu28/',
        'Norms_Gender.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Norms_Gender.csv',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    ) 