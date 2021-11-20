
# Empty work space
rm(list = ls())

# Load libraries
library(readr)
library(ggplot2)
library(ggthemes)
library(ggpubr)
library(gridExtra)



# Import data sets
English_Scott_2019 <- read_delim("./concepticon/norare-data/concept_set_meta/Scott-2019-Ratings/Scott-2019-Ratings.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), 
                                 trim_ws = TRUE)

Dutch_Moors_2013 <- read_delim("./concepticon/norare-data/concept_set_meta/Moors-2013-Ratings/Moors-2013-Ratings.tsv", 
                                            "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), 
                                            trim_ws = TRUE)

Spanish_Stadthagen_2017 <- read_delim("./concepticon/norare-data/concept_set_meta/StadthagenGonzalez-2017-ValenceArousal/StadthagenGonzalez-2017-ValenceArousal.tsv", 
                                    "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), 
                                    trim_ws = TRUE)

# Show size of data sets
nrow(English_Scott_2019)
nrow(Dutch_Moors_2013)
nrow(Spanish_Stadthagen_2017)

# Merge data sets 
overlap_English_Dutch <- merge(English_Scott_2019, Dutch_Moors_2013, by = "CONCEPTICON_ID")
overlap_English_Spanish <- merge(English_Scott_2019,Spanish_Stadthagen_2017, by = "CONCEPTICON_ID")
overlap_Spanish_Dutch <- merge(Spanish_Stadthagen_2017, Dutch_Moors_2013, by = "CONCEPTICON_ID")

# Show overlap between the data sets
nrow(overlap_English_Dutch)
nrow(overlap_English_Spanish)
nrow(overlap_Spanish_Dutch)

# Test correlations of the variables in the data sets
cor.test(overlap_English_Dutch$ENGLISH_AROUSAL_MEAN, overlap_English_Dutch$DUTCH_AROUSAL_MEAN, method="pearson")
cor.test(overlap_English_Dutch$ENGLISH_VALENCE_MEAN, overlap_English_Dutch$DUTCH_VALENCE_MEAN, method="pearson")

cor.test(overlap_English_Spanish$ENGLISH_AROUSAL_MEAN, overlap_English_Spanish$SPANISH_AROUSAL_MEAN, method="pearson")
cor.test(overlap_English_Spanish$ENGLISH_VALENCE_MEAN, overlap_English_Spanish$SPANISH_VALENCE_MEAN, method="pearson")

cor.test(overlap_Spanish_Dutch$DUTCH_AROUSAL_MEAN, overlap_Spanish_Dutch$SPANISH_AROUSAL_MEAN, method="pearson")
cor.test(overlap_Spanish_Dutch$DUTCH_VALENCE_MEAN, overlap_Spanish_Dutch$SPANISH_VALENCE_MEAN, method="pearson")

# Create and save plots for arousal
a_arousal <- ggplot(overlap_English_Dutch, aes(x=ENGLISH_AROUSAL_MEAN, y=DUTCH_AROUSAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "English-Dutch: 335 concepts", y="Dutch", x = "English") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
a_arousal

b_arousal <- ggplot(overlap_English_Spanish, aes(x=ENGLISH_AROUSAL_MEAN, y=SPANISH_AROUSAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "English-Spanish: 654 concepts",y="Spanish", x = "English") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
b_arousal

c_arousal <- ggplot(overlap_Spanish_Dutch, aes(x=SPANISH_AROUSAL_MEAN, y=DUTCH_AROUSAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 9, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 9, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "Dutch-Spanish: 280 concepts", y="Dutch", x = "Spanish") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
c_arousal

g_arousal = grid.arrange(a_arousal, b_arousal, c_arousal, nrow=1)

ggsave("arousal.png", g_arousal, width=33, height=10)


# Create and save plots for valence

a_valence <- ggplot(overlap_English_Dutch, aes(x=ENGLISH_VALENCE_MEAN, y=DUTCH_VALENCE_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "English-Dutch: 335 concepts", y="Dutch", x = "English") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
a_valence

b_valence <- ggplot(overlap_English_Spanish, aes(x=ENGLISH_VALENCE_MEAN, y=SPANISH_VALENCE_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 10, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "English-Spanish: 654 concepts",y="Spanish", x = "English") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
b_valence

c_valence <- ggplot(overlap_Spanish_Dutch, aes(x=SPANISH_VALENCE_MEAN, y=DUTCH_VALENCE_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(1, 9),breaks=seq(1, 9, by = 2)) +
  scale_y_continuous(limits=c(1, 9),breaks=seq(1, 9, by = 2)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title = "Dutch-Spanish: 280 concepts", y="Dutch", x = "Spanish") +
  stat_cor(method = "pearson", label.x = 7, label.y = 8.75, p.accuracy = 0.0001, size = 6) +
  theme_hc(base_size = 24)
c_valence

g_valence = grid.arrange(a_valence, b_valence, c_valence, nrow=1)

ggsave("valence.png", g_valence, width=33, height=10, limitsize = FALSE)
