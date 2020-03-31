# Database of Cross-Linguistic Norms, Ratings, and Relations for Words and Concepts

## Installation of the Python code

```
$ git clone https://github.com/lingpy/pynorare/
$ cd pynorare
$ python setup.py develop
```

## Downloading data for a given dataset (only local)

```
$ cd concept_set_meta/Brysbaert-2014-Concreteness/
$ python map.py download
```

## Running the mapping algorithm and checking the data

```
$ python map.py map validate
```

## Mapping procedure

You need to derive a dataset first:

```python
from pynorare.data import NormDataSet
class Dataset(NormDataSet):
    ...
```

Then you can define a download command for this dataset:

```python

    def download(self):
        ....
```

Then, you define a `map` command:

```python
    def map(self):
        ....
```

If you derive a new `Dataset` from a `NormDataSet`, you have automatically data loaded from Concepticon which you can use (`self.mappings`). The mapping is often individual, so you should study what we do so far. But we tend to store the mappings we find in a given dataset in the attribute `self.mapped`. 

To write your data to file, create a `header` and the `table` and then use this command:

```python
        self.writefile(header, table)
```

To have the code executed when typing `python map.py`, add this line to your script:

```python
if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)
```




## Note

Current checks are not yet fully functional, but will be added soon.
