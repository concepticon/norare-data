def download(dataset):
    dataset.download_file(
        'https://ars.els-cdn.com/content/image/1-s2.0-S0001691814000985-mmc3.xlsx',
        '1-s2.0-S0001691814000985-mmc3.xlsx'
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        '1-s2.0-S0001691814000985-mmc3.xlsx',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    )
