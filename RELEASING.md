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
- Create the release commit:
  ```shell
  git commit -a -m "release <VERSION>"
  ```
- Create a release tag:
  ```
  git tag -a v<VERSION> -m"<VERSION> release"
  ```
- Push to github:
  ```
  git push origin
  git push --tags
  ```
- Create release on GitHub, making sure it is picked up by Zenodo
