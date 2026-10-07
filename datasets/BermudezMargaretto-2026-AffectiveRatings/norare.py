def download(dataset):
    dataset.download_file(
        'https://osf.io/download/hw7q8/?view_only=1737b64054bc4c52b629efa8a8b405c8',
        'Affective norms in ELF_averaged data.xlsx',
    )

def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_excel('Affective norms in ELF_averaged data.xlsx', 1, dicts=False)

    # Define the column names as valid fields, avoid duplicates
    valid_fields = [
        'word', 'Valid_obs1', 'Missing1', 'Mean1', 'SD1', 'Min1', 'Max1',
        'Valid_obs2', 'Missing2', 'Mean2', 'SD2', 'Min2', 'Max2'
    ]

    sheet = []
    for row in sheet_list[2:]:
        sheet += [dict(zip(valid_fields, row[:len(valid_fields)]))]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
    )