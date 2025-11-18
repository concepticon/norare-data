def download(dataset):
    dataset.download_zip(
        'https://www.neuro.mcw.edu/representations/word_ratings.zip',
        'word_ratings.zip',
        'WordSet1_Ratings.xlsx'
    )

def replace_null(v):
    return None if v in {'na', 'n/a'} else v

def map(dataset, concepticon, mappings):
    rows = dataset.get_excel('WordSet1_Ratings.xlsx', 0, dicts=True)
    cleaned_rows = [{k: replace_null(v) for k, v in row.items()} for row in rows]
    dataset.extract_data(
        cleaned_rows,
        concepticon,   
        mappings, 
        gloss='ENGLISH', language='en', pos=True,
        pos_mapper={'1': 'Person/Thing', '2': 'Action/Process', '3': 'Property'},
        pos_name="ENGLISH_POS",
    )