from collections import defaultdict, OrderedDict

def download(dataset):
    dataset.download_zip(
        'https://figshare.com/ndownloader/articles/19328939/versions/8',
        'MultiPic.zip',
        'MultiPic Dataset Open Materials.csv',
    )


def map(dataset, concepticon, mappings):
    mapping = {}
    for concept in concepticon.conceptlists["Dunabeitia-2022-500"].concepts.values():
        mapping[concept.attributes["picture_code"]] = (
            concept.concepticon_id,
            concept.concepticon_gloss,
            concept.english
            )
    data = dataset.get_csv(
        "MultiPic Dataset Open Materials.csv",
        delimiter=";")

    # define languages we want to keep
    languages = OrderedDict({
            "Australian English": "AUSTRALIAN_ENGLISH",
            "Basque": "BASQUE",
            "Belgium Dutch": "FLEMISH",
            "British English": "ENGLISH",
            "Catalan": "CATALAN",
            "Cypriot Greek": "CYPRIOTIC_GREEK",
            "Czech": "CZECH", 
            "Finnish": "FINNISH",
            "French": "FRENCH",
            "German": "GERMAN",
            "Greek": "GREEK",
            "Hebrew": "HEBREW",
            "Hungarian": "HUNGARIAN",
            "Italian": "ITALIAN",
            "Korean": "KOREAN",
            "Lebanese Arabic": "ARABIC",
            "Malay": "MALAYSIAN",
            "Mandarin Chinese": "MANDARIN",            
            "Netherlands Dutch": "DUTCH",
            "Norwegian": "NORWEGIAN",
            "Polish": "POLISH",
            "Portuguese": "PORTUGUESE",
            "Russian": "RUSSIAN",
            "Serbian": "SERBIAN",
            "Slovak": "SLOVAK",
            "Spanish": "SPANISH",
            "Turkish": "TURKISH",
            "Welsh": "WELSH",
            })
    responses = {
            language : {} for language in languages
            }
    # organize the data per code
    for row in data:
        if row["Language"] in languages:
            print("yes")
            print(row["Language"])
            responses[row["Language"]][int(row["Code"])] = [
                    row["Modal Response"],
                    row["Number of Responses"],
                    row["H Statistic"].replace(",", '.'),
                    row["Modal Response Percentage"].replace(",", "."),
                    row['''"I don't know" Response Percentage'''].replace(",",
                                                                          "."),
                    row["Idiosyncratic Response Percentage"].replace(",", "."),
                    row["Familiarity"].replace(",", ".") or ""
                    ]
    
    # fill the table
    table = []
    for code, (cid, cgl, eng) in mapping.items():
        row = [cid, cgl, code]
        for language in languages:
            if code in responses[language]:
                row += responses[language][code]
            else:
                row += ["", "", "", "", "", "", ""]
        table += [row]
    dataset.table.write(table)

