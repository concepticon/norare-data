from pynorare.dataset import NormDataSet, download_file, get_excel
from pynorare.types import integer

class Dataset(NormDataSet):
    
    id = "Riegel-2015-AffectiveRatings"

    def download(self):
        download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0552-1/MediaObjects/13428_2014_552_MOESM1_ESM.xlsx',
            'riegel.xlsx'
            )

    def map(self):

        sheet = get_excel('riegel.xlsx', 0, dicts=True)

        # modify mappings
        for m in list(self.mappings['de']):
            if m.lower() not in self.mappings['de']:
                self.mappings['de'][m.lower()] = self.mappings['de'][m]

        self.extract_data(
                sheet,
                [
                    ("No.", "NUMBER_IN_SOURCE", str),
                    ("BAWL_word", "GERMAN", str),
                    ("NAWL_word", "POLISH", str),
                    ("val_M_men", "POLISH_VALENCY_MEAN_MEN", str),
                    ("val_M_women", "POLISH_VALENCY_MEAN_WOMEN", str),
                    ("val_M_all", "POLISH_VALENCY_MEAN_ALL", str),
                    ("aro_M_men", "POLISH_AROUSAL_MEAN_MEN", str),
                    ("aro_M_women", "POLISH_AROUSAL_MEAN_WOMEN", str),
                    ("aro_M_all", "POLISH_AROUSAL_MEAN_ALL", str),
                    ("ima_M_men", "POLISH_IMAGEABILITY_MEAN_MEN", str),
                    ("ima_M_women", "POLISH_IMAGEABILITY_MEAN_WOMEN", str),
                    ("ima_M_all", "POLISH_IMAGEABILITY_MEAN_ALL", str),
                    ("SUBTLEX-PL_freq", "POLISH_FREQUENCY", str),
                    ("SUBTLEX-PL_cd", "POLISH_FREQUENCY_CD", str),
                    ],
                [
                    "CONCEPTICON_ID",
                    "CONCEPTICON_GLOSS",
                    "POLISH",
                    "GERMAN",
                    "NUMBER_IN_SOURCE",
                    "POLISH_VALENCY_MEAN_MEN",
                    "POLISH_VALENCY_MEAN_WOMEN",
                    "POLISH_VALENCY_MEAN_ALL",
                    "POLISH_AROUSAL_MEAN_MEN",
                    "POLISH_AROUSAL_MEAN_WOMEN",
                    "POLISH_AROUSAL_MEAN_ALL",
                    "POLISH_IMAGEABILITY_MEAN_MEN",
                    "POLISH_IMAGEABILITY_MEAN_WOMEN",
                    "POLISH_IMAGEABILITY_MEAN_ALL",
                    "POLISH_FREQUENCY",
                    "POLISH_FREQUENCY_CD",
                    "LINE_IN_SOURCE"
                    ],
                gloss='GERMAN',
                language='de'
                )
        
if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)
