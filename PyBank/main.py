import os

import csv

budget_csv = '/Users/ismahanadan/Desktop/python-challenge/PyBank/budget_data.csv'

#Define for list
date = []
revenue = []
revenue_change = []

#Open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    #For loop for the total number of months and revenue
    for row in csv_reader:
        date.append(row[0])
        revenue.append(int(row[1]))
    #to calculate profit/loss change and the average.  
    for row in range(1,len(revenue)):
        revenue_change.append(revenue[row]- revenue[row-1])
    print(f"Greatest Increase in Profits: {date[revenue_change.index(max(revenue_change)) +1]} ({max(revenue_change)}) \n")



 






print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Net Profit/Loss: ${sum(revenue)}")
print(f"Average Profit/Loss Change: ${sum(revenue_change) / len(date)}")




