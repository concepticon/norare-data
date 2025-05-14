def download(dataset):
    dataset.download_file(
        'https://inco.grupos.uniovi.es/documents/264612/264724/Motor+content+norms+for+4%2C565+verbs+in+Spanish.+Appendix+1./26f1e90c-ca24-4005-92b7-1e05ef2680b7',
        'Motor content norms for 4,565 verbs in Spanish. Appendix 1..xlsx',
    )

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Motor content norms for 4,565 verbs in Spanish. Appendix 1..xlsx',
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )    