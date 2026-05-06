import ssl
from urllib.request import urlopen, Request
from pathlib import Path

def download(dataset):
    URL = "https://ndownloader.figshare.com/files/38169297"
    FILE_NAME = "Norms for 9,000 Spanish words in seven discrete positive emotions.csv"

    save_dir = Path(__file__).resolve().parent / "raw"
    save_dir.mkdir(parents=True, exist_ok=True)

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # keep your existing SSL setting

    # IMPORTANT: add browser header + Request wrapper
    req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(req, context=ctx) as resp:
        content = resp.read()

    file_path = save_dir / FILE_NAME

    with open(file_path, "wb") as f:
        f.write(content)

def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        dataset.get_csv('Norms for 9,000 Spanish words in seven discrete positive emotions.csv', delimiter=";"),
        concepticon,
        mappings,
        gloss='SPANISH',
        language='es'
    )    