from pynorare.data import download_zip, NormDataSet, get_excel
from pynorare.types import integer

class Dataset(NormDataSet):
    id = 'Kuperman-2012-AoA'
    
    def download(self):
        download_zip(
                'http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip',
                'kuperman_aoa.zip',
                filename='AoA_ratings_Kuperman_et_al_BRM.xlsx',
            )

    def map(self):
        sheet = get_excel('AoA_ratings_Kuperman_et_al_BRM.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                [
                    ("Word", "ENGLISH", str),
                    ("OccurTotal", "ENGLISH_OCCURRENCES_TOTAL", integer),
                    ("OccurNum", "ENGLISH_OCCURRENCES_NUM", integer),
                    ("Freq_pm", "ENGLISH_FREQUENCY_PM", str),
                    ("Rating.Mean", "ENGLISH_RATING_MEAN", str),
                    ("Rating.SD", "ENGLISH_RATING_SD", str),
                    ("Dunno", "ENGLISH_DUNNO", str),
                    ],
                [
                    "CONCEPTICON_ID",
                    "CONCEPTICON_GLOSS",
                    "ENGLISH",
                    "ENGLISH_OCCURRENCES_TOTAL",
                    "ENGLISH_OCCURRENCES_NUM",
                    "ENGLISH_FREQUENCY_PM",
                    "ENGLISH_RATING_MEAN",
                    "ENGLISH_RATING_SD",
                    "ENGLISH_DUNNO",
                    "LINE_IN_SOURCE"
                    ],
                gloss='ENGLISH',
                language='en')

if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)

