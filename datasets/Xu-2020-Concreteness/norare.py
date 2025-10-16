import rarfile
rarfile.UNRAR_TOOL = r"C:\Users\mirah\Downloads\unrar.exe"

def download(dataset):
    dataset.download_zip(
        'https://ndownloader.figstatic.com/files/23311322',
        'Concretenss Ratings of 9877 Two Character Chinese Words.rar',
        'Concretenss Ratings of 9877 Two Character Chinese Words.xlsx',
        cls=rarfile.RarFile,
    )


def map(dataset, concepticon, mappings):    
    dataset.extract_data(
        'Concretenss Ratings of 9877 Two Character Chinese Words.xlsx',
        concepticon,
        mappings,
        gloss='CHINESE',
        language='zh'
    )
