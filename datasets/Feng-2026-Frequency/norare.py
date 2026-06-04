from pathlib import Path

def download(dataset):
    import requests

    url = "https://download.scidb.cn/download?fileId=98b1ae34121c0872d03f9fdb81dbc5af&path=/V3/CPCSLD%20Lexical%20Database/Words_all.xlsx&shortLink=Vb6vIb&fileName=Words_all.xlsx"

    raw_dir = Path.cwd() / "datasets" / "Feng-2026-Frequency" / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    filename = raw_dir / "Words_all.xlsx"

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

def map(dataset, concepticon, mappings):

    sheet = dataset.get_excel(
        "Words_all.xlsx", 0, dicts=True
    )

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh',
        pos=True,
        pos_mapper={
            'VV': 'Action/Process',
            'VE': 'Action/Process',
            'VC': 'Action/Process',
            'VA': 'Property',

            'NN': 'Person/Thing',
            'NR': 'Person/Thing',
            'NT': 'Person/Thing',

            'CD': 'Number',
            'M': 'Classifier',

            'AD': 'Other',
            'DT': 'Other',
            'P': 'Other',
            'CC': 'Other',
            'CS': 'Other',
            'SP': 'Other',
            'AS': 'Other',
            'DEC': 'Other',
            'BA': 'Other',
            'LC': 'Other',
            'IJ': 'Other',
            'OD': 'Other'
        },
        pos_name="CHINESE_POS"
    )