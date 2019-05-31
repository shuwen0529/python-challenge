# -*- coding: UTF-8 -*-

# Import the os module
import os
import csv

# Read CSV files
csvpath = os.path.join("/Users/shuwenzhang/Desktop/BootCamp/Homework/03-Python/PyBank/Resources/budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read header row 
    csv_header = next(csvreader)
    
    # Lists of data to store 
    date   = []
    profit = []
    monthly_profit_change = []
    
    # Initial values
    month_count = 0

    for row in csvreader:
        # Add Date
        date.append(row[0])
        # Add Profit/Loss
        profit.append(float(row[1]))
        # total number of months 
        month_count = month_count +1

    # Net total amount of Profit/Losses
    total_profit = sum(profit)

    # Get monthly change of profit 
    for i in range(len(profit)-1):
        monthly_change = profit[i+1] - profit[i]
        monthly_profit_change.append(monthly_change)

    # Get average of the changes in "Profit/Losses"
    average_profit = sum([i for i in monthly_profit_change]) / (month_count-1)

    # Get greatest increase in profits and date
    max_increase_profit = max(monthly_profit_change)
    increase_date = date[monthly_profit_change.index(max_increase_profit)+1]
  
    # Get greatest decrease in profits and date
    max_decrease_profit = min(monthly_profit_change)
    decrease_date = date[monthly_profit_change.index(max_decrease_profit)+1]

print ('----------Financial Analysis----------')
print ('Total number of months: '+ str(month_count))
print ('Net Profit/Losses: '+ '${:.0f}'.format(total_profit))
print ('Average changes in Profit/Losses: '+'${:.2f}'.format(average_profit))
print ('Greatest Increase in Profits: '+str(increase_date)+' ${:.0f}'.format(max_increase_profit)+')')
print ('Greatest Decrease in Profits: '+str(decrease_date)+' ${:.0f}'.format(max_decrease_profit)+')')
print ('---------------------------------------')

output = os.path.join('/Users/shuwenzhang/Desktop/BootCamp/Homework/03-Python/SZ_HW#3_PythonChanllege/python-challenge/PyBank/analysis.txt')

with open(output, 'w', newline='') as new:
    new.write("--------Financial Analysis-------")
    new.write("\n")
    new.write('Total number of months: '+ str(month_count))
    new.write("\n")
    new.write('Net Profit/Losses: '+ '${:.0f}'.format(total_profit))
    new.write("\n")
    new.write('Average changes in Profit/Losses: '+'${:.2f}'.format(average_profit))
    new.write("\n")
    new.write('Greatest Increase in Profits: '+str(increase_date)+' (${:.0f}'.format(max_increase_profit)+')')
    new.write("\n")
    new.write('Greatest Decrease in Profits: '+str(decrease_date)+' (${:.0f}'.format(max_decrease_profit)+')')