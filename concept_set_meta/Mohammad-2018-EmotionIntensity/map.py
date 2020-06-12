from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Mohammad-2018-EmotionIntensity"

    def download(self):
        self.download_zip(
            'http://sentiment.nrc.ca/lexicons-for-research/NRC-Emotion-Intensity-Lexicon-v1.zip',
            'NRC-Emotion-Intensity-Lexicon-v1.zip',
            'NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('NRC-Emotion-Intensity-Lexicon-v1/NRC-Emotion-Intensity-Lexicon-v1.txt', delimiter="\t", dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
