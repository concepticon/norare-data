def download(dataset):
    dataset.download_file(
        'https://lingualab.ca/normes-familiarity-chedid2018.xlsx')


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'normes-familiarity-chedid2018.xlsx',
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr'
    )

