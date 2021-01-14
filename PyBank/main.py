import os
import csv
import functools

csvpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # print(csvreader)

    budgetdata=[]

    for row in csvreader: 
        # print(row)
        budgetdata.append(row)


# The total number of months included in the dataset
    print(budgetdata.count(*))
# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period