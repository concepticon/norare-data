# R version 4.5.2

# Load libraries
library(groundhog)
pkgs <- c("readr", "dplyr")
groundhog.library(pkgs, "2026-08-20")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data
norare <- read_delim("norare.tsv", "\t", trim_ws = TRUE)

# Count entries by LANGUAGE
lang_counts <- norare %>%
  count(LANGUAGE, name = "Count") %>%
  arrange(desc(Count))

print(lang_counts, n = Inf)
write_tsv(lang_counts, "examples/lang_counts.tsv")

# Count entries by TYPE
type_counts <- norare %>%
  count(TYPE, name = "Count") %>%
  arrange(desc(Count))

print(type_counts, n = Inf)
write_tsv(type_counts, "examples/type_counts.tsv")

# Count entries by norms, ratings or relations (NORARE)
norare_counts <- norare %>%
  count(NORARE, name = "Count") %>%
  arrange(desc(Count))

print(norare_counts, n = Inf)
write_tsv(norare_counts, "examples/norare_counts.tsv")