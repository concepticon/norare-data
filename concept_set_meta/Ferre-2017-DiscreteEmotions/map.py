from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Ferre-2017-DiscreteEmotions"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-016-0768-3/MediaObjects/13428_2016_768_MOESM1_ESM.xls',
            '13428_2016_768_MOESM1_ESM.xls'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2016_768_MOESM1_ESM.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='SPANISH',
                language='es',
                write_file=write_file)
