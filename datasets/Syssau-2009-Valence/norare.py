def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.1.213/MediaObjects/13428_2010_410100213_MOESM1_ESM.zip',
        'syssau_monnier_norms.zip',
        'syssau_monnier_norms.xls',
    )


def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_excel('syssau_monnier_norms.xls', 0, dicts=False)
    sheet = []
    valid_fields = [
        'French Words', 'English Translation', 'Emotional Source', 'Picture Source', 'Picture Number', 'Rating Age', 
        '5 All % Neg', '5 Girls % Neg', '5 Boys % Neg', '5 All % Neu', '5 Girls % Neu', '5 Boys % Neu', '5 All % Pos', '5 Girls % Pos', '5 Boys % Pos', 
        '7 All % Neg', '7 Girls % Neg', '7 Boys % Neg', '7 All % Neu', '7 Girls % Neu', '7 Boys % Neu', '7 All % Pos', '7 Girls % Pos', '7 Boys % Pos', 
        '9 All % Neg', '9 Girls % Neg', '9 Boys % Neg', '9 All % Neu', '9 Girls % Neu', '9 Boys % Neu', '9 All % Pos', '9 Girls % Pos', '9 Boys % Pos', 
        'Adults S % Neg', 'Adults S % Neu', 'Adults S % Pos', 'M', 'SD', 'Age 5-7', 'Age 7-9', 'Sex 5 years', 'Sex 7 years', 'Sex 9 years']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields, row[:43]))]

        dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='FRENCH',
        language='fr',
    )        