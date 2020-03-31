from pynorare.data import NormDataSet, download_zip, get_excel
from pynorare.util import progressbar
from sys import argv

class Dataset(NormDataSet):

    id = "Brysbaert-2009-Freq"

    def download(self):
        download_zip(
            'https://static-content.springer.com/esm/art%3A10.3758%2FBRM.41.4.977/MediaObjects/Brysbaert-BRM-2009.zip',
            'brysbaert_freq',
            'Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx',
        )

    def map(self):
        
        sheet = get_excel('Brysbaert-BRM-2009/SUBTLEXusExcel2007.xlsx', 0)
        
        # map the data
        # get data and map them if possible
        for i, (gloss, freqcount, cdcount, freqlow, cdlow, subwf, lg10wf, subcd,
                lg10cd) in progressbar(enumerate(sheet)):
            if gloss in self.mappings['en']: 
                best_match, priority, pos = self.mappings['en'][gloss][0] 
                self.mapped[best_match] += [[ 
                    str(i), 
                    gloss, 
                    str(freqcount),
                    str(cdcount),
                    str(freqlow),
                    str(cdlow),
                    '{0:.2f}'.format(subwf),
                    '{0:.2f}'.format(lg10wf),
                    '{0:.2f}'.format(subcd),
                    '{0:.2f}'.format(lg10cd),
                    best_match, 
                    priority]]
        
        header = [
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "ENGLISH",
                "FREQUENCY_COUNT",
                "CD_COUNT",
                "SUBTITLE_FREQUENCY",
                "SUBTITLE_CD",
                "LG10_FREQUENCY",
                "LG10_CD",
                "LINE_IN_SOURCE"]
        table = []
        for key, lines in progressbar(self.mapped.items()): 
            best_line = sorted(lines, key=lambda x: (x[-1], x[-2]))[0] 
            best_line[-1] = str(best_line[-1]) 
            table += [[
                best_line[-2], # concepticon id
                self.concepticon.conceptsets[best_line[-2]].gloss,
                best_line[1],
                str(int(float(best_line[2]))), 
                str(int(float(best_line[3]))),
                best_line[6],
                best_line[8],
                best_line[7],
                best_line[9],
                best_line[0]
                ]]
        self.writefile(header, table)
        
if __name__ == '__main__':
    Dataset().run(argv)
