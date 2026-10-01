##############################################################################
#############       Lab Practice 1: Decomposition Methods     ################
##############################################################################

# Load libraries
library(fpp2)
library(tidyverse)
library(seasonal)

# Set working directory
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
getwd()

# Load dataset: canadian_gas.csv
# Relative path
fdata <- read.table("canadian_gas.csv", sep = ",", header = TRUE)

# Absolute path
abs_path <- normalizePath("canadian_gas.csv")
fdata_abs <- read.table(abs_path, sep = ",", header = TRUE)

# Object inspection
fdata
class(fdata)
str(fdata)
summary(fdata)
glimpse(fdata)

# Columns: unique_id (constant, identifies the series), ds (date) and y (production).
# As we only need ds and y -> remove unique_id.
fdata <- select(fdata, c(ds, y))
fdata <- rename(fdata, DATE = ds, PRODUCTION = y)

# Analyse the data
# Convert date from text to Date
fdata$DATE <- as.Date(fdata$DATE, format = "%Y-%m-%d")

# Explore types, ranges and extreme values
str(fdata)
summary(fdata)
range(fdata$DATE)
min(fdata$DATE)
max(fdata$DATE)
min(fdata$PRODUCTION)
max(fdata$PRODUCTION)

# Sort observations by date
fdata <- arrange(fdata, DATE)

# Check for time gaps in the data
date_range <- seq.Date(min(fdata$DATE), max(fdata$DATE), by = "months")
head(date_range)
tail(date_range)
date_range[!date_range %in% fdata$DATE]

# Check for missing values
sum(is.na(fdata$PRODUCTION))

# Time series
# Monthly data (frequency = 12), starting January 1960
y <- ts(fdata$PRODUCTION, start = c(1960, 1), frequency = 12)

# Plot the full time series
autoplot(y) +
  ggtitle("Canadian Gas Production (1960-2005)") +
  xlab("Year") + ylab("Production")

# Plot the last 12 months of the series: March 2004 - February 2005
y_last_year <- window(y, start = c(2004, 3), end = c(2005, 2))

autoplot(y_last_year) +
  ggtitle("Canadian Gas Production - Last 12 Months") +
  xlab("Year") + ylab("Production")

##############################################################################
# Decomposition methods
##############################################################################

# Additive decomposition
y_dec_add <- decompose(y, type = "additive")

autoplot(y_dec_add) +
  xlab("Year") +
  ggtitle("Classical additive decomposition")

# Multiplicative decomposition
y_dec_mult <- decompose(y, type = "multiplicative")

autoplot(y_dec_mult) +
  xlab("Year") +
  ggtitle("Classical multiplicative decomposition")

# SEATS decomposition
y_dec_seas <- seas(y)

autoplot(y_dec_seas) +
  xlab("Year") +
  ggtitle("SEATS decomposition")

# Store and compare seasonally adjusted series:
# multiplicative decomposition and SEATS
sa_mult <- seasadj(y_dec_mult)
sa_seats <- seasadj(y_dec_seas)

autoplot(sa_mult, series = "Multiplicative") +
  forecast::autolayer(sa_seats, series = "SEATS") +
  ggtitle("Seasonally adjusted series: Multiplicative vs SEATS") +
  xlab("Year") + ylab("Adjusted production")

# Compare seasonal components:
# multiplicative decomposition and SEATS
autoplot(seasonal(y_dec_mult), series = "Multiplicative") +
  forecast::autolayer(seasonal(y_dec_seas), series = "SEATS") +
  ggtitle("Seasonal component: Multiplicative vs SEATS") +
  xlab("Year")

# Seasonal subseries plots
ggsubseriesplot(seasonal(y_dec_add)) +
  ggtitle("Subseries - Additive seasonal component")

ggsubseriesplot(seasonal(y_dec_mult)) +
  ggtitle("Subseries - Multiplicative seasonal component")

ggsubseriesplot(seasonal(y_dec_seas)) +
  ggtitle("Subseries - SEATS seasonal component")
