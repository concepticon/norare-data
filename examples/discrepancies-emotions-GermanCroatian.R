# R version 4.6.1

# Load libraries
library(groundhog)
pkgs <- c("readr", "dplyr")
groundhog.library(pkgs, "2026-09-05")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import Croatian and German emotion rating datasets
Coso_2023_Emotions <- read_delim("datasets/Coso-2023-Emotions/Coso-2023-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

Briesemeister_2011_DiscreteEmotions <- read_delim("datasets/Briesemeister-2011-DiscreteEmotions/Briesemeister-2011-DiscreteEmotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

# Merge data sets on shared Concepticon IDs to find overlapping concepts
Emotions_Croatian_German_overlap <- merge(Coso_2023_Emotions, Briesemeister_2011_DiscreteEmotions, by = "CONCEPTICON_ID", suffixes = c(".Coso",".Briesemeister"))

# Identify the 10 concepts with the largest Croatian-German rating discrepancy, per emotion
top_disgust <- Emotions_Croatian_German_overlap %>%
  mutate(diff_disgust = abs(CROATIAN_DISGUST_MEAN - GERMAN_DISGUST_MEAN)) %>%
  arrange(desc(diff_disgust)) %>%
  select(ENGLISH, CROATIAN, GERMAN, CROATIAN_DISGUST_MEAN, GERMAN_DISGUST_MEAN, diff_disgust) %>%
  head(10)
top_disgust

top_sadness <- Emotions_Croatian_German_overlap %>%
  mutate(diff_sadness = abs(CROATIAN_SADNESS_MEAN - GERMAN_SADNESS_MEAN)) %>%
  arrange(desc(diff_sadness)) %>%
  select(ENGLISH, CROATIAN, GERMAN, CROATIAN_SADNESS_MEAN, GERMAN_SADNESS_MEAN, diff_sadness) %>%
  head(10)
top_sadness

top_happiness <- Emotions_Croatian_German_overlap %>%
  mutate(diff_happiness = abs(CROATIAN_HAPPINESS_MEAN - GERMAN_HAPPINESS_MEAN)) %>%
  arrange(desc(diff_happiness)) %>%
  select(ENGLISH, CROATIAN, GERMAN, CROATIAN_HAPPINESS_MEAN, GERMAN_HAPPINESS_MEAN, diff_happiness) %>%
  head(10)
top_happiness

top_fear <- Emotions_Croatian_German_overlap %>%
  mutate(diff_fear = abs(CROATIAN_FEAR_MEAN - GERMAN_FEAR_MEAN)) %>%
  arrange(desc(diff_fear)) %>%
  select(ENGLISH, CROATIAN, GERMAN, CROATIAN_FEAR_MEAN, GERMAN_FEAR_MEAN, diff_fear) %>%
  head(10)
top_fear

top_anger <- Emotions_Croatian_German_overlap %>%
  mutate(diff_anger = abs(CROATIAN_ANGER_MEAN - GERMAN_ANGER_MEAN)) %>%
  arrange(desc(diff_anger)) %>%
  select(ENGLISH, CROATIAN, GERMAN, CROATIAN_ANGER_MEAN, GERMAN_ANGER_MEAN, diff_anger) %>%
  head(10)
top_anger

# Save each top-10 discrepancy table to file
write_tsv(top_disgust, "examples/GC_top10_discrepancy_disgust.tsv")
write_tsv(top_sadness, "examples/GC_top10_discrepancy_sadness.tsv")
write_tsv(top_happiness, "examples/GC_top10_discrepancy_happiness.tsv")
write_tsv(top_fear, "examples/GC_top10_discrepancy_fear.tsv")
write_tsv(top_anger, "examples/GC_top10_discrepancy_anger.tsv")