# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr","ggplot2", "ggthemes", "dplyr", "plyr", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2023-05-01")

# Set working directory to Concepticon repository (please adapt the path accordingly)
setwd("./concepticon/concepticon-data/concepticondata/conceptlists/")

# Import data set from Concepticon
Lynott_2013_400 <- read_delim("Lynott-2013-400.tsv", 
                              "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                            CONCEPTICON_ID = col_integer()), 
                              trim_ws = TRUE)

Lynott_2009_423 <- read_delim("Lynott-2009-423.tsv", 
                              "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                            CONCEPTICON_ID = col_integer()), 
                              trim_ws = TRUE)

Winter_2016_300 <- read_delim("Winter-2016-300.tsv", 
                              "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                            CONCEPTICON_ID = col_integer()), 
                              trim_ws = TRUE)

# Use rbind to merge all three data sets
LLW <- rbind.fill(Lynott_2013_400, Lynott_2009_423, Winter_2016_300)


# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data set
Lynott_2020_Sensorimotor <- read_delim("datasets/Lynott-2020-Sensorimotor/Lynott-2020-Sensorimotor.tsv", 
                                       "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                     LINE_IN_SOURCE = col_integer()), 
                                       trim_ws = TRUE)

# Merge data sets 
overlap_LL <- merge(Lynott_2020_Sensorimotor, LLW, by = "CONCEPTICON_ID", suffixes = c(".Lynott_2020",".LLW"))

# Show overlap between the data sets
nrow(overlap_LL)

# Test correlations of the variables in the data sets
cor.test(overlap_LL$ENGLISH_AUDITORY_MEAN, overlap_LL$AUDITORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_GUSTATORY_MEAN, overlap_LL$GUSTATORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_HAPTIC_MEAN, overlap_LL$HAPTIC_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_OLFACTORY_MEAN, overlap_LL$OLFACTORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_VISUAL_MEAN, overlap_LL$VISUAL_MEAN, method="pearson")

# Create plots
plot_aud <- ggplot(overlap_LL, aes(x=ENGLISH_AUDITORY_MEAN, y=AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory", y="Automated mapping", x = "") +
  theme_hc(base_size = 30)

plot_gus <- ggplot(overlap_LL, aes(x=ENGLISH_GUSTATORY_MEAN, y=GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

plot_hap <- ggplot(overlap_LL, aes(x=ENGLISH_HAPTIC_MEAN, y=HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="Automated mapping", x = "") +
  theme_hc(base_size = 30)

plot_olf <- ggplot(overlap_LL, aes(x=ENGLISH_OLFACTORY_MEAN, y=OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Manual mapping") +
  theme_hc(base_size = 30)

plot_vis <- ggplot(overlap_LL, aes(x=ENGLISH_VISUAL_MEAN, y=VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Visual",  y="Automated mapping", x = "Manual mapping") +
  theme_hc(base_size = 30)

# Save plots
grid.arrange(plot_aud, plot_gus, plot_hap, plot_olf, plot_vis, nrow=3)

g = arrangeGrob(plot_aud, plot_gus, plot_hap, plot_olf, plot_vis, nrow=3)

ggsave("examples/English_sensory.pdf", g, width=20, height=30)
