from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Engelthaler-2018-Humor"

    def download(self):
        self.download_file(
            'https://raw.githubusercontent.com/tomasengelthaler/HumorNorms/master/humor_dataset.csv',
            'humor_dataset.csv'
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('humor_dataset.csv', ",", dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
