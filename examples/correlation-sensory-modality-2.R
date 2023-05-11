# R version: R-4.3.0

# Load libraries
library(groundhog) # Version 3.1.0
pkgs <- c("readr","ggplot2", "ggthemes", "dplyr", "plyr", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2023-05-01")


# Set working directory to Concepticon repository (please adapt the path accordingly)
setwd("./concepticon/concepticon-data/concepticondata/conceptlists/")

# Import data set
Morucci_2019_643 <- read_delim("Morucci-2019-643.tsv", 
                               delim = "\t", escape_double = FALSE, 
                               trim_ws = TRUE)

Vergallito_2020_1121 <- read_delim("Vergallito-2020-1121.tsv", 
                                   delim = "\t", escape_double = FALSE, 
                                   trim_ws = TRUE)

chinese <- read_delim("Zhong-2022-664.tsv", 
                      delim = "\t", escape_double = FALSE, 
                      trim_ws = TRUE)

# Combine Italian data sets

Morucci_2019_643 = data.frame(Morucci_2019_643[!is.na(Morucci_2019_643$CONCEPTICON_ID),])
Vergallito_2020_1121 = data.frame(Vergallito_2020_1121[!is.na(Vergallito_2020_1121$CONCEPTICON_ID),])

VM <- rbind.fill(Vergallito_2020_1121, Morucci_2019_643)

italian = VM[!duplicated(VM$CONCEPTICON_ID),]

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import data set from NoRaRe
english <- read_delim("datasets/Lynott-2020-Sensorimotor/Lynott-2020-Sensorimotor.tsv", 
                      "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer(), 
                                                                    LINE_IN_SOURCE = col_integer()), 
                      trim_ws = TRUE)


dutch <- read_delim("datasets/Speed-2021-Sensorimotor/Speed-2021-Sensorimotor.tsv", 
                    delim = "\t", escape_double = FALSE, 
                    trim_ws = TRUE)


# Merge data sets 
overlap_EC <- merge(english, chinese, by = "CONCEPTICON_ID", suffixes = c(".English",".Chinese"))
overlap_EI <- merge(english, italian, by = "CONCEPTICON_ID", suffixes = c(".English",".Italian"))
overlap_ED <- merge(english, dutch, by = "CONCEPTICON_ID", suffixes = c(".English",".Dutch"))
overlap_CD <- merge(chinese, dutch, by = "CONCEPTICON_ID", suffixes = c(".Chinese",".Dutch"))
overlap_ID <- merge(italian, dutch, by = "CONCEPTICON_ID", suffixes = c(".Italian",".Dutch"))
overlap_IC <- merge(italian, chinese, by = "CONCEPTICON_ID", suffixes = c(".Italian",".Chinese"))


# Show overlap between the data sets
nrow(overlap_EC)
nrow(overlap_EI)
nrow(overlap_ED)
nrow(overlap_CD)
nrow(overlap_ID)
nrow(overlap_IC)

# Test correlations of the variables in the data sets
cor.test(overlap_EC$ENGLISH_AUDITORY_MEAN, overlap_EC$AUDITORY_MEAN, method="pearson")
cor.test(overlap_EC$ENGLISH_GUSTATORY_MEAN, overlap_EC$GUSTATORY_MEAN, method="pearson")
cor.test(overlap_EC$ENGLISH_HAPTIC_MEAN, overlap_EC$HAPTIC_MEAN, method="pearson")
cor.test(overlap_EC$ENGLISH_OLFACTORY_MEAN, overlap_EC$OLFACTORY_MEAN, method="pearson")
cor.test(overlap_EC$ENGLISH_VISUAL_MEAN, overlap_EC$VISUAL_MEAN, method="pearson")

cor.test(overlap_EI$ENGLISH_AUDITORY_MEAN, overlap_EI$AUDITORY_MEAN, method="pearson")
cor.test(overlap_EI$ENGLISH_GUSTATORY_MEAN, overlap_EI$GUSTATORY_MEAN, method="pearson")
cor.test(overlap_EI$ENGLISH_HAPTIC_MEAN, overlap_EI$HAPTIC_MEAN, method="pearson")
cor.test(overlap_EI$ENGLISH_OLFACTORY_MEAN, overlap_EI$OLFACTORY_MEAN, method="pearson")
cor.test(overlap_EI$ENGLISH_VISUAL_MEAN, overlap_EI$VISUAL_MEAN, method="pearson")

cor.test(overlap_ED$ENGLISH_AUDITORY_MEAN, overlap_ED$DUTCH_AUDITORY_MEAN, method="pearson")
cor.test(overlap_ED$ENGLISH_GUSTATORY_MEAN, overlap_ED$DUTCH_GUSTATORY_MEAN, method="pearson")
cor.test(overlap_ED$ENGLISH_HAPTIC_MEAN, overlap_ED$DUTCH_HAPTIC_MEAN, method="pearson")
cor.test(overlap_ED$ENGLISH_OLFACTORY_MEAN, overlap_ED$DUTCH_OLFACTORY_MEAN, method="pearson")
cor.test(overlap_ED$ENGLISH_VISUAL_MEAN, overlap_ED$DUTCH_VISUAL_MEAN, method="pearson")

cor.test(overlap_CD$AUDITORY_MEAN, overlap_CD$DUTCH_AUDITORY_MEAN, method="pearson")
cor.test(overlap_CD$GUSTATORY_MEAN, overlap_CD$DUTCH_GUSTATORY_MEAN, method="pearson")
cor.test(overlap_CD$HAPTIC_MEAN, overlap_CD$DUTCH_HAPTIC_MEAN, method="pearson")
cor.test(overlap_CD$OLFACTORY_MEAN, overlap_CD$DUTCH_OLFACTORY_MEAN, method="pearson")
cor.test(overlap_CD$VISUAL_MEAN, overlap_CD$DUTCH_VISUAL_MEAN, method="pearson")

cor.test(overlap_ID$AUDITORY_MEAN, overlap_ID$DUTCH_AUDITORY_MEAN, method="pearson")
cor.test(overlap_ID$GUSTATORY_MEAN, overlap_ID$DUTCH_GUSTATORY_MEAN, method="pearson")
cor.test(overlap_ID$HAPTIC_MEAN, overlap_ID$DUTCH_HAPTIC_MEAN, method="pearson")
cor.test(overlap_ID$OLFACTORY_MEAN, overlap_ID$DUTCH_OLFACTORY_MEAN, method="pearson")
cor.test(overlap_ID$VISUAL_MEAN, overlap_ID$DUTCH_VISUAL_MEAN, method="pearson")

cor.test(overlap_IC$AUDITORY_MEAN.Italian, overlap_IC$AUDITORY_MEAN.Chinese, method="pearson")
cor.test(overlap_IC$GUSTATORY_MEAN.Italian, overlap_IC$GUSTATORY_MEAN.Chinese, method="pearson")
cor.test(overlap_IC$HAPTIC_MEAN.Italian, overlap_IC$HAPTIC_MEAN.Chinese, method="pearson")
cor.test(overlap_IC$OLFACTORY_MEAN.Italian, overlap_IC$OLFACTORY_MEAN.Chinese, method="pearson")
cor.test(overlap_IC$VISUAL_MEAN.Italian, overlap_IC$VISUAL_MEAN.Chinese, method="pearson")

# Plots English-Chinese comparison

