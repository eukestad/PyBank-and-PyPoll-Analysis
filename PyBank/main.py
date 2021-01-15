import os
import csv
import functools

csvpath = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # print(csvreader)

    # pull out header
    header = next(csvreader)

    #create list to count months
    months=[]
  
    #create variables for Profit/Loss analysis
    pnl = 0
    nettotal = 0
    lastpnl = 0
    delta = 0
    deltatotal = 0
    avgdelta = 0
    maxincrease = {"date":"", "amount":0}
    maxdecrease = {"date":"", "amount":0}

    for row in csvreader: 
        months.append(row[0])
        pnl = int(row[1])
        nettotal = nettotal + pnl
        delta = lastpnl + pnl
        deltatotal = deltatotal + delta
        if delta > 0:
            if delta > int(maxincrease["amount"]):
                maxincrease["date"] = row[0]
                maxincrease["amount"] = delta
        if delta < 0:
            if delta < int(maxdecrease["amount"]):
                maxdecrease["date"] = row[0]
                maxdecrease["amount"] = delta
        lastpnl = pnl

    monthcount = len(months)
    avgdelta = float(deltatotal/monthcount) 

#Begin printing output
print("Financial Analysis")
print("-"*20)

# The total number of months included in the dataset
print(f'Total Months: {monthcount}') 

# The net total amount of "Profit/Losses" over the entire period
print(f'Total: {nettotal}') #format as money

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
print(f'Average Change: {avgdelta}') #format as money

# The greatest increase in profits (date and amount) over the entire period
print(f'Greatest Increase in Profits: {maxincrease["date"]} ({maxincrease["amount"]})') #format as money

# The greatest decrease in losses (date and amount) over the entire period
print(f'Greatest Decrease in Profits: {maxdecrease["date"]} ({maxdecrease["amount"]})') #format as money