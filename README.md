# CSVToss
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV 
# Tested with: PluMA 1.1, Python 3.6
# Dependency:

PluMA plugin that takes as input a CSV file and throws away ('tosses')
all entries that are not present in a certain percentage of samples
(assuming samples are rows and entries are columns).

The plugin accepts as input a parameter file of keyword-value pairs:
csvfile: The input CSV file
threshold: Threshold precentage (entries must be in this percentage of 
samples to keep them).

The output CSV file will be the input csvfile with "scarce" entries removed.
