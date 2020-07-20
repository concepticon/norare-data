# Database of Cross-Linguistic Norms, Ratings, and Relations for Words and Concepts

## Installation of the database

### Get started

We recommend using your terminal to carry out the following instructions. Depending on your preferences, you might also want to install a [virtual environment](https://docs.python.org/3/tutorial/venv.html). For the installation, you need GIT and Python (version 3) on your system.

### Install pynorare

The NoRaRe database uses a Python package called `pynorare`. It can be installed with [PyPi](https://pypi.org/project/pynorare/). Use either `pip` or `pip3`.

```
$ pip install pynorare
```

### Clone norare-data GIT repository

To access the NoRaRe data sets, you need to clone the `norare-data` GIT repository into a folder of your choice. Navigate or create a folder where you want to store the `norare-data` repository.

```
$ mkdir PATH/TO/NAME-NEW-FOLDER
```
or
```
$ cd PATH/TO/FOLDER
```
Clone the repository by typing:

```
$ git clone https://github.com/concepticon/norare-data.git
```

### Commands

To check if the installation worked and see the available commands of the `pynorare` package, type:

```
$ norare
```

### Set up Concepticon

The NoRaRe database is linked to [Concepticon](https://concepticon.clld.org/). To access all data sets and perform the mapping of your own data, you need to install `pyconcepticon` and download the `concepticon-data` GIT repository.

```
$ pip install pyconcepticon
```

Clone the package.

```
$ git clone https://github.com/concepticon/concepticon-data.git
```

To make your live easier, you should define the default path to concepticon-data in a `catalog.ini` file. Otherwise you need to use the `--repos` argument in combination with `norare` commands.

Open a file in the terminal text editor.

For Mac users:

```
nano /Users/YOURNAME/Library/Application\ Support/cldf/catalog.ini
```

For Linux users:

```
$ nano /home/USER/.config/cldf/catalog.ini
```

Insert the following lines to the text file.

```
[clones]
concepticon = /PATH/TO/concepticon-data 
```

Exit with `CTRL + X` and save the file by typing `y` and then press `Enter`.


## List NoRaRe data sets

To see all available data sets, navigate into the `norare-data` folder and type:

```
$ norare ls
```

## Download a NoRaRe data set

By typing the following command, the original data set will be downloaded into the `raw` folder. It is only locally stored.

```
$ norare download Abdaoui-2017-EmoLex
```

## Mapping procedure

### Create a map.py file

You need to derive a dataset first:

```python
from pynorare.dataset import NormDataSet
class Dataset(NormDataSet):
    id = "Author-Year-Keyword"
    ...
```

Note that the `id` is important, as it will determine the name of your file.

Then you can define a download function for this dataset:

```python

    def download(self):
        ....
```

Note that there different options how data sets are usually stored. Use either `self.download_file` or `self.download_zip` after you defined the function.

After that, you define a `map` function:

```python
    def map(self, write_file=True):
        ....
```

Data sets are often stored in different file formats. To define the sheet, change the following line according to the file format of your target data set. Use either `.get_excel` or `.get_csv` for text files. 

```python
    sheet = self.get_excel('DATASET.xlsx', 0, dicts=True)
```

If the data comes in a straightforward structure with table headers in the first row, you only need to define the mappings depending on the language of the words in your data set.

```python
    self.extract_data(
                sheet,
                gloss='ENGLISH',
                language='en'
                )
```

### Create a metadata.json file

The metadata file is meant to provide additional information to your data set. It is also used to define the column names. For a comprehensive description of the possible namespace terms see the [CSVW](https://www.w3.org/ns/csvw) documentation. You can also follow the standards of the metadata.json files for other data sets. Note that you can specify the old `"titles"` and new column names with `"name"` as follows:

```
          {
            "name": "ENGLISH",
            "datatype": "string",
            "titles": "word"
          }, 
```

Indicate the data `"datatype"` of each column:  `integer`, `float`, `string`.

Don't forget to add the Conceticon columns:

```
          {
            "name": "CONCEPTICON_ID",
            "datatype": "integer"
          }, 
          {
            "name": "CONCEPTICON_GLOSS",
            "datatype": "string"
          } 
```

### Download and map

Make sure that you have stored the map.py and metadata.json files according to the schema provided for the other data sets and created a `raw` folder in your data set folder. If you are not already, navigate to the `norare-data` folder and type the following commands into your terminal:

```
$ norare download YOUR-DATASET-ID
$ norare map YOUR-DATASET-ID
```

The raw file should be stored in the `raw` folder and a new .tsv should occur in your data set folder.

### Validate

You can validate your data set by typing:

```
$ norare validate YOUR-DATASET-ID
```
