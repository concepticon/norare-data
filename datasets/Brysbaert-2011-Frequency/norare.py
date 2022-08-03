def download(dataset):
    dataset.download_zip(
        'http://crr.ugent.be/SUBTLEX-DE/SUBTLEX-DE%20cleaned%20with%20Google00%20frequencies.zip',
        'brysbaert_freq_de.zip',
        'SUBTLEX-DE cleaned with Google00 frequencies.xlsx'
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'SUBTLEX-DE cleaned with Google00 frequencies.xlsx',
        concepticon,
        mappings,
        gloss='GERMAN',
        language='de'
    )
