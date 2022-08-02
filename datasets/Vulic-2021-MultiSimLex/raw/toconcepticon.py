from collections import OrderedDict, defaultdict
from csvw.dsv import UnicodeDictReader

# read simlex data 
scores, simlex, conc = {}, {}, {}

with UnicodeDictReader('scores.csv') as reader:
    for row in reader:
        scores[row['ID']] = row
with UnicodeDictReader('translation.csv') as reader:
    for row in reader:
        simlex[row['ID']] = row

# read our data and merge those entries into the same gloss which have the same
# concepticon ID
mappings = defaultdict(list)
visited = set()
wrong_translations = []
with UnicodeDictReader('simlex-concepticon.tsv', delimiter="\t") as reader:
    for row in reader:
        for idx in row['SIMLEX_IDS'].split():
            conc[row['NUMBER']] = row
        idxs = row['SIMLEX_IDS'].split()
        for idx in idxs:
            if idx.endswith('1'):
                idx = idx[:-1]+'2'
            else:
                idx = idx[:-1]+'1'
            conc[idx] = row
        if row['CONCEPTICON_ID'].strip():
            gloss = row['CONCEPTICON_ID']+'/'+row['CONCEPTICON_GLOSS']
            gloss += '/'+row['GLOSS']
            visited.add(row['GLOSS'])
        else:
            gloss = row['GLOSS']
            if gloss in visited:
                for i in range(1, 20):
                    new_gloss = gloss+"_{0}".format(i)
                    if new_gloss not in visited:
                        visited.add(new_gloss)
                        gloss = new_gloss
                        break
        for idx in idxs:
            idxA, idxB = idx.split(':')
            mappings[gloss] += [(idxA, str(int(idxB)+1))]

for m in mappings:
    if m.split('_')[-1].isdigit():
        print(m)

# define the languages
languages = ["ENG", "ARA", "CMN", "CYM", "EST", "FIN", "FRA", "HEB", "POL",
        "RUS", "SPA", "YUE"]

# check if translations follow the rule
check = defaultdict(set)
for row in simlex.values():
    eng1, eng2 = row['ENG 1'], row['ENG 2']
    for lng in languages:
        w1, w2 = row[lng+' 1'], row[lng+' 2']
        check[w1, lng].add(eng1)
        check[w2, lng].add(eng2)
for lng in languages:
    for (w, l), engs in check.items():
        if l == lng:
            if len(engs) > 1:
                print(lng, w, ' '.join(engs))
input()


table = [[
        "NUMBER",
        "GLOSS",
        "POS",
        "CONCEPTICON_ID",
        "CONCEPTICON_GLOSS",
        "SIMLEX_IDS",
        "SIMLEX_GLOSSES",
        "LINKS",
        "ENGLISH",
        "ARABIC",
        "MANDARIN",
        "WELSH",
        "ESTONIAN",
        "FINNISH",
        "FRENCH",
        "HEBREW",
        "POLISH",
        "RUSSIAN",
        "SPANISH",
        "CANTONESE", 
        "ENGLISH_IN_SOURCE",
        "ARABIC_IN_SOURCE",
        "MANDARIN_IN_SOURCE",
        "WELSH_IN_SOURCE",
        "ESTONIAN_IN_SOURCE",
        "FINNISH_IN_SOURCE",
        "FRENCH_IN_SOURCE",
        "HEBREW_IN_SOURCE",
        "POLISH_IN_SOURCE",
        "RUSSIAN_IN_SOURCE",
        "SPANISH_IN_SOURCE",
        "CANTONESE_IN_SOURCE", 
        "ENGLISH_SCORE",
        "ARABIC_SCORE",
        "MANDARIN_SCORE",
        "WELSH_SCORE",
        "ESTONIAN_SCORE",
        "FINNISH_SCORE",
        "FRENCH_SCORE",
        "HEBREW_SCORE",
        "POLISH_SCORE",
        "RUSSIAN_SCORE",
        "SPANISH_SCORE",
        "CANTONESE_SCORE",
        "MANDARIN_ERRATUM",
        "FRENCH_ERRATUM",
        "RUSSIAN_ERRATUM",
        "SPANISH_ERRATUM"
        ]]
for i, (mapping, idxs) in enumerate(sorted(mappings.items())):
    # retrieve the values per language
    #print(mapping)
    entries = {lng: [] for lng in languages}
    glosses = []
    for idxA, idxB in idxs:
        if idxB == "1":
            glidx = "2"
        else:
            glidx = "1"
        glosses += [simlex[idxA]['ENG '+glidx]]
        for lng in languages:
            entries[lng] += [simlex[idxA][lng+' '+idxB]]

    if '/' in mapping:
        cid, cgl, gloss = mapping.split('/')
    else:
        cid, cgl, gloss = "", "", mapping

    pos = set([simlex[idx[0]]['PoS'] for idx in idxs])
    if len(pos) != 1:
        print(mapping, pos)
        input()
        pos = ' '.join(pos)
    else:
        pos = pos.pop()
    
    row = [
        str(i+1),
        mapping.split('/')[-1],
        pos,
        cid,
        cgl,
        ' '.join(['{0}:{1}'.format(idxA, idxB) for idxA, idxB in idxs]),
        ' '.join(glosses),
        "", # leave links empty at first
        ]
    for lng in languages:
        all_glosses = sorted(
                set(entries[lng]), 
                key=lambda x: entries[lng].count(x), 
                reverse=True
                )
        new_gloss = all_glosses[0]
        if len(all_glosses) > 1:
            new_gloss += ' ('+'/'.join(all_glosses[1:])+')'
        row += [new_gloss]
    for lng in languages:
        row += [' '.join(entries[lng])]
    for lng in languages:
        # get the score
        row += [" ".join([scores[idx[0]][lng] for idx in idxs])]

    for lng in ["MANDARIN", "FRENCH", "RUSSIAN", "SPANISH"]:
        notes = ['0' for x in idxs]
        for j, (idxA, idxB) in enumerate(idxs):
            if conc[idxA+':'+idxB][lng].startswith('!'):
                notes[j] = '1'
        row += [' '.join(notes)]

    table += [row]

# infer the links
M = {}
for row in table[1:]:
    for idx in row[5].split():
        M[idx] = row[0]

for row in table[1:]:
    num = row[1]
    idxs = row[5].split()
    links = []
    for idx in idxs:
        # invert index
        if idx.endswith('1'):
            idxB = idx[:-1]+'2'
        elif idx.endswith('2'):
            idxB = idx[:-1]+'1'
        links += [M[idxB]]
    row[7] = ' '.join(links)

with open('Simlex-2021-2240.tsv', 'w') as f:
    for row in table:
        f.write('\t'.join(row)+'\n')


