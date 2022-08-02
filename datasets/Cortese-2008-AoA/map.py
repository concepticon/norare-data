from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Cortese-2008-AoA"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.40.3.791/MediaObjects/Cortese-BRM-2008.zip',
            'Cortese-BRM-2008.zip',
            'Cortese-BRM-2008/Cortese B377 norms.xls',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('Cortese-BRM-2008/Cortese B377 norms.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
