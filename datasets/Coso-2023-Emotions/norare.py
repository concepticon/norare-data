import ssl
from urllib.request import urlopen, Request
from pathlib import Path

def download(dataset):
    URL = "https://ndownloader.figshare.com/files/36434421"
    FILE_NAME = "CROWD-5e.xlsx"

    save_dir = Path(__file__).resolve().parent / "raw"
    save_dir.mkdir(parents=True, exist_ok=True)

    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4 

    req = Request(URL, headers={"User-Agent": "Mozilla/5.0"})

    with urlopen(req, context=ctx) as resp:
        content = resp.read()

    file_path = save_dir / FILE_NAME

    with open(file_path, "wb") as f:
        f.write(content)

def map(dataset, concepticon, mappings):   
    sheet_list = dataset.get_excel('CROWD-5e.xlsx', 1, dicts=False)
    sheet = [dict(zip(sheet_list[0], row)) for row in sheet_list[1:]] 

    dataset.extract_data(
        sheet,
        concepticon,
        mappings,
        gloss='ENGLISH',
        language='en'
    )