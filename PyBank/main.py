import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 1
net_total = 0
monthly_change = 0
monthly_change_list = []

max_monthly_increase = ["", 0]
max_monthly_decrease = ["", 0]

# Open and read csv
with open(csvpath) as budget_data:
    reader = csv.reader(budget_data)
        
    header = next(reader) # skips header
    previous_month = next(reader)  
    net_total = int(previous_month[1])
    
    for row in reader:
        total_months += 1 # adds 1 for each row
        net_total += int(row[1])
        monthly_change = int(row[1]) - int(previous_month[1]) 
        previous_month = row
        monthly_change_list.append(monthly_change)

        if monthly_change > max_monthly_increase[1]:
            max_monthly_increase[0] = row[0]
            max_monthly_increase[1] = monthly_change

        if monthly_change < max_monthly_decrease[1]:
            max_monthly_decrease[0] = row[0]
            max_monthly_decrease[1] = monthly_change


    monthly_average = sum(monthly_change_list) / len(monthly_change_list)

output = (
    f"Financial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profit: ${net_total}\n"
    f"Average Change: ${monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {max_monthly_increase[0]} (${max_monthly_increase[1]})\n"
    f"Greatest Decrease in Profits: {max_monthly_decrease[0]} (${max_monthly_decrease[1]})\n")
print(output)    

output_path = open('Analysis/Financial_Analysis.txt', 'w')
output_path.write(output)
output_path.close()
  

        

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.