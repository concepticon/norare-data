import ssl
from urllib.request import urlopen
from pathlib import Path

def download(dataset):
    URL = 'https://inco.grupos.uniovi.es/documents/264612/264724/Motor+content+norms+for+4%2C565+verbs+in+Spanish.+Appendix+1./26f1e90c-ca24-4005-92b7-1e05ef2680b7'
    FILE_NAME = 'Motor content norms for 4,565 verbs in Spanish. Appendix 1..xlsx'

    # Construct the path to the `raw` directory relative to the script location
    save_dir = Path(__file__).resolve().parent / 'raw'

    # Ensure the directory exists
    save_dir.mkdir(parents=True, exist_ok=True)

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # Adjust SSL settings if necessary

    with urlopen(URL, context=ctx) as resp:
        content = resp.read()

    # Construct the full path where the file will be saved in the `raw` directory
    file_path = save_dir / FILE_NAME

    with open(file_path, 'wb') as f:
        f.write(content)


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Motor content norms for 4,565 verbs in Spanish. Appendix 1..xlsx',
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )    