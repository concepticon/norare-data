from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "StadthagenGonzalez-2018-DiscreteEmotions"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-017-0962-y/MediaObjects/13428_2017_962_MOESM1_ESM.csv',
            '13428_2017_962_MOESM1_ESM.csv',
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('13428_2017_962_MOESM1_ESM.csv', delimiter=",", dicts=True, coding='cp1252')
        self.extract_data(
                sheet,
                pos_mapper = {
                    'NOUN': 'Person/Thing',
                    'ADJECTIVE': 'Property',
                    'VERB': 'Action/Process',
                    'ADPOSITION': 'Other',
                    'ADVERB': 'Other',
                    'CONJUNCTION': 'Other',
                    'DATE': "Person/Thing",
                    'DETERMINER': "Other",
                    "PRONOUN": "Other"},
                pos_name = "SPANISH_POS",
                gloss='SPANISH',
                language='es',
                write_file=write_file)
