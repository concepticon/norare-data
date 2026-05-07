def download(dataset):
    dataset.download_zip(
        'https://github.com/yoonwonj/EVOKE/archive/refs/heads/main.zip',
        'EVOKE-main.zip',
        'EVOKE-main/Korean_English_mappings/Emotion_Words_Combined_Clean.csv'
    )
        
def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('EVOKE-main/Korean_English_mappings/Emotion_Words_Combined_Clean.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=True,
        pos_mapper = {
            'noun': 'Person/Thing',
            'verb': 'Action/Process',
            'adjective': 'Property'},
        pos_name = "ENGLISH_POS"
    )