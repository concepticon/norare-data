def download(dataset):
    dataset.download_file(
        'https://osf.io/download/qazjk/',
        'Full list GPT4 estimates familiarity and Multilex frequencies.xlsx'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'Full list GPT4 estimates familiarity and Multilex frequencies.xlsx',
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )