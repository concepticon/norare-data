from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "StadthagenGonzalez-2017-ValenceArousal"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-015-0700-2/MediaObjects/13428_2015_700_MOESM1_ESM.csv',
            '13428_2015_700_MOESM1_ESM.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('13428_2015_700_MOESM1_ESM.csv', delimiter=",", dicts=True,
                coding='cp1252')
        self.extract_data(
                sheet,
                gloss='SPANISH',
                language='es'
                )
