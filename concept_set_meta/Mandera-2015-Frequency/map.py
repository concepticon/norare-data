from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Mandera-2015-Frequency"

    def download(self):
        self.download_file(
            'http://crr.ugent.be/subtlex-pl/subtlex-pl-cd-3.csv',
            'subtlex-pl-cd-3.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('subtlex-pl-cd-3.csv', '\t', dicts=True)
        self.extract_data(
                sheet,
                gloss='POLISH',
                language='pl',
                pos=True,
                pos_mapper = {
                    'subst': 'Person/Thing',
                    'adj': 'Property',
                    'verb': 'Action/Process',
                    'adv': 'Other',
                    'qub': 'Other',
                    'conj': 'Other',
                    'ign': "Other",
                    'interp': "Other",
                    'pred': 'Other',
                    "tnum": "Other",
                    "tsym": "Other",
                    "prep": "Other",
                    "To": "Other",
                    "num": "Number",
                    "pron": "Other",
                    "xxx": "Other"},
                pos_name = "POLISH_POS",
                write_file=write_file)
