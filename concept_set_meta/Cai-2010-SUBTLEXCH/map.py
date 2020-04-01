from pynorare.data import NormDataSet, download_zip, get_excel
from urllib import request
from zipfile import ZipFile
from pynorare import log
from pynorare.types import integer
from collections import OrderedDict

class Dataset(NormDataSet):
    id = "Cai-2010-SUBTLEXCH"

    def download(self):
        
        # custom commando to mask that we are a program
        url = 'https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/subtlexchwf.zip/at_download/file'
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        request.urlretrieve(url, "raw/cai_frequency.zip")
        with open('raw/cai_frequency.zip', 'rb') as f:
            with ZipFile(f) as zf:
                zf.extract('SUBTLEX-CH-WF.xlsx', path='raw')
        log.download('SUBTLEX-CH-WF.xlsx')

    def map(self):
        
        sheet_list = get_excel('SUBTLEX-CH-WF.xlsx', 0)
        sheet = [OrderedDict(zip(sheet_list[2], row)) for row in sheet_list[3:]]
        self.extract_data(
                sheet,
                [
                    ("Word", "CHINESE", str),
                    ("WCount", "CHINESE_FREQUENCY", integer),
                    ("W/million", "CHINESE_FREQUENCY_PM", str),
                    ("logW", "CHINESE_FREQUENCY_LOG", str),
                    ("W-CD", "CHINESE_CD", integer),
                    ("W-CD%", "CHINESE_CD_PERCENTAGE", str),
                    ("logW-CD", "CHINESE_CD_LOG", str),
                    ],
                [
                    "CONCEPTICON_ID",
                    "CONCEPTICON_GLOSS",
                    "CHINESE",
                    "CHINESE_FREQUENCY",
                    "CHINESE_FREQUENCY_LOG",
                    "CHINESE_FREQUENCY_PM",
                    "CHINESE_CD",
                    "CHINESE_CD_LOG",
                    "CHINESE_CD_PERCENTAGE",
                    "LINE_IN_SOURCE"
                    ],
                gloss='CHINESE',
                language='zh'
                )

if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)

