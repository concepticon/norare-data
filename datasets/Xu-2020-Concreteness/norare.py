import patoolib  # this can extract RARs

def download(dataset):
    rar_path = dataset.download_file(
        'https://ndownloader.figstatic.com/files/23311322',
        'Concretenss Ratings of 9877 Two Character Chinese Words.rar'
    )
    # Extract the XLSX from the RAR into the raw folder
    patoolib.extract_archive(
        rar_path,
        outdir=str(dataset.raw_dir)
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Concretenss Ratings of 9877 Two Character Chinese Words.xlsx',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )
