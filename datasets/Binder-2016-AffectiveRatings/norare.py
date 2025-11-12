def download(dataset):
    dataset.download_zip(
        'https://www.neuro.mcw.edu/representations/word_ratings.zip',
        'word_ratings.zip',
        'WordSet1_Ratings.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'WordSet1_Ratings.xlsx',
        concepticon,   
        mappings, 
        gloss='ENGLISH', language='en', pos=True,
        pos_mapper={'1': 'Person/Thing', '2': 'Action/Process', '3': 'Property'},
        pos_name="ENGLISH_POS"
    )