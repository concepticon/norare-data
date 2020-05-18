from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Riegel-2015-AffectiveRatings"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0552-1/MediaObjects/13428_2014_552_MOESM1_ESM.xlsx',
            '13428_2014_552_MOESM1_ESM.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2014_552_MOESM1_ESM.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='POLISH',
                language='pl',
                write_file=write_file)