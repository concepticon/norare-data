def download(dataset):
    dataset.download_file(
        'https://osf.io/download/3nvh6/',
        'ItAoA.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'ItAoA.xlsx',
        sheet=1,
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            'n': 'Person/Thing',
            'a': 'Property',
            'v': 'Action/Process'},
        pos_name = "ITALIAN_POS"
    )

