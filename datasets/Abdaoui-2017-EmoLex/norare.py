def download(dataset):
    dataset.download_file('http://advanse.lirmm.fr/FEEL.csv')


def map(dataset, concepticon, mappings):    
    sheet = dataset.get_csv('FEEL.csv', delimiter=";", dicts=True)
    bools = 'joy;fear;sadness;anger;surprise;disgust'.split(';')
    sheet = [
        {k: (True if v == '1' else (False if v == '0' else None)) if k in bools else v for k, v in row.items()}
        for row in sheet]
    dataset.extract_data(sheet, concepticon, mappings, gloss='FRENCH', language='fr')
