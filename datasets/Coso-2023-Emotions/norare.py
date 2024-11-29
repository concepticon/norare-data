def download(dataset):
    dataset.download_file(
        'https://figshare.com/ndownloader/files/36434421',
        'CROWD-5e.xlsx',
    )

def map(dataset, concepticon, mappings):   
    sheet_list = dataset.get_excel('CROWD-5e.xlsx', 1, dicts=False)
    sheet = [dict(zip(sheet_list[0], row)) for row in sheet_list[1:]] 

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )