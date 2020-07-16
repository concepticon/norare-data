
# Empty work space
rm(list = ls())

# Load libraries
library(readr)
library(ggplot2)
library(ggthemes)

# Set working directory (this should automatically set the working directory to the norare-data repository)
dir <- setwd(system("git rev-parse --show-toplevel", intern=T))


Brysbaert_2009_Frequency <- read_delim("./concept_set_meta/Brysbaert-2009-Frequency/Brysbaert-2009-Frequency.tsv", 
                                       "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                     ENGLISH_FREQUENCY = col_double()), 
                                       trim_ws = TRUE)

Cuetos_2011_Frequency <- read_delim("./concept_set_meta/Cuetos-2011-Frequency/Cuetos-2011-Frequency.tsv", 
                                    "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                                  SPANISH_FREQUENCY = col_double()), 
                                    trim_ws = TRUE)

Cai_2010_Frequency <- read_delim("concept_set_meta/Cai-2010-Frequency/Cai-2010-Frequency.tsv", 
                                 "\t", escape_double = FALSE, col_types = cols(CHINESE_CD = col_double()), 
                                 trim_ws = TRUE)

# Merge data sets 

overlap_BCu <- merge(Brysbaert_2009_Frequency, Cuetos_2011_Frequency, by = "CONCEPTICON_ID")

overlap_BCa <- merge(Brysbaert_2009_Frequency, Cai_2010_Frequency, by = "CONCEPTICON_ID")

overlap_CuCa <- merge(Cuetos_2011_Frequency, Cai_2010_Frequency, by = "CONCEPTICON_ID")

# Show length of data sets
nrow(Brysbaert_2009_Frequency)
nrow(Cuetos_2011_Frequency)
nrow(Cai_2010_Frequency)

# Show overlap between the data sets
nrow(overlap_BCu)
nrow(overlap_BCa)
nrow(overlap_CuCa)

# Test correlations of the variables in the data sets

cor.test(overlap_BCu$ENGLISH_FREQUENCY_LOG, overlap_BCu$SPANISH_FREQUENCY_LOG, method="pearson")
# p-value is < 0.0001

cor.test(overlap_BCa$ENGLISH_FREQUENCY_LOG, overlap_BCa$CHINESE_FREQUENCY_LOG, method="pearson")
# p-value is < 0.0001

cor.test(overlap_CuCa$SPANISH_FREQUENCY_LOG, overlap_CuCa$CHINESE_FREQUENCY_LOG, method="pearson")
# p-value is < 0.0001


# Create plots

a <- ggplot(overlap_BCu, aes(x=ENGLISH_FREQUENCY_LOG, y=SPANISH_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Log10 Frequency", y="English", x = "Spanish") +
  theme_hc(base_size = 24)

b <- ggplot(overlap_BCa, aes(x=ENGLISH_FREQUENCY_LOG, y=CHINESE_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Log10 Frequency", y="English", x = "Chinese") +
  theme_hc(base_size = 24)

c <- ggplot(overlap_CuCa, aes(x=SPANISH_FREQUENCY_LOG, y=CHINESE_FREQUENCY_LOG)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 7)) +
  scale_y_continuous(limits=c(0, 7)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  labs(title= "Distribution of Log10 Frequency", y="Spanish", x = "Chinese") +
  theme_hc(base_size = 24)

# Save plots 
ggsave("./examples/log10-english-spanish.pdf", a, width=11, height=8.5)

ggsave("./examples/log10-english-chinese.pdf", b, width=11, height=8.5)

ggsave("./examples/log10-spanish-chinese.pdf", c, width=11, height=8.5)
