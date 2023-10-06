# this is the start of the pypoll file
# author: chris burk
# start somewhere 

import os 
import csv

# set path

pypoll = os.path.join("Resources","election_data.csv")
analysistxt = os.path.join("analysis", "election_analysis.txt")


# Create lists and init

count = 0
candlist = []
unique_cand = []
vote_count = []
vote_percent = []

# open csv

with open(pypoll, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Does the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the unique candidate names to candlist
        candlist.append(row[2])
        #this part makes a set from unique candidate names
    for cand in set(candlist):
        unique_cand.append(cand)
        # total is the total number of votes per candidate
        total = candlist.count(cand)
        vote_count.append(total)
        # percent is the percent of total votes per candidate
        percent = round((total/count)*100,2)
        vote_percent.append(percent)
        
    winning_vote_count = max(vote_count)
    winner = unique_cand[vote_count.index(winning_vote_count)]
     
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_cand)):
            print(unique_cand[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# this outputs to a txt file, rounded two decimal points per winner, in the proper directory with the same trick i learned from doing pybank

with open(analysistxt, 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_cand))):
        text.write(unique_cand[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")