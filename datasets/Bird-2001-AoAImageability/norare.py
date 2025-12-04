def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2FBF03195349/MediaObjects/Bird-BRM-2001.zip',
        'Bird-BRM-2001.zip',
        'Bird-BRMIC-2001/bird.xls'
    )



def replace_null(v):
    if v == '.':
        return None
    else:
        return v

def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_excel('Bird-BRMIC-2001/bird.xls', 0, dicts=False)
    sheet = []
    valid_fields = ['WORD', 'Word type', 'new AoA', 'new Imageability', 'MRC AoA', 'MRC Imageability', 'Frequency']

    for row in sheet_list[3:]:
        sheet.append({k: replace_null(v) for k, v in zip(valid_fields, row[:6])})

    dataset.extract_data(sheet, concepticon, mappings, gloss='ENGLISH', language='en',pos=True,
        pos_mapper = {
            'N': 'Person/Thing',
            'A': 'Property',
            'V': 'Action/Process',
            'ADV': 'Other',
            'F': 'Other',
            'Num': 'Number'},
        pos_name = "ENGLISH_POS")