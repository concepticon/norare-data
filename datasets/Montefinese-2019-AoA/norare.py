def download(dataset):
    dataset.download_file(
        'https://osf.io/download/3nvh6/',
        'ItAoA.xlsx'
    )


def map(dataset, concepticon, mappings):  
    sheet_list = dataset.get_excel('ItAoA.xlsx', 1, dicts=False)
    sheet = [dict(zip(sheet_list[0], row)) for row in sheet_list[1:]]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        pos_mapper = {
            'n': 'Person/Thing',
            'a': 'Property',
            'v': 'Action/Process'},
        pos_name = "ITALIAN_POS",
        gloss='ENGLISH',
        language='en'
    )