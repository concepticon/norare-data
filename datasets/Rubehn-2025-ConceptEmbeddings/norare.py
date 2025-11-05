import collections
import json
import gzip
import statistics


modes = {
    "fullfams": "EMBEDDINGS_FULL",
    "full-affix": "EMBEDDINGS_FULL_AFFIX",
    "full-affix-overlap": "EMBEDDINGS_FULL_AFFIX_OVERLAP"
}

fasttext_langs = {
    "arabic": "ar",
    "english": "en",
    "spanish": "es",
    "estonian": "et",
    "finnish": "fi",
    "french": "fr",
    "polish": "pl",
    "russian": "ru",
    "chinese": "zh"
}

def download(dataset):
    # download concept embeddings
    for mode in modes:
        dataset.download_file(f"https://raw.githubusercontent.com/calc-project/concept-embeddings/refs/tags/v.1.0/embeddings/{mode}/prone.json", f"{mode}.json")

    # download fasttext embeddings
    for lang in fasttext_langs.values():
        dataset.download_file(f"https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.{lang}.300.vec.gz")

def map_fasttext_embeddings(dataset, concepticon, concepts):
    # retrieve concepts that are present in both multisimlex and our embeddings
    conceptlist = list(c for c in concepticon.conceptlists["Vulic-2020-2244"].concepts.values()
                        if c.concepticon_gloss in concepts)

    # for each concept, collect the translations in the individual languages
    translations = collections.defaultdict(lambda: collections.defaultdict(list))
    vocabularies = collections.defaultdict(set)

    for concept in conceptlist:
        gloss = concept.concepticon_gloss
        if not gloss:
            continue
        for l in fasttext_langs:
            gloss_translations = concept.attributes.get(f"{l}_in_source", [])
            translations[gloss][l].extend(gloss_translations)
            vocabularies[l] = vocabularies[l] | set(gloss_translations)

    final_ft_embeddings = collections.defaultdict(lambda: collections.defaultdict(list))

    # now look up the pretrained fasttext embeddings for each language
    for lang, lang_id in fasttext_langs.items():
        vocab = vocabularies[lang]
        # load fasttext embeddings
        ft_embeddings = {}
        with gzip.open(dataset.raw_dir / f"cc.{lang_id}.300.vec.gz", "rt") as f:
            for line in f:
                values = line.strip().split()
                word = values[0]
                # only store relevant words to save memory
                if word in vocab:
                    ft_embeddings[word] = [float(x) for x in values[1:]]

        for concept, trans in translations.items():
            translations_in_lang = trans[lang]
            embeddings = [ft_embeddings[word] for word in translations_in_lang if word in ft_embeddings]
            if not embeddings:
                continue
            mean_embedding = []
            for dimension in zip(*embeddings):
                mean_embedding.append(statistics.mean(dimension))

            final_ft_embeddings[lang_id][concept] = mean_embedding

    return final_ft_embeddings

def map(dataset, concepticon, mappings):
    embedding_data = {}

    for mode in modes:
        with open(dataset.raw_dir / f"{mode}.json") as f:
            embedding_data[mode] = json.load(f)["embeddings"]

    concepts = set()
    for mode in modes:
        concepts.update(embedding_data[mode].keys())

    # map concepticon gloss to id
    concepticon_gloss_to_id = {c.gloss: c.id for c in concepticon.conceptsets.values()
                               if c.gloss in concepts}

    # retrieve fasttext embeddings
    ft_embeddings = map_fasttext_embeddings(dataset, concepticon, concepts)

    table = []
    for i, (concepticon_gloss, concepticon_id) in enumerate(concepticon_gloss_to_id.items()):
        row = collections.OrderedDict([
            ("CONCEPTICON_ID", concepticon_id),
            ("CONCEPTICON_GLOSS", concepticon_gloss)
        ])

        for mode, col_name in modes.items():
            emb = embedding_data[mode].get(concepticon_gloss)
            emb = [round(x, 4) for x in emb] if emb else emb  # round to 4 floating point digits to save memory
            row[col_name] = emb

        for lang in fasttext_langs.values():
            row[f"FASTTEXT_{lang.upper()}"] = ft_embeddings[lang].get(concepticon_gloss, None)

        table.append(row)

    # Write to output
    dataset.table.write(table)
