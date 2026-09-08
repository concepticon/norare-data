# R version 4.6.1

# Load libraries
library(groundhog)
pkgs <- c("readr","ggplot2", "ggthemes", "ggpubr", "gridExtra")
groundhog.library(pkgs, "2026-09-05")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import Croatian and German emotion rating datasets
Coso_2023_Emotions <- read_delim("datasets/Coso-2023-Emotions/Coso-2023-Emotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

Briesemeister_2011_DiscreteEmotions <- read_delim("datasets/Briesemeister-2011-DiscreteEmotions/Briesemeister-2011-DiscreteEmotions.tsv", "\t", escape_double = FALSE, col_types = cols(CONCEPTICON_ID = col_integer()), trim_ws = TRUE)

# Merge data sets on shared Concepticon IDs to find overlapping concepts
Emotions_Croatian_German_overlap <- merge(Coso_2023_Emotions, Briesemeister_2011_DiscreteEmotions, by = "CONCEPTICON_ID", suffixes = c(".Coso",".Briesemeister"))

# Test correlations between Croatian and German ratings for each emotion
cor.test(Emotions_Croatian_German_overlap$CROATIAN_DISGUST_MEAN, Emotions_Croatian_German_overlap$GERMAN_DISGUST_MEAN, method="pearson")

cor.test(Emotions_Croatian_German_overlap$CROATIAN_ANGER_MEAN, Emotions_Croatian_German_overlap$GERMAN_ANGER_MEAN, method="pearson")

cor.test(Emotions_Croatian_German_overlap$CROATIAN_FEAR_MEAN, Emotions_Croatian_German_overlap$GERMAN_FEAR_MEAN, method="pearson")

cor.test(Emotions_Croatian_German_overlap$CROATIAN_HAPPINESS_MEAN, Emotions_Croatian_German_overlap$GERMAN_HAPPINESS_MEAN, method="pearson")

cor.test(Emotions_Croatian_German_overlap$CROATIAN_SADNESS_MEAN, Emotions_Croatian_German_overlap$GERMAN_SADNESS_MEAN, method="pearson")

# Create scatter plots comparing Croatian vs. German ratings, one per emotion
disgust_plot2 <- ggplot(Emotions_Croatian_German_overlap, aes(x=CROATIAN_DISGUST_MEAN, y=GERMAN_DISGUST_MEAN)) + 
     geom_point() + 
     scale_x_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     scale_y_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
     stat_cor(method = "pearson", label.x = 1.2, label.y = 4.8, p.accuracy = 0.0001, size = 10) +
     labs(title = "Disgust", x = "Coso et al. (2023)", y = "Briesemeister et al. (2011)") +
     theme_hc(base_size = 30)

fear_plot2 <- ggplot(Emotions_Croatian_German_overlap, aes(x=CROATIAN_FEAR_MEAN, y=GERMAN_FEAR_MEAN)) + 
     geom_point() + 
     scale_x_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     scale_y_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
     stat_cor(method = "pearson", label.x = 1.2, label.y = 4.8, p.accuracy = 0.0001, size = 10) +
     labs(title = "Fear", x = "Coso et al. (2023)", y = "Briesemeister et al. (2011)") +
     theme_hc(base_size = 30)

anger_plot2 <- ggplot(Emotions_Croatian_German_overlap, aes(x=CROATIAN_ANGER_MEAN, y=GERMAN_ANGER_MEAN)) + 
     geom_point() + 
     scale_x_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     scale_y_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
     stat_cor(method = "pearson", label.x = 1.2, label.y = 4.8, p.accuracy = 0.0001, size = 10) +
     labs(title = "Anger", x = "Coso et al. (2023)", y = "Briesemeister et al. (2011)") +
     theme_hc(base_size = 30)

sadness_plot2 <- ggplot(Emotions_Croatian_German_overlap, aes(x=CROATIAN_SADNESS_MEAN, y=GERMAN_SADNESS_MEAN)) + 
     geom_point() + 
     scale_x_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     scale_y_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
     stat_cor(method = "pearson", label.x = 1.2, label.y = 4.8, p.accuracy = 0.0001, size = 10) +
     labs(title = "Sadness", x = "Coso et al. (2023)", y = "Briesemeister et al. (2011)") +
     theme_hc(base_size = 30)

happiness_plot2 <- ggplot(Emotions_Croatian_German_overlap, aes(x=CROATIAN_HAPPINESS_MEAN, y=GERMAN_HAPPINESS_MEAN)) + 
     geom_point() + 
     scale_x_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     scale_y_continuous(limits = c(0.5, 5.5), breaks = 1:5) +
     geom_smooth(method = "gam", formula = y ~ x, se=TRUE, fullrange=FALSE, level=0.95) +
     stat_cor(method = "pearson", label.x = 1.2, label.y = 4.8, p.accuracy = 0.0001, size = 10) +
     labs(title = "Happiness", x = "Coso et al. (2023)", y = "Briesemeister et al. (2011)") +
     theme_hc(base_size = 30)

# Preview all five plots together in a 2-row grid
grid.arrange(happiness_plot2, sadness_plot2, anger_plot2, disgust_plot2, fear_plot2, nrow=2)

# Combine plots into a single grob object for saving
affective_g = arrangeGrob(happiness_plot2, sadness_plot2, anger_plot2, disgust_plot2, fear_plot2, nrow=2)

# Save combined plot to file
ggsave("examples/Emotions_Croatian_German.pdf", affective_g, width=20, height=20)