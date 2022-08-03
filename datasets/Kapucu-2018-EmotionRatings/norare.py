def download(dataset):
    dataset.download_file(
        'https://osf.io/wkeb7/download',
        'TurkishEmotionalWordNorms.csv'
    )


def map(dataset, concepticon, mappings):    
    for m in list(mappings['tr']):
        if m.upper() not in mappings['tr']:
            mappings['tr'][m.upper()] = mappings['tr'][m]

    dataset.extract_data(
        dataset.get_csv('TurkishEmotionalWordNorms.csv', ';', dicts=True),
        concepticon,
        mappings,
        gloss='TURKISH',
        language='tr'
    )
