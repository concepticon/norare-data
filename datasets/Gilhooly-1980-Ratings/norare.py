def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'Gilhooly-1980.tsv',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=False
    )
