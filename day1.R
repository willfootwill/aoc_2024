library(tidyverse)
df <- readr::read_delim("input/day1", delim = "   ", col_names = FALSE, show_col_types = FALSE)
sum(abs(sort(df$X1) - sort(df$X2)))

