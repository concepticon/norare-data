from pynorare.dataset import NormDataSet
import attr
from pathlib import Path

@attr.s
class Dataset(NormDataSet):
    repos = attr.ib(default=Path('.'))
    id = 'Kuperman-2012-AoA'
    
    def download(self):
        self.download_zip(
                'http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip',
                'kuperman_aoa.zip',
                filename='AoA_ratings_Kuperman_et_al_BRM.xlsx',
            )

    def map(self, write_file=True):
        sheet = self.get_excel(
            'AoA_ratings_Kuperman_et_al_BRM.xlsx', 
            0, 
            dicts=True
            )
        self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en',
                write_file=write_file)


