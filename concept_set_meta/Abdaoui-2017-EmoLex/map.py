from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Abdaoui-2017-EmoLex"

    def download(self):
        self.download_file(
            'http://advanse.lirmm.fr/FEEL.csv',
            'FEEL.csv',
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('FEEL.csv', delimiter=";", dicts=True)
        self.extract_data(
                sheet,
                gloss='FRENCH',
                language='fr',
                write_file=write_file)
