def download(dataset):
    dataset.download_file(
        'https://osf.io/download/63y8w/',
        'sensorimotor dataset.xlsx',
    )

def map(dataset, concepticon, mappings):
    sheet_list = dataset.get_excel('sensorimotor dataset.xlsx', 1, dicts=False)

    # Define the column names as valid fields, avoid duplicates
    valid_fields = [
        'Ita_Word', 'WordClass', 'Let_ITA', 'FreqColfis', 'Ln_Colfis', 'FreqRepub', 'Ln_FreqRep', 
        'N_OrtNeig', 'MeanFreq_Neig', 'N_Part_p', 'M_Fam', 'SD_Fam', 'M_Ima', 'SD_Ima', 
        'M_Con', 'SD_Con', 'N_Part_a', 'M_Val', 'SD_Val', 'M_Aro', 'SD_Aro', 'M_Dom', 'SD_Dom', 
        'N_Part1', 'M_head', 'SD_head', 'M_foot/leg', 'SD_foot/leg', 'M_hand/arm', 'SD_hand/arm', 
        'M_mouth/throat', 'SD_mouth/throat', 'M_torso', 'SD_torso', 'N_Part2', 'M_int', 'SD_int', 
        'M_taste', 'SD_taste', 'M_smell', 'SD_smell', 'M_touch', 'SD_touch', 'M_audition', 
        'SD_audition', 'M_vision', 'SD_vision', 'Max_strength.action', 'Exclusivity.action', 
        'Dominant.action', 'Max_strength.perceptual', 'Exclusivity.perceptual', 'Dominant.perceptual', 
        'Max_strength.sensorimotor', 'Exclusivity.sensorimotor', 'Dominant.sensorimotor'
    ]

    sheet = []
    for row in sheet_list[2:]:
        sheet += [dict(zip(valid_fields, row[:len(valid_fields)]))]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ITALIAN',
        language='it',
        pos=True,
        pos_mapper = {
            'n': 'Person/Thing',
            'v': 'Action/Process'},
            pos_name = "ITALIAN_POS"
    )
