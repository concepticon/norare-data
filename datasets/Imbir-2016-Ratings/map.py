from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Imbir-2016-Ratings"

    def download(self):
        self.download_file(
            'https://www.frontiersin.org/articles/file/downloadfile/174568_supplementary-materials_datasheets_1_xlsx/octet-stream/Data%20Sheet%201.XLSX/1/174568',
            'data sheet 1.xlsx',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('data sheet 1.xlsx', 0, dicts=True)
        self.extract_data(
                sheet,
                pos_mapper = {
                    'N': 'Person/Thing',
                    'A': 'Property',
                    'V': 'Action/Process',
                    'pron': 'Other',
                    'adv': 'Other',
                    'I': 'Action/Process',
                    'pred': "Person/Thing",
                    'ign': "Other",
                    'num': 'Number',
                    "prep": "Other",
                    "qub": "Other"},
                pos_name = "POLISH_POS",
                gloss='POLISH',
                language='pl'
                )