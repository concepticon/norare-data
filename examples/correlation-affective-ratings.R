# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr","ggplot2", "ggthemes", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2023-05-01")


# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data sets
Scott_2019_Ratings <- read_delim("datasets/Scott-2019-Ratings/Scott-2019-Ratings.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), 
                                 trim_ws = TRUE)

Warriner_2013_AffectiveRatings <- read_delim("datasets/Warriner-2013-AffectiveRatings/Warriner-2013-AffectiveRatings.tsv", 
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
arousal_plot <- ggplot(overlap_WS, aes(x=ENGLISH_AROUSAL_MEAN.Scott, y=ENGLISH_AROUSAL_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 8.25, p.accuracy = 0.0001, size = 10) +
  labs(title= "Arousal", y="Scott et al. (2019)", x = "") +
  theme_hc(base_size = 30)

valence_plot <- ggplot(overlap_WS, aes(x=ENGLISH_VALENCE_MEAN.Scott, y=ENGLISH_VALENCE_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 8.25, p.accuracy = 0.0001, size = 10) +
  labs(title= "Valence", y="", x = "Warriner et al. (2013)") +
  theme_hc(base_size = 30)

dominance_plot <- ggplot(overlap_WS, aes(x=ENGLISH_DOMINANCE_MEAN.Scott, y=ENGLISH_DOMINANCE_MEAN.Warriner)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 9)) +
  scale_y_continuous(limits=c(0, 9)) +
  geom_smooth(method = 'gam', formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 8.25, p.accuracy = 0.0001, size = 10) +
  labs(title= "Dominance", y="Scott et al. (2019)", x = "Warriner et al. (2013)") +
  theme_hc(base_size = 30) 

# Save plots
grid.arrange(arousal_plot, valence_plot, dominance_plot, nrow=2)

affective_g = arrangeGrob(arousal_plot, valence_plot, dominance_plot, nrow=2)

ggsave("examples/affective.pdf", affective_g, width=20, height=20)
