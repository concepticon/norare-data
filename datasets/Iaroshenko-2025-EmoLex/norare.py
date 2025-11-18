def download(dataset):
    dataset.download_zip(
        'https://github.com/nl-pi/rusemolex/archive//refs/heads/master.zip',
        'rusemolex-main.zip',
        'rusemolex-main/RusEmoLex.csv',
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv(
            'rusemolex-main/RusEmoLex.csv',
            delimiter=";"
        ),
        concepticon,
        mappings,
        gloss='RUSSIAN',
        language='ru',
        pos=True,
        pos_mapper = {
            'существительное': 'Person/Thing',
            'прилагательное': 'Property',
            'глагол': 'Action/Process'},
        pos_name = "RUSSIAN_POS"
    )
