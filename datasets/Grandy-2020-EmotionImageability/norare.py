def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-019-01294-2/MediaObjects/13428_2019_1294_MOESM1_ESM.dat',
        '13428_2019_1294_MOESM1_ESM.dat'
    )

def map(dataset, concepticon, mappings):
    dataset.extract_data(
        dataset.get_csv('13428_2019_1294_MOESM1_ESM.dat', '\t', dicts=True),
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de'
    )