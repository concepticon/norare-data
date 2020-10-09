from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Crepaldi-2015-Frequency"

    def download(self):
        self.download_file(
            'http://crr.ugent.be/subtlex-it/subtlex-it.csv',
            'subtlex-it.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('subtlex-it.csv', ',', dicts=True)
        self.extract_data(
                sheet,
                gloss='ITALIAN',
                language='it',
                pos=True,
                pos_mapper = {
                    'NOM': 'Person/Thing',
                    'ADJ': 'Property',
                    'VER': 'Action/Process',
                    'ADV': 'Other',
                    'CON': 'Other',
                    'ABR': 'Other',
                    'DET': "Other",
                    'FW': "Other",
                    'PRE': 'Other',
                    "NPR": "Other",
                    "PRO": "Other",
                    "SENT": "Other",
                    "SYM": "Other",
                    "NUM": "Number",
                    "INT": "Other",
                    "PON": "Other"},
                pos_name = "ITALIAN_POS"
                )
