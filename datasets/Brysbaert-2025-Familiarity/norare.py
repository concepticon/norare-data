def download(dataset):
    dataset.download_file(
        'https://osf.io/download/qazjk/',
        'Full list GPT4 estimates familiarity and Multilex frequencies.xlsx'
    )



def replace_null(v):
    return None if v in {'NA'} else v

def map(dataset, concepticon, mappings):
    rows = dataset.get_excel('Full list GPT4 estimates familiarity and Multilex frequencies.xlsx', 0, dicts=True)
    cleaned_rows = [{k: replace_null(v) for k, v in row.items()} for row in rows]
    dataset.extract_data(
        cleaned_rows,
        concepticon,   
        mappings, 
        gloss='ENGLISH', language='en'
    )