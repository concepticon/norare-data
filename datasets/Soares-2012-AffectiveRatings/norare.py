def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0131-7/MediaObjects/13428_2011_131_MOESM1_ESM.xls',
        '13428_2011_131_MOESM1_ESM.xls',
    )

def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_excel('13428_2011_131_MOESM1_ESM.xls', 1, dicts=False)
    sheet = [dict(zip(sheet_list[0], row)) for row in sheet_list[1:]]    
    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='PORTUGUESE',
        language='pt',
        pos=True,
        pos_mapper = {
            'N': 'Person/Thing',
            'Adj': 'Property',
            'V': 'Action/Process',
            'Adv': 'Other',
            'Int': 'Other'},
        pos_name = "PORTUGUESE_POS"
    )