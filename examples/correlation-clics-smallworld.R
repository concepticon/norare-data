# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr", "dplyr")
groundhog.library(pkgs, "2023-05-01")


# Set working directory to Concepticon repository (please adapt the path accordingly)
setwd("./concepticon/concepticon-data/concepticondata/conceptlists/")

# Import data set from Concepticon
clics3 <- read_delim("Rzymski-2020-1624.tsv", 
                     "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                   CONCEPTICON_ID = col_integer()), 
                     trim_ws = TRUE)

clics2 <- read_delim("List-2018-1105.tsv", 
                     "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                   CONCEPTICON_ID = col_integer()), 
                     trim_ws = TRUE)

clics1 <- read_delim("List-2014-1280.tsv", 
                     "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                   CONCEPTICON_ID = col_integer()), 
                     trim_ws = TRUE)

Verheyen_2020_1000 <- read_delim("Verheyen-2020-1000.tsv", 
                                 delim = "\t", escape_double = FALSE, 
                                 trim_ws = TRUE)

smallworld <- Verheyen_2020_1000[!is.na(Verheyen_2020_1000$CONCEPTICON_ID),]
  
  
# Merge data sets 
overlap_c3 <- merge(clics3, smallworld, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".SmallWorld"))
overlap_c2 <- merge(clics2, smallworld, by = "CONCEPTICON_ID", suffixes = c(".CLICS2",".SmallWorld"))
overlap_c1 <- merge(clics1, smallworld, by = "CONCEPTICON_ID", suffixes = c(".CLICS1",".SmallWorld"))


# Show overlap between the data sets
nrow(overlap_c3)
nrow(overlap_c2)
nrow(overlap_c1)


# Test correlations of the variables in the data sets
cor.test(overlap_c3$WEIGHTED_FAMILY_DEGREE, overlap_c3$INSTRENGTH, method="pearson", exact = FALSE)
cor.test(overlap_c2$WEIGHTED_FAMILY_DEGREE, overlap_c2$INSTRENGTH, method="pearson", exact = FALSE)
cor.test(overlap_c1$WEIGHTED_DEGREE, overlap_c1$INSTRENGTH, method="pearson", exact = FALSE)

