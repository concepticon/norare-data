import ssl
from urllib.request import urlopen, Request

def download(dataset):
    url = 'https://www.saifmohammad.com/WebDocs/bwsvsrs/RS-scores.txt'

    save_dir = dataset.raw_dir
    save_dir.mkdir(parents=True, exist_ok=True)
    file_path = save_dir / 'RS-scores.txt'

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4

    req = Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Accept': 'text/plain, text/html, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'identity'
        }
    )

    with urlopen(req, context=ctx) as resp:
        content = resp.read()

    with open(file_path, 'wb') as f:
        f.write(content)


def map(dataset, concepticon, mappings):
    rows = dataset.get_csv(
        'RS-scores.txt',
        delimiter='\t',
        dicts=False
    )

    valid_fields = ['WORD', 'VALENCE']
    sheet = []

    for row in rows:
        sheet.append(dict(zip(valid_fields, row[:2])))

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )
