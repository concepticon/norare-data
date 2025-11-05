def download(dataset):
    dataset.download_file(
        'https://osf.io/download/ma586/?view_only=ca45900ffc264645a32394d256101e7d',
        'AI Generated AoA Estimates for the ECP.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'AI Generated AoA Estimates for the ECP.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )