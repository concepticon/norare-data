from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Warriner-2013-AffectiveRatings"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-012-0314-x/MediaObjects/13428_2012_314_MOESM1_ESM.zip',
            'warriner_affective.zip',
            'BRM-emot-submit.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('BRM-emot-submit.csv', ",", dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
