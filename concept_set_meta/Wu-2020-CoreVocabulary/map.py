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

        sheet_list = self.get_csv('corevoc-master/lists/core', "\t", dicts=False)

        sheet = []

        valid_fields = ["word", "count"]

        for row in sheet_list[0:]:  # iterate over the lines after header
            sheet += [dict(zip(valid_fields, row[:43]))]

        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)
