def download(dataset):
    dataset.download_file(
        'https://github.com/mdingemanse/playful_iconicity/raw/refs/heads/master/data/combined-experimental-norms-with-humour-iconicity-aversion-taboo-predictions-logletterfreq.csv',
        'combined-experimental-norms-with-humour-iconicity-aversion-taboo-predictions-logletterfreq.csv',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('combined-experimental-norms-with-humour-iconicity-aversion-taboo-predictions-logletterfreq.csv', delimiter=","),
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )    