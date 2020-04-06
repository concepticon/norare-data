from pynorare.data import NormDataSet, download_zip, get_excel


class Dataset(NormDataSet):

    def download(self):
        download_zip(
            'http://crr.ugent.be/papers/SUBTLEX-ESP.zip',
            'cuetos_freq',
            'SUBTLEX-ESP.xlsx',
        )

    def map_concepts(self):

        sheet = get_excel('SUBTLEX-ESP.xlsx', 0)

        for line in range(1, len(sheet)):
            line_list = [sheet[line][0:4], sheet[line][5:9], sheet[line][10:14]]

            for line_item in line_list:
                gloss, freqcount, freqmill, freqlog = line_item

                if gloss in self.mappings['es']:
                    best_match, priority, pos = self.mappings['es'][gloss][0]
                    self.mapped[best_match] += [[
                        str(line + 1),
                        gloss,
                        str(freqcount),
                        '{0:.2f}'.format(freqmill),
                        '{0:.2f}'.format(freqlog),
                        best_match,
                        priority]]

        with open('Cuetos-2011-Freq.tsv', 'w') as f:
            f.write('\t'.join(["CONCEPTICON_ID",
                               "CONCEPTICON_GLOSS",
                               "SPANISH",
                               "FREQUENCY_COUNT",
                               "FREQUENCY_PER_MILLION",
                               "LG10_FREQUENCY",
                               "LINE_IN_SOURCE"]) + '\n')
            for key, lines in self.mapped.items():
                best_line = sorted(lines, key=lambda x: (x[-1], x[-2]))[0]
                best_line[-1] = str(best_line[-1])
                f.write('\t'.join([
                    best_line[-2],  # concepticon id
                    self.concepticon.conceptsets[best_line[-2]].gloss,
                    best_line[1],
                    best_line[2],
                    best_line[3],
                    best_line[4],
                    best_line[0]
                ]) + '\n')

        print('Found {0} direct matches in data.'.format(len(self.mapped)))


if __name__ == '__main__':
    from sys import argv

    if 'download' in argv:
        Dataset().download()
    if 'map_concepts' in argv:
        Dataset().map_concepts()
