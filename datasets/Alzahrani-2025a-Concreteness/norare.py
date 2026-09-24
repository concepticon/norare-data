def download(dataset):
    dataset.download_file(
        'https://osf.io/download/sc9ak/?view_only=b2ce3c47a0c640f68dda1e718e9f39b5',
        'kalimah_norms_aoa_cnc.xlsx'
    )

def map(dataset, concepticon, mappings):
     dataset.extract_data(
        'kalimah_norms_aoa_cnc.xlsx',
        concepticon,
        mappings,
        gloss='ARABIC',
        language='ar',
        pos=True,
        pos_mapper = {
            'noun': 'Person/Thing',
            'adjective': 'Property',
            'verb': 'Action/Process'},
        pos_name = "ARABIC_POS"
    )
