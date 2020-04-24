from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Brysbaert-2011-SUBTLEXDE"

    def download(self):
        self.download_zip(
            'http://crr.ugent.be/SUBTLEX-DE/SUBTLEX-DE%20cleaned%20with%20Google00%20frequencies.zip',
            'brysbaert_freq_de',
            'SUBTLEX-DE cleaned with Google00 frequencies.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('SUBTLEX-DE cleaned with Google00 frequencies.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='GERMAN',
                language='de',
                write_file=write_file)
