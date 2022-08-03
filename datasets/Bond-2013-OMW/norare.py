def download(dataset):
    dataset.download_file(
        'http://compling.hss.ntu.edu.sg/omw/wn30-core-synsets.tab',
        'core-synsets.tsv',
    )
    # download nltk stuff
    #dataset.download_file(
    #    'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip',
    #    'wordnet.zip'
    #        )


def map(dataset, concepticon, mappings):
    sheet = dataset.get_csv('wordnet.tsv')
    dataset.extract_data(
        'wordnet.tsv',
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            'v': 'Action/Process',
            'n': 'Person/Thing',
            'a': 'Property'}
    )

