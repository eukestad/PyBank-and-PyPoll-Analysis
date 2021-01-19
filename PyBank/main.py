import os
import csv
# import locale

# # set locale to format currency later
# locale.setlocale( locale.LC_ALL, '' )

# #function to calculate average
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length

# import budget data in csv file
csvpath = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # print(csvreader)

    # pull out header
    header = next(csvreader)

    #create lists to count months and calculate average change and max/min change
    months=[]
    delta_list = []
    maxincrease = {"date":"", "amount":0}
    maxdecrease = {"date":"", "amount":0}
    
  
    #create variables for Profit/Loss analysis
    pnl = 0
    nettotal = 0
    lastpnl = 0
    delta = 0
    deltatotal = 0
    avgdelta = 0.0


    for row in csvreader: 
        months.append(row[0])
        pnl = int(row[1])
        nettotal = nettotal + pnl
        delta = pnl - lastpnl
        delta_list.append(delta)
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

# get final variables before printing output
monthcount = len(months)
# avgdelta = average(delta_list)
avgdelta = sum(delta_list)/len(delta_list)

# # Format variables as money
# nettotal = locale.currency(nettotal)
# avgdelta = locale.currency(avgdelta)

with open("Output.txt", "w") as text_file:

    #Begin printing output
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