# PyPoll

#![Vote-Counting](Images/Vote_counting.png)
#
#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#
#  * The total number of votes cast
#
#  * A complete list of candidates who received votes
#
#  * The percentage of votes each candidate won
#
#  * The total number of votes each candidate won
#
#  * The winner of the election based on popular vote.
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    RowCount = 0
    VoterIDSet = []
    VoterCountySet = []
    VoterCandidateChoiceSet = []

    csvfile.__next__()

    for row in csvreader:
        VoterIDSet.append(row[0])
        VoterCountySet.append(row[1])
        VoterCandidateChoiceSet.append(row[2])
        RowCount = RowCount + 1
    
    TotalVotes = RowCount

    KhanCount = VoterCandidateChoiceSet.count("Khan")
    KhanPercent = float(round((KhanCount/TotalVotes)*100))

    CorreyCount = VoterCandidateChoiceSet.count("Correy")
    CorreyPercent = float(round((CorreyCount/TotalVotes)*100))

    LiCount = VoterCandidateChoiceSet.count("Li")
    LiPercent = float(round((LiCount/TotalVotes)*100))

    OTooleyCount = VoterCandidateChoiceSet.count("O'Tooley")
    OTooleyPercent = float(round((OTooleyCount/TotalVotes)*100))

    CandidateNames = []
    CandidateNames = ["Khan", "Correy", "Li", "O'Tooley"]

    CandidateCounts = []
    CandidateCounts = [KhanCount, CorreyCount, LiCount, OTooleyCount]

    maxCountIndex = CandidateCounts.index(max(CandidateCounts))
    winnerName = CandidateNames[maxCountIndex]

    line01 = "Election Results"
    line02 = "-------------------------"
    line03 = f"Total Votes: {TotalVotes}"
    line04 = "-------------------------"
    line05 = f"Khan: {KhanPercent}% ({KhanCount})"
    line06 = f"Correy: {CorreyPercent}% ({CorreyCount})"
    line07 = f"Li: {LiPercent}% ({LiCount})"
    line08 = f"O'Tooley: {OTooleyPercent}% ({OTooleyCount})"
    line09 = "-------------------------"
    line10 = f"Winner {winnerName}"
    line11 = "-------------------------"

    print(line01)
    print(line02)
    print(line03)
    print(line04)
    print(line05)
    print(line06)
    print(line07)
    print(line08)
    print(line09)
    print(line10)
    print(line11)

    pollResults = open("pollResults.txt", "w")
    pollResults.write(line01+"\n")
    pollResults.write(line02+"\n")
    pollResults.write(line03+"\n")
    pollResults.write(line04+"\n")
    pollResults.write(line05+"\n")
    pollResults.write(line06+"\n")
    pollResults.write(line07+"\n")
    pollResults.write(line08+"\n")
    pollResults.write(line09+"\n")
    pollResults.write(line10+"\n")
    pollResults.write(line11+"\n")
