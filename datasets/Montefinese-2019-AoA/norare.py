def download(dataset):
    dataset.download_file(
        'https://osf.io/download/3nvh6/',
        'ItAoA.xlsx'
    )


def map(dataset, concepticon, mappings):    
    sheet = dataset.get_excel('ItAoA.xlsx', 1, dicts=False)
    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            'n': 'Person/Thing',
            'a': 'Property',
            'v': 'Action/Process'},
        pos_name = "ITALIAN_POS"
    )

