from collections import defaultdict

from csvw.dsv import reader, UnicodeWriter
import nltk


def download(dataset):
    dataset.download_file(
        'http://compling.hss.ntu.edu.sg/omw/wn30-core-synsets.tab',
        'core-synsets.tsv',
    )
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    preprocess(dataset.raw_dir)


def map(dataset, concepticon, mappings):
    dataset.extract_data(
        'wordnet.tsv',
        concepticon,
        mappings,
        pos=True,
        pos_mapper = {
            'v': 'Action/Process',
            'n': 'Person/Thing',
            'a': 'Property'}
    )


def preprocess(d):
    from nltk.corpus import wordnet as wn

    core = [x[0] for x in reader(d / 'core-synsets.tsv')]

    def name(ss):
        return str(ss._offset).rjust(8, '0')+'-'+ss._pos

    sheet = [
        'word', 'pos', 'wordnet_id', 'nltk_name', 'hypernyms', 'hyponyms',
        'hypernym_names', 'hyponym_names', 'in_degree', 'out_degree']
    with UnicodeWriter(d / 'wordnet.tsv', delimiter='\t') as w:
        w.writerow(sheet)
        for row in core:
            ss = wn.of2ss(row)
            lemma_name = ss.lemma_names()[0]
            # get hyponyms
            hpn = []
            for h in ss.hypernyms():
                hpn += [(name(h), h._name)]
            hon = []
            for h in ss.hyponyms():
                hon += [(name(h), h._name)]
    
            w.writerow([
                lemma_name,
                ss._pos,
                row,
                ss._name,
                ';'.join([x[0] for x in hpn]),
                ';'.join([x[0] for x in hon]),
                ';'.join([x[1] for x in hpn]),
                ';'.join([x[1] for x in hon]),
                str(len(hpn)),
                str(len(hon))
            ])

