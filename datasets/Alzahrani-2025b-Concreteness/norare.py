def download(dataset):
    dataset.download_file(
        'https://osf.io/download/ky45v/?view_only=b2ce3c47a0c640f68dda1e718e9f39b5',
        'LLM_CNC_30K_Ratings.xlsx'
    )

def map(dataset, concepticon, mappings):
     dataset.extract_data(
        'LLM_CNC_30K_Ratings.xlsx',
        concepticon,
        mappings,
        gloss='ARABIC',
        language='ar'
    )