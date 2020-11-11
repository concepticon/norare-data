from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Vulic-2020-MultiSimLex"

    def download(self):
        self.download_file(
            'https://multisimlex.com/data/scores.xlsx',
            'scores.xlsx',
        )
        self.download_file(
            'https://multisimlex.com/data/translation.xlsx',
            'translation.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_csv('scores-with-translations.tsv', dicts=True)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )