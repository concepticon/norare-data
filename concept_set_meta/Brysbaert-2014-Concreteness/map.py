from pynorare.dataset import NormDataSet

class Dataset(NormDataSet):
    id = 'Brysbaert-2014-Concreteness'

    def download(self):
        self.download_file(
        'http://crr.ugent.be/papers/Concreteness_ratings_Brysbaert_et_al_BRM.txt',
        'brysbaert_concreteness.tsv'
        )

    def map(self, write_file=True):
        
        # for comparison with part of speech
        remap = {
                'Noun': 'Person/Thing',
                'Adjective': 'Property',
                'Verb': 'Action/Process',
                'Adverb': 'Other',
                'Article': 'Other',
                'Conjunction': 'Other',
                'Determiner': "Other",
                'Ex': "Other",
                '#N/A': 'Other',
                "Interjection": "Other",
                "Name": "Person/Thing",
                "Preposition": "Other",
                "To": "Other",
                "Number": "Number",
                "Pronoun": "Other",
                "Not": "Other",
                }

        # get the data
        sheet = self.get_csv('brysbaert_concreteness.tsv')

        # get data and map them if possible
        for i in range(0, len(sheet)):
            (gloss, bigram, concm, concsd, dunno, total, percknown, subtl, pos
                    ) = list(sheet[i].values())

            if gloss in self.mappings['en']:
                best_matches = self.mappings['en'][gloss]
                all_best_match, all_best_priority = False, False
                j = 0
                while j < len(best_matches):
                    cid, priority, concepticon_pos = best_matches[j]
                    if remap[pos] == concepticon_pos:
                        all_best_match = cid
                        all_best_priority = priority
                        break
                    j += 1
                if not all_best_match:
                    all_best_match, all_best_priority, _ = best_matches[0]
                self.mapped[all_best_match] += [[ 
                    str(i), 
                    gloss, 
                    '{0}'.format(concm),
                    '{0}'.format(concsd),
                    '{0}'.format(dunno),
                    '{0}'.format(subtl),
                    '{0}'.format(pos),
                    all_best_match, 
                    all_best_priority]]
        
        header = ["CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "ENGLISH",
                "CONCRETENESS_MEAN",
                "CONCRETENESS_SD",
                "DUNNO",
                "FREQUENCY_SUBTITLE",
                "POS",
                "LINE_IN_SOURCE"]
        table = []
        for key, lines in self.mapped.items(): 
            best_line = sorted(lines, key=lambda x: (x[-1], x[-2]))[0] 
            best_line[-1] = str(best_line[-1]) 
            table += [[
                best_line[-2], # concepticon id
                self.concepticon.conceptsets[best_line[-2]].gloss,
                best_line[1],
                best_line[2], 
                best_line[3],
                best_line[4],
                best_line[5],
                best_line[6],
                best_line[0]
                ]]
        self._table = table
        self._header = header
        if write_file:
            self.writefile()

