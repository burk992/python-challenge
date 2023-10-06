# this is the start of the pybank file
# author: chris burk


# start somewhere 

import os 
import csv

# set path
pybank = os.path.join("Resources","budget_data.csv")
finatxt = os.path.join("analysis", "financial_analysis.txt")

# make lists
profit = []
month_change = []
date = []

#init var
count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

#open csv
with open(pybank, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #objective 1: start ask and then count months in the data
    for row in csvreader:
        count = count + 1 
    
    #making date for later
        date.append(row[0])
    
    #objective 2: make prof info and then calc total prof
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

    #calc monthly changes and then the avg change
        final_profit = int(row[1])
        month_change_profit = final_profit - initial_profit
    
    #make list for monthly change
        month_change.append(month_change_profit)
        total_change_profit = total_change_profit + month_change_profit
        initial_profit = final_profit
    
    #calc above for profit change
        average_change_profit = (total_change_profit/count)
    
    #min/max profits and what month
    greatest_inc_profit = max(month_change)
    greatest_dec_profit = min(month_change)

    inc_date = date[month_change.index(greatest_inc_profit)]
    dec_date = date[month_change.index(greatest_dec_profit)]

    #now print some of it 
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profit)))
    print("Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc_profit) + ")")
    print("Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec_profit)+ ")")
    print("----------------------------------------------------------")

#now open the analysis as a text file
with open(finatxt, 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profit)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(inc_date) + " ($" + str(greatest_inc_profit) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(dec_date) + " ($" + str(greatest_dec_profit) + ")\n")
    text.write("----------------------------------------------------------\n")

# now check the .csv file against the output
# everything is right but the average change... why? ?
