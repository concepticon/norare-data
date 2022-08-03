def download(dataset):
    dataset.download_zip(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-012-0314-x/MediaObjects/13428_2012_314_MOESM1_ESM.zip',
        'warriner_affective.zip',
        'BRM-emot-submit.csv'
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'BRM-emot-submit.csv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )

