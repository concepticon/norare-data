from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Lynott-2019-Sensorimotor"

    def download(self):
        self.download_file(
            'https://osf.io/48wsc/download',
            'Lancaster_sensorimotor_norms_for_39707_words.csv',
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('Lancaster_sensorimotor_norms_for_39707_words.csv', ',', dicts=True)

        for m in list(self.mappings['en']):
            if m.upper() not in self.mappings['en']:
                self.mappings['en'][m.upper()] = self.mappings['en'][m]

        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
