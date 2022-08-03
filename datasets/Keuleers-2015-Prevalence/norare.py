def download(dataset):
    dataset.download_file(
        'http://crr.ugent.be/papers/prevalence%20B%20&%20NL.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'prevalence%20B%20&%20NL.xlsx',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    )
