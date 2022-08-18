def download(dataset):
    dataset.download_file(
        'https://raw.githubusercontent.com/tomasengelthaler/HumorNorms/master/humor_dataset.csv',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'humor_dataset.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
