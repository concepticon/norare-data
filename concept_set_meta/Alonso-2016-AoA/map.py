from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Alonso-2016-AoA"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-015-0675-z/MediaObjects/13428_2015_675_MOESM1_ESM.xlsx',
            '13428_2015_675_MOESM1_ESM.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2015_675_MOESM1_ESM.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='SPANISH',
                language='es'
                )

                
