def download(dataset):
    dataset.download_file(
        'https://www.bcbl.eu/sites/default/files/files/SUBTLEX-GR_full.txt',
        'SUBTLEX-GR_full.txt'
    )


def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_csv('SUBTLEX-GR_full.txt', delimiter='\t', dicts=False)
    sheet = []
    valid_fields = [
        'ID', 'Word', 'FREQcount', 'CD', 'SUBTLEX_WF', 'Lg10WF', 'SUBTLEX_CD', 'Lg10CD']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields, row[:8]))]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='GREEK',
        language='el'
    )

