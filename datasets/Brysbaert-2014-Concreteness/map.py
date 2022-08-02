from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):
    id = 'Brysbaert-2014-Concreteness'

    def download(self):
        self.download_file(
        'http://crr.ugent.be/papers/Concreteness_ratings_Brysbaert_et_al_BRM.txt',
        'brysbaert_concreteness.tsv'
        )

        self.download_file(
                'https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/wordnet.zip',
                'wordnet.zip'
                )

    def map(self, write_file=True):

        sheet = self.get_csv('brysbaert_concreteness.tsv')

        self.extract_data(
                sheet,
                pos=True,
                pos_mapper = {
                    'Noun': 'Person/Thing',
                    'Adjective': 'Property',
                    'Verb': 'Action/Process',
                    'Adverb': 'Other',
                    'Article': 'Other',
                    'Conjunction': 'Other',
                    'Determiner': "Other",
                    'Ex': "Other",
                    '#N/A': 'Other',
                    "Interjection": "Other",
                    "Name": "Person/Thing",
                    "Preposition": "Other",
                    "To": "Other",
                    "Number": "Number",
                    "Pronoun": "Other",
                    "Not": "Other"},
                pos_name = "ENGLISH_POS"
                )

