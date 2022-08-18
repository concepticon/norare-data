def download(dataset):
    dataset.download_zip(
        'http://saifmohammad.com/WebDocs/VAD/NRC-VAD-Lexicon-Aug2018Release.zip',
        'NRC-VAD-Lexicon.zip',
        'NRC-VAD-Lexicon-Aug2018Release/NRC-VAD-Lexicon.txt'
    )


def map(dataset, concepticon, mappings):
    items = [
        dict(zip(['Word', 'Valence', 'Arousal', 'Dominance'], row)) for row in
        dataset.get_csv('NRC-VAD-Lexicon-Aug2018Release/NRC-VAD-Lexicon.txt', delimiter="\t")]
    dataset.extract_data(
        items,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
