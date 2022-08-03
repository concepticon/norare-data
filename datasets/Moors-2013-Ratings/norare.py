def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-012-0243-8/MediaObjects/13428_2012_243_MOESM1_ESM.xlsx',
    )


def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_excel('13428_2012_243_MOESM1_ESM.xlsx', 0, dicts=False)
    sheet = []
    valid_fields = [
        'Words', 'Translation', 'M V', 'SD V', 'N V', 'M A', 'SD A', 'N A', 'M P', 'SD  P', 'N P', 'M AoA', 'SD AoA', 'N AoA',
        'M V Men', 'SD V Men', 'N V Men', 'M A Men', 'SD A Men', 'N A Men', 'M P Men', 'SD  P Men', 'N P Men', 'M AoA Men', 'SD AoA Men', 'N AoA Men',
        'M V Women', 'SD V Women', 'N V Women', 'M A Women', 'SD A Women', 'N A Women', 'M P Women', 'SD  P Women', 'N P Women', 'M AoA Women', 'SD AoA Women', 'N AoA Women',
        'Freq(Log10)', 'Freq(1E6)', 'Length', 'N( %)', 'Grammatical category']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields, row[:43]))]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl',
        pos=True,
        pos_mapper={
            'N': 'Person/Thing',
            'A': 'Property',
            'V': 'Action/Process',
            'A/R': 'Other',
            'N/A': 'Other'},
        pos_name="DUTCH_POS"
    )
