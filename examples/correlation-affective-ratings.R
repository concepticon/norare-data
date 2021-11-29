
# Empty work space
rm(list = ls())

# R version: R-4.1.

# Load libraries
library(groundhog) # Version 1.5.0
pkgs <- c("readr","ggplot2", "ggthemes")
groundhog.library(pkgs, "2021-11-27")


# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data sets
Scott_2019_Ratings <- read_delim("concept_set_meta/Scott-2019-Ratings/Scott-2019-Ratings.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), 
                                 trim_ws = TRUE)

Warriner_2013_AffectiveRatings <- read_delim("concept_set_meta/Warriner-2013-AffectiveRatings/Warriner-2013-AffectiveRatings.tsv", 
                                             "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                           LINE_IN_SOURCE = col_integer()), 
                                             trim_ws = TRUE)

# Merge data sets 
overlap_WS <- merge(Scott_2019_Ratings, Warriner_2013_AffectiveRatings, by = "CONCEPTICON_ID", suffixes = c(".Scott",".Warriner"))

# Show size of each data set and overlap between the data sets
nrow(Scott_2019_Ratings)
nrow(Warriner_2013_AffectiveRatings)
nrow(overlap_WS)

# Test correlations of the variables in the data sets
cor.test(overlap_WS$ENGLISH_AROUSAL_MEAN.Scott, overlap_WS$ENGLISH_AROUSAL_MEAN.Warriner, method="pearson")
cor.test(overlap_WS$ENGLISH_VALENCE_MEAN.Scott, overlap_WS$ENGLISH_VALENCE_MEAN.Warriner, method="pearson")
cor.test(overlap_WS$ENGLISH_DOMINANCE_MEAN.Scott, overlap_WS$ENGLISH_DOMINANCE_MEAN.Warriner, method="pearson")

# Create plots
a <- ggplot(overlap_WS, aes(x=ENGLISH_AROUSAL_MEAN.Scott, y=ENGLISH_AROUSAL_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Arousal Ratings", y="Arousal (mean) in Scott et al. (2019)", x = "Arousal (mean) in Warriner et al. (2013)") +
  theme_hc(base_size = 24)

b <- ggplot(overlap_WS, aes(x=ENGLISH_VALENCE_MEAN.Scott, y=ENGLISH_VALENCE_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Valence Ratings", y="Valence (mean) in Scott et al. (2019)", x = "Valence (mean) in Warriner et al. (2013)") +
  theme_hc(base_size = 24)

c <- ggplot(overlap_WS, aes(x=ENGLISH_DOMINANCE_MEAN.Scott, y=ENGLISH_DOMINANCE_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = 'gam', formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Dominance Ratings", y="Dominance (mean) in Scott et al. (2019)", x = "Dominance (mean) in Warriner et al. (2013)") +
  theme_hc(base_size = 24) 
  
# Save plots
ggsave("examples/arousal.pdf", a, width=11, height=8.5)
ggsave("examples/valence.pdf", b, width=11, height=8.5)
ggsave("examples/dominance.pdf", c, width=11, height=8.5)
