from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Wierzba-2015-DiscreteEmotions"

    def download(self):
        self.download_file(
            'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4492597/bin/pone.0132305.s004.xlsx',
            'pone.0132305.s004.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('pone.0132305.s004.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='POLISH',
                language='pl'
                )
