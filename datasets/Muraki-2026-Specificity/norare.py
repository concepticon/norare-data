def download(dataset):
    dataset.download_file(
        'https://osf.io/download/a7tzg/?view_only=4a39331890a4453cac833aa5f1c584d22',
        'Specificity_Ratings_Eng.04.17.2025.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Specificity_Ratings_Eng.04.17.2025.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=True,
        pos_mapper = {
            'Verb': 'Action/Process',
            'Noun': 'Person/Thing',
            'Adjective': 'Property'},
        pos_name = "ENGLISH_POS"
    )    