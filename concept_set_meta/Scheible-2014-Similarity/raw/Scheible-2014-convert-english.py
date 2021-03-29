from csvw.dsv import UnicodeDictReader
from collections import defaultdict, OrderedDict
from pysen.glosses import to_concepticon


data = defaultdict(list)
with UnicodeDictReader("exp-ratings-EN.csv", delimiter=" ") as reader:
    for i, row in enumerate(reader):
        w1, w2 = row["Target"], row["Relatum"]
        # we add the row to the data
        data[w1] += [(i+1, row["Pair"].replace(' ', '-'), 0, w2, row)]
        data[w2] += [(i+1, row["Pair"].replace(' ', '-'), 1, w1, row)]

# pos converter
poses = {
        "ADJ": "adjective",
        "NOUN": "noun",
        "VERB": "verb"
        }

# we need to get the sorted words to be able to number them
numbered = OrderedDict([(y, x+1) for x, y in enumerate(sorted(data))])

with open('Scheible-2014.tsv', 'w') as f:
    f.write(
            '\t'.join([
                "NUMBER",
                "ENGLISH",
                "POS",
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "IDS_IN_SOURCE",
                "LINKS",
                "POLYSEMY_CLASS",
                "FREQUENCY_CLASS",
                "DEGREE_CLASS",
                "RELATION_TYPE",
                "FORWARD_SCORES",
                "BACKWARD_SCORES",
                ])+"\n")
    # iterate over dat anow
    for word, number in numbered.items():
        values = data[word]
        indices = " ".join(["{0}:{1}:{2}".format(
            x[0], x[1], x[2]) for x in values])
        links, forwards, backwards, reltypes, polysemyclass, frequencyclass, degreeclass = [], [], [], [], [], [], []
        for idx, pair, pos, wordB, row in values:
            if pos == 0:
                link = "→"
            else:
                link = "←"
            links += [link+str(numbered[wordB])]
            forwards += [row['Forward']]
            backwards += [row['Backward']]
            reltypes += [row['Relation']]
            polysemyclass += [row['Polisemy']]
            frequencyclass += [row['Frequency']]
            degreeclass += [row['Degree']]
        pos = [value[-1]['Pos'] for value in values]
        pos = poses[sorted(pos, key=lambda x: pos.count(x), reverse=True)[0]]

        # entsprechend für FREQ und DEGREE und WN (=wordnet?)
        freq = [] # ... wie bei pos        
        

        maps = to_concepticon([{"gloss": word, "pos": pos}])[word]
        if maps:
            maps = maps[0]
        else:
            maps = ["", ""]

        f.write("\t".join([
            str(number),
            str(word),
            pos,
            maps[0],
            maps[1],
            indices,
            " ".join(links),
            ' '.join(polysemyclass),
            ' '.join(frequencyclass),
            ' '.join(degreeclass),
            ' '.join(reltypes),
            ' '.join(forwards),
            ' '.join(backwards)
            ])+'\n'
            )
