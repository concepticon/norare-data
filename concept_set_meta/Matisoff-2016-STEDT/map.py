from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Matisoff-2016-STEDT"

    def download(self):
        self.download_file(
            'https://github.com/stedt-project/sss/raw/master/semcats/revision1/lexicon_semcats-glosses_20110913.xlsx',
            'lexicon_semcats-glosses_20110913.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('lexicon_semcats-glosses_20110913.xlsx', 0, dicts=True)

        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
