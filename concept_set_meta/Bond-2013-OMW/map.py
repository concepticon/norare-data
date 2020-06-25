from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Bond-2013-OMW"

    def download(self):
        # download synset
        self.download_file(
                'http://compling.hss.ntu.edu.sg/omw/wn30-core-synsets.tab',
                'core-synsets.tsv',
        )
        # download nltk stuff
        self.download_file(
                'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip',
                'wordnet.zip'
                )

    def map(self, write_file=True):
        
        sheet = self.get_csv('wordnet.tsv')

        self.extract_data(
                sheet,
                pos=True,
                pos_mapper = {
                    'v': 'Action/Process',
                    'n': 'Person/Thing',
                    'a': 'Property'}
                )

