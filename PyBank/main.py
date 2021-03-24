import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0

# Open and read csv
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
    

# The total number of months in the dataset
    header = next(reader) # skips header
    for row in reader:
        total_months += 1 # adds 1 for each row

print(f'Total Months: {total_months}')

               



# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.