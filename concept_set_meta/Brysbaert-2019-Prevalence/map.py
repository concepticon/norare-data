from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Brysbaert-2019-Prevalence"

    def download(self):
        self.download_file(
            'https://osf.io/nbu9e/download',
            'English_Word_Prevalences.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('English_Word_Prevalences.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
