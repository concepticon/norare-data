def download(dataset):
    dataset.download_file(
        'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-015-0700-2/MediaObjects/13428_2015_700_MOESM1_ESM.csv',
    )


def map(dataset, concepticon, mappings):    
    sheet = dataset.get_csv('13428_2015_700_MOESM1_ESM.csv', delimiter=",", dicts=True,
            coding='cp1252')
    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )

