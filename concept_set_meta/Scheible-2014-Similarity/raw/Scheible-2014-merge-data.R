# clean workspace
rm(list = ls())

library(tidyverse)
library(readr)
library(unpivotr)


setwd("Desktop/sem-rel-database/exp-rating/")

ADJ_ratings_asANT <- read_table2("ADJ_ratings_asANT.txt", col_names = F)
ADJ_ratings_asHYP <- read_table2("ADJ_ratings_asHYP.txt", col_names = F)
ADJ_ratings_asSYN <- read_table2("ADJ_ratings_asSYN.txt", col_names = F)

adj = rbind.data.frame(ADJ_ratings_asANT, ADJ_ratings_asHYP, ADJ_ratings_asSYN)
adj = add_column(adj, POS = "ADJ")



N_ratings_asANT <- read_table2("N_ratings_asANT.txt", col_names = F)
N_ratings_asHYP <- read_table2("N_ratings_asHYP.txt", col_names = F)
N_ratings_asSYN <- read_table2("N_ratings_asSYN.txt", col_names = F)

noun = rbind.data.frame(N_ratings_asANT, N_ratings_asHYP, N_ratings_asSYN)
noun = add_column(noun, POS = "NOUN")


V_ratings_asANT <- read_table2("V_ratings_asANT.txt", col_names = F)
V_ratings_asHYP <- read_table2("V_ratings_asHYP.txt", col_names = F)
V_ratings_asSYN <- read_table2("V_ratings_asSYN.txt", col_names = F)

verb = rbind.data.frame(V_ratings_asANT, V_ratings_asHYP, V_ratings_asSYN)
verb = add_column(verb, POS = "VERB")

data = rbind.data.frame(adj, noun, verb)

data$scale0 = data$X4*0
data$scale1 = data$X5*1
data$scale2 = data$X6*2
data$scale3 = data$X7*3
data$scale4 = data$X8*4
data$scale5 = data$X9*5

data$score <- rowMeans(subset(data, select = c(scale0,scale1,scale2,scale3,scale4,scale5)), na.rm = TRUE)
data$score = round(data$score,4)

colnames(data)[1] = "Relation"
colnames(data)[2] = "Target"
colnames(data)[3] = "Relatum"
colnames(data)[4] = "rate0"
colnames(data)[5] = "rate1"
colnames(data)[6] = "rate2"
colnames(data)[7] = "rate3"
colnames(data)[8] = "rate4"
colnames(data)[9] = "rate5"
colnames(data)[10] = "Dunno"

data$Pair = paste(data$Target,data$Relatum)

write.csv(data,"data.csv", row.names = FALSE)

