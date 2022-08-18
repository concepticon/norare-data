def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'Medler-2005.tsv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=False
    )
