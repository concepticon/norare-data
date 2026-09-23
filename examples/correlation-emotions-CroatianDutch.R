# R version 4.6.1

# Load libraries
library(groundhog)
pkgs <- c("readr","ggplot2", "ggthemes", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2026-09-05")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import Croatian and Dutch emotion rating datasets
Coso_2023_Emotions <- read_delim("datasets/Coso-2023-Emotions/Coso-2023-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

Speed_2024_Emotions <- read_delim("datasets/Speed-2024-Emotions/Speed-2024-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

# Merge data sets on shared Concepticon IDs to find overlapping concepts
Emotions_Croatian_Dutch_overlap <- merge(Coso_2023_Emotions, Speed_2024_Emotions, by = "CONCEPTICON_ID", suffixes = c(".Coso",".Speed"))

# Test correlations between Croatian and Dutch ratings for each emotion
cor.test(Emotions_Croatian_Dutch_overlap$CROATIAN_HAPPINESS_MEAN, Emotions_Croatian_Dutch_overlap$DUTCH_HAPPINESS_MEAN, method="pearson")

cor.test(Emotions_Croatian_Dutch_overlap$CROATIAN_SADNESS_MEAN, Emotions_Croatian_Dutch_overlap$DUTCH_SADNESS_MEAN, method="pearson")

cor.test(Emotions_Croatian_Dutch_overlap$CROATIAN_ANGER_MEAN, Emotions_Croatian_Dutch_overlap$DUTCH_ANGER_MEAN, method="pearson")

cor.test(Emotions_Croatian_Dutch_overlap$CROATIAN_FEAR_MEAN, Emotions_Croatian_Dutch_overlap$DUTCH_FEAR_MEAN, method="pearson")

cor.test(Emotions_Croatian_Dutch_overlap$CROATIAN_DISGUST_MEAN, Emotions_Croatian_Dutch_overlap$DUTCH_DISGUST_MEAN, method="pearson")

# Create scatter plots comparing Croatian vs. Dutch ratings, one per emotion
happiness_plot <- ggplot(Emotions_Croatian_Dutch_overlap, aes(x=CROATIAN_HAPPINESS_MEAN, y=DUTCH_HAPPINESS_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits = c(1, 5), breaks = 1:5) +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 1.2, label.y = 5.2, p.accuracy = 0.0001, size = 5) +
  labs(title = "Happiness", x = "", y = "Speed & Brysbaert (2024)") +
  theme_hc(base_size = 14) +
  theme(
    plot.title = element_text(size = 25),
    axis.title.y = element_text(size = 30)
  )


sadness_plot <- ggplot(Emotions_Croatian_Dutch_overlap, aes(x=CROATIAN_SADNESS_MEAN, y=DUTCH_SADNESS_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits = c(1, 5), breaks = 1:5) +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 1.2, label.y = 5.2, p.accuracy = 0.0001, size = 5) +
  labs(title = "Sadness", x = "", y = "") +
  theme_hc(base_size = 14) +
  theme(plot.title = element_text(size = 25))

anger_plot <- ggplot(Emotions_Croatian_Dutch_overlap, aes(x=CROATIAN_ANGER_MEAN, y=DUTCH_ANGER_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits = c(1, 5), breaks = 1:5) +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 1.2, label.y = 5.2, p.accuracy = 0.0001, size = 5) +
  labs(title = "Anger", x = "Coso et al. (2023)", y = "") +
  theme_hc(base_size = 14) +
  theme(
    plot.title = element_text(size = 25),
    axis.title.x = element_text(size = 30)
  )

fear_plot <- ggplot(Emotions_Croatian_Dutch_overlap, aes(x=CROATIAN_FEAR_MEAN, y=DUTCH_FEAR_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits = c(1, 5), breaks = 1:5) +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 1.2, label.y = 5.2, p.accuracy = 0.0001, size = 5) +
  labs(title = "Fear", x = "", y = "") +
  theme_hc(base_size = 14) +
  theme(plot.title = element_text(size = 25))

disgust_plot <- ggplot(Emotions_Croatian_Dutch_overlap, aes(x=CROATIAN_DISGUST_MEAN, y=DUTCH_DISGUST_MEAN)) + 
  geom_point() + 
  scale_x_continuous(limits = c(1, 5), breaks = 1:5) +
  scale_y_continuous(limits = c(1, 5), breaks = 1:5) +
  geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
  stat_cor(method = "pearson", label.x = 1.2, label.y = 5.2, p.accuracy = 0.0001, size = 5) +
  labs(title = "Disgust", x = "", y = "") +
  theme_hc(base_size = 14) +
  theme(plot.title = element_text(size = 25))

# Arrange all five in a single row
grid.arrange(happiness_plot, sadness_plot, anger_plot, disgust_plot, fear_plot, nrow=1)

affective_g = arrangeGrob(happiness_plot, sadness_plot, anger_plot, disgust_plot, fear_plot, nrow=1)

# Save combined plot to file
ggsave("examples/Emotions_Croatian_Dutch.pdf", affective_g, width=30, height=6.5)

