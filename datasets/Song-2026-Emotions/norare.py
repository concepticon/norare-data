def download(dataset):
    dataset.download_file(
        'https://osf.io/download/xcw4v/?view_only=3d56e6dfcfb043eba2d3fb850ee27f68',
        'Ratings_gender.xlsx',
    )

def replace_null(v):
    return None if v in {'#DIV/0!', 'NA'} else v

def map(dataset, concepticon, mappings):
    rows = dataset.get_excel('Ratings_gender.xlsx', 0, dicts=True)
    cleaned_rows = [{k: replace_null(v) for k, v in row.items()} for row in rows]
    dataset.extract_data(
        cleaned_rows,
        concepticon,   
        mappings, 
        gloss='CHINESE', language='zh'
    )