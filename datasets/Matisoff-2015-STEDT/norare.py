def download(dataset):
    dataset.download_file(
        'https://github.com/stedt-project/sss/raw/master/semcats/revision1/lexicon_semcats-glosses_20110913.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'lexicon_semcats-glosses_20110913.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
