def download(dataset):
    dataset.download_file(
        'https://osf.io/download/buatr/?view_only=ca45900ffc264645a32394d256101e7d',
        'AI Generated Print AoA Estimates for Kuperman et al. (2012).xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'AI Generated Print AoA Estimates for Kuperman et al. (2012).xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )