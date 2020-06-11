from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Wu-2020-CoreVocabulary"

    def download(self):
        self.download_zip(
            'https://github.com/wswu/corevoc/archive/master.zip',
            'master.zip',
            'corevoc-master/lists/core'
        )

    def map(self, write_file=True):

        column_names=["word", "count"]
        
        sheet = self.get_csv('core', "\t", dicts=True, header=None, names=column_names)
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
