def download(dataset):
    dataset.download_zip(
        "https://github.com/clics/clics3/raw/refs/tags/v1.1/clics3-infomap.gml.zip",
        "clics3-infomap.gml.zip",
        "graphs/infomap-3-families.gml"
        )
