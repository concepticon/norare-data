# R version 4.5.2

# Load libraries
library(groundhog)
pkgs <- c("readr", "dplyr")
groundhog.library(pkgs, "2026-03-29")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import Croatian and Dutch emotion rating datasets
Coso_2023_Emotions <- read_delim("datasets/Coso-2023-Emotions/Coso-2023-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

Speed_2024_Emotions <- read_delim("datasets/Speed-2024-Emotions/Speed-2024-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

# Merge data sets on shared Concepticon IDs to find overlapping concepts
Emotions_Croatian_Dutch_overlap <- merge(Coso_2023_Emotions, Speed_2024_Emotions, by = "CONCEPTICON_ID", suffixes = c(".Coso",".Speed"))

# Identify the 10 concepts with the largest Croatian-Dutch rating discrepancy, per emotion

top_disgust <- Emotions_Croatian_Dutch_overlap %>%
     mutate(diff_disgust = abs(CROATIAN_DISGUST_MEAN - DUTCH_DISGUST_MEAN)) %>%
     arrange(desc(diff_disgust)) %>%
     select(ENGLISH, CROATIAN, DUTCH, CROATIAN_DISGUST_MEAN, DUTCH_DISGUST_MEAN, diff_disgust) %>%
     head(10)
top_disgust

top_sadness <- Emotions_Croatian_Dutch_overlap %>%
     mutate(diff_sadness = abs(CROATIAN_SADNESS_MEAN - DUTCH_SADNESS_MEAN)) %>%
     arrange(desc(diff_sadness)) %>%
     select(ENGLISH, CROATIAN, DUTCH, CROATIAN_SADNESS_MEAN, DUTCH_SADNESS_MEAN, diff_sadness) %>%
     head(10)
top_sadness

top_happiness <- Emotions_Croatian_Dutch_overlap %>%
     mutate(diff_happiness = abs(CROATIAN_HAPPINESS_MEAN - DUTCH_HAPPINESS_MEAN)) %>%
     arrange(desc(diff_happiness)) %>%
     select(ENGLISH, CROATIAN, DUTCH, CROATIAN_HAPPINESS_MEAN, DUTCH_HAPPINESS_MEAN, diff_happiness) %>%
     head(10)
top_happiness

top_fear <- Emotions_Croatian_Dutch_overlap %>%
     mutate(diff_fear = abs(CROATIAN_FEAR_MEAN - DUTCH_FEAR_MEAN)) %>%
     arrange(desc(diff_fear)) %>%
     select(ENGLISH, CROATIAN, DUTCH, CROATIAN_FEAR_MEAN, DUTCH_FEAR_MEAN, diff_fear) %>%
     head(10)
top_fear

top_anger <- Emotions_Croatian_Dutch_overlap %>%
     mutate(diff_anger = abs(CROATIAN_ANGER_MEAN - DUTCH_ANGER_MEAN)) %>%
     arrange(desc(diff_anger)) %>%
     select(ENGLISH, CROATIAN, DUTCH, CROATIAN_ANGER_MEAN, DUTCH_ANGER_MEAN, diff_anger) %>%
     head(10)
top_anger

# Save each top-10 discrepancy table to file
write_tsv(top_disgust, "examples/GC_top10_discrepancy_disgust.tsv")
write_tsv(top_sadness, "examples/GC_top10_discrepancy_sadness.tsv")
write_tsv(top_happiness, "examples/GC_top10_discrepancy_happiness.tsv")
write_tsv(top_fear, "examples/GC_top10_discrepancy_fear.tsv")
write_tsv(top_anger, "examples/GC_top10_discrepancy_anger.tsv")