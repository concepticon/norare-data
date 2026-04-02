def download(dataset):
    dataset.download_file(
        'https://s3.amazonaws.com/openneuro.org/ds004301/derivatives/annotations/semantic%20feature/feature.csv?versionId=WqWGq.Q0tf86nxnusvPHNkvz3YRatDnC&AWSAccessKeyId=AKIARTA7OOV5WQ3DGSOB&Signature=FOQ157iV5QLzoSawyDyupKs0eIM%3D&Expires=1775629822'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'feature.csv',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )    