import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Open and read csv
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
