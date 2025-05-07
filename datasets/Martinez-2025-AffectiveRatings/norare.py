def download(dataset):
    dataset.download_file(
        'https://osf.io/download/mkghz/',
        'GPT norms concreteness valence and arousal for single words.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'GPT norms concreteness valence and arousal for single words.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )