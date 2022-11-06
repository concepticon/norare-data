# Releasing NoRaRe

- make sure your clone of concepticon-data is checked out to the correct release tag
- run norare download
  ```shell
  norare --repos ../concepticon-data/ --norarepo . download
  ```
- run norare map
  ```shell
  norare --repos ../concepticon-data/ --norarepo . map
  ```
- validation
  ```shell
  norare --repos ../concepticon-data/ --norarepo . validate
  ```
- summary statistics
  ```shell
  norare --repos ../concepticon-data/ --norarepo . stats
  ```
- make sure `cldfbench makecldf` succeeds.
- commit, push

