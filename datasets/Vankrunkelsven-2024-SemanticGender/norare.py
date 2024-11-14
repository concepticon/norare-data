def download(dataset):
    dataset.download_file(
        'https://osf.io/download/wfu28/',
        'Norms_Gender.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('Norms_Gender.csv', delimiter=";"),
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl',
        pos=True,
        pos_mapper = {
            'N': 'Person/Thing',
            'ADJ': 'Property',
            'WW': 'Action/Process',
            'Function': 'Other',
            "TW": "Number"},
        pos_name = "DUTCH_POS"
    )
