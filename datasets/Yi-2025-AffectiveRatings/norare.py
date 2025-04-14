def download(dataset):
    dataset.download_file(
        'https://osf.io/download/836th/?view_only=4a67691a0fef40a9b8f8ec7296c1e1da',
        'emotion.en.ch.csv'
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv('emotion.en.ch.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh',
        pos=True,
        pos_mapper={'noun': 'Person/Thing', 'verb': 'Action/Process', 'adjective': 'Property'},
        pos_name="CHINESE_POS"
    )       

