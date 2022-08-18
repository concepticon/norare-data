def download(dataset):
    dataset.download_file(
        'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4492597/bin/pone.0132305.s004.xlsx')


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'pone.0132305.s004.xlsx',
        concepticon,
        mappings,
        gloss='POLISH', 
        language='pl')

