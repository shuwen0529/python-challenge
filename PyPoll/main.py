# -*- coding: UTF-8 -*-

# Import the os module
import os
import csv

# Read CSV files
csvpath = os.path.join("/Users/shuwenzhang/Desktop/BootCamp/Homework/03-Python/PyPoll/Resources/election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row 
    csv_header = next(csvreader)

    # Lists of data to store 
    candidate_option = []
    candidate_vote   = []
    candidate_vote_percent = []

    # Dictionary of data to store 
    candidate_vote_dic = {}

    # Initial values
    vote_count = 0

    for row in csvreader:
        # total number of votes cast
        vote_count = vote_count +1

        # Get candidate name in the row
        candidate_name = row[2]

        if candidate_name not in candidate_option:
            # Get a new candidate
            candidate_option.append(candidate_name)
            # Initial value to count for a new candidate
            candidate_vote_dic[candidate_name] = 1
        else:
            candidate_vote_dic[candidate_name] = candidate_vote_dic[candidate_name] + 1        


for i in candidate_vote_dic:
    # Retrieve vote count
    vote = candidate_vote_dic.get(i)
    candidate_vote.append(vote)
    # Calculate percentage
    vote_percent = vote / vote_count * 100
    candidate_vote_percent.append (vote_percent)

# Get the winner of the election
winning_candidate = candidate_option[candidate_vote.index(max(candidate_vote))]

# Print the analysis to the terminal
print ('Election Results')
print ('--------------------------------')
print ('Total Votes: '+ str(vote_count))
print ('--------------------------------')
for i in range(len(candidate_option)):
    print (candidate_option[i]+ ': {:.3f}'.format(candidate_vote_percent[i])+'% ('+ str(candidate_vote[i])+')')
print ('--------------------------------')
print ('Winner: '+winning_candidate)

# Export a text file with the results
output = os.path.join('/Users/shuwenzhang/Desktop/BootCamp/Homework/03-Python/SZ_HW#3_PythonChanllege/python-challenge/PyPoll/analysis.txt')

with open(output, 'w', newline='') as new:
    new.write('Election Results')
    new.write("\n")
    new.write('--------------------------------')
    new.write("\n")
    new.write('Total Votes: '+ str(vote_count))
    new.write("\n") 
    new.write('--------------------------------')
    new.write("\n")
    for i in range(len(candidate_option)):
        new.write (candidate_option[i]+ ': {:.3f}'.format(candidate_vote_percent[i])+'% ('+ str(candidate_vote[i])+')')
        new.write("\n")
    new.write('--------------------------------')
    new.write("\n")
    new.write('Winner: '+winning_candidate)
    new.write("\n")
    new.write('--------------------------------')
