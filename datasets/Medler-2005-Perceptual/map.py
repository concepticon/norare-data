from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Medler-2005-Perceptual"

    def map(self, write_file=True):
        
        sheet = self.get_csv('Medler-2005.tsv', '\t', dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                pos=False
                )
