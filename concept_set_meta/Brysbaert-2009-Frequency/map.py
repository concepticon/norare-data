from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Brysbaert-2009-Frequency"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.4.977/MediaObjects/Brysbaert-BRM-2009.zip',
            'brysbaert_freq.zip',
            'Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx', 0,
                dicts=True)

        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)

