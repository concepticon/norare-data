def download(dataset):
    dataset.download_zip(
        'http://saifmohammad.com/WebDocs/NRC-Emotion-Intensity-Lexicon-v1.zip',
        'NRC-Emotion-Intensity-Lexicon-v1.zip',
        'NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt'
    )


def map(dataset, concepticon, mappings):
    sheet = dataset.get_csv('NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt', delimiter="\t", dicts=True)
    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
