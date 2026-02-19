def download(dataset):
    dataset.download_file(
        'https://mst-cbs.polyu.edu.hk/Database/HK_norm_2021.xlsx',
        'HK_norm_2021.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'HK_norm_2021.xlsx',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )
