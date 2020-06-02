from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):

    id = "Alonso-2015-AoA"

    def download(self):
        self.download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0454-2/MediaObjects/13428_2014_454_MOESM1_ESM.zip',
            'SpanishAoA.zip',
            'SpanishAoA.xls',
        )

    def map(self, write_file=True):
        
        sheet = self.get_excel('SpanishAoA.xls', 0, dicts=True)
        
        self.extract_data(
                sheet,
                pos_mapper = {
                    'NOUN': 'Person/Thing',
                    'ADJECTIVE': 'Property',
                    'VERB': 'Action/Process',
                    'ADPOSITION': 'Other',
                    'ADVERB': 'Other',
                    'CONJUNCTION': 'Other',
                    'DATE': "Person/Thing",
                    'DETERMINER': "Other",
                    'INTERJECTION': 'Other',
                    "PRONOUN": "Other",
                    " ": "Other"},
                pos_name = "SPANISH_POS",
                gloss='SPANISH',
                language='es',
                write_file=write_file)

                

