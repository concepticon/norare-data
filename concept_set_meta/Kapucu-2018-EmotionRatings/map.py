from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Kapucu-2018-EmotionRatings"

    def download(self):
        self.download_file(
            'https://osf.io/wkeb7/download',
            'TurkishEmotionalWordNorms.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('TurkishEmotionalWordNorms.csv', ';', dicts=True)

        for m in list(self.mappings['tr']):
            if m.upper() not in self.mappings['tr']:
                self.mappings['tr'][m.upper()] = self.mappings['tr'][m]

        self.extract_data(
                sheet,
                gloss='TURKISH',
                language='tr',
                write_file=write_file)