EC_plot_aud <- ggplot(overlap_EC, aes(x=ENGLISH_AUDITORY_MEAN, y=AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="English", x = "") +
  theme_hc(base_size = 30)

EC_plot_gus <- ggplot(overlap_EC, aes(x=ENGLISH_GUSTATORY_MEAN, y=GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

EC_plot_hap <- ggplot(overlap_EC, aes(x=ENGLISH_HAPTIC_MEAN, y=HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="English", x = "") +
  theme_hc(base_size = 30)

EC_plot_olf <- ggplot(overlap_EC, aes(x=ENGLISH_OLFACTORY_MEAN, y=OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Chinese") +
  theme_hc(base_size = 30)

EC_plot_vis <- ggplot(overlap_EC, aes(x=ENGLISH_VISUAL_MEAN, y=VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="English", x = "Chinese") +
  theme_hc(base_size = 30)

grid.arrange(EC_plot_aud, EC_plot_gus, EC_plot_hap, EC_plot_olf, EC_plot_vis, nrow=3)

EC_g = arrangeGrob(EC_plot_aud, EC_plot_gus, EC_plot_hap, EC_plot_olf, EC_plot_vis, nrow=3)

ggsave("examples/EC_sensory.pdf", EC_g, width=20, height=30)


# Plots English-Italian comparison

EI_plot_aud <- ggplot(overlap_EI, aes(x=ENGLISH_AUDITORY_MEAN, y=AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="English", x = "") +
  theme_hc(base_size = 30)

EI_plot_gus <- ggplot(overlap_EI, aes(x=ENGLISH_GUSTATORY_MEAN, y=GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

EI_plot_hap <- ggplot(overlap_EI, aes(x=ENGLISH_HAPTIC_MEAN, y=HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="English", x = "") +
  theme_hc(base_size = 30)

EI_plot_olf <- ggplot(overlap_EI, aes(x=ENGLISH_OLFACTORY_MEAN, y=OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Italian") +
  theme_hc(base_size = 30)

EI_plot_vis <- ggplot(overlap_EI, aes(x=ENGLISH_VISUAL_MEAN, y=VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="English", x = "Italian") +
  theme_hc(base_size = 30)

grid.arrange(EI_plot_aud, EI_plot_gus, EI_plot_hap, EI_plot_olf, EI_plot_vis, nrow=3)

EI_g = arrangeGrob(EI_plot_aud, EI_plot_gus, EI_plot_hap, EI_plot_olf, EI_plot_vis, nrow=3)

ggsave("examples/EI_sensory.pdf", EI_g, width=20, height=30)


# Plots English-Dutch comparison

ED_plot_aud <- ggplot(overlap_ED, aes(x=ENGLISH_AUDITORY_MEAN, y=DUTCH_AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="English", x = "") +
  theme_hc(base_size = 30)

ED_plot_gus <- ggplot(overlap_ED, aes(x=ENGLISH_GUSTATORY_MEAN, y=DUTCH_GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

ED_plot_hap <- ggplot(overlap_ED, aes(x=ENGLISH_HAPTIC_MEAN, y=DUTCH_HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="English", x = "") +
  theme_hc(base_size = 30)

ED_plot_olf <- ggplot(overlap_ED, aes(x=ENGLISH_OLFACTORY_MEAN, y=DUTCH_OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Dutch") +
  theme_hc(base_size = 30)

ED_plot_vis <- ggplot(overlap_ED, aes(x=ENGLISH_VISUAL_MEAN, y=DUTCH_VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="English", x = "Dutch") +
  theme_hc(base_size = 30)

grid.arrange(ED_plot_aud, ED_plot_gus, ED_plot_hap, ED_plot_olf, ED_plot_vis, nrow=3)

ED_g = arrangeGrob(ED_plot_aud, ED_plot_gus, ED_plot_hap, ED_plot_olf, ED_plot_vis, nrow=3)

ggsave("examples/ED_sensory.pdf", ED_g, width=20, height=30)


# Plots Chinese-Dutch comparison

CD_plot_aud <- ggplot(overlap_CD, aes(x=AUDITORY_MEAN, y=DUTCH_AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="Chinese", x = "") +
  theme_hc(base_size = 30)

CD_plot_gus <- ggplot(overlap_CD, aes(x=GUSTATORY_MEAN, y=DUTCH_GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

CD_plot_hap <- ggplot(overlap_CD, aes(x=HAPTIC_MEAN, y=DUTCH_HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="Chinese", x = "") +
  theme_hc(base_size = 30)

CD_plot_olf <- ggplot(overlap_CD, aes(x=OLFACTORY_MEAN, y=DUTCH_OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Dutch") +
  theme_hc(base_size = 30)

CD_plot_vis <- ggplot(overlap_CD, aes(x=VISUAL_MEAN, y=DUTCH_VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="Chinese", x = "Dutch") +
  theme_hc(base_size = 30)

grid.arrange(CD_plot_aud, CD_plot_gus, CD_plot_hap, CD_plot_olf, CD_plot_vis, nrow=3)

CD_g = arrangeGrob(CD_plot_aud, CD_plot_gus, CD_plot_hap, CD_plot_olf, CD_plot_vis, nrow=3)

ggsave("examples/CD_sensory.pdf", CD_g, width=20, height=30)

# Plots Italian-Dutch comparison

ID_plot_aud <- ggplot(overlap_ID, aes(x=AUDITORY_MEAN, y=DUTCH_AUDITORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="Italian", x = "") +
  theme_hc(base_size = 30)

ID_plot_gus <- ggplot(overlap_ID, aes(x=GUSTATORY_MEAN, y=DUTCH_GUSTATORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

ID_plot_hap <- ggplot(overlap_ID, aes(x=HAPTIC_MEAN, y=DUTCH_HAPTIC_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="Italian", x = "") +
  theme_hc(base_size = 30)

ID_plot_olf <- ggplot(overlap_ID, aes(x=OLFACTORY_MEAN, y=DUTCH_OLFACTORY_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Dutch") +
  theme_hc(base_size = 30)

ID_plot_vis <- ggplot(overlap_ID, aes(x=VISUAL_MEAN, y=DUTCH_VISUAL_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="Italian", x = "Dutch") +
  theme_hc(base_size = 30)

grid.arrange(ID_plot_aud, ID_plot_gus, ID_plot_hap, ID_plot_olf, ID_plot_vis, nrow=3)

ID_g = arrangeGrob(ID_plot_aud, ID_plot_gus, ID_plot_hap, ID_plot_olf, ID_plot_vis, nrow=3)

ggsave("examples/ID_sensory.pdf", ID_g, width=20, height=30)

# Plots Italian-Chinese comparison

IC_plot_aud <- ggplot(overlap_IC, aes(x=AUDITORY_MEAN.Italian, y=AUDITORY_MEAN.Chinese)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Auditory",  y="Italian", x = "") +
  theme_hc(base_size = 30)

IC_plot_gus <- ggplot(overlap_IC, aes(x=GUSTATORY_MEAN.Italian, y=GUSTATORY_MEAN.Chinese)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Gustatory",  y="", x = "") +
  theme_hc(base_size = 30)

IC_plot_hap <- ggplot(overlap_IC, aes(x=HAPTIC_MEAN.Italian, y=HAPTIC_MEAN.Chinese)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Haptic",  y="Italian", x = "") +
  theme_hc(base_size = 30)

IC_plot_olf <- ggplot(overlap_IC, aes(x=OLFACTORY_MEAN.Italian, y=OLFACTORY_MEAN.Chinese)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Olfactory",  y="", x = "Chinese") +
  theme_hc(base_size = 30)

IC_plot_vis <- ggplot(overlap_IC, aes(x=VISUAL_MEAN.Italian, y=VISUAL_MEAN.Chinese)) + 
  geom_point() + 
  scale_x_continuous(limits=c(0, 5)) +
  scale_y_continuous(limits=c(0, 5)) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 0.5, label.y = 4.75, p.accuracy = 0.0001, size = 10) +
  labs(title= "Visual",  y="Italian", x = "Chinese") +
  theme_hc(base_size = 30)

grid.arrange(IC_plot_aud, IC_plot_gus, IC_plot_hap, IC_plot_olf, IC_plot_vis, nrow=3)

IC_g = arrangeGrob(IC_plot_aud, IC_plot_gus, IC_plot_hap, IC_plot_olf, IC_plot_vis, nrow=3)

ggsave("examples/IC_sensory.pdf", IC_g, width=20, height=30)
