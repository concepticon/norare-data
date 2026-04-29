def download(dataset):
    dataset.download_file(
        'https://osf.io/download/xk3p6/',
        '3 - Validity.xlsx'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        '3 - Validity.xlsx',
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )    