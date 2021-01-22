import os
import csv

#create lists and dictionaries
budget_data = []
amounts = []
delta_list = []
maxincrease = {"date":"", "amount":0}
maxdecrease = {"date":"", "amount":0}

# import budget data in csv file
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # pull out header
    header = next(csvreader)

    # append data into memory list for use later 
    for row in csvreader:
        budget_data.append(row)

# get total months
monthcount = len(budget_data)

# separate amounts from all budget data and calculate net total
amounts = [int(item[-1]) for item in budget_data]
nettotal = sum(amounts)

# iterate through budget data and compare changes to get the average change
for previous, current in zip(budget_data,budget_data[1:]):
    
    delta = int(current[1]) - int(previous[1])
    delta_list.append(delta)
    if delta > 0:
        if delta > int(maxincrease["amount"]):
            maxincrease["date"] = row[0]
            maxincrease["amount"] = delta
    if delta < 0:
        if delta < int(maxdecrease["amount"]):
            maxdecrease["date"] = row[0]
            maxdecrease["amount"] = delta
    
avgdelta = round(sum(delta_list)/len(delta_list),2)

#print to terminal
print("Financial Analysis")
print("-"*20)
# The total number of months included in the dataset
print(f'Total Months: {monthcount}') 
# The net total amount of "Profit/Losses" over the entire period
print(f'Total: ${nettotal}') 
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average Change: ${avgdelta}') 
# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {maxincrease["date"]} (${maxincrease["amount"]})') 
# The greatest decrease in losses (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {maxdecrease["date"]} (${maxdecrease["amount"]})') 

#print to text file
outpath = os.path.join('Analysis','Output.txt')

with open(outpath, "w") as text_file:
    print("Financial Analysis",file=text_file)
    print("-"*20,file=text_file)
    # The total number of months included in the dataset
    print(f'Total Months: {monthcount}',file=text_file) 
    # The net total amount of "Profit/Losses" over the entire period
    print(f'Total: ${nettotal}',file=text_file) 
    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    print(f'Average Change: ${avgdelta}',file=text_file) 
    # The greatest increase in profits (date and amount) over the entire period
    print(f'Greatest Increase in Profits: {maxincrease["date"]} (${maxincrease["amount"]})',file=text_file) 
    # The greatest decrease in losses (date and amount) over the entire period
    print(f'Greatest Decrease in Profits: {maxdecrease["date"]} (${maxdecrease["amount"]})',file=text_file) 