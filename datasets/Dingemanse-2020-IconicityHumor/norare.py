def download(dataset):
    dataset.download_zip(
        'https://github.com/mdingemanse/playful_iconicity/archive/refs/heads/master.zip',
        'playful_iconicity-master.zip',
        'playful_iconicity-master/data/combined-experimental-norms-with-humour-iconicity-aversion-taboo-predictions-logletterfreq.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('playful_iconicity-master/data/combined-experimental-norms-with-humour-iconicity-aversion-taboo-predictions-logletterfreq.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )    