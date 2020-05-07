from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Keuleers-2012-LexicalDecision"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0118-4/MediaObjects/13428_2011_118_MOESM1_ESM.zip',
            'keuleers_bld.zip',
            '13428_2011_118_MOESM1_ESM/blp-items.xls',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2011_118_MOESM1_ESM/blp-items.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
