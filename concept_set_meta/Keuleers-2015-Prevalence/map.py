from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Keuleers-2015-Prevalence"

    def download(self):
        self.download_file(
            'http://crr.ugent.be/papers/prevalence%20B%20&%20NL.xlsx',
            'prevalence%20B%20&%20NL.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('prevalence%20B%20&%20NL.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='DUTCH',
                language='nl'
                )
