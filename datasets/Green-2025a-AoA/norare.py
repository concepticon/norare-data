def download(dataset):
    dataset.download_file(
        'https://osf.io/download/rczyu/?view_only=ca45900ffc264645a32394d256101e7d',
        'Crowdsourced Print AoA Estimates for Earlier Acquired Vocabulary (Study 1).xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'Crowdsourced Print AoA Estimates for Earlier Acquired Vocabulary (Study 1).xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )