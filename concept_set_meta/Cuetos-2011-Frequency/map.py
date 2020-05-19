from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Cuetos-2011-Frequency"

    def download(self):
        self.download_zip(
            'http://crr.ugent.be/papers/SUBTLEX-ESP.zip',
            'cuetos_freq.zip',
            'SUBTLEX-ESP.xlsx',
        )

    def map(self, write_file=True):
        sheet_ = self.get_excel('SUBTLEX-ESP.xlsx', 0, dicts=False)

        sheet = []
        valid_fields = ['Word', 'Freq. count', 'Freq. per million', 'Log freq.']
        for row in sheet_[1:]:  # iterate over the lines after header
            sheet += [dict(zip(valid_fields, row[:4]))]
            sheet += [dict(zip(valid_fields, row[5:9]))]
            sheet += [dict(zip(valid_fields, row[10:14]))]

        self.extract_data(
            sheet,
            gloss='SPANISH',
            language='es',
            write_file=write_file)