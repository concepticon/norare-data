def download(dataset):
    dataset.download_file(
        'https://osf.io/download/jsmd9',
        'data_boi.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('data_boi.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='JAPANESE',
        language='ja',
        pos=True,
        pos_mapper = {
          'Verb': 'Action/Process',
          'Noun': 'Person/Thing',
          'Adjective': 'Property'},
        pos_name = "JAPANESE_POS"
    )   
