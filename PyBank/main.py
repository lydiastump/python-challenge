#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:19:37 2019

@author: lydiaclaire
"""

import os
import csv

# Identify path
csvpath = os.path.join('budget_data.csv')

revenue = []
dates = []
# Read file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    
    # number of rows = number of months
    #do in for loop (Add variable)
    #number_of_months = sum(1 for row in csvreader)
    #print(number_of_months)
   
    # define function and calculate net profit
    totalprofit = 0
    rowcount = 0
    for row in csvreader:
        rowcount += 1
        
        totalprofit += int(row[1])
        revenue.append(row[1])
        
        dates.append(row[0])
 
    


    rev_change = []
    #calculate revenue differences
    for i in range(len(revenue)):
        rev_change.append(int(revenue[i]) - int(revenue[i-1]))
    

    #identify max and related date
    max_rev_change = max(rev_change)


    #identify max and related date
    min_rev_change = min(rev_change)


    f = open("pypoll.txt", "w")
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(rowcount))
    print("Total: $" + str(totalprofit))
    print("Greatest Increase in Profits: " + (dates[rev_change.index(max(rev_change))]) + " $" + str(max_rev_change))
    print("Greatest Decrease in Profits: " + (dates[rev_change.index(min(rev_change))]) + " $" + str(min_rev_change)) 
    
    f.close()       
    
    
    
    
    
    
    
  