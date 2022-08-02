from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Mohammad-2018-AffectiveRatings"

    def download(self):
        self.download_zip(
            'http://sentiment.nrc.ca/lexicons-for-research/NRC-VAD-Lexicon.zip',
            'NRC-VAD-Lexicon.zip',
            'NRC-VAD-Lexicon/NRC-VAD-Lexicon.txt'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('NRC-VAD-Lexicon/NRC-VAD-Lexicon.txt', delimiter="\t", dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
