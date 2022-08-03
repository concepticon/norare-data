def download(dataset):
    dataset.download_zip(
        'http://crr.ugent.be/subtlex-nl/SUBTLEX-NL.cd-above2.xlsx.zip',
        'keuleers_freq.zip',
        'Users/emmanuel/projects/frequencies/subtlex-nl/distribution/version1.3/SUBTLEX-NL.cd-above2.xlsx'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Users/emmanuel/projects/frequencies/subtlex-nl/distribution/version1.3/SUBTLEX-NL.cd-above2.xlsx',
        concepticon,
        mappings,
        gloss='DUTCH',
        language='nl'
    )
