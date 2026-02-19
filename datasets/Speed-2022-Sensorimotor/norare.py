def download(dataset):
    dataset.download_file(
        'https://osf.io/wzfpd/download',
        'SpeedBrysbaert_Norms.xlsx',
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'SpeedBrysbaert_Norms.xlsx',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl',
        pos=True,
        pos_mapper = {
            'N': 'Person/Thing',
            'ADJ': 'Property',
            'WW': 'Action/Process',
            'Function': 'Other',
            "TW": "Number"},
        pos_name = "DUTCH_POS"
    )
