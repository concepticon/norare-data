from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Alonso-2011-OralFrequency"

    def download(self):
        self.download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-011-0062-3/MediaObjects/13428_2011_62_MOESM1_ESM.xls',
            '13428_2011_62_MOESM1_ESM.xls',
        )

    def map(self, write_file=True):

        sheet_ = self.get_excel('13428_2011_62_MOESM1_ESM.xls', 0, dicts=True)

        sheet = [['Word', 'Frequency', 'Frequency per million', 'Log10(freq count+1)']]
        for row in sheet_[1:]:  # iterate over the lines after header
            new_row = {}
            for head, cell in zip(sheet_[0], row):
                if head in sheet[0]:
                    new_row[head] = cell
                if len(new_row) == 3:
                    sheet.append(new_row)
                    new_row = {}

        self.extract_data(
                sheet,
                gloss='SPANISH',
                language='es',
                write_file=write_file)