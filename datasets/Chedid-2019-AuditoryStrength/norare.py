def download(dataset):
    dataset.download_file(
        'https://lingualab.ca/dataset/SemantiQc_auditory.xlsx')


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SemantiQc_auditory.xlsx',
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr'
    )

