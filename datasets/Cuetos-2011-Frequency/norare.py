def download(dataset):
    dataset.download_zip(
        'http://crr.ugent.be/papers/SUBTLEX-ESP.zip',
        'cuetos_freq.zip',
        'SUBTLEX-ESP.xlsx',
    )


def map(dataset, concepticon, mappings):
    sheet = []
    valid_fields = ['Word', 'Freq. count', 'Freq. per million', 'Log freq.']
    for row in dataset.get_excel('SUBTLEX-ESP.xlsx', 0, dicts=False)[1:]:
        sheet.append(dict(zip(valid_fields, row[:4])))
        sheet.append(dict(zip(valid_fields, row[5:9])))
        sheet.append(dict(zip(valid_fields, row[10:14])))

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )
