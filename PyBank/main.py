import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 1
net_total = 0
monthly_change = 0
monthly_change_list = []
months = []

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
    previous_month = next(reader)  
    net_total = int(previous_month[1])
    for row in reader:
        total_months += 1 # adds 1 for each row
        
        net_total += int(row[1])
       
        monthly_change = int(row[1]) - int(previous_month[1]) 
        
        previous_month = row
        
        monthly_change_list.append(monthly_change)

    monthly_average = sum(monthly_change_list) / len(monthly_change_list)
    
    max_monthly_increase = max(monthly_change_list)
    max_monthly_decrease = min(monthly_change_list)

    # matching appropriate month with max increase and max decrease
    max_increase_month = monthly_change_list.index(max(monthly_change_list)) + 1
    max_decrease_month = monthly_change_list.index(min(monthly_change_list)) + 1

   #  max_month = max_increase_month.append(row[0])



    # print(f'monthly changes: {monthly_change_list}') # Testing
    # print(f'previous month: {previous_month}') # Testing
    # print(f'max increase: {max_month}') Testing
    # print(f'max increase: {max_month}')


    print(f'max monthly increase: ${max_monthly_increase}')
    print(f'max monthly decrease: ${max_monthly_decrease}')
    print(f'monthly average: ${monthly_average:.2f}')
    print(f'Total Months: {total_months}') 
    print(f'Net Total Profit: ${net_total}')
    

#   output = (
#         f"Financial Analysis\n"
#         f"------------------------\n"
#         f"Total Months: {total_months}\n"
#         f"Total Profit: ${net_total}\n"
#         f"Average Change: ${monthly_average: .2f}\n"
#         f"Greatest Increase in Profits: \n"
#         f"Greatest Decrease in Profits: \n")
#     print(output)


    #specify file to write to
output_path = os.path.join("Analysis", "Financial_Analysis.txt")   
with open(output_path, 'w', newline = '') as txt_file:
    csvwriter = csv.writer(txt_file)
    csvwriter.writerow(['Financial Analysis'])
        # f"Financial Analysis\n"
        # f"------------------------\n"
        # f"Total Months: {total_months}\n"
        # f"Total Profit: ${net_total}\n"
        # f"Average Change: ${monthly_average: .2f}\n"
        # f"Greatest Increase in Profits: \n"
        # f"Greatest Decrease in Profits: \n")
    
    # print(output)

        

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.