import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 1
net_total = 0
monthly_change = 0
monthly_change_list = []


# average_change = mean monthly change
# greatest_increase = max monthly change
# greatest_decrease = min monthly change

# create variable that equals month 


# Open and read csv
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
    

# The total number of months in the dataset
# The net total amount of "Profit/Losses" over the entire period
    
    header = next(reader) # skips header
    previous_month = next(reader)  # do we need "header"? 
    net_total = int(previous_month[1])
    for row in reader:
        total_months += 1 # adds 1 for each row
        
        net_total += int(row[1])

        
        
        monthly_change = int(row[1]) - int(previous_month[1]) 
        
        previous_month = row
        
        monthly_change_list.append(monthly_change)

    monthly_average = sum(monthly_change_list) / len(monthly_change_list)


    print(f'monthly changes: {monthly_change_list}')
    print(f'monthly average: {monthly_average}')


    print(f'previous month: {previous_month}')
    print(f'Total Months: {total_months}') 
    print(f'Net Total Profit: ${net_total}')
    
        


        

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.