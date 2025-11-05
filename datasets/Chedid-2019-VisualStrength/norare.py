def download(dataset):
    dataset.download_file(
        'https://lingualab.ca/dataset/SemantiQc_visual.xlsx')


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SemantiQc_visual.xlsx',
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr'
    )

