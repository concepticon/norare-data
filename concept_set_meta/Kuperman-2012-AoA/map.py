from pynorare.data import download_zip, NormDataSet, get_excel

class Dataset(NormDataSet):
    id = 'Kuperman-2012-AoA'
    
    def download(self):
        download_zip(
                'http://crr.ugent.be/papers/AoA_ratings_Kuperman_et_al_BRM.zip',
                'kuperman_aoa.zip',
                filename='AoA_ratings_Kuperman_et_al_BRM.xlsx',
            )

    def map(self):
        sheet = get_excel('AoA_ratings_Kuperman_et_al_BRM.xlsx', 0)

        # iterate over data and map them
        for i in range(1, len(sheet)):
            gloss, occtot, occnum, freq, ratm, rats, dun = sheet[i] 
            if gloss in self.mappings['en']: 
                best_match, priority, pos = self.mappings['en'][gloss][0]
                self.mapped[best_match] += [[ 
                    str(i), 
                    gloss, 
                    str(int(float(occtot))),
                    str(int(float(occnum))),
                    '{0:.2f}'.format(freq),
                    '{0:.2f}'.format(ratm),
                    '{0:.2f}'.format(rats),
                    '{0:.2f}'.format(dun),
                    best_match, 
                    priority]]
        table = []
        header = [
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "ENGLISH",
                "OCCURRENCES_TOTAL",
                "OCCURRENCES_NUM",
                "FREQ_PM",
                "RATING_MEAN",
                "RATING_SD",
                "DUNNO",
                "LINE_IN_SOURCE"]

        for key, lines in self.mapped.items(): 
            best_line = sorted(lines, key=lambda x: (x[-1], x[-2]))[0] 
            best_line[-1] = str(best_line[-1]) 
            table += [[
                best_line[-2],
                self.concepticon.conceptsets[best_line[-2]].gloss,
                best_line[1],
                best_line[2], 
                best_line[3],
                best_line[4],
                best_line[5],
                best_line[6],
                best_line[7],
                best_line[0]
                ]]
        self.writefile(header, table)

if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)

