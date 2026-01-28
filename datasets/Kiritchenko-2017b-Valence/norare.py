def download(dataset):
    dataset.download_file(
        'https://www.saifmohammad.com/WebDocs/bwsvsrs/RS-scores.txt',
        'RS-scores.txt',
    )


def map(dataset, concepticon, mappings):
    rows = dataset.get_csv(
        'RS-scores.txt',
        delimiter='\t',
        dicts=False
    )

    valid_fields = ['WORD', 'VALENCE']
    sheet = []

    for row in rows:
        sheet.append(dict(zip(valid_fields, row[:2])))

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
