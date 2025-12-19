def download(dataset):
    dataset.download_file(
        'https://osf.io/download/envd2/',
        'specificity_score_en_ANEW.tsv'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'specificity_score_en_ANEW.tsv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )