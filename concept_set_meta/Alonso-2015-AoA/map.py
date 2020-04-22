from pynorare.dataset import NormDataSet
from sys import argv

class Dataset(NormDataSet):

    id = "Alonso-2015-AoA"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0454-2/MediaObjects/13428_2014_454_MOESM1_ESM.zip',
            'SpanishAoA.zip',
            'SpanishAoA.xls',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('SpanishAoA.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='SPANISH',
                language='es',
                write_file=write_file)

                
if __name__ == '__main__':
    Dataset().run(argv)
