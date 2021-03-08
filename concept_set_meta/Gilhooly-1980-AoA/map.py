from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Gilhooly-1980-AoA"

    def map(self, write_file=True):
        
        sheet = self.get_csv('Gilhooly-1980.tsv', '\t', dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                pos=False
                )
