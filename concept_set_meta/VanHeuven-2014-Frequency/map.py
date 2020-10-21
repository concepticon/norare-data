from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "VanHeuven-2014-Frequency"

    def download(self):
        self.download_file(
            'http://crr.ugent.be/papers/SUBTLEX-UK.xlsx',
            'SUBTLEX-UK.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('SUBTLEX-UK.xlsx',0, dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                pos=True,
                pos_mapper = {
                    'noun': 'Person/Thing',
                    'adjective': 'Property',
                    'verb': 'Action/Process',
                    'adverb': 'Other',
                    'conjunction': 'Other',
                    'pronoun': 'Other',
                    'determiner': "Other",
                    'unclassified': "Other",
                    "preposition": "Other",
                    "name": "Other",
                    "number": "Number",
                    "interjection": "Other",
                    "marker": "Other"},
                pos_name = "ENGLISH_POS"
                )
