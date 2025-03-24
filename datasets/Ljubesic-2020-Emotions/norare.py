def download(dataset):
    dataset.download_zip(
        'https://www.clarin.si/repository/xmlui/bitstream/handle/11356/1318/LiLaH-HR-NL-SL.zip?sequence=6&isAllowed=y'
        'LiLaH-HR-NL-SL.zip',
        'LiLaH-HR-NL-SL/LiLaH-HR-NL-SL.tsv',
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv('LiLaH-HR-NL-SL/LiLaH-HR-NL-SL.tsv', delimiter= "\t", dicts = True, coding = 'utf-8-sig'),
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    )    