from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Clark-2004-ImageryFamiliarity"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBF03195584/MediaObjects/Clark-BRM-2004.zip',
            'Clark-BRM-2004.zip',
            'Clark-BRMIC-2004/cp2004b.txt'
        )

    def map(self, write_file=True):

        with open(self.raw_dir.joinpath('Clark-BRMIC-2004/cp2004b.txt')) as f:
            data = [row.split() for row in f]
        sheet = [dict(zip(data[1], row)) for row in data[2:2313]]

        for m in list(self.mappings['en']):
            if m.upper() not in self.mappings['en']:
                self.mappings['en'][m.upper()] = self.mappings['en'][m]

        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
