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
                ('AROU', "AROUSAL_MEAN", str),
                ('VAL', 'VALENCE_MEAN', str),
                ('DOM', "DOMINANCE_MEAN", str),
                ('CNC', "CONCRETENESS_MEAN", str),
                ('IMAG', "IMAGEABILITY_MEAN", str),
                ('FAM', "FAMILIARITY_MEAN", str),
                ('AOA', "AOA_MEAN", str),
                ('SIZE', "SEM_SIZE_MEAN", str),
                ('GEND', "GENDER_ASSOCIATION_MEAN", str)},
            [
                'CONCEPTICON_ID',
                'CONCEPTICON_GLOSS',
                'ENGLISH',
                "AROUSAL_MEAN",
                "VALENCE_MEAN",
                "DOMINANCE_MEAN",
                "CONCRETENESS_MEAN",
                "IMAGEABILITY_MEAN",
                "FAMILIARITY_MEAN",
                "AOA_MEAN",
                "SEM_SIZE_MEAN",
                "GENDER_ASSOCIATION_MEAN"
            ],
            gloss='ENGLISH',
            language='en')


if __name__ == '__main__':
    Dataset().run(argv)
