# R version 4.6.1

# Load libraries
library(groundhog)
pkgs <- c("readr", "dplyr", "ggplot2", "ggwordcloud", "magick")
groundhog.library(pkgs, "2026-09-01")

# Set working directory to NoRaRe repository (please adapt the path accordingly)
setwd("./concepticon/norare-data/")

# Import norare data
norare <- read_delim("norare.tsv", "\t", trim_ws = TRUE)

# Count entries by TYPE, for word cloud sizing
type_counts <- norare %>%
  count(TYPE, name = "Count") %>%
  arrange(desc(Count))

# Merge valence subcategories (neutral, positive, negative) into a single "valence" category
type_counts <- type_counts %>%
  mutate(TYPE = case_when(
    TYPE %in% c("valence neutral", "valence positive", "valence negative") ~ "valence",
    TRUE ~ TYPE
  )) %>%
  count(TYPE, wt = Count, name = "Count") %>%
  arrange(desc(Count))

# Remove types that only occur once
type_counts <- type_counts %>%
  filter(Count > 1)

#adjust sizing of words
type_counts <- type_counts %>%
  mutate(Size = Count^1.3)

# Generate word cloud
# lower eccentricity widens the packing area
set.seed(42)  # for reproducible layout

wc <- ggplot(type_counts, aes(label = TYPE, size = Count, color = Count)) +
  geom_text_wordcloud_area(shape = "square", rm_outside = TRUE, eccentricity = 1) +
  scale_size_area(max_size = 40) +
  scale_color_viridis_c() +
  theme_void() +
  theme(plot.margin = margin(0, 0, 0, 0))

wc

# Build the plot object
wc_built <- ggplot_build(wc)

# Extract the real bounding box of the placed words (accounting for text size/extent)
x_range <- range(wc_built$data[[1]]$xmin, wc_built$data[[1]]$xmax, na.rm = TRUE)
y_range <- range(wc_built$data[[1]]$ymin, wc_built$data[[1]]$ymax, na.rm = TRUE)

# Rebuild the plot with tightly fitted axis limits and zero expansion
wc_final <- wc +
  scale_x_continuous(limits = x_range, expand = c(0, 0)) +
  scale_y_continuous(limits = y_range, expand = c(0, 0))

wc_final

# Save PNG
ggsave("examples/wordcloud_variables.png", wc_final, width = 14, height = 5.25, dpi = 300, bg = "white")

# Trim any residual border from PNG
img <- image_read("examples/wordcloud_variables.png")
img_trimmed <- image_trim(img)
image_write(img_trimmed, "examples/wordcloud_variables.png")