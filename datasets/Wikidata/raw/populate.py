from qwikidata.sparql import return_sparql_query_results
from qwikidata.linked_data_interface import get_entity_dict_from_api
from pynorare.files import get_mappings
from collections import defaultdict
from clldutils.text import strip_brackets


query = r"""
select ?lexemeId ?lemma WHERE {{
  ?lexemeId <http://purl.org/dc/terms/language> wd:Q1860;
            wikibase:lemma ?lemma.
  FILTER (regex(?lemma, '^{0}$'))
}}
"""




findings = defaultdict(list)
mappings, concepticon = get_mappings()
visited = set()

words = defaultdict(list)
for w, vals in mappings['en'].items():
    w2 = strip_brackets(w.lower().strip())
    if w2 not in words:
        words[w2] = vals[0][0]

with open('wikidata.tsv', 'r') as f:
    for line in f:
        if line.strip():
            cid = line.split('\t')[0]
            visited.add(cid)

print(len(words))
with open('fails.tsv', 'r') as f:
    for line in f:
        visited.add(line.strip())


current = ''
for idx, (word, cid) in enumerate(sorted(words.items(), key=lambda x: x[1])):
    try:
        if cid not in visited:
            visited.add(cid)
            new_query = query.format(word)
            print(len(findings))
            print('{0} ...'.format(word))
            res_ = return_sparql_query_results(new_query)
            res = res_['results']['bindings']
            for r in res:
                key = r['lexemeId']['value'].split('/')[-1]
                #print(r['lexemeId'], key)
                dct = get_entity_dict_from_api(key)
                if dct['senses']:
                    this_sense = dct['senses'][0]['glosses'].get('en', {'value': ''})['value']
                    if this_sense:
                        findings[
                                cid, 
                                concepticon.conceptsets[cid].gloss
                                ] += [(key, this_sense, word)]
                        print('... ', this_sense)
    except Exception as e:
        print(e)
    if cid != current:
        current = cid
        cgl = concepticon.conceptsets[cid].gloss
        if (cid, cgl) in findings:
            with open('wikidata.tsv', 'a') as f:
                f.write('\t'.join(['', '', '', ''])+'\n')
                this_key = ''
                for lid, dfn, word in sorted(set(findings[cid, cgl]), key=lambda x:
                        findings[cid, cgl].count(x)):
                    if lid != this_key:
                        this_key = lid
                        f.write('\t'.join([cid, cgl, word, lid, dfn])+'\n')
        else:
            with open('fails.tsv', 'a') as f:
                f.write(cid+'\n')
            
