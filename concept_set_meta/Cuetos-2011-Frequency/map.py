from pynorare.dataset import NormDataSet, download_zip, get_excel
from pynorare.util import progressbar
from sys import argv


class Dataset(NormDataSet):
    id = "Cuetos-2011-Frequency"

    def download(self):
        download_zip(
            'http://crr.ugent.be/papers/SUBTLEX-ESP.zip',
            'cuetos_freq.zip',
            'SUBTLEX-ESP.xlsx',
        )

    def map(self):
        sheet = []
        for row in get_excel('SUBTLEX-ESP.xlsx', 0)[1:]:
            sheet += [dict(zip(
                ["Word", "Freq. count", "Freq. per million", "Log freq."],
                row[:4]))]
            sheet += [dict(zip(
                ["Word", "Freq. count", "Freq. per million", "Log freq."],
                row[5:9]))]
            sheet += [dict(zip(
                ["Word", "Freq. count", "Freq. per million", "Log freq."],
                row[10:14]))]

        self.extract_data(
            sheet,
            [
                ('Word', 'SPANISH', str),
                ('Freq. count', "SPANISH_FREQUENCY", str),
                ('Freq. per million', 'SPANISH_FREQUENCY_PM', str),
                ('Log freq.', "SPANISH_FREQUENCY_LOG", str)],
            [
                'CONCEPTICON_ID',
                'CONCEPTICON_GLOSS',
                'SPANISH',
                "SPANISH_FREQUENCY",
                "SPANISH_FREQUENCY_PM",
                "SPANISH_FREQUENCY_LOG"
            ],
            gloss='SPANISH',
            language='es')


if __name__ == '__main__':
    Dataset().run(argv)
