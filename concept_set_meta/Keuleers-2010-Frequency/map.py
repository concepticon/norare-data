from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Keuleers-2010-Frequency"

    def download(self):
        self.download_zip(
            'http://crr.ugent.be/subtlex-nl/SUBTLEX-NL.cd-above2.xlsx.zip',
            'keuleers_freq.zip',
            'Users/emmanuel/projects/frequencies/subtlex-nl/distribution/version1.3/SUBTLEX-NL.cd-above2.xlsx'
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('Users/emmanuel/projects/frequencies/subtlex-nl/distribution/version1.3/SUBTLEX-NL.cd-above2.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                gloss='DUTCH',
                language='nl',
                write_file=write_file)
