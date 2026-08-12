def download(dataset):
    dataset.download_file(
        'https://osf.io/download/nu974/?view_only=5ca8ae4af6a74bceab77ff3fc6d60284',
        'item_level_data.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'item_level_data.xlsx',
        concepticon,
        mappings,
        gloss='ARABIC',
        language='ar'
    )    