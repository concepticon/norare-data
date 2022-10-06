def download(dataset):
    dataset.download_file(
        'https://osf.io/download/3bvdy/?view_only=c814286465dd4b119ce83bf8eb4c82fb',
        'ANEW-ITA_specificity_ratings_all_POS.csv'
    )


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'ANEW-ITA_specificity_ratings_all_POS.csv',
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            's': 'Person/Thing',
            'a': 'Property',
            'v': 'Action/Process'},
        pos_name = "ITALIAN_POS"
    )

