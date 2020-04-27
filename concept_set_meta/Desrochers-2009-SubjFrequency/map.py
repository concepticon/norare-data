from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Desrochers-2009-SubjFrequency"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.2.546/MediaObjects/Desrochers-BRM-2009.zip',
            'desrochers_freq_fr',
            'Desrochers-Thompson_2009_Ratings.xls'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('Desrochers-Thompson_2009_Ratings.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='FRENCH',
                language='fr',
                write_file=write_file)
