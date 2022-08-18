def download(dataset):
    dataset.download_file(
        'https://www.researchgate.net/profile/Maria_Gonzalez-Nosti/publication/330281146_Appendix_1_Reaction_times/data/5c371ceca6fdccd6b5a0a3a0/Appendix.xls?_sg%5B0%5D=9brm3_nSenyo0v5p_j3REncrW4fuKLhLd6TWXKk7LJP_IClPjY4U68j_CI5_tHJnS8COO0YKCEf6AX3W6RftTQ.Hp2gZucbHQayDs7udNwuhC-92A-GoHUlLisH6yOB76uV9c6kMC9pl3YYSHY_gks_UGo1ZBojhNwdYfU8RddADg&_sg%5B1%5D=7lOvlVEKZpfdzojGnoWeMVEMv_q-j2YGUMhhmUyGovANFyEI7EYb7yXHsnrCpdIyavyRoX7jwvXlsxMKHJTExqLp85TV0vltwLTLHj90vRYL.Hp2gZucbHQayDs7udNwuhC-92A-GoHUlLisH6yOB76uV9c6kMC9pl3YYSHY_gks_UGo1ZBojhNwdYfU8RddADg&_iepl=',
        'Appendix.xls',
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Appendix.xls',
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )
