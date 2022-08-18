def download(dataset):
    dataset.download_zip(
        'https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/subtlexchwf.zip/at_download/file',
        'SUBTLEX-CH-WF.zip',
        'SUBTLEX-CH-WF.xlsx'
    )


def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_excel('SUBTLEX-CH-WF.xlsx', 0, dicts=False)
    sheet = [dict(zip(sheet_list[2], row)) for row in sheet_list[3:]]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )
