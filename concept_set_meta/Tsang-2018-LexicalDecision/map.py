from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Tsang-2018-LexicalDecision"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-017-0944-0/MediaObjects/13428_2017_944_MOESM1_ESM.xlsx',
            '13428_2017_944_MOESM1_ESM.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('13428_2017_944_MOESM1_ESM.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='CHINESE',
                language='zh',
                write_file=write_file)
