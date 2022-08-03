def download(dataset):
    dataset.download_file(
        'https://osf.io/nbu9e/download',
        'English_Word_Prevalences.xlsx'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'English_Word_Prevalences.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
