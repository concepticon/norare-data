def download(dataset):
    dataset.download_zip(
        'https://github.com/AnnaDiNatale/colex_affective/archive/refs/heads/master.zip',
        'colex_affective-master.zip',
        'colex_affective-master/lexica/clics3_WKB.csv'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv('colex_affective-master/lexica/clics3_WKB.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )

