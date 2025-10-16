# Handling `.rar` Files
The data for this particular dataset was available in a `.rar` format which requires special treatment: since `.rar` files are not supported by Python’s standard library, the usual automated download and extraction workflow will not work directly. A separate unpacking tool must be installed and configured locally.
The steps described below can aid in replicating this special workflow.


*Install an unpacking tool*
Install a tool to unpack rar files (like UnRAR for Windows by rarlab https://www.rarlab.com/rar_add.htm)
Note the path, for example:
```
C:\Users\mirah\Downloads\unrar.exe
```

*Install the Python package `rarfile` in the console*
```
pip install rarfile
```

*Import rarfile and specify the tool path in `norare.py`*
```python
import rarfile
rarfile.UNRAR_TOOL = r"C:\Users\mirah\Downloads\unrar.exe"
```

*Treat the archive like you would a `.zip` but specify the archive class in the download command so that Python knows it's dealing with a `.rar` instead of a `.zip`*
```python
def download(dataset):
    dataset.download_zip(
        'https://ndownloader.figstatic.com/files/23311322',
        'Concretenss Ratings of 9877 Two Character Chinese Words.rar',
        'Concretenss Ratings of 9877 Two Character Chinese Words.xlsx',
        cls=rarfile.RarFile,
    )
```

The `map` command works the same it usually does.