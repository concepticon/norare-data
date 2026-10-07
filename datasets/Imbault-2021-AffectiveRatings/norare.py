def download(dataset):
    dataset.download_file(
        'https://osf.io/download/dzv6j/?view_only=d731c1111f7048a492e6a5cdb88c081b',
        'l2emotion-submit.csv',
    )


def replace_null(v):
    return None if v == 'NA' else v

def map(dataset, concepticon, mappings):
    rows = dataset.get_csv('l2emotion-submit.csv', dicts=True, delimiter=',')
    cleaned_rows = [{k: replace_null(v) for k, v in row.items()} for row in rows]
    dataset.extract_data(
        cleaned_rows,
        concepticon,   
        mappings, 
        gloss='ENGLISH', language='en'
    )