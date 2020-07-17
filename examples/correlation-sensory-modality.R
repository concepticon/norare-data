
# Empty work space
rm(list = ls())

# Load libraries
library(readr)
library(ggplot2)
library(ggthemes)


# Set working directory to Concepticon repository (please adapt the path accordingly)
setwd("~/GitHub/Repos/concepticon/concepticon-data/concepticondata/conceptlists/")

# Import data set from Concepticon
Lynott_2013_400 <- read_delim("Lynott-2013-400.tsv", 
                              "\t", escape_double = FALSE, col_types = cols(NUMBER = col_integer(), 
                                                                            CONCEPTICON_ID = col_integer()), 
                              trim_ws = TRUE)

# Set working directory (this should automatically set the working directory to the norare-data repository)
try(setwd(dirname(rstudioapi::getActiveDocumentContext()$path)))
dir <- setwd(system("git rev-parse --show-toplevel", intern=T))


# Import data set
Lynott_2019_Sensorimotor <- read_delim("./concept_set_meta/Lynott-2019-Sensorimotor/Lynott-2019-Sensorimotor.tsv", 
                                       "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                     LINE_IN_SOURCE = col_integer()), 
                                       trim_ws = TRUE)

# Merge data sets 
overlap_LL <- merge(Lynott_2019_Sensorimotor, Lynott_2013_400, by = "CONCEPTICON_ID", suffixes = c(".Lynott_2019",".Lynott_2013"))

# Show overlap between the data sets
nrow(overlap_LL)

# Test correlations of the variables in the data sets
cor.test(overlap_LL$ENGLISH_AUDITORY_MEAN, overlap_LL$AUDITORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_GUSTATORY_MEAN, overlap_LL$GUSTATORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_HAPTIC_MEAN, overlap_LL$HAPTIC_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_OLFACTORY_MEAN, overlap_LL$OLFACTORY_MEAN, method="pearson")
cor.test(overlap_LL$ENGLISH_VISUAL_MEAN, overlap_LL$VISUAL_MEAN, method="pearson")

# Create plots
a <- ggplot(overlap_LL, aes(x=ENGLISH_AUDITORY_MEAN, y=AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 6)) +
  scale_y_continuous(limits=c(0, 6)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Auditory Ratings", y="Automatic mapping", x = "Hand-curated mapping") +
  theme_hc(base_size = 28)

b <- ggplot(overlap_LL, aes(x=ENGLISH_GUSTATORY_MEAN, y=GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 6)) +
  scale_y_continuous(limits=c(0, 6)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Gustatory Ratings",  y="Automated mapping", x = "Hand-curated mapping") +
  theme_hc(base_size = 28)

c <- ggplot(overlap_LL, aes(x=ENGLISH_HAPTIC_MEAN, y=HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 6)) +
  scale_y_continuous(limits=c(0, 6)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Haptic Ratings",  y="Automated mapping", x = "Hand-curated mapping") +
  theme_hc(base_size = 28)

d <- ggplot(overlap_LL, aes(x=ENGLISH_OLFACTORY_MEAN, y=OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 6)) +
  scale_y_continuous(limits=c(0, 6)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Olfactory Ratings",  y="Automated mapping", x = "Hand-curated mapping") +
  theme_hc(base_size = 28)

e <- ggplot(overlap_LL, aes(x=ENGLISH_VISUAL_MEAN, y=VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 6)) +
  scale_y_continuous(limits=c(0, 6)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Visual Ratings",  y="Automated mapping", x = "Hand-curated mapping") +
  theme_hc(base_size = 28)

# Save plots
ggsave("./examples/auditory.pdf", a, width=11, height=8.5)
ggsave("./examples/gustatory.pdf", b, width=11, height=8.5)
ggsave("./examples/haptic.pdf", c, width=11, height=8.5)
ggsave("./examples/olfactory.pdf", d, width=11, height=8.5)
ggsave("./examples/visual.pdf", e, width=11, height=8.5)
