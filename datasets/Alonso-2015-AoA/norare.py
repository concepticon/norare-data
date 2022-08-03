import shutil


def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0454-2/MediaObjects/13428_2014_454_MOESM1_ESM.zip',
        'SpanishAoA.zip',
        'SpanishAoA.xls',
    )
    shutil.copy(dataset.raw_dir / 'SpanishAoA.xls', dataset.raw_dir / 'SpanishAoA.xlsx')


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'SpanishAoA.xlsx',
        concepticon,
        mappings,
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
        language='es'
    )
