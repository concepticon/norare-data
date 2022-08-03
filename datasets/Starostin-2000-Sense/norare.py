import collections


def map(dataset, concepticon, mappings):
    sheet = dataset.get_csv('sense.tsv', dicts=False)
    mapped = collections.defaultdict(list)

    # get data and map them if possible
    for i, line in enumerate(sheet[1:]): 
        number, gloss, senses = line[:3]
        
        gloss_ = gloss.replace(' (V)', '')
        if gloss in mappings['en']:
            best_matches = mappings['en'][gloss]
            pos = ''
        elif gloss_ in mappings['en']:
            best_matches = mappings['en'][gloss_]
            pos = 'Action/Process'
        else:
            best_matches = []
        if best_matches:
            all_best_match, all_best_priority = False, False
            j = 0
            while j < len(best_matches):
                cid, priority, concepticon_pos = best_matches[j]
                if pos == concepticon_pos:
                    all_best_match = cid
                    all_best_priority = priority
                    break
                j += 1
            if not all_best_match:
                all_best_match, all_best_priority, _ = best_matches[0]
            mapped[all_best_match] += [[ 
                number,
                gloss,
                senses,
                all_best_match,
                all_best_priority]]
    header = [
        "CONCEPTICON_ID",
        "CONCEPTICON_GLOSS",
        "ENGLISH",
        "SENSES",
        "LINE_IN_SOURCE"]
    table = []
    for key, lines in mapped.items(): 
        best_line = sorted(lines, key=lambda x: (x[-1], x[-2]))[0] 
        best_line[-1] = str(best_line[-1]) 
        table.append([
            best_line[-2], # concepticon id
            concepticon.conceptsets[best_line[-2]].gloss,
            best_line[1],
            best_line[2], 
            best_line[0]
        ])
    dataset.write_table([dict(zip(header, row)) for row in table])

