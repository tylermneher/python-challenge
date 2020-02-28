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

csvpath = os.path.join('/python-challenge/PyBank/budget_data.csv')

MonthToMonth = []
MonthYear = []
NetProfitLossTOTAL = 0
MonthDiffSet = []
MonthDiffSetTOTAL = 0

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    RowCount = 0
    csvfile.__next__()
    for row in csvreader:
        MonthToMonth.append(int(row[1]))
        MonthYear.append(row[0])
        RowCount = RowCount + 1
    
    for i in MonthToMonth:
        NetProfitLossTOTAL = NetProfitLossTOTAL + i
    
    LengthMonthToMonth = len(MonthToMonth)

    for x in range(1, LengthMonthToMonth):
        second = float(MonthToMonth[x])
        first = float(MonthToMonth[x-1])
        MonthDiffSet.append(float(second - first))
    

    for i in MonthDiffSet:
        MonthDiffSetTOTAL = MonthDiffSetTOTAL + i
    LengthMonthDiffSet = len(MonthDiffSet)
    AverageChange = int(MonthDiffSetTOTAL/(LengthMonthDiffSet))
    
    minn = MonthDiffSet.index(min(MonthDiffSet))
    maxx = MonthDiffSet.index(max(MonthDiffSet))

    minnMonthYear = MonthYear[minn+1]
    maxxMonthYear = MonthYear[maxx+1]

    # Report
    line1 = "Financial Analysis"
    line2 = "----------------------------"
    line3 = f"Total Months: {RowCount}"
    line4 = f"Total: ${NetProfitLossTOTAL}"
    line5 = f"Average Change: ${AverageChange}"
    line6 = f"Greatest Increase in Profits: {maxxMonthYear} (${int(MonthDiffSet[maxx])})"
    line7 = f"Greatest Decrease in Profits: {minnMonthYear} (${int(MonthDiffSet[minn])})"

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)

    financialAnalysis = open("/python-challenge/PyBank/FinancialAnalysis.txt", "w")
    financialAnalysis.write(line1+"\n")
    financialAnalysis.write(line2+"\n")
    financialAnalysis.write(line3+"\n")
    financialAnalysis.write(line4+"\n")
    financialAnalysis.write(line5+"\n")
    financialAnalysis.write(line6+"\n")
    financialAnalysis.write(line7+"\n")
