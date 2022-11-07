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
- run validation
  ```shell
  norare --repos ../concepticon-data/ --norarepo . validate
  ```
- report summary statistics
  ```shell
  norare --repos ../concepticon-data/ --norarepo . stats
  ```
- make sure `cldfbench makecldf` succeeds.
- create the release commit:
  ```shell
  git commit -a -m "release <VERSION>"
  ```
- create a release tag:
  ```shell
  git tag -a v<VERSION> -m"<VERSION> release"
  ```
- push to GitHub:
  ```shell
  git push origin
  git push --tags
  ```
- create release on GitHub, making sure it is picked up by Zenodo
