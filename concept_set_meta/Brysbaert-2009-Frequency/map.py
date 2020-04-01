from pynorare.data import NormDataSet, download_zip, get_excel
from pynorare.util import progressbar
from sys import argv

class Dataset(NormDataSet):

    id = "Brysbaert-2009-Freq"

    def download(self):
        download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.4.977/MediaObjects/Brysbaert-BRM-2009.zip',
            'brysbaert_freq',
            'Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx',
        )

    def map(self):
        
        sheet = get_excel('Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx', 0,
                dicts=True)

        self.extract_data(
                sheet,
                [
                    ("Word", "ENGLISH", str),
                    ("FREQcount", "ENGLISH_FREQUENCY", str),
                    ("CDcount", "ENGLISH_CD", str),
                    ("SUBTLWF", "ENGLISH_SUBTITLE_FREQUENCY", str),
                    ("SUBTLCD", "ENGLISH_SUBTITLE_CD", str),
                    ("Lg10WF", "ENGLISH_FREQUENCY_LOG", str),
                    ("Lg10CD", "ENGLISH_CD_LOG", str),
                    ],
                [
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "ENGLISH",
                "ENGLISH_FREQUENCY",
                "ENGLISH_CD",
                "ENGLISH_SUBTITLE_FREQUENCY",
                "ENGLISH_SUBTITLE_CD",
                "ENGLISH_FREQUENCY_LOG",
                "ENGLISH_CD_LOG",
                "LINE_IN_SOURCE"],
                gloss='ENGLISH',
                language='en')
        
if __name__ == '__main__':
    Dataset().run(argv)
