def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1014-y/MediaObjects/13428_2018_1014_MOESM3_ESM.xlsx',
        '13428_2018_1014_MOESM3_ESM.xlsx',
    )


def replace_null(v):
    if v == '#NULL!':
        return None
    else:
        return v


def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_excel('13428_2018_1014_MOESM3_ESM.xlsx', 0, dicts=False)
    sheet = []
    valid_fields = [
        'items', 'English translation', 'mean', 'sd', 'Mean context availability', 'SD context availability', 'Mean valence', 'SD valence', 'Mean arousal', 'SD arousal']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet.append({
            k: replace_null(v)
            for k, v in zip(valid_fields, row[:10])})

        dataset.extract_data(
            sheet,
            concepticon,
            mappings,
            gloss='FRENCH',
            language='fr',
        )
