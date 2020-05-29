from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Breisemeister-2011-DiscreteEmotions"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0059-y/MediaObjects/13428_2011_59_MOESM1_ESM.xls',
            '13428_2011_59_MOESM1_ESM.xls'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2011_59_MOESM1_ESM.xls', 0, dicts=True)

        for m in list(self.mappings['de']):
            if m.lower() not in self.mappings['de']:
                self.mappings['de'][m.lower()] = self.mappings['de'][m]

        self.extract_data(
                sheet,
                gloss='GERMAN',
                language='de',
                write_file=write_file)
