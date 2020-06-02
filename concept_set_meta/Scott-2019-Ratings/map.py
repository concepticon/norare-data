from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):
    id = "Scott-2019-Ratings"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1099-3/MediaObjects/13428_2018_1099_MOESM2_ESM.csv',
            '13428_2018_1099_MOESM2_ESM.csv',
        )

    def map(self, write_file=True):
        sheet = self.get_csv('13428_2018_1099_MOESM2_ESM.csv', delimiter=",", dicts=True)

        self.extract_data(
            sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)

