def download(dataset):
    dataset.download_file(
        'https://osf.io/download/y6ebr/',
        'SUBTLEX-DE cleaned version with Zipf values.xlsx'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SUBTLEX-DE cleaned version with Zipf values.xlsx',
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de'
    )
