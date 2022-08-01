import subprocess

from csvw.dsv import reader, UnicodeWriter

from pynorare.dataset import NormDataSet


class Dataset(NormDataSet):

    id = "Speed-2021-Sensorimotor"

    def download(self):
        self.download_file(
            'https://osf.io/wzfpd/download',
            'SpeedBrysbaert_Norms.xlsx',
        )
        subprocess.check_call('libreoffice --headless --convert-to csv {0}/SpeedBrysbaert_Norms.xlsx --outdir {0}'.format(self.raw_dir).split())
        rows = list(reader(self.raw_dir / 'SpeedBrysbaert_Norms.csv', encoding='cp1252'))
        with UnicodeWriter(self.raw_dir / 'SpeedBrysbaert_Norms.csv') as w:
            w.writerows(rows)

    def map(self, write_file=True):
        sheet = self.get_csv('SpeedBrysbaert_Norms.csv', ',', dicts=True)
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
