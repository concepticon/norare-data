def download(dataset):
    dataset.download_file(
        'https://osf.io/download/xfubm',
        'Norms.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('Norms.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )    