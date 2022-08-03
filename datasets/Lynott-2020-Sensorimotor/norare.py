def download(dataset):
    dataset.download_file(
        'https://osf.io/48wsc/download',
        'Lancaster_sensorimotor_norms_for_39707_words.csv',
    )


def map(dataset, concepticon, mappings):    
    sheet = dataset.get_csv('Lancaster_sensorimotor_norms_for_39707_words.csv', ',', dicts=True)

    for m in list(mappings['en']):
        if m.upper() not in mappings['en']:
            mappings['en'][m.upper()] = mappings['en'][m]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
