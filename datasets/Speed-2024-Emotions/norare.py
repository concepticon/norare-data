def download(dataset):
    dataset.download_file(
        'https://osf.io/download/h76zj/',
        'SpeedBrysbaertEmotionNorms.xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SpeedBrysbaertEmotionNorms.xlsx',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    )          