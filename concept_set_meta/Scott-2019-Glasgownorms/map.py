from pynorare.data import NormDataSet, download_file, get_csv
from pynorare.util import progressbar
from sys import argv


class Dataset(NormDataSet):
    id = "Scott-2019-Glasgownorms"

    def download(self):
        download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-018-1099-3/MediaObjects/13428_2018_1099_MOESM2_ESM.csv',
            'scott_glasgownorms.csv',
        )

    def map(self):
        sheet = get_csv('scott_glasgownorms.csv', delimiter=",", dicts=True)

        self.extract_data(
            sheet,
            {
                ('Words', 'ENGLISH', str),
                ('AROU', "ENGLISH_AROUSAL_MEAN", str),
                ('VAL', 'ENGLISH_VALENCE_MEAN', str),
                ('DOM', "ENGLISH_DOMINANCE_MEAN", str),
                ('CNC', "ENGLISH_CONCRETENESS_MEAN", str),
                ('IMAG', "ENGLISH_IMAGEABILITY_MEAN", str),
                ('FAM', "ENGLISH_FAMILIARITY_MEAN", str),
                ('AOA', "ENGLISH_AOA_MEAN", str),
                ('SIZE', "ENGLISH_SEM_SIZE_MEAN", str),
                ('GEND', "ENGLISH_GENDER_ASSOCIATION_MEAN", str)},
            [
                'CONCEPTICON_ID',
                'CONCEPTICON_GLOSS',
                'ENGLISH',
                "ENGLISH_AROUSAL_MEAN",
                "ENGLISH_VALENCE_MEAN",
                "ENGLISH_DOMINANCE_MEAN",
                "ENGLISH_CONCRETENESS_MEAN",
                "ENGLISH_IMAGEABILITY_MEAN",
                "ENGLISH_FAMILIARITY_MEAN",
                "ENGLISH_AOA_MEAN",
                "ENGLISH_SEM_SIZE_MEAN",
                "ENGLISH_GENDER_ASSOCIATION_MEAN"
            ],
            gloss='ENGLISH',
            language='en')


if __name__ == '__main__':
    Dataset().run(argv)
