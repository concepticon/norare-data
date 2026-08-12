import json


def download(dataset):
    dataset.download_file(
        'https://raw.githubusercontent.com/lexibank/datsemshift/refs/tags/v1.1rc/cldf/parameters.csv',
        "parameters.csv"
    )

def map(dataset, concepticon, mappings):
    # get mappings
    zalizniak = {c.number: (c.concepticon_id, c.concepticon_gloss, c.english) for c in
                 concepticon.conceptlists["Zalizniak-2024-4583"].concepts.values()}
    
    # the cldf is already formatted as needed, we keep it in this form, just
    # transform it a bit
    table = []
    for row in dataset.get_csv("parameters.csv", dicts=True, delimiter=","):
        if row["Number"] in zalizniak:
            new_row = {"ID": row["ID"]}
            new_row["CONCEPTICON_ID"] = zalizniak[row["Number"]][0]
            new_row["CONCEPTICON_GLOSS"] = zalizniak[row["Number"]][1]
            new_row["ENGLISH"] = zalizniak[row["Number"]][2]
            if new_row["CONCEPTICON_ID"]:
                for itm in ["Linked_Concepts", "Target_Concepts", "Domain", "Alias",
                            "Shifts", "Gloss_in_Source", "Definition"]:
                    new_row[itm.upper()] = row[itm]
                    
                new_row["TARGET_CONCEPTS"] = json.loads(new_row["TARGET_CONCEPTS"])
                new_row["LINKED_CONCEPTS"] = json.loads(new_row["LINKED_CONCEPTS"])

                # add further items that must be p
                table.append(new_row)

    dataset.table.write(table)
