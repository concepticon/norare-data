
def download(dataset):
    dataset.download_file(
        'https://osf.io/download/cdu3b/',
        '2014-Montefinese_Database.xlsx'    
    )

def map(dataset, concepticon, mappings):    
    sheet_list = dataset.get_excel('2014-Montefinese_Database.xlsx', 0, dicts=False)
    sheet = []
    valid_fields = [
        'Num_ANEW', 'ANEW', 'Eng_Word', 'Ita_Word', 'WordClass', 'Let_ITA', 'FreqColfis', 'Ln_Colfis', 'FreqRepub', 'Ln_FreqRep', 'N_OrtNeig', 'MeanFreq_Neig', 'N_Part_p', 'M_Fam',
        'SD_Fam', 'M_Ima', 'SD_Ima', 'M_Con', 'SD_Con', 'N_Part_all', 'M_Val_all', 'SD_Val_all', 'M_Aro_all', 'SD_Aro_all', 'M_Dom_all', 'SD_Dom_all',
        'N_Part_f', 'M_Val_f', 'SD_Val_f', 'M_Aro_f', 'SD_Aro_f', 'M_Dom_f', 'SD_Dom_f', 'N_Part_m', 'M_Val_m', 'SD_Val_m', 'M_Aro_m', 'SD_Aro_m',
        'M_Dom_m', 'SD_Dom_m', 'df_diff', 't_Val_diff', 'p_Val_diff', 't_Aro_diff', 'p_Aro_diff', 't_Dom_diff', 'p_Dom_diff']

    for row in sheet_list[2:]:  # iterate over the lines after header
        sheet += [dict(zip(valid_fields, row[:46]))]

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en',
        pos=True,
        pos_mapper={
            's': 'Person/Thing',
            'a': 'Property',
            'a/s': 'Person/Thing',
            'v': 'Action/Process'},
        pos_name="ITALIAN_POS"
    )