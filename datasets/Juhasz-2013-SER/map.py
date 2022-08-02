from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Juhasz-2013-SER"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-012-0242-9/MediaObjects/13428_2012_242_MOESM1_ESM.xls',
            '13428_2012_242_MOESM1_ESM.xls'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2012_242_MOESM1_ESM.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
