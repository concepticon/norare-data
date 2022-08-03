def download(dataset):
    dataset.download_zip(
        'https://github.com/wswu/corevoc/archive/master.zip',
        'master.zip',
        'corevoc-master/lists/core'
    )

def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_csv('corevoc-master/lists/core', "\t", dicts=False)
    sheet = [dict(zip(["word", "count"], row[:2])) for row in sheet_list[0:]]
    dataset.extract_data(sheet, concepticon, mappings, gloss='ENGLISH', language='en')

