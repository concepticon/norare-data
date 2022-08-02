from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Cai-2010-Frequency"

    def download(self):
        self.download_zip(
            'https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/subtlexchwf.zip/at_download/file',
            'SUBTLEX-CH-WF.zip',
            'SUBTLEX-CH-WF.xlsx'
        )

    def map(self, write_file=True):
        
        sheet_list = self.get_excel('SUBTLEX-CH-WF.xlsx', 0, dicts=False)

        sheet = [dict(zip(sheet_list[2], row)) for row in sheet_list[3:]]

        self.extract_data(
                sheet,
                gloss='CHINESE',
                language='zh'
                )
