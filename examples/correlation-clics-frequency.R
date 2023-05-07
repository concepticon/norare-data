# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr","ggplot2", "ggthemes", "dplyr", "ggpubr")
groundhog.library(pkgs, "2023-05-01")


# Set working directory to Concepticon repository (please adapt the path accordingly)
setwd("./concepticon/concepticon-data/concepticondata/conceptlists/")

# Import data set from Concepticon
clics3 <- read_delim("Rzymski-2020-1624.tsv", 
                     "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                   CONCEPTICON_ID = col_integer()), 
                     trim_ws = TRUE)

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data set from NoRaRe

english <- read_delim("datasets/Brysbaert-2009-Frequency/Brysbaert-2009-Frequency.tsv", 
                      "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                    ENGLISH_FREQUENCY = col_double()), 
                      trim_ws = TRUE)

german <- read_delim("datasets/Brysbaert-2011-Frequency/Brysbaert-2011-Frequency.tsv", 
                     delim = "\t", escape_double = FALSE, 
                     trim_ws = TRUE)

chinese <- read_delim("datasets/Cai-2010-Frequency/Cai-2010-Frequency.tsv", 
                      "\t", escape_double = FALSE, col_types = cols(CHINESE_CD = col_double()), 
                      trim_ws = TRUE)

spanish <- read_delim("datasets/Cuetos-2011-Frequency/Cuetos-2011-Frequency.tsv", 
                      delim = "\t", escape_double = FALSE, 
                      trim_ws = TRUE)

dutch <- read_delim("datasets/Keuleers-2010-Frequency/Keuleers-2010-Frequency.tsv", 
                    delim = "\t", escape_double = FALSE, 
                    trim_ws = TRUE)

polish <- read_delim("datasets/Mandera-2015-Frequency/Mandera-2015-Frequency.tsv", 
                     delim = "\t", escape_double = FALSE, 
                     trim_ws = TRUE)

# Merge data sets 
overlap_ce <- merge(clics3, english, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".English"))
overlap_cg <- merge(clics3, german, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".German"))
overlap_cc <- merge(clics3, chinese, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".Chinese"))
overlap_cs <- merge(clics3, spanish, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".Spanish"))
overlap_cd <- merge(clics3, dutch, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".Dutch"))
overlap_cp <- merge(clics3, polish, by = "CONCEPTICON_ID", suffixes = c(".CLICS3",".Polish"))


# Show overlap between the data sets
nrow(overlap_ce)
nrow(overlap_cg)
nrow(overlap_cc)
nrow(overlap_cs)
nrow(overlap_cd)
nrow(overlap_cp)


# Test correlations of the variables in the data sets
cor.test(overlap_ce$WEIGHTED_FAMILY_DEGREE, overlap_ce$ENGLISH_FREQUENCY, method="spearman", exact = FALSE)
cor.test(overlap_cg$WEIGHTED_FAMILY_DEGREE, overlap_cg$GERMAN_FREQUENCY, method="spearman", exact = FALSE)
cor.test(overlap_cc$WEIGHTED_FAMILY_DEGREE, overlap_cc$CHINESE_FREQUENCY, method="spearman", exact = FALSE)
cor.test(overlap_cs$WEIGHTED_FAMILY_DEGREE, overlap_cs$SPANISH_FREQUENCY, method="spearman", exact = FALSE)
cor.test(overlap_cd$WEIGHTED_FAMILY_DEGREE, overlap_cd$DUTCH_FREQUENCY, method="spearman", exact = FALSE)
cor.test(overlap_cp$WEIGHTED_FAMILY_DEGREE, overlap_cp$POLISH_FREQUENCY, method="spearman", exact = FALSE)


# Example plot
plot_ce = ggplot(overlap_ce, aes(x= WEIGHTED_FAMILY_DEGREE, y= ENGLISH_FREQUENCY_LOG)) + 
  geom_point() + 
  stat_cor(method = "spearman", label.x = 150, label.y = 0.75, p.accuracy = 0.0001, size = 10) +
  geom_smooth(method = "loess", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Frequency-Meaning Relation", y="English Log10 Frequency", x = "CLICS Weighted Family Degree") +
  theme_hc(base_size = 30)

ggsave("examples/clics-freq.pdf", plot_ce, width=30, height=10)
