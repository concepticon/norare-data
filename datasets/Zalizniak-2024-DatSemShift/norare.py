import json


def download(dataset):
    dataset.download_file(
        'https://raw.githubusercontent.com/lexibank/datsemshift/refs/tags/v1.1rc/cldf/parameters.csv',
        "parameters.csv"
    )

def map(dataset, concepticon, mappings):
    # get mappings
    zalizniak = {c.number: (c.id, c.concepticon_id, c.concepticon_gloss, c.english) for c in
                 concepticon.conceptlists["Zalizniak-2024-4583"].concepts.values()
                 if c.concepticon_id}
    
    # the cldf is already formatted as needed, we keep it in this form, just
    # transform it a bit
    cldf = []
    id_converter = {}
    for row in dataset.get_csv("parameters.csv", dicts=True, delimiter=","):
        if row["Number"] in zalizniak:
            cldf += [row]
            id_converter[row["ID"]] = zalizniak[row["Number"]][0]
    
    table = []
    for row in cldf:
        if row["ID"] in id_converter:
            # get ID, Concepticon ID and Gloss, and English
            new_row = {}
            new_row["ID"] = zalizniak[row["Number"]][0]
            new_row["NUMBER"] = row["Number"]
            new_row["CONCEPTICON_ID"] = zalizniak[row["Number"]][1]
            new_row["CONCEPTICON_GLOSS"] = zalizniak[row["Number"]][2]
            new_row["ENGLISH"] = zalizniak[row["Number"]][3]

            # get links
            tc, lc = json.loads(row["Target_Concepts"]), json.loads(row["Linked_Concepts"])
            for kind, links in [("TARGET_CONCEPTS", tc), ("LINKED_CONCEPTS", lc)]:
                if links:
                    new_links = []
                    for edge in links:
                        if edge["ID"] in id_converter:
                            new_edge = {}
                            new_edge["ID"] = id_converter[edge["ID"]]
                            new_edge["NAME"] = edge["NAME"]
                            for entry in ["Polysemy", "PolysemyByFamily", "Derivation",
                                          "DerivationByFamily"]:
                                new_edge[entry] = edge[entry]
                            new_links += [new_edge]
                    new_row[kind] = new_links
                else:
                    new_row[kind] = []
            for itm in ["Domain", "Alias", "Shifts", "Gloss_in_Source", "Definition"]:
                new_row[itm.upper()] = row[itm]

            # add further items that must be p
            table.append(new_row)
    table = sorted(table, key=lambda x: int(x["NUMBER"]))

    dataset.table.write(table)
