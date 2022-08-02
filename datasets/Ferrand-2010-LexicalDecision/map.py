from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Ferrand-2010-LexicalDecision"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.42.2.488/MediaObjects/Ferrand-BRM-2010.zip',
            'ferrand_fld.zip',
            'Ferrand-BRM-2010/FLP-words.xls',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('Ferrand-BRM-2010/FLP-words.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='FRENCH',
                language='fr'
                )
