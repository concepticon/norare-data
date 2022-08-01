from pynorare.dataset import NormDataSet


class Dataset(NormDataSet):

    id = "Speed-2021-Sensorimotor"

    def download(self):
        self.download_file(
            'https://osf.io/wzfpd/download',
            'SpeedBrysbaert_Norms.xlsx',
        )

    def map(self, write_file=True):
        sheet = self.get_excel('SpeedBrysbaert_Norms.xlsx', 0, dicts=True)
        self.extract_data(
            sheet,
            gloss='DUTCH',
            language='nl',
            pos=True,
            pos_mapper = {
                'N': 'Person/Thing',
                'ADJ': 'Property',
                'WW': 'Action/Process',
                'Function': 'Other',
                "TW": "Number"},
            pos_name = "DUTCH_POS"
        )
