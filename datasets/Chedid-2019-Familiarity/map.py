from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Chedid-2019-Familiarity"

    def download(self):
        self.download_file(
            'https://lingualab.ca/normes-familiarity-chedid2018.xlsx',
            'normes-familiarity-chedid2018.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('normes-familiarity-chedid2018.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='FRENCH',
                language='fr'
                )

