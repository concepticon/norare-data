from pynorare.data import NormDataSet, download_zip, get_excel
from urllib import request
from zipfile import ZipFile
from pynorare import log

class Dataset(NormDataSet):
    id = "Cai-2010-SUBTLEXCH"

    def download(self):
        
        # custom commando to mask that we are a program
        url = 'https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexch/subtlexchwf.zip/at_download/file'
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        request.urlretrieve(url, "raw/cai_frequency.zip")
        with open('raw/cai_frequency.zip', 'rb') as f:
            with ZipFile(f) as zf:
                zf.extract('SUBTLEX-CH-WF.xlsx', path='raw')
        log.download('SUBTLEX-CH-WF.xlsx')

    def map(self):
        
        sheet = get_excel('SUBTLEX-CH-WF.xlsx', 0)
        # map the data
        # get data and map them if possible
        for i in range(1, len(sheet)):
            gloss, freqcount, freqcountmill, lg10wf, cd, cdperc, logcd = sheet[i]
            if gloss in self.mappings['zh']: 
                best_match, priority, pos = self.mappings['zh'][gloss][0] 
                self.mapped[best_match] += [[ 
                    str(i), 
                    gloss, 
                    str(int(float(freqcount))),
                    str(freqcountmill),
                    '{0:.2f}'.format(lg10wf),
                    str(int(float(cd))),
                    '{0:.2f}'.format(cdperc),
                    '{0:.2f}'.format(logcd),
                    best_match, 
                    priority]]
        
        header = [
                "CONCEPTICON_ID",
                "CONCEPTICON_GLOSS",
                "CHINESE",
                "FREQUENCY_COUNT",
                "FREQUENCY_COUNT_PM",
                "LG10_FREQUENCY",
                "CD_COUNT",
                "CD_PERCENTAGE",
                "LG10_CD",
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
                best_line[0]
                ]]
        self.writefile(header, table)
        

if __name__ == '__main__':
    from sys import argv
    Dataset().run(argv)

