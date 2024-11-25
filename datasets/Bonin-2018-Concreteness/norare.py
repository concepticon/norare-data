def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1014-y/MediaObjects/13428_2018_1014_MOESM3_ESM.xlsx',
        '13428_2018_1014_MOESM3_ESM.xlsx',
    )

def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_excel('13428_2018_1014_MOESM3_ESM.xlsx', 0, dicts=False)
    sheet = []
    valid_fields = [
        'items', 'English translation', 'mean', 'sd', 'Mean context availability', 'SD context availability', 'Mean valence', 'SD valence', 'Mean arousal', 'SD arousal']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields, row[:10]))]

        dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr',
    )        