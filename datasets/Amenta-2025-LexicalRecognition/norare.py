def download(dataset):
    dataset.download_file(
        'https://osf.io/download/69nqy/?view_only=20c718b7a8594fdba02256b475832597',
        'ICP.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('ICP.csv', delimiter="\t"),
        concepticon,
        mappings,
        gloss='ITALIAN',
        language='it'
    )    