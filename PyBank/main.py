# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 1 The total number of months included in the dataset
# 2 The net total amount of "Profit/Losses" over the entire period
# 3 The average of the changes in "Profit/Losses" over the entire period
# 4 The greatest increase in profits (date and amount) over the entire period
# 5 The greatest decrease in losses (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:
# ```text
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
import os
import csv

csvpath = os.path.join('/Users/tylermneher/RU Data Science/TylerRUDataScienceWorkspace/02-Homework/03-Python/python-challenge/PyBank/budget_data.csv')

NetProfitLoss = []
NetProfitLossTOTAL = 0

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    RowCount = 0
    csvfile.__next__()
    for row in csvreader:
        NetProfitLoss.append(float(row[1]))
        RowCount = RowCount + 1
 

    #Report
    print("Financial Analysis")
    print("----------------------------")
    #total num months
    print(f"Total Months: {RowCount}")
    print(f"Total: ${NetProfitLoss}")