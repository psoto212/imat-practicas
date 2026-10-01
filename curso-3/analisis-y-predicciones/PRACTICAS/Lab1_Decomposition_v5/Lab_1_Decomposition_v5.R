##############################################################################
#############       Lab Practice 1: Decomposition Methods     ################
##############################################################################

# Load libraries
library(fpp2) 
library(tidyverse)
library(readxl)

# Set working directory ---------------------------------------------------------------------------------------------
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# Load dataset from text file ---------------------------------------------------------------------------------------
fdata <- read.table("Unemployment.dat", sep = ",", header = TRUE)

# Object inspection
fdata
class(fdata)
str(fdata)
summary(fdata)
glimpse(fdata)

# Reading Excel files
fdata_excel <- read_excel("Unemployment.xlsx")
fdata_excel
glimpse(fdata_excel)

# What is the frequency of observation for this data? 

# Date format
# Two options:
#   as.Date("2014-5-12")
#   as.POSIXct("2014-5-12 20:05:35", tz = "EST")

# Symbol Meaning Example (see https://r4ds.hadley.nz/datetimes.html)
#   %a    Abbreviated weekday name in the current locale on this platform     Sun, Mon, Thu
#   %A    Full weekday name in the current locale                             Sunday, Monday, Thursday
#   %b    Abbreviated month name in the current locale on this platform       Jan, Feb, Mar
#   %B    Full month name in the current locale                               January, February, March
#   %d    Day of the month as a decimal number                                01, 02, 03
#   %m    Month as a decimal number                                           01, 02, 03
#   %y    A year without a century (two-digit)                                18
#   %Y    A year with a century (four-digit)                                  2018


fdata$DATE1 <- as.Date(fdata$DATE, format = "%d/%m/%Y") # Convert DATE from char to date (Date or DateTime)
fdata$DATE2 <- as.POSIXct(fdata$DATE, format = "%d/%m/%Y")

fdata$DATE <- as.Date(fdata$DATE, format = "%d/%m/%Y")

# Selecting columns
fdata <- select(fdata, c(DATE, TOTAL))
#fdata <- select(fdata, -c(DATE1, DATE2))
str(fdata)

# Check for missing dates
fdata <- arrange(fdata, DATE)
glimpse(fdata)

# How do we know if there are time gaps in the data?
range(fdata$DATE)
min(fdata$DATE)
max(fdata$DATE)

# Therefore we can create a complete sequence of months with the same range and
# compare it to the dates in our data.
date_range <- seq.Date(min(fdata$DATE), max(fdata$DATE), by = "months")

head(date_range)
tail(date_range)

# Now we do the comparison
date_range[!date_range %in% fdata$DATE] 

# Check for NAs
sum(is.na(fdata$TOTAL))

# Convert to time series object
# start -> (periodo, subperiodo) -> ()
# frequency = 12 -> monthly data
# frequency = 4 -> quarterly data
y <- ts(fdata$TOTAL, start = c(2010,1), frequency = 12)

#Plot time series:
autoplot(y) +
  ggtitle("Unemployment in Spain") +
  xlab("Year") + ylab("Number unemployed")

# or:
plot.ts(y, 
        main="Unemployment in Spain",
        xlab="Year",
        ylab="Number unemployed")

# Select time series time frame
y <- window(y, start = c(2010,1), end = c(2019,12))

# or:
y <- ts(fdata$TOTAL, start = c(2010,1), end = c(2019,12), frequency = 12)

#Plot time series
autoplot(y) +
  ggtitle("Unemployment in Spain") +
  xlab("Year") + ylab("Number unemployed")


#################################################################################
# Decomposition methods
#################################################################################


## Classical additive decomposition
y_dec_add <- decompose(y,type="additive")
autoplot(y_dec_add) + xlab("Year") +
  ggtitle("Classical additive decomposition")


## Classical Multiplicative decomposition
y_dec_mult <- decompose(y, type="multiplicative")
autoplot(y_dec_mult) + xlab("Year") +
  ggtitle("Classical multiplicative decomposition")


## SEATS
library(seasonal)
y_dec_seas <- seas(y)
autoplot(y_dec_seas) + xlab("Year") +
  ggtitle("SEATS decomposition")


# Use seasonal(), trendcycle() and remainder() functions to extract the individual components.
# Use seasadj() to compute the seasonally adjusted time series.

#Compare seasonal components
autoplot(seasonal(y_dec_mult), series = "Multiplicative") +
  forecast::autolayer(seasonal(y_dec_seas), series = "SEATS")


#Compare seasonal adjustment components (i.e. subtracting the seasonal component from the raw series)
autoplot(seasadj(y_dec_add), series = "Additive") +
  forecast::autolayer(seasadj(y_dec_mult), series = "Multiplicative") +
  forecast::autolayer(seasadj(y_dec_seas),series = "SEATS")

autoplot(seasadj(y_dec_seas), series = "SEATS")

#Seasonal subseries plot
ggsubseriesplot(seasonal(y_dec_add)) 
ggsubseriesplot(seasonal(y_dec_mult)) 
ggsubseriesplot(seasonal(y_dec_seas)) 


