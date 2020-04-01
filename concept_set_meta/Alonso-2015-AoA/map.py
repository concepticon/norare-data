from pynorare.data import NormDataSet, download_zip, get_excel
from pynorare.util import progressbar
from sys import argv


class Dataset(NormDataSet):

    id = "Alonso-2015-AoA"

    def download(self):
        download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0454-2/MediaObjects/13428_2014_454_MOESM1_ESM.zip',
            'SpanishAoA.zip',
            'SpanishAoA.xls',
        )

    def map(self):
        
        sheet = get_excel('SpanishAoA.xls', 0, dicts=True)
        self.extract_data(
                sheet,
                [
                    ('word', 'SPANISH', str),
                    ('averageAoA', "SPANISH_AOA_RATING_MEAN", str),
                    ('SD', 'SPANISH_AOA_RATING_SD', str),
                    ('Min', "SPANISH_AOA_RATING_MIN", lambda x: '{0:.0f}'.format(x)),
                    ('Max', 'SPANISH_AOA_RATING_MAX', lambda x: '{0:.0f}'.format(x)),
                    ('OralFreq_Log', 'SPANISH_ORAL_FREQUENCY_LOG', str),
                    (' WrittenFreq_Subtlex-ESP_Log',
                        'SPANISH_WRITTEN_FREQUENCY_LOG', str)],
                [
                    'CONCEPTICON_ID', 
                    'CONCEPTICON_GLOSS',
                    'SPANISH',
                    "SPANISH_AOA_RATING_MEAN",
                    'SPANISH_AOA_RATING_SD',
                    "SPANISH_AOA_RATING_MIN",
                    'SPANISH_AOA_RATING_MAX',
                    'SPANISH_ORAL_FREQUENCY_LOG',
                    'SPANISH_WRITTEN_FREQUENCY_LOG'
                    ],
                gloss='SPANISH',
                language='es')

                
if __name__ == '__main__':
    Dataset().run(argv)
