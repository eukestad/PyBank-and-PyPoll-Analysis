import os
import csv

# create lists to store data
votes=[]
candidates = []
percentages = []
votetotals = []

# import data
csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # pull out header
    header = next(csvreader)

    # append data into memory list for use later and get unique list of candidates
    for row in csvreader:
        votes.append(row)
        if row[2] not in candidates:
            candidates.append(row[2])

# get total votes cast
total = len(votes)

# itereate through candidate list and write totals and % to lists
for candidate in candidates:
    votetotal = 0

    for vote in votes:
        if candidate == vote[2]:
            votetotal = votetotal + 1
        else: 
            votetotal = votetotal

    # get vote totals and % for each candidate
    percent = round((votetotal/total)*100,3)
    percentages.append(percent)
    votetotals.append(votetotal)

# zip all lists together so the candidate is in list with their % and vote total
allresults = [list(a) for a in zip(candidates, percentages, votetotals)]

# get winner
def getwinner(resultlist):
    mostvotes = max([votelist[-1] for votelist in resultlist])

    for result in resultlist:
        if result[2]==mostvotes:
            winner = result[0]
        
    return winner

winner = getwinner(allresults)

#Print to terminal
print("Election Results")
print("-"*20)
print(f"Total Votes: {total}")
print("-"*20)
for result in allresults:
    printline = str(f'{result[0]}: {result[1]}00% ({result[2]})')
    print(printline)
print("-"*20)
print(f"Winner: {winner}")
print("-"*20)

#Print to text file
outpath = os.path.join('Analysis','Output.txt')

with open(outpath, "w") as text_file:
    print("Election Results",file=text_file)
    print("-"*20,file=text_file)
    print(f"Total Votes: {total}",file=text_file)
    print("-"*20,file=text_file)
    for result in allresults:
        printline = str(f'{result[0]}: {result[1]}00% ({result[2]})')
        print(printline,file=text_file)
    print("-"*20,file=text_file)
    print(f"Winner: {winner}",file=text_file)
    print("-"*20,file=text_file)