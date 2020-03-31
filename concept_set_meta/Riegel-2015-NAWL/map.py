from pynorare.data import NormDataSet, download_file, get_excel


class Dataset(NormDataSet):
    
    id = "Riegel-2015-NAWL"

    def download(self):
        download_file(
            'https://static-content.springer.com/esm/art%3A10.3758%2Fs13428-014-0552-1/MediaObjects/13428_2014_552_MOESM1_ESM.xlsx',
            'riegel.xlsx'
            )

    def map(self):

        sheet = get_excel('riegel.xlsx', 0)

        # modify mappings
        for m in list(self.mappings['de']):
            if m.lower() not in self.mappings['de']:
                self.mappings['de'][m.lower()] = self.mappings['de'][m]

        # get data and map them if possible
        for i, line in enumerate(sheet[1:]):
            german, polish = line[1], line[2]
            valm, valmf, valma = line[6], line[7], line[8]
            arom, aromf, aroma = line[12], line[13], line[14]
            imam, imamf, imama = line[18], line[19], line[20]

            if german in self.mappings['de']: 
                best_match, priority, pos = self.mappings['de'][german][0]
                self.mapped[best_match] += [[ 
                    line[0], # indicated as number here
                    polish,
                    german,
                    '{0:.2f}'.format(valm),
                    '{0:.2f}'.format(valmf),
                    '{0:.2f}'.format(valma),
                    '{0:.2f}'.format(arom),
                    '{0:.2f}'.format(aromf),
                    '{0:.2f}'.format(aroma),
                    '{0:.2f}'.format(imam),
                    '{0:.2f}'.format(imamf),
                    '{0:.2f}'.format(imama),
                    line[27], # suptlex frequency
                    line[28],
                    best_match, 
                    priority]]

        header = [
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "POLISH",
                "GERMAN",
                "VALENCY_MEAN_MEN",
                "VALENCY_MEAN_WOMEN",
                "VALENCY_MEAN_ALL",
                "AROUSAL_MEAN_MEN",
                "AROUSAL_MEAN_WOMEN",
                "AROUSAL_MEAN_ALL",
                "IMAGEABILITY_MEAN_MEN",
                "IMAGEABILITY_MEAN_WOMEN",
                "IMAGEABILITY_MEAN_ALL",
                "POLISH_FREQUENCY",
                "POLISH_FREQUENCY_CD",
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
                best_line[7],
                best_line[8],
                best_line[9],
                best_line[10],
                best_line[11],
                str(int(float(best_line[12]))) if best_line[12] else "NaN",
                str(int(float(best_line[13]))) if best_line[13] else "NaN",
                str(int(float(best_line[0])))
                ]]
        self.writefile(header, table)

        
if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)
