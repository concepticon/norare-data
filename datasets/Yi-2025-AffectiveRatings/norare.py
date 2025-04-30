def download(dataset):
    dataset.download_file(
        'https://osf.io/download/836th/?view_only=4a67691a0fef40a9b8f8ec7296c1e1da',
        'emotion.en.ch.csv'
    )
def replace_null(v):
    return None if v in {'NA', '#N/A'} else v

def map(dataset, concepticon, mappings):
    rows = dataset.get_csv('emotion.en.ch.csv', delimiter=",", dicts=True)
    cleaned_rows = [{k: replace_null(v) for k, v in row.items()} for row in rows]

    dataset.extract_data(
        cleaned_rows,
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh',
        pos=True,
        pos_mapper={'noun': 'Person/Thing', 'verb': 'Action/Process', 'adjective': 'Property'},
        pos_name="CHINESE_POS"
    )