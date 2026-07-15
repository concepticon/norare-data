def download(dataset):
    dataset.download_file(
        'https://osf.io/download/7w2tv',
        'Utility values words and MWEs.xlsx',
    )

def replace_null(v):
    if v == '#N/A':
        return None
    else:
        return v

def map(dataset, concepticon, mappings):

    sheet = dataset.get_excel(
        'Utility values words and MWEs.xlsx',
        dicts=True
    )

    # apply missing-value normalization
    for row in sheet:
        for k, v in row.items():
            row[k] = replace_null(v)

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
