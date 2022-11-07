# Database of Cross-Linguistic Norms, Ratings, and Relations for Words and Concepts

## Installation of the database

### Get started

We recommend using your terminal to carry out the following instructions. We (strongly) advise you to install a [virtual environment](https://docs.python.org/3/tutorial/venv.html). In addition, you need GIT and Python (version 3) on your system.

### Install pynorare

The NoRaRe database uses a Python package called `pynorare` for data curation (as a dependency `pyconcepticon` will be installed automatically). 
The Python package can be installed from [PyPi](https://pypi.org/project/pynorare/).

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

### Clone concepticon-data GIT repository

The NoRaRe database is linked to [Concepticon](https://concepticon.clld.org/). To access all data sets and perform the mapping of your own data, you need to download the `concepticon-data` GIT repository.

```
$ git clone https://github.com/concepticon/concepticon-data.git
```

## Commands

To check if the installation worked and see the available commands of the `pynorare` package, type:

```
$ norare
```

### Show NoRaRe statistics

For example, you can get statistic of the distribution of the Concepticon identifiers by typing the following command. Note that you should add the path to a specific clone of concepticon-data, because you are not within the root of the concepticon-data. The same is possible for the norare-data repository if you are working with multiple clones. You can also use the `catalog.ini` file to specify the path (see 'Define repository paths' section).

```
$ norare --repos=/PATH/TO/concepticon-data --norarepo=/PATH/TO/norare-data stats
```

### List NoRaRe data sets

To see all available data sets, navigate into the `norare-data` folder and type:

```
$ norare --repos=/PATH/TO/concepticon-data ls
```

### Download a NoRaRe data set

By typing the following command, the original data set will be downloaded into the `raw` folder. It is only locally stored.

```
$ norare --repos=/PATH/TO/concepticon-data download Abdaoui-2017-EmoLex
```

### Define repository paths

To make your live easier, you can define the default path to concepticon-data in a `catalog.ini` file (Linux users can follow the desciption in this [blog post](https://calc.hypotheses.org/2225)).

For Mac users: Open the `catalog.ini` file in a text editor of your choice and add the following lines.  

```
[clones]
concepticon = /PATH/TO/concepticon-data 
```

If you can't find the `catalog.ini` file, create a directory `mkdir /Users/YOURNAME/Library/Application\ Support/cldf/` and add it to the `cldf` folder.


## Mapping procedure

"Mapping a dataset" refers to the process of mapping the words or concepts described in a dataset to Concepticon's
concept sets and extracting associated norms, ratings or relations from a dataset's "raw" data.

This is facilitated with small Python modules (one per dataset), located at `datasets/<dataset-ID>/norare.py`. These
python modules may provide two functions, `download` and `map` with signatures as shown below, which will be called
when the respective command is run with `norare`.

```python
def download(dataset: pynorare.api.Dataset):
    """use methods of `dataset` to download or manipulate data"""

def map(dataset: pynorare.api.Dataset, concepticon: pyconcepticon.Concepticon, mappings: dict):
    """eventually call `dataset.extract_data` to write the extracted data to files."""
```


### Create a metadata.json file

The metadata file is meant to provide additional information to your data set. It is also used to define the column names. 
For a comprehensive description of the possible namespace terms see the [CSVW](https://www.w3.org/ns/csvw) documentation. 
You can also follow the standards of the metadata.json files for other data sets. Note that you can specify the old 
`"titles"` and new column names with `"name"` as follows:

```json
          {
            "name": "ENGLISH",
            "datatype": "string",
            "titles": "word"
          }
```

Indicate the data `"datatype"` of each column:  `integer`, `float`, `string`.

Don't forget to add the Concepticon columns:

```json
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

Make sure that you have stored the `norare.py` and `<YOUR-DATASET-ID>.tsv-metadata.json` files and created a `raw` folder in your data set folder. If you are ready, navigate to the 
`norare-data` folder and type the following commands into your terminal:

```
$ norare download YOUR-DATASET-ID
$ norare map YOUR-DATASET-ID
```

The raw file should be stored in the `raw` folder and a new `<YOUR-DATASET-ID>.tsv` should occur in your data set folder.


### Validate

You can validate your data set by typing:

```
$ norare validate YOUR-DATASET-ID
```

## References

Tjuka, Annika, Robert Forkel, and Johann-Mattis List. 2022. Linking Norms, Ratings, and Relations of Words and Concepts Across Multiple Language Varieties. _Behavior Research Methods_ 54. 864–884. https://doi.org/10.3758/s13428-021-01650-1.

Tjuka, Annika. “Adding Data Sets to NoRaRe: A Guide for Beginners,” in _Computer-Assisted Language Comparison in Practice_, 11/08/2021, https://calc.hypotheses.org/2890.

Tjuka, Annika. “Comparing NoRaRe Data Sets: Calculation of Correlations and Creation of Plots in R,” in _Computer-Assisted Language Comparison in Practice_, 24/11/2021, https://calc.hypotheses.org/3109.
