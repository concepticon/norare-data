# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr","ggplot2", "ggthemes", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2023-05-01")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data sets
Brysbaert_2009_Frequency <- read_delim("datasets/Brysbaert-2009-Frequency/Brysbaert-2009-Frequency.tsv", 
                                       "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                     ENGLISH_FREQUENCY = col_double()), 
                                       trim_ws = TRUE)

Brysbaert_2011_Frequency <- read_delim("datasets/Brysbaert-2011-Frequency/Brysbaert-2011-Frequency.tsv", 
                                       delim = "\t", escape_double = FALSE, 
                                       trim_ws = TRUE)


Cai_2010_Frequency <- read_delim("datasets/Cai-2010-Frequency/Cai-2010-Frequency.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(CHINESE_CD = col_double()), 
                                 trim_ws = TRUE)

# Merge data sets 
overlap_EG <- merge(Brysbaert_2009_Frequency, Brysbaert_2011_Frequency, by = "CONCEPTICON_ID")
overlap_EC <- merge(Brysbaert_2009_Frequency, Cai_2010_Frequency, by = "CONCEPTICON_ID")
overlap_GC <- merge(Brysbaert_2011_Frequency, Cai_2010_Frequency, by = "CONCEPTICON_ID")

# Show size of data sets
nrow(Brysbaert_2009_Frequency)
nrow(Brysbaert_2011_Frequency)
nrow(Cai_2010_Frequency)

# Show overlap between the data sets
nrow(overlap_EG)
nrow(overlap_EC)
nrow(overlap_GC)

# Test correlations of the variables in the data sets
cor.test(overlap_EG$ENGLISH_FREQUENCY_LOG, overlap_EG$GERMAN_FREQUENCY_LOG, method="pearson")
cor.test(overlap_EC$ENGLISH_FREQUENCY_LOG, overlap_EC$CHINESE_FREQUENCY_LOG, method="pearson")
cor.test(overlap_GC$GERMAN_FREQUENCY_LOG, overlap_GC$CHINESE_FREQUENCY_LOG, method="pearson")

# Create plots
EG_plot <- ggplot(overlap_EG, aes(x=ENGLISH_FREQUENCY_LOG, y=GERMAN_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 6.25, p.accuracy = 0.0001, size = 10) +
  labs(title= "Log10 Word Frequency", y="English", x = "German") +
  theme_hc(base_size = 30)

EC_plot <- ggplot(overlap_EC, aes(x=ENGLISH_FREQUENCY_LOG, y=CHINESE_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 6.25, p.accuracy = 0.0001, size = 10) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "", y="English", x = "Chinese") +
  theme_hc(base_size = 30)

GC_plot <- ggplot(overlap_GC, aes(x=GERMAN_FREQUENCY_LOG, y=CHINESE_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 6.25, p.accuracy = 0.0001, size = 10) +
  labs(title= "", y="German", x = "Chinese") +
  theme_hc(base_size = 30)


# Save plots 
grid.arrange(EG_plot, EC_plot, GC_plot, nrow=2)

freq_g = arrangeGrob(EG_plot, EC_plot, GC_plot, nrow=2)

ggsave("examples/frequencies.pdf", freq_g, width=20, height=20)
