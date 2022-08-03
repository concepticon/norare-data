def download(dataset):
    dataset.download_file('http://advanse.lirmm.fr/FEEL.csv')


def map(dataset, concepticon, mappings):    
    sheet = dataset.get_csv('FEEL.csv', delimiter=";", dicts=True)
    dataset.extract_data(sheet, concepticon, mappings, gloss='FRENCH', language='fr')
