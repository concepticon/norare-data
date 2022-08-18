def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0062-3/MediaObjects/13428_2011_62_MOESM1_ESM.xls',
    )


def map(dataset, concepticon, mappings):
    sheet_ = dataset.get_excel('13428_2011_62_MOESM1_ESM.xls', 0, dicts=False)
    sheet = []
    valid_fields = ['Word', 'Frequency', 'Frequency per million', 'Log10(freq count+1)']
    for row in sheet_[1:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields,row[:4]))]
        sheet += [dict(zip(valid_fields,row[5:9]))]

    dataset.extract_data(sheet, concepticon, mappings, gloss='SPANISH', language='es')

