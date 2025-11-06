from pynorare import NoRaRe
from tabulate import tabulate

nora = NoRaRe("../../")

mp = {k: v for k, v in nora.datasets["Dunabeitia-2022-MultiPic"].concepts.items()}


languages = [ 
        "ARABIC",
        "BASQUE",
        "CATALAN",
        "CZECH",
        "DUTCH",
        "ENGLISH",
        "FINNISH",
        "FLEMISH",
        "FRENCH",
        "GERMAN",
        "GREEK",
        "HEBREW",
        "HUNGARIAN",
        "ITALIAN",
        "KOREAN",
        "MALAYSIAN",
        "MANDARIN_CHINESE",
        "NORWEGIAN",
        "POLISH",
        "PORTUGUESE",
        "RUSSIAN",
        "SERBIAN",
        "SLOVAK",
        "SPANISH",
        "TURKISH",
        "WELSH",
             ]

table = []
for language in languages:
    table += [[
        language,
        mp[1476][language.lower()],
        mp[1476][language.lower() + "_shannon_diversity"]
        ]]
print(tabulate(
    table, 
    headers=["Language", "Word", "Entropy"], 
    tablefmt="pipe",
    floatfmt=".2f"))
