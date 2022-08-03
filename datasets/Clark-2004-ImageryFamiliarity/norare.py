def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBF03195584/MediaObjects/Clark-BRM-2004.zip',
        'Clark-BRM-2004.zip',
        'Clark-BRMIC-2004/cp2004b.txt'
    )


def map(dataset, concepticon, mappings):
    with open(dataset.raw_dir.joinpath('Clark-BRMIC-2004/cp2004b.txt')) as f:
        data = [row.split() for row in f]
    sheet = [dict(zip(data[1], row)) for row in data[2:2313]]

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
